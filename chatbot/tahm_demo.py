from gensim.models import KeyedVectors 
import numpy as np
import json
import tensorflow
import tflearn
import pickle
import random
w2v = KeyedVectors.load_word2vec_format("vi.vec")
vocab = w2v.wv.vocab #Danh sách các từ trong từ điển

from pyvi import ViTokenizer
with open('data/tahm.json',encoding="utf8") as f:
    data = json.load(f)
try:
    with open("data.pickle","rb")  as f:
        list_words,labels,training,output = pickle.load(f)
except :
    X = []
    list_words = []
    labels = []
    docs_x = []
    docs_y = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern.lower()
            sentence_tokenized = ViTokenizer.tokenize(pattern)
            words = sentence_tokenized.split(" ")      
            list_words.extend(words)
            docs_x.append(words)
            docs_y.append(intent["tag"])
            if (intent["tag"] not in labels):
                    labels.append(intent['tag'])

    list_words = sorted(list(set(list_words)))

    labels =sorted(labels)

    training = []
    output = []
    out_empty = [ 0 for _ in range(len(labels))]
    for x,doc in enumerate(docs_x):
        bag = []
        for w in list_words :
            if w in doc:
                bag.append(1)
            else :
                bag.append(0)
        output_row = out_empty[:]
        output_row  [labels.index(docs_y[x])] = 1
        training.append(bag)
        output.append(output_row)
        with open("data.pickle","wb") as f:
            pickle.dump((list_words,labels,training,output),f)
training = np.array(training)
output = np.array(output)
tensorflow.reset_default_graph()
net = tflearn.input_data(shape=[None,len(training[0])])
net = tflearn.fully_connected(net,128)
net = tflearn.fully_connected(net,68)
net = tflearn.fully_connected(net,len(output[0]),activation='softmax')
net = tflearn.regression(net)
try :
    model.load("model.tflearn")
except:
    model = tflearn.DNN(net)
    model.fit(training,output,n_epoch=1000,show_metric=True,batch_size=8)
    model.save("model.tflearn")




def bag_of_words(s,words):
    bag = [0 for _ in range(len(words))]
    s_words = ViTokenizer.tokenize(s)
    s_words = s_words.split(" ") 
    # s_words =  [stem.stem(word.lower()) for word in words]
    for se in s_words :
        for i ,w in enumerate(words):
            if w == se:
                bag[i] = 1 
    return np.array(bag)
def chat() :
    print ("start")
    while True:
        inp = input("You:")
        inp.lower()
        if inp.lower() == "quit":
            break
        results =  model.predict([bag_of_words(inp,list_words)])[0]
        results_index = np.argmax(results)
        tag = labels[results_index]
        if results[results_index] >0.6 :
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    repo = tg['responses']
            print(random.choice(repo))
        else :
            print ("khoong hieu cau do")

def chat2(inp) :
    print ("start")
    while True:
        # inp = input("You:")
        inp.lower()
        if inp.lower() == "quit":
            break
        results =  model.predict([bag_of_words(inp,list_words)])[0]
        results_index = np.argmax(results)
        tag = labels[results_index]
        if results[results_index] >0.6 :
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    repo = tg['responses']
            return  (random.choice(repo))
        else :
            return ("khoong hieu cau do")