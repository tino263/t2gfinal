from flask import Flask, render_template, request

app = Flask(__name__)

customers =  []


@app.route('/index')
def index():
  return render_template("index.html") 

@app.route('/about')
def about():
   return render_template("about.html")

@app.route('/projects')
def projects():
   return render_template("projects.html")

@app.route('/team')
def team():
   return render_template("team.html")

@app.route('/donations')
def donations():
   return render_template("donations.html")

@app.route('/contact')
def contact():
   title = "Please fill contact form with enquiry"
   return render_template("contact.html", title=title)

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name") 
    email = request.form.get("email")

    if not first_name or not last_name or not email:
        error_statement = "Please Fill In Missing Information"
        return render_template("contact.html", error_statement=error_statement)

    customers.append(f"{first_name} {last_name} {email}")
    title = "Thank You"
    return render_template("form.html", title=title, customers=customers)


