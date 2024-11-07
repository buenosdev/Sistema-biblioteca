from livro import Livro
from database import Database
import mysql.connector

class controllerLivro:
  def inserirLivro(self):
    db = Database('10.28.2.66','Sim','','biblioteca')
    db.conectar()
    query = Livro('Livro','lindo','maravilhoso', 444).inserirLivro()
    db.executarQuery(query)
    db.desconectar()
  
  def visualizarLivro(self):
    db = Database('10.28.2.66','Sim','','biblioteca')
    db.conectar()
    query = Livro('Livro','lindo','maravilhoso', 444).visualizarLivro()
    visu = db.visualizarQuery(query)
    for x in visu:
      print(f'Livro: {x}')
    db.desconectar()

  def atualizarLivro(self):
    db = Database('10.28.2.66','Sim','','biblioteca')
    db.conectar()
    query = Livro('Livro','lindo','maravilhoso', 444).updateLivro('aasdf', 'sim', "seia", "Davi")
    db.executarQuery(query)
    db.desconectar()
  
  def deletarLivro(self):
    db = Database('10.28.2.66','Sim','','biblioteca')
    db.conectar()
    query = Livro('Livro','lindo','maravilhoso', 444).deleteLivro('autor', 'teste')
    db.executarQuery(query)
    db.desconectar()

controllerLivro().inserirLivro()
controllerLivro().visualizarLivro()
controllerLivro().atualizarLivro()
controllerLivro().deletarLivro()