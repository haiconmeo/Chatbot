from gensim.models import KeyedVectors 
import numpy as np
w2v = KeyedVectors.load_word2vec_format("vi.vec")
vocab = w2v.wv.vocab #Danh sách các từ trong từ điển

from pyvi import ViTokenizer

X = []
# sentences =["công sở đậm dư âm tết trong ngày đầu làm việc","mạnh học rất giỏi"]
# for sentence in sentences:
#     sentence_tokenized = ViTokenizer.tokenize(sentence)
#     words = sentence_tokenized.split(" ")
#     sentence_vec = np.zeros((100))
#     for word in words:
#         if word in vocab:
#             sentence_vec+=w2v.wv[word]
#     X.append(sentence_vec)
#     print (words)
sentences ="công sở đậm dư âm tết trong ngày đầu làm việc"
sentence_tokenized = ViTokenizer.tokenize(sentences)
words = sentence_tokenized.split(" ")
print (words)