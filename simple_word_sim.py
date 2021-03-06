from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
cb = wordnet.synsets('tree')[0]
ib = wordnet.synsets('house')[0]

print("wup: ", cb.wup_similarity(ib))
print("jcn: ",cb.jcn_similarity(ib,  brown_ic))
print("lch: ",cb.lch_similarity(ib))
print("path: ",cb.path_similarity(ib))
print("res: ",cb.res_similarity(ib,  brown_ic))
print("lin: ",cb.lin_similarity(ib, brown_ic))
