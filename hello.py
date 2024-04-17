from flask import Flask

app = Flask(__name__)

@app.route("/jin")
def hello_jin():
    return "<h1> Hello Jin!</h1>"
@app.route("/")
def hello_world():
    return """<table><caption>Phone numbers</caption>
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
</table>"""