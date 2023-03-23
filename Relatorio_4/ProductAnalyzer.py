import save_json
from database import Database

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()
class ProductAnalyzer():
    def clienteB(self): #Retorne o total que o cliente “B” gastou
        json1 = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": 2, "media": {"$sum": "$total"}}}
        ])
        return json1

    def produtoMenosV(self): #Retorne o produto menos vendido em todas as compras
        json2 = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": None, "media": {"$avg": "$total"}}}
        ])
        return json2
    def clienteMenosG(self): #Encontre o cliente que menos gastou em uma única compra
        json3 = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": None, "media": {"$avg": "$total"}}}
        ])
        return json3
    def listaProdutos(self): #Liste todos os produtos que tiveram uma quantidade vendida acima de 2 unidades
        json4 = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": None, "media": {"$avg": "$total"}}}
        ])
        return json4
