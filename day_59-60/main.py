from flask import Flask, render_template, request
import requests
from post import Post
import smtplib
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# api url/blog posts
blog_api_url = getenv('BLOG_API_URL')
blog_response = requests.get(blog_api_url)
all_posts = blog_response.json()
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in all_posts]

# smtp information
my_email = getenv('MY_EMAIL')
app_password = getenv('APP_PASSWORD')  # app password

# bot
app = Flask(__name__)


# Functions
def send_email(response):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secures connection by making the email encrypted
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email, to_addrs="example@example.com",
                            msg=f"Subject:Blog Contact\n\n "
                                f"{response['name']} "
                                f"\n{response['email']} "
                                f"\n{response['phone_number']} "
                                f"\n{response['message']}")


# homepage
@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        # client information
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone')
        message = request.form.get('message')

        response = {
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "message": message
        }
        send_email(response=response)

        return render_template("contact.html", message_sent=True)
    return render_template("contact.html", message_sent=False)


# blog posts
@app.route('/post/<int:index>')
def get_blog(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
