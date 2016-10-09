# Contains our model for the database

from app import db

# Create our Trip model, which contains date and lat, lng for pickups, dropoffs
class Trip(db.Model):
    __tablename__ = "trip"
    id = db.Column(db.Integer, db.Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    date = db.Column(db.DateTime)
    pickup_lat = db.Column(db.Float)
    pickup_lng = db.Column(db.Float)
    dropoff_lat = db.Column(db.Float)
    dropoff_lng = db.Column(db.Float)
    pickup_location = db.Column(db.String(30))
    dropoff_location = db.Column(db.String(30))

    def __init__(self, date, pickup_lat, pickup_lng, dropoff_lat, dropoff_lng, pickup_location, dropoff_location):
        self.date = date
        self.pickup_lat = pickup_lat
        self.pickup_lng = pickup_lng
        self.dropoff_lat = dropoff_lat
        self.dropoff_lng = dropoff_lng 
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location     

    def __repr__(self):
        return '<Date %r>' % self.date

# PickUp model that contains the location and the number of pickups
class PickUp(db.Model):
    __tablename__ = "pickup"
    pickup_location = db.Column(db.String(30), unique=True, primary_key=True)
    pickup_lat = db.Column(db.Float)
    pickup_lng = db.Column(db.Float)
    total_pickups = db.Column(db.Integer)

    def __init__(self, pickup_location, pickup_lat, pickup_lng, total_pickups):
        self.pickup_location = pickup_lat + ',' + pickup_lng
        self.pickup_lat = pickup_lat
        self.pickup_lng = pickup_lng
        self.total_pickups = total_pickups

    def __repr__(self):
        return '<total_pickups %r>' % self.total_pickups

# Dropoff model that contains the location and the number of dropoffs
class Dropoff(db.Model):
    __tablename__ = "dropoff"
    dropoff_location = db.Column(db.String(30), unique=True, primary_key=True)
    dropoff_lat = db.Column(db.Float)
    dropoff_lng = db.Column(db.Float)
    total_dropoffs = db.Column(db.Integer)

    def __init__(self, dropoff_location, dropoff_lat, dropoff_lng, total_dropoffs):
        self.dropoff_location = dropoff_lat + ',' + dropoff_lng
        self.dropoff_lat = dropoff_lat
        self.dropoff_lng = dropoff_lng
        self.total_dropoffs = total_dropoffs

    def __repr__(self):
        return '<total_dropoffs %r>' % self.total_dropoffs