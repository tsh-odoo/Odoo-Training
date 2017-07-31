#!/usr/bin/env python
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import psycopg2
import pgdb

html = """

<!DOCTYPE html>
<html>
<head>
  <title>Registration</title>
</head>
<body>
  <form method="POST">
    <div>
      <label for="first_name">First Name</label>
      <input type="text" name="first_name" value="%(first_name)s" id="textbox1">
    </div>
    <div>
      <label for="last_name">Last Name</label>
      <input type="text" name="last_name" value="%(last_name)s" id="textbox2">
    </div>
    <button type="submit">Submit</button>
  </form>
    <p>

        Congo,%(first_name)s Successfully inserted into database.
    </p>
</body>
</html>
"""

# some credential
hostname = ''
username = 'odoo'
password = 'postgres'
database = 'training'

def application(environ, start_response):

    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # if request_body_size is not 0:
    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    first_name = d.get('first_name', [''])[0] # Returns the first_name value.
    last_name = d.get('last_name', [''])[0] # Returns the last_name value.

    # Always escape user input to avoid script injection
    first_name = escape(first_name)
    last_name = escape(last_name)

    response_body = html % { # Fill the above html template in
        'first_name': first_name,
        'last_name': last_name
    }
    
    if len(first_name) > 0 and len(last_name) > 0:

        # makeconnection with db
        conn = psycopg2.connect(database=database, user = username, password = password, host = "", port = "5432")
    
        cur = conn.cursor()
        query = "INSERT INTO registration VALUES ('" + first_name + "','" + last_name + "');"
        # print query
        cur.execute(query)
        conn.commit()
        conn.close()

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)

    return [response_body]


httpd = make_server('localhost', 8051, application)
print "serving at port 8051"

httpd.serve_forever()
