# Using CGI script


#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi

PORT_NUMBER = 8000

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        if self.path=="/":
            self.path="/index.html"

        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(curdir + sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    #Handler for the POST requests
    def do_POST(self):

        
        import pdb
        pdb.set_trace()

        # print "got post!!"
        # content_len = int(self.headers.getheader('content-length', 0))
        # post_body = self.rfile.read(content_len)
        # test_data = simplejson.loads(post_body)
        # print "post_body(%s)" % (test_data)
        # return SimpleHTTPRequestHandler.do_POST(self)

        # 2 working
        # Parse the form data posted
        # form = cgi.FieldStorage(
        #     fp=self.rfile, 
        #     headers=self.headers,
        #     environ={'REQUEST_METHOD':'POST',
        #              'CONTENT_TYPE':self.headers['Content-Type'],
        #              })

        # # Begin the response
        # self.send_response(200)
        # self.end_headers()
        # self.wfile.write('Client: %s\n' % str(self.client_address))
        # self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        # self.wfile.write('Path: %s\n' % self.path)
        # self.wfile.write('Form data:\n')

        # # Echo back information about what was posted in the form
        # for field in form.keys():
        #     field_item = form[field]
        #     if field_item.filename:
        #         # The field contains an uploaded file
        #         file_data = field_item.file.read()
        #         file_len = len(file_data)
        #         del file_data
        #         self.wfile.write('\tUploaded %s as "%s" (%d bytes)\n' % \
        #                 (field, field_item.filename, file_len))
        #     else:
        #         # Regular form value
        #         self.wfile.write('\t%s=%s\n' % (field, form[field].value))

        # return


        # 1 working code
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}


        # if os.environ['REQUEST_METHOD'] == 'POST':

        # print "post_request"
        # return          

    #     if self.path=="/send":
    #         form = cgi.FieldStorage(
    #             fp=self.rfile, 
    #             headers=self.headers,
    #             environ={'REQUEST_METHOD':'POST',
    #                      'CONTENT_TYPE':self.headers['Content-Type'],
    #         })

    #         print "Your name is: %s" % form["your_name"].value
    #         self.send_response(200)
    #         self.end_headers()
    #         self.wfile.write("Thanks %s !" % form["your_name"].value)
            
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
    