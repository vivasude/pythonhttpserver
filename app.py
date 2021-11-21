from json import dumps
from flask import Flask, render_template
from pymongo import MongoClient


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
	collection = db.list_collection_names()
	if collection:
		print('collection table exists')
	else:
		data = {"_id": "103", "name": "Vishnu", "age": "28", "city": "Budapest"}
		coll.insert_one(data)
	result = []
	for x in coll.find():
		result.append(x)
	return result



app = Flask(__name__, template_folder='.')


@app.route('/')
def Results():
	try:
		questions = mongo_client()
		print(questions)
		return render_template('questions.html', questions=questions )

	except Exception as e:
		return dumps({'error': str(e)})

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

