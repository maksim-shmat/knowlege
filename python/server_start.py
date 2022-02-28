"""Start a server in localhost."""

# python -m http.server --cgi

# and go to webbrowser ant open http://localhost

# That is Nginx

# chmod 755 somescript.cgi
# chmod 666 editable_file.txt  # security risk with 666

#1 Simple CGI script, save it into simple1.cgi

print('Content-type: text/html')
print() # Prints an empty line, to end the headers
print('Hello, world!')

#2 A CGI script that invokes a Traceback(faulty.cgi)

import cgitb; cgitb.enable()

print('Content-type: text/html\n')
print(1/0)
print('Hello, world!')

#3 A CGI script that retrieves a single value from a FieldStorage(simple2.cgi)

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print('Content-type: texgt/plain\n')
print('Hello,{}!'.format(name))
print(urlencode({'name':'Gumby', 'age':'42'})

#4 A greeting script with an HTML form (simple3.cgi)

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print("""Content-type:text/html
    <html>
      <head>
        <title>Greeting Pagef</title>
      </head>
      <body>
        <h1>Hello,{}!</h1>
        <form action='simple3.cgi'>
        Change name <input type='text' name = 'name'/>
        <input type='submit'/>
        </form>
      </body>
    </html>
    """.format(name))

#5
