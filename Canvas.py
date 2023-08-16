from tkinter import *
from tkinter import ttk, messagebox
import turtle
from tkinter.tix import *

primeiravez = True

main = Tk()
main.title('Quadro de Desenhos')
main.geometry('809x637')
main.config(bg='black')
msg= Balloon(main)

class Movements:

    def cor(self):
        corlapis = cbcores.get()
        lapis.pencolor(cbcores.get())
        lapis.color(cbcores.get())


    def sair():
        sairmb = messagebox.askyesno('Sair', 'Voce deseja sair do programa?')
        if(sairmb == True):
            main.destroy()
        else:
            pass

    sairbtn = Button(main, text='Sair', bg= "red", command= sair, width= 5, height= 3, padx= 5, pady= 5)
    sairbtn.grid(row=1, column= 0)
    msg.bind_widget(sairbtn, balloonmsg= 'Saia do programa')

    def up(self):
        lapis.forward(45)

    def down(self):
        lapis.back(45)

    def right(self):
        lapis.right(45)

    def left(self):
        lapis.left(45)

cores= ["red", 'blue', 'yellow', 'brown', 'orange', 'pink', 'purple']
cbcores= ttk.Combobox(main, values= cores, width= 30)
cbcores.grid(row= 1, column= 5)
cbcores.set('Mudar cor')
cbcores['state']= 'readonly'

mov = Movements()

quadro = Canvas(main, width= 780, height= 500, bg= 'white')
quadro.grid(row=0, columnspan=6, padx= 10, pady= 20)

lapis = turtle.RawTurtle(quadro)

savebtn = Button(main, text='Salvar', bg= 'black', fg= 'white', padx= 30, command=mov.cor)
savebtn.grid(row=2, column=5)
msg.bind_widget(savebtn, balloonmsg= 'Salve a cor que você selecionou!')

#Botoes
btncima = Button(main, text='↑', bg= 'black', fg= 'white', padx= 10, pady=10,
                  font= 'Arial 15', command=mov.up)
btncima.place(y=550, x=155)

btnbaixo = Button(main, text='↓', bg= 'black', fg= 'white', padx= 10, pady=10,
                   font= 'Arial 15', command= mov.down)
btnbaixo.place(y= 550, x=200)

btndir = Button(main, text='→', bg= 'black', fg= 'white', padx= 10, pady=8, font= 'Arial 15', command= mov.right)
btndir.place(y=550, x=400)

btnesq = Button(main, text='←', bg= 'black', fg= 'white', padx= 10, pady=8, font= 'Arial 15', command= mov.left)
btnesq.place(x=345, y= 550)

def off():
    lapis.penup()
    caneta.config(fg= 'white')
    borracha.config(fg= 'white')
    mouse.config(fg= 'green')
    canbtn.config(fg= 'white')
    lapis.pencolor('black')

def apagar():
    lapis.pencolor('white')
    caneta.config(fg= 'white')
    borracha.config(fg= 'green')
    mouse.config(fg= "white")
    canbtn.config(fg= 'white')

def desenhar():
    lapis.pendown()
    lapis.pencolor('Black')
    borracha.config(fg= 'white')
    caneta.config(fg = 'green')
    mouse.config(fg= 'white')
    canbtn.config(fg ='white')
    lapis.pensize(1)

def reset():
    snclean = messagebox.askyesno('Apagar', 'Certeza? Você irá apagar todo o seu desenho')
    if snclean == True:
        lapis.clear()
        lapis.pencolor('black')
    else:
        pass

def voltar():
    lapis.undo()

borracha = Button(main, text='⌦', bg= 'black', fg= 'white', command= apagar)
borracha.place(y= 550, x=305)
msg.bind_widget(borracha, balloonmsg= 'Use a borracha para apagar seus desenhos!')

caneta = Button(main, text= '✒', bg= 'black', fg= 'green', command= desenhar)
caneta.place(y=550, x= 280)
msg.bind_widget(caneta, balloonmsg= 'Afim de desenhar? Selecione a caneta!')

mouse = Button(main, bg= 'black', fg= 'white', text= '☛', command= off)
mouse.place(y=575, x= 280)
msg.bind_widget(mouse, balloonmsg= 'Mova-se livremente pela tela sem "suja-la"!')

reiniciar = Button(main, text='⟳', bg= 'black', fg= "red", padx= 3, command= reset)
reiniciar.place(y= 575, x= 305)
msg.bind_widget(reiniciar, balloonmsg= 'Não gostou do desenho? Apague-o!')

lapis.speed(5)

def circulo():
    lapis.circle(50)

cbtn = Button(main, text= '⬤', bg= 'black', fg= 'white', command= circulo, width= 2)
cbtn.place(y= 600, x= 513)
msg.bind_widget(cbtn, balloonmsg= 'Desenhe um pequeno circulo!')

def canetao():
    lapis.pensize(20)
    lapis.pencolor('black')
    mouse.config(fg= 'white')
    borracha.config(fg= 'white')
    caneta.config(fg='white')
    canbtn.config(fg = 'green')

canbtn = Button(main, text= '🖌', bg= 'black', fg= 'white', command= canetao, width= 2)
canbtn.place(y= 600, x= 280)
msg.bind_widget(canbtn, balloonmsg= 'Igual a caneta... Mas é mais grosso!')

volbtn = Button(main, text= '↵', bg= 'black', fg= 'white', command= voltar, width= 2)
volbtn.place(y= 600, x= 305)
msg.bind_widget(volbtn, balloonmsg= 'Fez um erro? Desfaça ele!')

def quadrado():
    lapis.forward(100)
    lapis.right(90)
    lapis.forward(100)
    lapis.right(90)
    lapis.forward(100)
    lapis.right(90)
    lapis.forward(100)

quabtn = Button(main, text= '■', bg= 'black', fg= 'white', command= quadrado, width= 2)
quabtn.place(y= 575, x= 490)
msg.bind_widget(quabtn, balloonmsg= 'Desenhe um quadrado!')

def triangulo():
    lapis.forward(100)
    lapis.left(120)
    lapis.forward(100)
    lapis.left(120)
    lapis.forward(100)
    lapis.left(120)

tribtn = Button(main, text= '▲', bg= 'black', fg= 'white', command= triangulo, width= 2)
tribtn.place(y= 575, x= 513)
msg.bind_widget(tribtn, balloonmsg= 'Desenhe um triangulo!')

def retangulo():
    lapis.forward(200)
    lapis.right(90)
    lapis.forward(100)
    lapis.right(90)
    lapis.forward(200)
    lapis.right(90)
    lapis.forward(100)

retbtn = Button(main, text= '▅', bg= 'black', fg= 'white', command= retangulo, width= 2)
retbtn.place(y= 600, x= 490)
msg.bind_widget(retbtn, balloonmsg= 'Desenhe um retangulo!')

main.mainloop()