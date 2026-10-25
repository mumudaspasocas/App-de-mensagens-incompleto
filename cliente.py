import socket
import threading 
import tkinter as tk
import json




#conectamento
cliente = socket.socket()
cliente.connect(("localhost", 5000))
print("six seven conectou")

#funcções
mensagens_recebidas = []
def receber():
    while True:
        dados = cliente.recv(1024)
        msg = dados.decode()

        mensagens_recebidas.append(msg)

def verificar_mensagens():
    if mensagens_recebidas:
        msg = mensagens_recebidas.pop(0)

        mensagens.insert(tk.END, f"Cliente 2: {msg}\n")

    janela.after(100, verificar_mensagens)

thread = threading.Thread(target=receber)

thread.start()


def enviar():
    texto = entrada.get().strip()

    if texto == "":
        mensagens.insert(tk.END, "Você não pode mandar uma msg vazia!\n")
        entrada.delete(0, tk.END)
    else:
        cliente.send(texto.encode())
        entrada.delete(0, tk.END)
        mensagens.insert(tk.END, f"Você: {texto}\n")

#tintker
janela = tk.Tk()
janela.title("MumuChat 1")

janela.geometry("600x800")

mensagens = tk.Text(janela)
mensagens.pack()

entrada = tk.Entry(janela, width=50)
entrada.pack()

botao = tk.Button(janela, text="enviar msg", command=enviar)
botao.pack()

janela.after(100, verificar_mensagens)

janela.mainloop()

