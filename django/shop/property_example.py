""" Cached your property for fast access. """

from django.utils.functional import cached_property
    # ...
    @cached_property
    def full_name(self):
        # Expensive operation e.g. external service call
        return "{0} {1}".format(self.firstname, serlf.lastname)
