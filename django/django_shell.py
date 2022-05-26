"""Interactive environment about."""

# From place where is manage.py(base)
python manage.py shell

>>> from learning_logs.models import Topic
>>> Topic.objects.all()
Results:
    <QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>

# Check id
>>> topics = Topic.objects.all()
>>> for topic in topics:
    print(topic.id, topic)

Results:
    1 Chess
    2 Rock Climbing

# Check text and date_added for Chess theme

>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
Result:
    datetime.datetime(2019, 2, 19, 1, 55, 31, 98500, tzinfo=<UTC>)

# Check notes from theme

>>> t.entry_set.all()
<QuerySet [<Entry: The opening is the first part of the game, roughly...>,
<Entry:
In the opening phase of the game, it`s important t...>]>


