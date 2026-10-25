import socket
import threading 
import tkinter as tk
janela = tk.Tk()



cliente2 = socket.socket()
cliente2.connect(("localhost", 5000))
print("six seven conectou")



mensagens_recebidas2 = []

def enviar():
    texto = entrada.get().strip()

    if texto == "":
        mensagens.insert(tk.END, "Você não pode mandar uma msg vazia!\n")
        entrada.delete(0, tk.END)
    else:
        cliente2.send(texto.encode())
        entrada.delete(0, tk.END)
        mensagens.insert(tk.END, f"Você: {texto}\n")

def receber():
    while True:
        dados = cliente2.recv(1024)
        msg2 = dados.decode()

        mensagens_recebidas2.append(msg2)

def verificar_mensagens():
    if mensagens_recebidas2:
        msg2 = mensagens_recebidas2.pop(0)

        mensagens.insert(tk.END, f"Cliente 1: {msg2}\n")

    janela.after(100, verificar_mensagens)

thread = threading.Thread(target=receber)

thread.start()



janela.title("MumuChat 2")

janela.geometry("600x800")

mensagens = tk.Text(janela)
mensagens.pack()

entrada = tk.Entry(janela, width=50)
entrada.pack()

botao = tk.Button(janela, text="enviar msg", command=enviar)
botao.pack()

janela.after(100, verificar_mensagens)

janela.mainloop()
