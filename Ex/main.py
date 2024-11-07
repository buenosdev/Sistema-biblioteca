from livro import Livro
from usuario import Usuario
from biblioteca import Biblioteca
import mysql.connector

class Database: 
    def __init__(self, host, user, password, database):
        self.host = host 
        self.user = user 
        self.password = password 
        self.database = database 

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database

        )
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()
        
Sim = Database("localhost","root","","biblioteca")     
Sim.conectar()
print(vars(Sim.conexao))
Sim.cursor.execute("select * from livro")
print(Sim.cursor.fetchall())

# print(vars(Sim.conexao))
Sim.desconectar()
print(vars(Sim.conexao))

# criar uma classe ControllerLivro
# sera responsavel por executar as querys SQL chamando o banco de dados e o livro
# ajustar a classe livro para que implemente um crud (a classe )