import scrape_animals
from flask_restful import Resource

class AnimalList(Resource):
    def get(self):
        return scrape_animals.get_all_animals()

class AnimalInfo(Resource):
    def get(self, animal_name):
        return scrape_animals.get_animal_details(animal_name)

class EndangeredList(Resource):
    def get(self):
        return scrape_animals.get_endangered_list()

class SearchAnimal(Resource):
    def get(self, search_text):
        return scrape_animals.search_animal(search_text)

class FishList(Resource):
    def get(self):
        return scrape_animals.get_fish()

class BirdList(Resource):
    def get(self):
        return scrape_animals.get_birds()

class MammalList(Resource):
    def get(self):
        return scrape_animals.get_mammals()

class ReptilesList(Resource):
    def get(self):
        return scrape_animals.get_reptiles()
    
class AmphibiansList(Resource):
    def get(self):
        return scrape_animals.get_amphibians()

class HomePage(Resource):
    def get(self):
        return scrape_animals.directory_guide()