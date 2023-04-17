from pymongo import MongoClient
from bson.objectid import ObjectId
from Habitat import Habitat
from Cuidador import Cuidador
class animal:
    def __init__(self, database):
        self.db = database

    def create_animal(self, nome: str, especie: str, idade: int, habitat: Habitat):
        try:
            res = self.db.collection.insert_one({"nome": nome, "especie": especie, "idade": idade, "habitat": habitat})
            print(f"Animal created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating animal: {e}")
            return None

    def read_animal_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"animal found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading animal: {e}")
            return None

    def update_animal(self, id:str, nome: str, especie: str, idade: int, habitat: Habitat):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nome": nome, "especie": especie, "idade": idade}})
            print(f"animal updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating animal: {e}")
            return None

    def delete_animal(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"animal deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting animal: {e}")
            return None
