from http.server import BaseHTTPRequestHandler, HTTPServer

def printNumber(number):
    html = '<h2 class="page-header">' + str(number) + '</h2>'

    for i in range(1, 11):
        html += str(number) + ' * ' + str(i) + ' = ' + str(number * i) + '<br>'

    return html

def getTable():
    html = '<table class="table table-bordered">'

    html += '<tr>'

    i = 1

    while i <= 5:
        html += '<td>' + printNumber(i) + '</td>'
        i += 1

    html += '</tr>'

    html += '<tr>'

    while i <= 10:
        html += '<td>' + printNumber(i) + '</td>'
        i += 1

    html += '</tr>'

    html += "</table>"
    return html

def getHtml():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Multiplication table by atnartur</title>
        <link rel="stylesheet" href="https://yastatic.net/bootstrap/3.3.6/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1>Таблица умножения</h1>
            """ + getTable() + """
            &copy; 2017 Атнагулов Артур, группа 11-607 КФУ ИТИС
         </div>
    </body>
</html>
    """

# HTTPRequestHandler class
class HttpHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()


        message = getHtml()

        self.wfile.write(bytes(message, "utf8"))
        return



server_address = ('127.0.0.1', 8080)
httpd = HTTPServer(server_address, HttpHandler)
print('open http://' + server_address[0] + ':' + str(server_address[1]))
httpd.serve_forever()

