"""How use **kwargs in QuerySet class."""

# Use KeyWord Arguments **kwargs, with tuple

bob_stories = Story.objects.filter(title__contains="bob",
                                   subtitle__contains="bob",
                                   text__contains="bob",
                                   byline__contains="bob")


# Use **kwargs with dict

bobargs = {'title__contains': 'bob', 
           'subtitle__contains': 'bob',
           'text__contains': 'bob',
           'byline__contains': 'bob'}

# Make dict dinamically

bobargs = dict((f + '__contains', 'bob') for f in ('title', 'subtitle', 'text', 'byline'))
bob_stories = Story.objects.filter(**bobargs)
