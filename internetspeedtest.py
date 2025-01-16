#Ruggero Colussi

#importando o tkinter
from tkinter import *

#importando o pillow
from PIL import Image, ImageTk

#importando
import speedtest

#cores
cor0 = '#000000'  #preto
cor1 = '#ffffff'  #branco
cor2 = '#00b809'  #verde
cor3 = '#ff0000'  #vermelho
cor4 = '#403d3d'  #letra
cor5 = '#0059ff'  #azul

#criando a janela
janela = Tk()
janela.title('Projeto 3')
janela.geometry('350x200')
janela.configure(background = cor1)
janela.resizable(width = FALSE, height = FALSE)

#dividindo a janela em dois frames
frame_logo = Frame(janela, width = 350, height = 60, bg = cor1)
frame_logo.grid(row = 0, column = 0, pady = 1, padx = 0, sticky = NSEW)

frame_corpo = Frame(janela, width = 350, height = 140, bg = cor1)
frame_corpo.grid(row = 1, column = 0, pady = 1, padx = 0, sticky = NSEW)

#configurando o frame_logo
imagem = Image.open('images/speed.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

l_logo_imagem = Label(frame_logo, height = 60, image = imagem, compound = LEFT, padx = 10, anchor = 'nw', font = ('Ivy 16 bold'), bg = cor1, fg = cor3)
l_logo_imagem.place(x = 20, y = 0)
l_logo_nome = Label(frame_logo, text = 'Internet Speed Test', padx = 10, anchor = NE, font = ('Ivy 20'), bg = cor1, fg = cor4)
l_logo_nome.place(x = 75, y = 10)

l_logo_linha = Label(frame_logo, width = 350, anchor = NW, font = ('Ivy 1'), bg = cor2)
l_logo_linha.place(x = 0, y = 57)

#função
def main():
    speed = speedtest.Speedtest(secure=True)
    download = f"{'{:.2f}'.format(speed.download() / 1024 / 1024)}"
    upload = f"{'{:.2f}'.format(speed.upload() / 1024 / 1024)}"

    l_download['text'] = download
    l_upload['text'] = upload

    botao_testar['text'] = 'Teste novamente'
    botao_testar.place(x = 115, y = 100)

#configurando o frame_corpo
l_download = Label(frame_corpo, text = '', anchor = NW, font = ('arial 18 bold'), bg = cor1, fg = cor4)
l_download.place(x = 44, y = 25)
l_download_mb = Label(frame_corpo, text = 'MB/s download', anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
l_download_mb.place(x = 30, y = 70)

imagem_down = Image.open('images/download.png')
imagem_down = imagem_down.resize((50,50))
imagem_down = ImageTk.PhotoImage(imagem_down)
l_logo_imagem = Label(frame_corpo, height = 60, image = imagem_down, compound = LEFT, padx = 10, anchor = 'nw', font = ('Ivy 16 bold'), bg = cor1, fg = cor3)
l_logo_imagem.place(x = 130, y = 35)


l_upload = Label(frame_corpo, text = '', anchor = NW, font = ('arial 18 bold'), bg = cor1, fg = cor4)
l_upload.place(x = 235, y = 25)
l_upload_mb = Label(frame_corpo, text = 'MB/s upload', anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
l_upload_mb.place(x = 230, y = 70)

imagem_up = Image.open('images/upload.png')
imagem_up = imagem_up.resize((50,50))
imagem_up = ImageTk.PhotoImage(imagem_up)
l_logo_imagem = Label(frame_corpo, height = 60, image = imagem_up, compound = LEFT, padx = 10, anchor = 'nw', font = ('Ivy 16 bold'), bg = cor1, fg = cor3)
l_logo_imagem.place(x = 170, y = 35)

botao_testar = Button(frame_corpo, command = main, text = 'Iniciar teste', font = ('Ivy 10 bold'), relief = RAISED, overrelief = RIDGE, bg = cor5, fg = cor1)
botao_testar.place(x = 135, y = 100)


janela.mainloop()