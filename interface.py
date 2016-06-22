# conding: utf-8

from Tkinter import *
from tkFileDialog import askopenfilename
from compactador import *
import tkMessageBox
from threading import Thread

class Aplicacao:
	def __init__(self, master):
		self.frame = Frame(master)
		self.frame.pack()

		self.botao_adicionar = Button(self.frame)
		self.botao_adicionar["text"] = "Adicionar"
		self.botao_adicionar["command"] = self.adicionar
		self.botao_adicionar["bd"] = 3
		self.botao_adicionar["font"] = ("Arial", 12)
		self.botao_adicionar.pack(pady=10, padx=30, side="left")

		self.botao_deletar = Button(self.frame)
		self.botao_deletar["text"] = "Deletar"
		self.botao_deletar["command"] = self.deletar
		self.botao_deletar["bd"] = 3
		self.botao_deletar["font"] = ("Arial", 12)
		self.botao_deletar.pack(pady=10, padx=30, side="right")

		self.frame2 = Frame(master)
		self.frame2.pack()

		self.sby = Scrollbar(self.frame2)
		self.sby.pack(side=RIGHT, fill=Y)

		self.sbx = Scrollbar(self.frame2, orient=HORIZONTAL)
		self.sbx.pack(side=BOTTOM, fill=X)

		self.listbox = Listbox(self.frame2, width=50, height=10, selectmode=EXTENDED)
		self.listbox.pack()
		
		self.listbox.config(yscrollcommand=self.sby.set)
		self.sby.config(command=self.listbox.yview)
		
		self.listbox.config(xscrollcommand=self.sbx.set)
		self.sbx.config(command=self.listbox.xview)

		self.frame3 = Frame(master)
		self.frame3.pack()
		self.botao_compactar = Button(self.frame3)
		self.botao_compactar["text"] = "Compactar"
		self.botao_compactar["command"] = self.compactar
		self.botao_compactar["bd"] = 3
		self.botao_compactar["font"] = ("Arial", 12)
		self.botao_compactar.pack(pady=10)

	def adicionar(self):
		nome_arquivo = askopenfilename()
		if nome_arquivo !="":
			self.listbox.insert(END, nome_arquivo)

	def deletar(self):
		itens = self.listbox.curselection()
		if len(itens) == 0:
			tkMessageBox.showinfo("Compactador", "Selecione pelo menos um item.")
		else:
			pos = 0
			for i in itens:
				item_pos = int(i) - pos
				self.listbox.delete(item_pos, item_pos)
				pos = pos + 1


	def compactar(self):
		lista_arquivos = self.listbox.get(0, END)
		if len(lista_arquivos) == 0:
			tkMessageBox.showinfo("Compactador", "Adicione algum arquivo para compactar.")
			return
		
		def executar():
			self.botao_compactar.configure(state=DISABLED)
			compactador = Compactador()
			compactador.compactar(lista_arquivos)
			self.botao_compactar.configure(state=NORMAL)
		t = Thread(target=executar)
		t.start()



				



root = Tk()
root.title("Compactador de arquivos")
#root.iconbitmap(default="hi_tux.ico")
root.geometry("400x300")
root.resizable(width=False, height=False)
Aplicacao(root)
root.mainloop()