""" in tdd.py - testing info, thats it each debuging. """

for debug templates:

TEMPLATE_DEBUB to True (in addition to DEBUG) in settings.py

{% debug %} is a tag of debug, insert in in code

<textarea onclick="this.focus();this.select()" style="width: 100%;">
    {% filter force_escape %}
        {% debug %}
    {% endfilter %}
</textarea>
# How inserted debug tag?
# templatetags/debug.py
import pudb as dbg    # change to any *db
from django.template import Library, Node

register = Library()

class PdbNode(Node):
    def render(self, context):
        dbg.set_trace()    # Debugger will stop here
        return ''

@ register.tag
def pdb(parser, token):
    return PdbNode()

########
{% load debug %}

{% for item in items %}
   # {# Some place you want to break #}
    {% pdb %}
{% endfor %}

###### Scanning Incoming Files for Viruses

import pyclamd
from django.core.files import uplodhandler
from django.conf import settings

# Set up pyclamd to access running instance of clamavd, according to settings
host = getattr(settings, 'CLAMAV_HOST', 'localhost')
post = getattr(settings, 'CLAMAV_PORT', 3310)
pyclamd.init_network_socket(host, port)

class VirusScan(uploadhandler.FileUploadHandler):
    def receive_data_chunk(self, raw_data, start):
        try:
            if pyclamd.scan_stream(raw_data):
                # A virus was found, so the file should
                # be removed from the input stream.
                raise uploadhandler.SkipFile()
            except pyclamd.ScanError:
                # Clam AV could't be contacted, so the file wasn't scanned.
                # Since we can't guarantee the safety of any files,
                # no other files should be processed either.
                raise uploadhandler.StopUpload()

            # If everything went fine, pass the data along
            return raw_data

        def file_compete(self, file_size):
            # This doesn't store the file anywhere, so it should
            # rely on other handlers to provide a File instance.
            return None

######
