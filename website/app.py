
from flask_mail import Mail,Message
from flask import Flask,request, render_template, Blueprint
import json,jsonify
app = Flask(__name__)

with open("website/config/config.json", 'r') as c:
    params = json.load(c)["params"]

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USE_TLS = False,
    MAIL_USERNAME = params["email"],
    MAIL_PASSWORD = params["password"],
    MAIL_DEFAULT_SENDER=params["email"],
    
)
mail = Mail(app)
@app.route("/", methods=['GET', 'POST'])
def test():
    # if request.method == 'POST':
    #     name = request.form.get('name')
    #     email = request.form.get('email')
    #     subject = request.form.get('subject')
    #     message = request.form.get('message')
    #     mail.send_message(
    #         f'{subject}' ,
    #         sender=email,  # Replace with your email address
    #         recipients=[params["email"]],
    #         body=f"{message}", 
    #     )
    # return render_template("test.html", params=params)
     if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        msg = Message(
            subject=f"{subject}",
            recipients=[params["email"]],  # Recipient email address (a list of recipients)
            
            # html=f"<p>{message}</p>" ,
             # Convert the message to an HTML paragraph
        )
         #if email else app.config['MAIL_DEFAULT_SENDER']  # Set the sender email address
        msg.sender = email  # Replace with your email address
        msg.body = f"{name}  \n  {message}  \n  {email}"
        mail.send(msg)
     return render_template("test.html", params=params)
if __name__ == '__main__':
    app.run(debug=False)