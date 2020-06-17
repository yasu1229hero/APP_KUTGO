# Code written by Fitra
# Function    : a sample of using Flask
# Output      : string of Hello World

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"