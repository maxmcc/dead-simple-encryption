from WebUI import WebUI # Add WebUI to your imports
from flask import Flask, render_template, request

app = Flask(__name__)
ui = WebUI(app, debug=True) # Create a WebUI instance

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
  ui.run() 