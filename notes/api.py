from tornado import gen
from tornado_json.requesthandlers import APIHandler
from tornado_json import schema
from tornado_json.gen import coroutine
from pydblite import Base

db = Base('test.pdl')
if db.exists():
	db.open()
else:
	db.create('body', 'guid')

class post_data(APIHandler):

	@schema.validate(
		input_schema={
			"type": "object",
			"properties": {
				"body": {"type": "string"},
				"guid": {"type": "string"},
			}
		},
		input_example={
			"body": "Very Important Post-It Note",
			"guid": "information",
		}

	)
	def post(self):
		# `schema.validate` will JSON-decode `self.request.body` for us
		#   and set self.body as the result, so we can use that here
		rec_id = (db.insert(body=self.body['body'], guid=self.body['guid']))
		record = db[rec_id]
		return db.commit()

# Test subroutine to check if the code is working or the server is running
class Greeting(APIHandler):
	@schema.validate(
		output_schema={"type": "string"},
		output_example="Greetings, Named Person!"
	)
	def get(self, fname, lname):
		"""Greets you."""
		return "Greetings, {} {}!".format(fname, lname)
		
class delete_record(APIHandler):
	
	@schema.validate(
		input_schema={
			"type": "object",
			"properties": {
				"id": {"type": "number"},
			}
		},
		input_example={
			"id": 0
		}

	)
	def post(self):
		del db[self.body["id"]]

class getting_data(APIHandler):
	def get(self):
		for r in db:
			self.write(r)
