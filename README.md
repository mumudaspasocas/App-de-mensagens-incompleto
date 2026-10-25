MumuChat

Aplicativo de mensagens feito em Python, com sockets para a comunicação e Tkinter para a interface. É um projeto de aprendizado.

Status: incompleto (pausado). O chat funciona entre dois clientes na mesma máquina, e o cadastro de contas funciona. Login, integração e publicação ainda não estão prontos.

O que funciona
Servidor em localhost, porta 5000, que aceita dois clientes e repassa as mensagens de um para o outro.
Clientes com Tkinter que enviam e recebem mensagens ao mesmo tempo, usando threads.
Cadastro de contas (auth.py): valida campos vazios e impede nomes repetidos.
Armazenamento local das contas em usuarios.json, com senhas guardadas como hash SHA-256 (nunca em texto puro).
O que falta
Ligar a tela de login à função auth.login.
Abrir a tela do chat somente depois de um login válido.
Juntar os dois arquivos de cliente em um só, que recebe o nome do usuário ao iniciar.
Trocar o hash simples por um método mais seguro, com salt (por exemplo, bcrypt ou argon2).
Colocar o servidor em uma máquina acessível pela internet, em vez de localhost.
Substituir o JSON por um banco de dados de verdade (como o Firebase).
Gerar um executável (.exe) com PyInstaller.
Como rodar o que já existe

Use três terminais, nesta ordem:

Rode o servidor. Ele fica esperando dois clientes.
Rode o cliente 1 e depois o cliente 2. As duas janelas já trocam mensagens.
Para testar o cadastro, rode o login.py, clique em "Ir para cadastro", preencha nome e senha e clique em "Cadastrar".

Requisitos: Python 3 com Tkinter (já incluso na instalação padrão do Windows).

Aviso de segurança

Este projeto é educacional. O JSON local e o hash SHA-256 sem salt não são adequados para um serviço público. Não use senhas reais de outras contas em testes.

Estrutura
APP mensagens/
├── servidor.py      # servidor que liga os dois clientes
├── cliente1.py      # janela "MumuChat 1"
├── cliente2.py      # janela "MumuChat 2"
├── auth.py          # cadastro, login e hash de senha
├── login.py         # telas de login e cadastro (Tkinter)
└── usuarios.json    # contas cadastradas

Os nomes dos arquivos de cliente e servidor são exemplos. Ajuste para os nomes que você usou.

Aprendizado

Projeto feito como estudo de Python: sockets, threads, Tkinter, JSON e hash de senhas.
