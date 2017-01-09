from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<html>
  <head>
    <title>Moravec</title>
  </head>
  <body>
        Moravec
  </body>
</html>
'''
