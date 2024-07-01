import os
from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
from form import detailsForm

load_dotenv()

app = Flask(__name__)
app.secret_key=os.getenv("SECRET_KEY")

@app.route('/contact', methods=["POST", "GET"])
def contact():
    form = detailsForm()

    if request.method == "POST":
        if not form.validate_on_submit():
            flash('All fields are required')
            return render_template("contactForm.html", form = form)
        else:
            return "Form submitted successfully"
    if request.method == "GET":
        return render_template("contactForm.html", form = form)
    
if __name__ == '__main__':
    app.run(debug=True)