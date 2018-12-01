'''
DOCUMENT DISTANCE
Lot of common words between two documents will generate a higher dot product.

'''


import re
import numpy as np


doc1 = '''
Vikas is 20 years old, and Ajay is 43 years old.
'''

doc2 = '''
Edward is 37 years old, and his grandfather, Dan, is 102.
'''

list_doc1 = re.findall(r'\w+', doc1)
list_doc2 = re.findall(r'\w+', doc2)

doc1_len = len(list_doc1)
doc2_len = len(list_doc2)

set_all_words = set(list_doc1 + list_doc2)
print(set_all_words)

#set_doc1 = set(list_doc1)
#set_doc2 = set(list_doc2)

word_frequency_doc1 = {}
word_frequency_doc2 = {}
for word in set_all_words :
    word_frequency_doc1[word] = list_doc1.count(word)
    
for word in set_all_words :
    word_frequency_doc2[word] = list_doc2.count(word)

vd1 = np.array(list(word_frequency_doc1.values()))
vd2 = np.array(list(word_frequency_doc2.values()))
print("Vector of Document 1", vd1)
print("Vector of Document 2", vd2)

d1 = np.dot(vd1, vd2)
print("Dot Product:",d1)
d2 = d1 / (doc1_len * doc2_len)
print("Scalable Dot Product:",d2)
distance = np.arccos(d2)
print("Angle between vectors of both the documents:",distance)



