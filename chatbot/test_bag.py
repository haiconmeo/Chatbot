def bag_of_words(s,words):
    bag = [0 for _ in range(len(words))]
    s_words = ViTokenizer.tokenize(s)
    s_words = s_words.split(" ") 
    # s_words =  [stem.stem(word.lower()) for word in words]
    for se in s_words :
        for i ,w in enumerate(words):
            if w == words:
                bag[i] = 1 
    return np.array(bag)
    