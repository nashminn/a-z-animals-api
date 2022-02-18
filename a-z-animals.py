from flask import Flask
from flask_restful import Api, Resource
import models

app = Flask(__name__)
api = Api(app)

api.add_resource(models.HomePage, '/')
api.add_resource(models.AnimalList, '/animals')
api.add_resource(models.AnimalInfo, '/animals/name=<string:animal_name>')
api.add_resource(models.EndangeredList, '/animals/endangered')
api.add_resource(models.SearchAnimal, '/search/<string:search_text>')
api.add_resource(models.MammalList, '/animals/mammals')
api.add_resource(models.FishList, '/animals/fish')
api.add_resource(models.BirdList, '/animals/birds')
api.add_resource(models.ReptilesList, '/animals/reptiles')
api.add_resource(models.AmphibiansList, '/animals/amphibians')

if __name__ == "__main__":
    app.run()