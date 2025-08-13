from flask import *
from forms import KycForm

app = Flask(__name__)
# csrf token
app.config["SECRET_KEY"] = "iotkycform"

# routers
@app.route("/",methods=["GET","POST"])
def kyc():
    form = KycForm()
    if form.validate_on_submit():
        values = {
            form.fullname.name:form.fullname.data,
            form.passcode.name:form.passcode.data,
            form.email.name:form.email.data,
            form.aadhaar.name:form.aadhaar.data,
            form.pan.name:form.pan.data,
            form.type.name:form.type.data,
            form.branch.name:form.branch.data,
        }
        return jsonify(values)
    return render_template('kyc.html',account=form)

if __name__ == "__main__": app.run('localhost',6111)