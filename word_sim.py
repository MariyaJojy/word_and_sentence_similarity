import tkinter as tk
from tkinter import ttk
from nltk.corpus import wordnet
window = tk.Tk()
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
window.title('Word Similarity')
window.geometry('1000x500')

ttk.Label(window, text="Word similarity",
           foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=1)


ttk.Label(window, text="Meaning :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=3, padx=10, pady=25)
ttk.Label(window, text="Meaning :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=5, padx=10, pady=25)


global vara
def submit():

    name = name_var.get()
    cb = wordnet.synsets(name)

    # Combobox creation
    global n
    n = tk.StringVar()
    drop = ttk.Combobox(window, width=40, textvariable=n)


    drop['values']=[(i.name()+"-->"+i.definition()) for i in cb]


    drop.grid(column=1, row=3)
    drop.current(0)


def submit1():

    name = name_var1.get()
    cb = wordnet.synsets(name)

    print(cb)
    # Combobox creation
    global n1
    n1 = tk.StringVar()
    drop = ttk.Combobox(window, width=40, textvariable=n1)


    drop['values']=[(i.name()+"-->"+i.definition()) for i in cb]


    drop.grid(column=1, row=5)
    drop.current(0)



def val1():
    a=n.get().split("-->")[0]
    b = n1.get().split("-->")[0]
    cb = wordnet.synset(a)
    ib = wordnet.synset(b)
    wup=cb.wup_similarity(ib)
    ttk.Label(window, text="WUP: "+str(wup),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=7, column=1)
    ttk.Label(window, text="LCH: " + str(cb.lch_similarity(ib)),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=8, column=1)
    ttk.Label(window, text="JCN: " + str(cb.jcn_similarity(ib,  brown_ic)),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=9, column=1)
    ttk.Label(window, text="PATH: " + str(cb.path_similarity(ib)),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=10, column=1)
    ttk.Label(window, text="RES: " + str(cb.res_similarity(ib,  brown_ic)),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=11, column=1)
    ttk.Label(window, text="lin: " + str(cb.lin_similarity(ib,  brown_ic)),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=12, column=1)



name_var=tk.StringVar()
name_var1=tk.StringVar()

name_label = tk.Label(window, text = 'word1', font=('calibre',10, 'bold'))
name_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 10, 'normal'))
name_label1 = tk.Label(window, text = 'word2', font=('calibre',10, 'bold'))
name_entry1 = tk.Entry(window, textvariable=name_var1, font=('calibre', 10, 'normal'))
name_label.grid(row=2,column=0)
name_entry.grid(row=2,column=1)
name_label1.grid(row=4,column=0)
name_entry1.grid(row=4,column=1)

sub_btn=tk.Button(window,text = 'Next', command = submit)
sub_btn.grid(row=2,column=3)

sub_btn=tk.Button(window,text = 'Next', command = submit1)
sub_btn.grid(row=4,column=3)

sub_btn1=tk.Button(window,text = 'Calculate', command = val1)
sub_btn1.grid(row=6,column=3)
window.mainloop()