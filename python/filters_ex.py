"""Filters about."""

#Remove all false values: false, 0, None

def Filtering(lst):
    return list(filter(None,lst))
lst=[None,1,3,0,"",5,7]
Filtering(lst)

###### simple filter just example

class ContentFilter(object):
    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            self._filters += filters

    def filter(self, content):
        for filter in self._filters:
            content = filter(content)
        return content

filter = ContentFilter([
    offensive_filter,
    ads_filter,
    porno_video_filter])
filtered_content = filter.filter(content)

######
