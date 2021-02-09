"""About PostgreSQL with Django."""

# postgreSQL specific db constraints
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.field import DateTimeRangeField, RangeOperators
from django.db import models
from django.db.models import Q

class Room(models.Model):
    number = models.IntegerField()


class Reservation(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    timespan = DateTimeRangeField()
    cancelled = models.BooleanField(default=False)

    
    class Meta:
        constraints = [
                ExclusionConstraint(
                    name='exclude_overlapping_reservations',
                    expressions=[
                        ('timespan', RangeOperators.OVERLAPS),
                        ('room', RangeOperators.EQUAL),
                    ],
                    condition=Q(cancelled=False),
                ),
        ]

############## case using two fields
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.field import (
        DateTimeRangeField,
        RangeBoundary,
        RangeOperators,
)
from django.db import models
from django.db.models import Func, Q


class TsTzRange(Func):
    function = 'TSTZRANGE'
    output_field = DateTimeRangeField()


class Reservation(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    cancelled = models.BooleanField(default=False)

    
    class Meta:
        constraints = [
                ExclusionConstraint(
                    name='exclude_overlapping_reservations',
                    expressions=(
                        (TsTzRange('start', 'end', RangeBoundary()),
                            RangeOperators.OVERLAPS),
                        ('room', RangeOperators.EQUAL),
                    ),
                    condition=Q(cancelled=False),
                ),
        ]

############# subclassing the built-in database backend
# mysite/mydbengine/base.py
from django.db.backends.postgresql import base, features

class DatabaseFeatures(features.DatabaseFeatures):
    def allows_group_by_selected_pks_on_model(self, model):
        return True


class DatabaseWrapper(base.DatabaseWrapper):
    features_class = DatabaseFeatures

### DATABASE-ENGINE in your settings.py file
DATABASES = {
        'default': {
            'ENGINE': 'mydbengine',
            ...
        },
}

########### migration operations
# RunPython
from django.db import migrations

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Country = apps.get_model("myapp", "Country")
    db_alias = schema_editor.connection.alias
    Country.objects.using(db_alias).bulk_create([
        Country(name="USA", code="us"),
        Country(name="France", code="fr"),
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Country = apps.get_model("myapp", "Country")
    db_alias = schema_editor.connection.alias
    Country.objects.using(db_alias).filter(name="USA", code="us").delete()
    Country.objects.using(db_alias).filter(name="France", code="fr").delete()


class Migration(migrations.Migration):
    dependencies = []
    operations = [
            migrations.RunPython(forwards_func, reverse_func),
    ]

############ SeparateDatabaseAndState
from django.db.migrations.operations.base import Operation

class MyCustomOperation(Operation):
    # If this is False, it means that this operation will be ignored by
    # sqlmigrate; if true, it will be run and the SQL collected for its output
    reduces_to_sql = False

    # If this is False, Django will refuse to reverse past this operation.
    reversible = False

    def __init__(self, arg1, arg2):
        # Operations are usually instantiated with arguments in migration
        # files. Store the values of them on self for later use.
        pass

    def state_forwards(self, app_label, state):
        # The Operation should take the 'state' parameter (an instance of
        # django.db.migrations.state.ProjectState) and mutate it to match
        # any schema changes that have occurred.
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        # The Operation should use schema_editor to apply any changes it
        # wants to make to the database.
        pass

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        # If reversible is True, this is called when the operation is reversed.
        pass

    def describe(self):
        # This is used to describe what the operation does in console output.
        return "Custom Operation"

############# load in postgres 
from django.db.migrations.operations.base import Operation

class LoadEctension(Operation):
    reversible = True

    def __init__(self, name):
        self.name = name

    def state_forwards(self, app_label, state):
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        shema_editor.execute("CREATE EXTENSION IF NOT EXISTS %s" % self.name)

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        schema_editor.execute("DROP EXTENSION %s" % self.name)

    def describe(self):
        return "Creates extension %s" % self.name

############### both ot these models use the same underlying db table
class CommonlyUseModel(models.Model):
    f1 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'app_largetable'


class ManagedModel(models.Model):
    f1 = models.CharField(max_length=10)
    f2 = models.CharField(max_length=10)

    class Meta:
        db_table = 'app_largetable'

# Two equivalent QuerySets:
CommonlyUsedModel.objects.all()
ManagedModel.objects.all().defer('f2')

########### creating your own Aggregate Functions
from django.db.models import Aggregate

class Sum(Aggregate):
    # Supports SUM(ALL field).
    function = 'SUM'
    template = '%(function)s(%(all_values)s%(expressions)s)'
    allow_distinct = False

    def __init__(self, expression, all_values=False, **extra):
        super().__init__(
                expression,
                all_values='All ' all_values else '',
                **extra
        )

########## Expression API
def relabeled_clone(self, change_map):
    clone = copy.copy(self)
    clone.expression = self.expression.relabeled_clone(change_map)
    return clone

### writing your own Query Expressions
import copy
from django.db.models import Expression

class Coalesce(Expression):
    template = 'COALESCE( %(expression)s )'

    def __init__(self, expressions, output_field):
        super().__init__(output_field=output_field)
        if len(expressions) < 2:
            raise ValueError('expressions must have at least 2 elements')
        for expression in expressions:
            if not hasattr(expression, 'resolve_expression'):
                raise TypeError('%r is not an Expression' % expression)
        self.expressions = expressions

###
def resolve_expression(self, query=None, allow_joins=True, reuse=None,
        summerize=False, for_save=False):
    c = self.copy()
    c.is_summary = summarize
    for pos, expression in enumerate(self.expressions):
        c.expressions[pos] = expression.resolve_expression(query, allow_joins,
                reuse, summerize, for_save)
        return c

###
def as_sql(self, compiler, connection, template=None):
    sql_expressions, sql_params = [], []
    for expression in self.expressions:
        sql, params = compiler.compile(expression)
        sql_expressions.append(sql)
        sql_params.extend(params)
    template = template or self.template
    data = {'expressions': ','.join(sql_expressions)}
    return template % data, sql_params

def as_oracle(self, compiler, connection):
    """
    Example of vendor specific handling (Oracle in this case).
    Let's make the function name lowercase.
    """
    return self.as_sql(compiler, connection, template='coalesce( %(expressions)s )')

########### avoiding SQL injection
# bad example
from django.db.models import Func

class Position(Func):
    function = 'POSITION'
    template = "%(function)s('%(substring)s' in %(expressions)s)"

    def __init__(self, expression,substring):
        # substring=substring is an SQL injection vulnerability!
        super().__init__(expression, substring=substring)

# better example
class Position(Func):
    function = 'POSITION'
    arg_joiner = ' IN '

    def __init__(self, expression, substring):
        super().__init__(substing, expression)

###########
