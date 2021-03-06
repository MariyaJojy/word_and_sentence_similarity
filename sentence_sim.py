import tkinter as tk
from tkinter import ttk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')
import string
table = str.maketrans('', '', string.punctuation)
from nltk.corpus import wordnet
window = tk.Tk()
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
window.title('Word Similarity')
window.geometry('1000x500')

ttk.Label(window, text="Sentence similarity",
           foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=1)




#wup similarity score
def w_simscore(synsets1, synsets2):
    global avgScores
    avgScores=0
    score = 0
    count = 0
    for i in syn1:
        synscore=0
        sim=[]
        for j in syn2:
            if i.pos()==j.pos():
                synscore=i.wup_similarity(j)
                if synscore!=None:
                    sim.append(synscore)
                elif i.name().split(".")[0] == j.name().split(".")[0]:
                    sim.append(1)
                synscore=0

        if (len(sim) > 0):
            score += max(sim)
            count += 1

    if count > 0:
        avgScores =score / count

    return avgScores

#jcn similarity score
def j_simscore(synsets1, synsets2):
    global avgScores
    avgScores=0
    score = 0
    count = 0
    for i in syn1:
        synscore=0
        sim=[]
        for j in syn2:
            if i.pos()!=None and j.pos()!=None and i.pos()==j.pos():
                synscore=i.jcn_similarity(j,  brown_ic)
                if synscore!=None:
                    sim.append(synscore)
                elif i.name().split(".")[0] == j.name().split(".")[0]:
                    sim.append(1)
                synscore=0

        if (len(sim) > 0):
            score += max(sim)
            count += 1

    if count > 0:
        avgScores =score / count

    return avgScores

#lch similarity score
def l_simscore(synsets1, synsets2):
    global avgScores
    avgScores=0
    score = 0
    count = 0
    for i in syn1:
        synscore=0
        sim=[]
        for j in syn2:
            if i.pos()==j.pos():
                synscore=i.lch_similarity(j)
                if synscore!=None:
                    sim.append(synscore)
                elif i.name().split(".")[0] == j.name().split(".")[0]:
                    sim.append(1)
                synscore=0

        if (len(sim) > 0):
            score += max(sim)
            count += 1

    if count > 0:
        avgScores =score / count
    return avgScores

#path similarity score
def p_simscore(synsets1, synsets2):
    global avgScores
    avgScores=0
    score = 0
    count = 0
    for i in syn1:
        synscore=0
        sim=[]
        for j in syn2:
            if i.pos()==j.pos():
                synscore=i.path_similarity(j)
                if synscore!=None:
                    sim.append(synscore)
                elif i.name().split(".")[0] == j.name().split(".")[0]:
                    sim.append(1)
                synscore=0

        if (len(sim) > 0):
            score += max(sim)
            count += 1

    if count > 0:
        avgScores =score / count

    return avgScores

#res similarity score
def r_simscore(synsets1, synsets2):
    global avgScores
    avgScores=0
    score = 0
    count = 0
    for i in syn1:
        synscore=0
        sim=[]
        for j in syn2:
            if i.pos()==j.pos():
                synscore=i.res_similarity(j,  brown_ic)
                if synscore!=None:
                    sim.append(synscore)
                elif i.name().split(".")[0] == j.name().split(".")[0]:
                    sim.append(1)
                synscore=0

        if (len(sim) > 0):
            score += max(sim)
            count += 1

    if count > 0:
        avgScores =score / count
    return avgScores

#lin similarity score
def li_simscore(synsets1, synsets2):
    global avgScores
    avgScores=0
    score = 0
    count = 0
    for i in syn1:
        synscore=0
        sim=[]
        for j in syn2:
            if i.pos()==j.pos():
                synscore=i.lin_similarity(j,  brown_ic)
                if synscore!=None:
                    sim.append(synscore)
                elif i.name().split(".")[0] == j.name().split(".")[0]:
                    sim.append(1)
                synscore=0

        if (len(sim) > 0):
            score += max(sim)
            count += 1

    if count > 0:
        avgScores =score / count

    return avgScores



def val1():
    sent1 = name_var.get()
    sent2 = name_var1.get()
    tokens1 = word_tokenize(sent1)
    tokens1 = [w.lower() for w in tokens1]
    token1 = [w.translate(table) for w in tokens1]
    words1 = [word for word in tokens1 if word.isalpha()]
    words1 = [w for w in words1 if w not in stop_words]
    words1 = [lemmatizer.lemmatize(w) for w in words1]
    # print(words1)

    tokens2 = word_tokenize(sent2)
    tokens2 = [w.lower() for w in tokens2]
    token2 = [w.translate(table) for w in tokens2]
    words2 = [word for word in tokens2 if word.isalpha()]
    words2 = [w for w in words2 if w not in stop_words]
    words2 = [lemmatizer.lemmatize(w) for w in words2]
    global syn1
    global syn2
    syn1 = []
    for w in words1:
        for i in wordnet.synsets(w):
            syn1.append(i)
    syn2 = []
    for w in words2:
        for i in wordnet.synsets(w):
            syn2.append(i)

    wup=w_simscore(syn1, syn2)
    jcn = j_simscore(syn1, syn2)
    lch = l_simscore(syn1, syn2)
    path = p_simscore(syn1, syn2)
    lin = li_simscore(syn1, syn2)
    res = r_simscore(syn1, syn2)


    ttk.Label(window, text="WUP: "+str(wup),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=5, column=1)
    ttk.Label(window, text="LCH: " + str(lch),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=6, column=1)
    ttk.Label(window, text="JCN: " + str(jcn),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=7, column=1)
    ttk.Label(window, text="PATH: " + str(path),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=8, column=1)
    ttk.Label(window, text="RES: " + str(res),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=9, column=1)
    ttk.Label(window, text="LIN: " + str(lin),
              background='white', foreground="black",
              font=("Times New Roman", 15)).grid(row=10, column=1)



name_var=tk.StringVar()
name_var1=tk.StringVar()

name_label = tk.Label(window, text = 'Sentence1', font=('calibre',10, 'bold'))
name_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 10, 'normal'))
name_label1 = tk.Label(window, text = 'Sentence2', font=('calibre',10, 'bold'))
name_entry1 = tk.Entry(window, textvariable=name_var1, font=('calibre', 10, 'normal'))
name_label.grid(row=2,column=0)
name_entry.grid(row=2,column=1)
name_label1.grid(row=4,column=0)
name_entry1.grid(row=4,column=1)

sub_btn1=tk.Button(window,text = 'Calculate', command = val1)
sub_btn1.grid(row=5,column=3)
window.mainloop()