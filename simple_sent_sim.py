from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')
import string
table = str.maketrans('', '', string.punctuation)

sent1="Fruits are healthy"
sent2="apple is a fruit"

#text cleaning
tokens1 = word_tokenize(sent1)
tokens1 = [w.lower() for w in tokens1]
token1 = [w.translate(table) for w in tokens1]
words1 = [word for word in tokens1 if word.isalpha()]
words1 = [w for w in words1 if w not in stop_words]
words1=[lemmatizer.lemmatize(w) for w in words1]


tokens2 = word_tokenize(sent2)
tokens2 = [w.lower() for w in tokens2]
token2 = [w.translate(table) for w in tokens2]
words2 = [word for word in tokens2 if word.isalpha()]
words2 = [w for w in words2 if w not in stop_words]
words2=[lemmatizer.lemmatize(w) for w in words2]

syn1=[]
for w in words1:
    for i in wordnet.synsets(w):
        syn1.append(i)
syn2=[]
for w in words2:
    for i in wordnet.synsets(w):
        syn2.append(i)

# def simscore(synsets1, synsets2):
#     score = 0
#     count = 0
#     for i in syn1:
#         synscore=0
#         sim=[]
#         for j in syn2:
#             if i.pos() == j.pos():
#                 synscore=i.wup_similarity(j)
#                 if synscore!=None:
#                     sim.append(synscore)
#                 elif i.name().split(".")[0] == j.name().split(".")[0]:
#                     sim.append(1)
#                 synscore=0
#
#
#         if (len(sim) > 0):
#             score += max(sim)
#             count += 1
#
#     if count > 0:
#         avgScores =score / count
#
#
#     print(avgScores)
#
# simscore(syn1, syn2)

def w_simscore(syn1, syn2):
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

    print("wup: ",avgScores)
w_simscore(syn2, syn1)