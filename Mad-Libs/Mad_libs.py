from tkinter import * 
from tkinter import ttk

root = Tk()
root.title("Mad labs")
s = ttk.Style()
s.configure("prin.TFrame", borderwidth=5, relief="raised")

tela2= ttk.Frame(root, style="prin.TFrame")
tela = ttk.Frame(root, style="prin.TFrame", padding="3 3 12 12")
tela.grid(column=0, row=0, sticky=(N, W, E, S))
tela2.grid(column=0, row=7, sticky=(N, W, E, S))
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

def hist(*args):
   if op.get() == "1":
       text.insert("1.0", f"Enquanto {sub.get()}  andava pela estrada encontrou um {anim.get()} {col.get()}.")
   if op.get() == "2":
       text.insert("1.0", f"Em um dia ensolarado, {sub.get()} queria sair para rua, mas ele estava de castigo porque ele manchou a casa e o seu {anim.get()} com tinta {col.get()}.")
   if op.get() == "3":
       text.insert("1.0", f"{sub.get()} odeia a cor {col.get()} porque ela o dia que {anim.get()} destruiu o seu brinquedo favorito.")
   
def apagar():
    text.delete("1.0", "end")

sub = StringVar()
name_entry = Entry(tela, textvariable=sub)
name_entry.grid(column=2, row=4, sticky=(W, E))
name = Label(tela, text="name")
name.grid(column=1, row=4, sticky=W)

anim = StringVar()
animal_entry= Entry(tela, textvariable=anim)
animal_entry.grid(column=2, row=5, sticky=(W, E))
animal = Label(tela, text="animal")
animal.grid(column=1,row=5, sticky=W)

col = StringVar()
col_entry = Entry(tela, textvariable=col)
col_entry.grid(column=2, row=6, sticky=(W, E))
cor = Label(tela, text="cor")
cor.grid(column=1, row=6, sticky=W)

name_hist = Label(tela, text="escolha uma opção")
name_hist.grid(column=1, row=1, sticky=W)

op = StringVar()
one = ttk.Radiobutton(tela, text="♧", variable=op, value="1")
one.grid(column=2, row=1, sticky=W)

two = ttk.Radiobutton(tela, text="♡", variable=op, value="2")
two.grid(column=2, row=2, sticky=W)

three = ttk.Radiobutton(tela, text="◇", variable=op, value="3")
three.grid(column=2, row=3, sticky=W)

inic = Button(tela, text="iniciar",command=hist)
inic.grid(column=1, row=7, sticky=W)

apag = Button(tela, text="Reiniciar",command=apagar)
apag.grid(column=2, row=7, sticky=W)


text = Text(tela2, width=40, height=10)
text.grid(column=0, row=7)


root.mainloop()