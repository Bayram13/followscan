from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    followers_file = request.files['followers']
    following_file = request.files['following']

    followers_data = json.load(followers_file)
    following_data = json.load(following_file)

    followers = set(entry['string_list_data'][0]['value'] for entry in followers_data['relationships_followers'])
    following = set(entry['string_list_data'][0]['value'] for entry in following_data['relationships_following'])

    not_following_back = following - followers
    not_followed_back_by_you = followers - following

    return render_template('index.html',
        not_following_back=not_following_back,
        not_followed_back_by_you=not_followed_back_by_you
    )

if __name__ == '__main__':
    app.run(debug=True)
