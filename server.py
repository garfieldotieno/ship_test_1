# Import the required modules
from flask import Flask

# Create an instance of the Flask app
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
