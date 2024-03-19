import unittest
import sqlite_utils
import csv
import os

class TestCSVImport(unittest.TestCase):
    
    def setUp(self):
        # temporary database for testing
        self.db_file = "test_spotify.db"
        self.db = sqlite_utils.Database(self.db_file)

    def tearDown(self):
        # Remove the temporary database file after the test
        os.remove(self.db_file)

    def test_csv_import(self):
        # Read data from the CSV file
        with open('spotify-data.csv', 'r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            data = [row for row in csvreader]

        # Insert data into the db table
        self.db['spotify_data'].insert_all(data)

        # Query the table to check if the data was inserted correctly
        result = self.db['spotify_data'].count()

        # Assert that the number of rows in the table matches the number of rows in the CSV file
        self.assertEqual(result, len(data), "Number of rows in database should match number of rows in CSV file")

if __name__ == '__main__':
    unittest.main()
