import json
import hashlib

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_usuarios():
    with open("usuarios.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_usuarios(usuarios):
    with open("usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def cadastrar(nome, senha):
    usuarios = carregar_usuarios()

    if nome == "":
        return "Digite um nome!"

    
    if senha == "":
        return "Digite uma senha!!"

    
    if nome in usuarios:
        return "Esse usuário já existe"

    usuarios[nome] = gerar_hash(senha)
    salvar_usuarios(usuarios)
    return "Conta criada!"

def login(nome, senha):
    usuarios = carregar_usuarios()

    if nome not in usuarios:
        return "Usuário não existe"

    if usuarios[nome] == gerar_hash(senha):
        return "Login certo!"

    return "Senha errada"