from pymongo import MongoClient
import argparse
from random import randrange

def get_details():
		parser = argparse.ArgumentParser('This is insert data into database and then reflect them to the webserver')
		parser.add_argument('--Name', nargs=1, required=True, help='Enter the Name of the person',)
		parser.add_argument('--age', nargs=1, required=True, type=int, help='Enter the age of the person')
		parser.add_argument('--city', nargs=1, required=True, default=None,
												help='Enter the city')
		return parser.parse_args()


def mongo_client():
	client = MongoClient(
		host='xx.xx.xx.xx:32001',  # <-- IP and port go here
		serverSelectionTimeoutMS=3000,  # 3 second timeout
		username="mongouser",
		password="mongopassword",
	)



	# Getting the database instance
	db = client['mydb']

	# Creating a collection
	coll = db['example']

	# Inserting document into a collection
	user_input = get_details()
	data = {"_id": randrange(1000), "name": user_input.Name[0], "age": user_input.age[0], "city": user_input.city[0]}
	coll.insert_one(data)
	result = []
	for x in coll.find():
		result.append(x)
	return result


if __name__ == "__main__":
	get_details()
	mongo_client()
