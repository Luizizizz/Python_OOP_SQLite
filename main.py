#Impora nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from DAO.PessoaDAO import PessoaDAO

#Exemplo de uso
Luiz = Pessoa(1, "Luiz Claudio")
#print(Luiz)

  #Quero mostrar só o nome
#print(Luiz.nome)

#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
PessoaDAO = PessoaDAO(db.conexao, db.cursor)


#Quero carregar uma lista com o que veio do banco de dados
pessoas = PessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)


#Criar um objeto com qualquer ator/atriz/diretor/diretora
novo = Pessoa(10, "Edson Arantes")

#Olha que simples...
novo = PessoaDAO.save(novo)

#consulta o banco de novo..
pessoas = PessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)