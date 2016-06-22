# conding: utf-8

import zipfile
import os.path



class Compactador:
	def compactar(self, lista_arquivos):
		arquivo_zip = zipfile.Zipfile("arquivo.zip", "w")
		for arquivo in lista_arquivos:
			if(os.path.isfile(arquivo) and os.path.exists(arquivo)):
				base = os.path.basename(arquivo)
				arquivo_zip.write(arquivo, base)
		arquivo_zip.close()