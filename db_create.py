from app import db
from models import Trip
from datetime import datetime
import os
import csv

# Insert Trip details into model trips for a given file.
def insert_trips(file_name):
    line_num = 0
    pick_up = True
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            line_num += 1
            # Skip header
            if line_num == 1:
                print("Header row, skipping")
                continue

            if pick_up:
                pick_up = False
                date_object = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S')
                pickup_lat = float(row[1])
                pickup_lng = float(row[2])
                pickup_location = str(pickup_lat) + ',' + str(pickup_lng)
            else:
                pick_up = True
                drop_off_lat = float(row[1])
                drop_off_lng = float(row[2])
                drop_off_location = str(drop_off_lat) + ',' + str(drop_off_lng)

                # This statement will insert a single row into the table called trips
                db.session.add(Trip(date_object, pickup_lat, pickup_lng, drop_off_lat, drop_off_lng, pickup_location, drop_off_location))
                db.session.commit()
        print("Done iterating over file contents - the file has been closed now!")

# Iterate through all the csv files in the directory and insert that data into our database
localExtractFilePath = "./RawData/"
for file in os.listdir(localExtractFilePath):
    if file.endswith(".csv"):
        # For each CSV file, call the function insertTrips to store its data to the table trips.
        insert_trips(localExtractFilePath + file)
