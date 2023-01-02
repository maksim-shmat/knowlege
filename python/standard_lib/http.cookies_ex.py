"""http.cookies about."""

#1 http cookies setheaders

from http import cookies

'''
c = cookies.SimpleCookie()
c['mycookie'] = 'cookie_value'
print(c)

RESULTS:
Set-Cookie: mycookie=cookie_value
'''

#2 http cookies Morsel

from http import cookies
import datetime

'''
def show_cookie(c):
    print(c)
    for key, morsel in c.items():
        print()
        print('key = ', morsel.key)
        print(' value = ', morsel.value)
        print(' coded_value = ', morsel.coded_value)
        for name in morsel.keys():
            if morsel[name]:
                print('  {} = {}'.format(name, morsel[name]))

c = cookies.SimpleCookie()

# Encode cookie value for put it to header
c['encoded_value_cookie'] = '"cookie,value;"'
c['encoded_value_cookie']['comment'] = 'Has escaped punctuation'

# Cookie for one part of site only
c['restricted_cookie'] = 'cookie_value'
c['restricted_cookie']['path'] = '/sub/path'
c['restricted_cookie']['domain'] = 'PyMOTW'
c['restricted_cookie']['secure'] = True

# Cookie, term of use ended from 5 min
c['with_max_age'] = 'expires in 5 minutes'
c['with_max_age']['max-age'] = 300  # seconds

# Cookie, term of use ended from time how is set
c['expires_at_time'] = 'cookies_value'
time_to_live = datetime.timedelta(hours=1)
expires = (datetime.datetime(2009, 2, 14, 18, 30, 14) +
           time_to_live)

# Date format: Wdy, DD-Mon-YY HH:MM:SS GMT
expires = (datetime.datetime(2023, 2, 14, 18, 30, 14) +
           time_to_live)

# Date format: Wdy, DD-Mon-YY HH:MM:SS GMT
expires_at_time = expires.strftime('%a, %d %b %Y %H:%M:%S')
c['expires_at_time']['expires'] = expires_at_time

show_cookie(c)

RESULTS:
Set-Cookie: encoded_value_cookie="\"cookie\054value\073\""; Comment="Has escaped punctuation"
Set-Cookie: expires_at_time=cookies_value; expires=Tue, 14 Feb 2023 19:30:14
Set-Cookie: restricted_cookie=cookie_value; Domain=PyMOTW; Path=/sub/path; Secure
Set-Cookie: with_max_age="expires in 5 minutes"; Max-Age=300

key =  encoded_value_cookie
 value =  "cookie,value;"
 coded_value =  "\"cookie\054value\073\""
  comment = Has escaped punctuation

key =  restricted_cookie
 value =  cookie_value
 coded_value =  cookie_value
  path = /sub/path
  domain = PyMOTW
  secure = True

key =  with_max_age
 value =  expires in 5 minutes
 coded_value =  "expires in 5 minutes"
  max-age = 300

key =  expires_at_time
 value =  cookies_value
 coded_value =  cookies_value
  expires = Tue, 14 Feb 2023 19:30:14
'''

#3 http cookie parse

from http import cookies

'''
HTTP_COOKIE = '; '.join([
    r'integer=5',
    r'with_quotes="He said, \"Hello, World!\""',
])

print('From constructor:')
c = cookies.SimpleCookie(HTTP_COOKIE)
print(c)

print()
print('From load():')
c = cookies.SimpleCookie()
c.load(HTTP_COOKIE)
print(c)

RESULTS:
From constructor:
Set-Cookie: integer=5
Set-Cookie: with_quotes="He said, \"Hello, World!\""

From load():
Set-Cookie: integer=5
Set-Cookie: with_quotes="He said, \"Hello, World!\""
'''

#4 http cookie js_output

from http import cookies
import textwrap

'''
c = cookies.SimpleCookie()
c['mycookie'] = 'cookie_value'
c['another_cookie'] = 'second value'
js_text = c.js_output()
print(textwrap.dedent(js_text).lstrip())

RESULTS:
<script type="text/javascript">
<!-- begin hiding
document.cookie = "another_cookie=\"second value\"";
// end hiding -->
</script>

<script type="text/javascript">
<!-- begin hiding
document.cookie = "mycookie=cookie_value";
// end hiding -->
</script>
'''
