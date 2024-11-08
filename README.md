# Sistema-biblioteca
 
Sistema de gerenciamento para uma biblioteca.
Desenvolver um sistema em python que permita realizar um gerenciamento de uma biblioteca aplicando 
conceitos da programação orientada a objetos e gerar a persistência das informações em um banco de dados sendo acessada em um sistema desktop.

## ----- Estudo de caso:

### ----- Uma biblioteca deseja automatizar o gerenciamento de seus livros e empréstimos. O sistema deve permitir aos bibliotecários controlar o cadastro de livros, usuários, gerenciar os empréstimos e devoluções.
Funcionalidades:

## |------Gerenciamento de livro------|

Cadastrar livros (create): deve receber título*, autor*, isbn deverá ser único; validar se isbn já está cadastrado;
Consultar livros (read): permitir consulta pelo título, autor, isbn ou gênero (consulta por livro individual ou por lote(vários));
Atualizar livros (update): verificar a existência do livro antes de atualizar, validar as colunas a serem atualizadas, não é permitido alterar isbn;
Excluir livros (delete): não pode excluir livro emprestado, validar se está emprestado;

## |------Gerenciamento de usuário------|

Cadastrar usuários: receber nome completo, email deve ser único, senha, cpf único; identificar usuário administrador; verificar formato do email;
Consultar usuário: permitir busca por nome, email ou id, busca individual ou por lote;
Atualizar usuário: admin pode atualizar de qualquer pessoa; verificar se usuário existe, não pode alterar cpf;
Excluir: não pode excluir usuário com empréstimo ativo;
Login do usuário: validar usuário e senha ao logar, livros podem ser visto somente quando os usuários estiverem logado;

## |------Gerenciamento de empréstimo------|

Realizar empréstimo: usuário só podem ter 3 livros emprestado ao mesmo tempo, livro deve estar disponível; verificar quantidade de empréstimo do usuário e status do livro;
Devolver empréstimo: atualizar status do livro e atualizar quantidade de livros do usuário caso não devolva todos;
Verificar empréstimo: consultar empréstimos pelo nome ou pelo livro;

## |------Telas------|

Login: inputs de email e senha e opção para cadastrar-se;
Home: só pode ser acessada por usuário logado; deve ter listas de livros de acordo com categorias e os livros devem apresentar um ancora para uma página individual do livro;
Livro: tela com as informações individuais do livro com opção para pegar emprestado;
Usuário: tela individual do usuário para atualizar as informações e verificar os livros que ele emprestou;
Admin: opção para listar usuários, livros e empréstimos e cadastra-los, atualizá-los e exclui-los.


## ---------------//---------------

Já feitos:

biblioteca.py
controllerLivro.py
database.py
livros.py
main.py
usuario.py