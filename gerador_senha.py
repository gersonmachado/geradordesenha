from tkinter import *

root = Tk()
root.title('Gerador de senha') #Título
root.geometry('410x280') #Tamanho padrão de abertura
root.minsize(410, 280) #Tamanho mínimo
root.maxsize(410, 350) #Tamanho máximo

def senhaforte():
    import random

    letra_maiuscula = chr(random.randint(65 ,90))
    letra_minuscula = chr(random.randint(97,122))
    char_especial = chr(random.randint(33,47))
    lista = []

    for i in range (0,5):
        x = random.randint(0, 9)
        lista.append(x)

    lista2 = lista[:]
    #random.shuffle para embaralhar lista
    random.shuffle(lista2)
    lista2 = str(lista2).strip("[]").replace(',', '').replace(' ', '')



    senhaforte = lista2+letra_minuscula+letra_maiuscula+char_especial
    entrada.delete(0, END)
    entrada.insert(END, senhaforte)  # Inserir no final, número

    #print('Senha forte:')
    #print(senhaforte)

def senhafraca():
    import random

    letra_maiuscula = chr(random.randint(65, 90))
    letra_minuscula = chr(random.randint(97, 122))
    char_especial = chr(random.randint(33, 47))
    lista = []

    for i in range(0, 5):
        x = random.randint(0, 9)
        lista.append(x)
    lista = str(lista).strip("[]").replace(',', '').replace(' ', '')
    senhafraca = lista


    entrada2.delete(0, END)
    entrada2.insert(END, senhafraca)  # Inserir no final, número
    #print('Senha fraca:')
    #print(senhafraca)

# Labels
website_label = Label(text="https://github.com/gersonmachado")
website_label.grid(row=0, column=9)


#Parte de entrada de dados com Entry - Visor da calculadora
entrada = Entry(root, width=15, borderwidth=4, relief=FLAT,
                fg='#FFFFFF', bg='#CCCCCC', font=('futura', 25, 'bold'), justify=CENTER)


#grid() adiciona o objeto criado no root/tela
entrada.grid(
    row=3, #Linha zero
    column=6, #Coluna zero
    columnspan=7,  #Ocupar 4 colunas
    pady= 2 #Distância entre o botão e o númer3
)

gerar = Button(root,
                text='Gerar Senha Forte', #texto do botão
                padx=135, #largura
                pady=20, #altura
                command=senhaforte, #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 11, 'bold'))

#adicionando a tecla na janela
gerar.grid(row=4,
          column=6,
           columnspan=7)


#Parte de entrada de dados com Entry - Visor da calculadora
entrada2 = Entry(root, width=15, borderwidth=4, relief=FLAT,
                fg='#FFFFFF', bg='#CCCCCC', font=('futura', 25, 'bold'), justify=CENTER)


#grid() adiciona o objeto criado no root/tela
entrada2.grid(
    row=6, #Linha zero
    column=6, #Coluna zero
    columnspan=7,  #Ocupar 4 colunas
    pady= 2 #Distância entre o botão e o númer3
)





gerar2 = Button(root,
                text='Gerar Senha Fraca', #texto do botão
                padx=135, #largura
                pady=20, #altura
                command=senhafraca, #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 11, 'bold'))

#adicionando a tecla na janela
gerar2.grid(row=7,
          column=6,
           columnspan=7,
            )




#Para a janela pernamecer aberta aguardando ação
root.mainloop()