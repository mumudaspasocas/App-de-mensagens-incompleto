import Autentificaçao
import tkinter as tk

janela = tk.Tk()
janela.title("MumuChat")
janela.geometry("400x300")

frame_login = tk.Frame(janela)
frame_cadastro = tk.Frame(janela)
def fazer_cadastro():
    nome = campo_nome_cadastro.get()
    senha = campo_senha_cadastro.get()
    resultado = Autentificaçao.cadastrar(nome, senha)
    mensagem_cadastro.config(text=resultado)

def ir_para_cadastro():
    frame_login.pack_forget()
    frame_cadastro.pack()

def ir_para_login():
    frame_cadastro.pack_forget()
    frame_login.pack()

tk.Label(frame_login, text="Tela de Login").pack()
tk.Button(frame_login, text="Ir para cadastro", command=ir_para_cadastro).pack()

tk.Label(frame_cadastro, text="Criar conta").pack()

campo_nome_cadastro = tk.Entry(frame_cadastro)
tk.Button(frame_cadastro, text = "cadastrar", command=fazer_cadastro).pack()
campo_nome_cadastro.pack()

campo_senha_cadastro = tk.Entry(frame_cadastro, show="*")
campo_senha_cadastro.pack()

mensagem_cadastro = tk.Label(frame_cadastro, text="")
mensagem_cadastro.pack()

tk.Button(frame_cadastro, text="ir para login", command=ir_para_login)

frame_login.pack()

janela.mainloop()