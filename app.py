from flask import Flask
app = Flask(__name__)

# index route
@app.route('/')
def index():
  return 'Hello this in PetFax!'

# pets index route
@app.route('/pets')
def pets(): 
    return 'These are our pets available for adoption!'
