from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


# pagina inicial! carrega ao entrar no sistema
@app.route('/')
def pagina_inicial():
  return render_template('inicio.html')


# carrega a tela para realizar o login inserindo usuario e senha
@app.route('/entrar/')
def admin_index():
  return render_template('login.html')


#efetua o teste que a rota entrar forneceu, redirecionando
#para a rota de admin ou se acesso errado redireciona para entrar novamente
@app.route('/login/', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    usuario = request.form['c_usuario']
    senha = request.form['c_senha']
    if usuario == "caio" and senha == "caio":
      return redirect(url_for('admin', nome=usuario, senha=senha))
    else:
      return redirect(url_for('entrar'))
  else:
    usuario = request.args.get('c_usuario')
    senha = request.args.get('c_senha')
    if usuario == "caio" and senha == "caio":
      return redirect(url_for('admin', nome=usuario, senha=senha))
    else:
      return redirect(url_for('entrar'))


#rota apenas para usuarios logados, chega aqui depois de percorrer a
#rota de login anterior e o acesso for concedido
@app.route('/admin/<nome>/<senha>')
def admin(nome, senha):
  frase = "<b>bem vindo</b>" + nome + "sua senha é:<i>" + senha + "</i>"
  return frase


if __name__ == '__main__':
  app.run('0.0.0.0')
