from flask import Flask, render_template
import requests
from post import Post

# api url/blog posts
blog_api_url = 'https://api.npoint.io/8712ecd425f97eed02f9'
blog_response = requests.get(blog_api_url)
all_posts = blog_response.json()
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in all_posts]

# bot
app = Flask(__name__)


# homepage
@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


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
