from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def conectar_banco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gelaty81@@", 
        database="loja_velas"
    )
    return conexao

@app.route('/')
def index():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    
    cursor.execute("SELECT COUNT(*) FROM velas")
    total_velas = cursor.fetchone()[0]

    
    cursor.execute("SELECT COALESCE(SUM(preco * quantidade), 0) FROM velas")
    valor_estoque = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    
    return render_template('index.html', total_velas=total_velas, valor_estoque=valor_estoque)
@app.route('/cadastro')
def tela_cadastro():
    return render_template('cadastro.html')
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        aroma = request.form['aroma']
        descricao = request.form['descricao']
        preco = request.form['preco']
        quantidade = request.form['quantidade']

        conexao = conectar_banco()
        cursor = conexao.cursor()

        sql = "INSERT INTO velas (nome, aroma, descricao, preco, quantidade) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, aroma, descricao, preco, quantidade)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        return redirect('/estoque')

@app.route('/estoque')
def estoque():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM velas")
    velas = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return render_template('estoque.html', velas=velas)
@app.route('/editar/<int:id>')
def editar(id):
    
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM velas WHERE id = %s", (id,))
    vela = cursor.fetchone() 
    
    cursor.close()
    conexao.close()
    
    return render_template('editar.html', vela=vela)

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    if request.method == 'POST':
        
        nome = request.form['nome']
        aroma = request.form['aroma']
        descricao = request.form['descricao']
        preco = request.form['preco']
        quantidade = request.form['quantidade']

        
        conexao = conectar_banco()
        cursor = conexao.cursor()

        sql = "UPDATE velas SET nome=%s, aroma=%s, descricao=%s, preco=%s, quantidade=%s WHERE id=%s"
        valores = (nome, aroma, descricao, preco, quantidade, id)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        
        return redirect('/estoque')
@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_vela(id):
    
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Gelaty81@@',
        database='loja_velas'
    )
    cursor = conexao.cursor()
    
    
    sql = "DELETE FROM velas WHERE id = %s"
    cursor.execute(sql, (id,))
    
    
    conexao.commit()
    cursor.close()
    conexao.close()
    
    
    return redirect('/estoque')

if __name__ == '__main__':
    app.run(debug=True)