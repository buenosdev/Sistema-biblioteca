import mysql.connector

class Database:
  def __init__(self, host, user, senha, database):
    self.host = host
    self.user = user
    self.senha = senha
    self.database = database
    self.cursor = None
  
  def conectar(self):
    self.conexao = mysql.connector.connect(
      host = self.host,
      user = self.user,
      password = self.senha,
      database = self.database
    )

    self.cursor = self.conexao.cursor()

    # if self.conexao.is_connected():
    #   print('Conexão estabelecida')
    
    # else:
    #     print('Conexão não estabelecida')
  
  def desconectar(self):
    self.conexao.close()
  
  def executarQuery(self, msg):
    self.cursor.execute(msg)
    self.conexao.commit()

  def visualizarQuery(self, msg):
    self.cursor.execute(msg)
    fetch = self.cursor.fetchall()
    return fetch

#CREATE database biblioteca;

# use biblioteca;

# create table livro(
# 	id_livro int auto_increment primary key,
#     titulo varchar(50),
#     autor varchar(50),
#     genero varchar(50),
#     status varchar(30),
#     codigo int
# );

# create table usuario(
# 	id_usuario int primary key,
#     nome varchar(100),
#     cpf varchar(13),
#     telefone varchar(20)
# );

# create table emprestimo(
# 	id_emprestimo int auto_increment primary key,
# 	id_usuario int,
#     id_livro int,
#     foreign key id_livro references livro(id_livro),
#     foreign key id_usuario references usuario(id_usuario)
# ); 