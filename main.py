from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# if __name__ == '__main__':
#     app.run(debug=True)