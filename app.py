from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# create the application object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/postgres'

#Create SQLAlchemy object
db = SQLAlchemy(app)

# Important
from models import Trip

db.create_all()
db.session.commit()

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# request will contain start date, end date, start hour, end hour, start minute, end minute
# return will be JSON of the fromat { {lat:lat_value, lng:lng_value, weight:total_pickups },...,..}
# Also would want to restrict the response to a max 50,000 rows
@app.route('/pickups')
def get_pickups():
    return "PickUp JSON!"

# request will contain start date, end date, start hour, end hour, start minute, end minute
# return will be JSON of the fromat { {lat:lat_value, lng:lng_value, weight:total_dropoffs },...,..}
# Also would want to restrict the response to a max 50,000 rows
@app.route('/dropoffs')
def get_pickups():
    return "Dropoff JSON"

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
