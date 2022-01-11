
app = Flask(__name__)

test = "TEST"

@app.route('/')
@app.route('/test')
def jobs():
    return test
