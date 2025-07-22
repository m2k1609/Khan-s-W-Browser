from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'ilikecats'  # Change this to a random secret key

@app.route('/')
def index():
    return render_template('index.svelte')
if __name__ == '__main__':
    app.run(debug=True)