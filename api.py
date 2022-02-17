from flask import Flask
from flask_restful import Resource, Api

from questionnaire import AutoQuestionnaire

app = Flask(__name__)
api = Api(app)

api.add_resource(AutoQuestionnaire, '/')

if __name__ == '__main__':
    app.run(debug=True)