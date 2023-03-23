import save_json
from save_json import writeAJson
from ProductAnalyzer import ProductAnalyzer
pd = ProductAnalyzer()
json1 = pd.clienteB()
json2 = pd.listaProdutos()
json3 = pd.clienteMenosG()
json4 = pd.produtoMenosV()
save_json.writeAJson(json1,"json1")
save_json.writeAJson(json2,"json2")
save_json.writeAJson(json3,"json3")
save_json.writeAJson(json4,"json4")




