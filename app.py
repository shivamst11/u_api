from logging import debug
from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)
app.debug=True

class HelloWorld (Resource):
    def get(self):
        return {"hello":"world"}
    
api.add_resource(HelloWorld,'/test')

