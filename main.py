from flask import Flask, render_template, request
import requests

requested_subreddit = ""

app = Flask(__name__)

def get_meme():
    if requested_subreddit == "":
        url = "https://meme-api.com/gimme"
    else:
        url = f"https://meme-api.com/gimme/{requested_subreddit}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        url = "https://meme-api.com/gimme"
        response = requests.get(url)

    response = response.json() # Convert the response to a JSON object
    
    subreddit = response["subreddit"]
    title = response["title"]
    url = response["postLink"]
    author = response["author"]
    ups = response["ups"]
    image = response["preview"][-1]

    return subreddit, title, url, author, ups, image

@app.route('/', methods=['GET', 'POST'])
def index():
    global requested_subreddit
    if request.method == 'POST':
        requested_subreddit = request.form['subreddit']

    response_subreddit, title, url, author, ups, image = get_meme()
    return render_template('index.html', subreddit=response_subreddit, requested_subreddit=requested_subreddit, title=title, url=url, author=author, ups=ups, image=image)

if __name__ == '__main__':
    app.run(debug=True)