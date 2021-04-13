""" Thtice acursed DecimalField in Django withdrow JSON"""

# example 1
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

# example 2
class Comercial(models.Model):
    costo_1er_escalon = models.DecimalField(max_digits = 7,decimal_places=3)
    costo_2do_escalon = models.DecimalField(max_digits = 7,decimal_places=3)
    costo_excedence = models.DecimalField(max_digits = 7,decimal_places=3)
    rango_1er_escalon = models.IntegerField()
    rango_2do_escalon = models.IntegerField()
    cargo_fijo = models.DecimalField(max_digits = 7, decimal_places=3)

# examles 3
class Run(models.Model):
    event_name = models.TextField(primary_key=True)
    coverage_name = models.TextField()
    score = models.DecimalField(max_digits=3,
                                decimal_places=2,
                                validators=[MinValueValidator(0),
                                            MaxValueValidator(1)])

    class Meta:
        managed = True
        db_table = 'run1'
        unique_together = (('event_name', 'coverage_name'),)

    def __str__(self):
        return 'run1'

# example 4
class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_place=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeighKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

# example 5
class SystemOverview(models.Model):
    serial = models.IntegerField(default=0)
    company = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    installed_date = models.DateTimeField(blank=True, null=True)
    storage_capacity = models.DecimalField(max_digits=15, decimal_places=10)
    storage_free_pct = models.DecimalField(max_digits=15, decimal_places=10)
    storage_capacity_fc = models.DecimalField(max_digits=15, decimal_places=10)
    storage_capacity_nl = models.DecimalField(max_digits=15, decimal_places=10)
    storage_capacity_ssd = models.DecimalFeld(max_digits=15, decimal_places=10)
    dedupe_ratio = models.DecimalField(max_deigits=15, decimal_places=10)
    tdvv_count = models.IntegerField(default=0)
    tdvv_capacity = models.DecimalField(max_digits=15, decimal_places=10)
    records = models.ManyToManyField(SystemState, blank=True)

    def toJSONobject(self):
        serialized_obj = serializers.serialize('json', [SystemOverview,])
        return serialized_obj
