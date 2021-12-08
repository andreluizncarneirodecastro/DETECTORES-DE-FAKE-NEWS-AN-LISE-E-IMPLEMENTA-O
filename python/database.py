import urllib
import time
import mysql.connector

# QUERIES
# 1) CREATE DATABASE fakenews;
# 2) CREATE TABLE fakenews (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
#                           search TEXT NOT NULL, perc FLOAT NOT NULL, 
#                           reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

class Database:
	db = None

	def save(self, search, perc_total):
		self.db = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  password="root",
		  database="fakenews"
		)

		cursor = self.db.cursor()

		query = "INSERT INTO fakenews (search, perc) VALUES (%s, %s)"
		cursor.execute(query, (search, perc_total))

		self.db.commit()