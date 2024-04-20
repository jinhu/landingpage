from flask import Flask
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ToDo Application</title>
</head>
<body>
    <table><caption>Phone numbers</caption>
 <thead>
   <tr>
	<th>Name</th>
	<th colspan="2">Phone</th>
   </tr>
 </thead>
 <tbody>
   <tr>
	<td>John</td>
	<td>577854</td>
	<td>577855</td>
   </tr>
   <tr>
	<td>Jack</td>
	<td>577856</td>
	<td>577857</td>
   </tr>
 </tbody>
 <tfoot>
   <tr>
	<td>&nbsp;</td>
	<td>Personal</td>
	<td>Office</td>
   </tr>
 </tfoot>
</table>

</body>
</html>
"""

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

@app.route('/hello/<path:path>')
def send_hello(path):
    return f"""
        Hello {path}
    """
@app.route("/jolee")
def hello_jolee():
    return """
<a href="/jin">
      <img src="/images/cry.jpg" alt="crybaby" width="100" height="48" /><br/>
      Cry Babies
</a>
"""

@app.route("/yinoch")
def hello_yinoch():
    return """
<a href="/eden">
      <img src="/images/ok.png"/>
</a>
"""

@app.route("/eden")
def hello_eden():
    return """
<a href="/iszu">
      Naar iszu
</a>
"""
@app.route("/jin")
def hello_jin():
    return "<h1> Hello Jin!</h1>"


