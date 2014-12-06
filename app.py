from flask import Flask
app = Flask(__name__)

@app.route('/')
def app():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()