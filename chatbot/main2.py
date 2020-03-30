import nltk
import tensorflow
import tflearn

from nltk.stem.lancaster  import LancasterStemmer
import numpy as np
import json
import pickle
import random
stem = LancasterStemmer()

with open("data/intents.json") as file:
    data =  json.load(file)
try:
    with open("data.pickle","rb")  as f:
        words,labels,training,output = pickle.load(f)

except :
    words = []
    labels= []
    docs_x =[]
    docs_y =[]
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wo = nltk.word_tokenize(pattern) # tachs tu
            words.extend(wo)
            docs_x.append(wo)
            docs_y.append(intent["tag"])
            if (intent["tag"] not in labels):
                labels.append(intent['tag'])
    
    words = [stem.stem(w.lower()) for w in words if w != '?']     
    words = sorted(list(set(words)))
    # print (words)
    labels =sorted(labels)
    training = []
    output = []
    out_empty = [ 0 for _ in range(len(labels))]
    for x,doc in enumerate(docs_x):
        bag = []
        wrds = [stem.stem(x) for x in doc]
        for w in words :
            if w in wrds:
                bag.append(1)
            else :
                bag.append(0)
        output_row = out_empty[:]
        output_row  [labels.index(docs_y[x])] = 1
        training.append(bag)
        output.append(output_row)
        with open("data.pickle","wb") as f:
            pickle.dump((words,labels,training,output),f)
    training = np.array(training)
    output = np.array(output)
    tensorflow.reset_default_graph()
    net = tflearn.input_data(shape=[None,len(training[0])])
    net = tflearn.fully_connected(net,8)
    net = tflearn.fully_connected(net,8)
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
    s_words = nltk.word_tokenize(words)
    s_words =  [stem.stem(word.lower()) for word in words]
    for se in s_words :
        for i ,w in enumerate(words):
            if w == se:
                bag[i] = 1 
    return np.array(bag)
def chat() :
    print ("start")
    while True:
        inp = input("You:")
        if inp.lower() == "quit":
            break
        results =  model.predict([bag_of_words(inp,words)])[0]
        results_index = np.argmax(results)
        tag = labels[results_index]
        if results[results_index] >0.7 :
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    repo = tg['responses']
            print(random.choice(repo))
        else :
            print ("khoong hieu cau do")


chat()