from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = f"https://meme-api.com/gimme"
    response = requests.get(url).json()
    subreddit = response["subreddit"]
    title = response["title"]
    url = response["postLink"]
    author = response["author"]
    ups = response["ups"]
    image = response["preview"][-1]
    return subreddit, title, url, author, ups, image

@app.route('/')
def index():
    subreddit, title, url, author, ups, image = get_meme()
    return render_template('index.html', subreddit=subreddit, title=title, url=url, author=author, ups=ups, image=image)

if __name__ == '__main__':
    app.run(debug=True)