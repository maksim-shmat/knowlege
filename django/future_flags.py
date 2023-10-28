"""Pattern - future flags about."""

#1

def my_view(request):
    if flag_is_active(request, 'flag_name'):
        # Behavior if flag is active

#2 for test case

def my_view(request):
    if sample_is_active(request, 'new_design'):
        # Behavior for test sample.

#3 downtime and disable 'Upload' button for example

def my_view(request):
    if switch_is_active('s3_down'):
        # Disable uploads and show it is downtime
