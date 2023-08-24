import pandas as pd
from flask import Flask, jsonify


app = Flask(__name__)
#contruir funcionalidades 


@app.route('/pegarvendas')
def homepage():
    tabela  = pd.read_csv('advertising.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_de_vendas':total_vendas}
    return jsonify(resposta)








#rodar aplicações

app.run()



