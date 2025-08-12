from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)

transactions = [
    {"id":8765678976,"from":"razaksr@okaxis","to":"mohamed@oksbi","amount":1200.9823,"date":"2025-10-01"},
    {"id":23454345,"from":"genesis@okaxis","to":"victor@oksbi","amount":900.25,"date":"2025-01-09"},
    {"id":987654567,"from":"yit@okaxis","to":"876567898733@oksbi","amount":121200.98,"date":"2025-05-10"},
    {"id":34567876545,"from":"madhav@okaxis","to":"Kamal@oksbi","amount":90.11,"date":"2025-07-20"}
]

@app.route("/edit/<id>",methods=["GET","POST"])
def edit(id):
    if request.method == "POST":
        print(int(id))
        id=int(id)
        for each in transactions:
            if each["id"]==id:
                each["from"] = request.form['from']
                each["to"] = request.form['to']
                each["amount"] = float(request.form['amount'])
                each["date"] = request.form['date']
                print(each)
                break
        return redirect("/home")
    else:
        id=int(id)
        # print(id)
        collected={}
        for each in transactions:
            if each["id"]==id:
                collected=each
                break
        # print(collected)
        return render_template("edit.html",object=collected)

@app.route("/home")
def dash():
    return render_template('main.html',records=transactions)

@app.route("/",methods=['GET'])
def welcomes():
    return jsonify({"message":"Welcome to Flask Tach Stack"})

# host, port
if __name__ == "__main__":
    app.run('localhost',6111)