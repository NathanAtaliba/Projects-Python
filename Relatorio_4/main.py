import save_json
from save_json import writeAJson
from ProductAnalyzer import ProductAnalyzer
pd = ProductAnalyzer()
json1 = pd.clienteB()
json2 = pd.listaProdutos()
json3 = pd.clienteMenosG()
json4 = pd.produtoMenosV()
save_json.writeAJson(json1,"Total que o cliente “B” gastou")
save_json.writeAJson(json2,"Produto menos vendido em todas as compras")
save_json.writeAJson(json3,"Cliente que menos gastou em uma única compra")
save_json.writeAJson(json4,"Produtos que tiveram uma quantidade vendida acima de 2 unidades")




