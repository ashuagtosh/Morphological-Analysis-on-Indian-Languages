import copy,re,os
import numpy as np
import math
import Classifier

headline = ""
author = ""

NOUNS_LIST = list()
ADJECTIVES_LIST = list()
VERBS_LIST = list()
ADVERBS_LIST = list()
index_list = list()
STOPS_LIST =[
             u'ਦੇ', #used to show the possession
             u'ਦੀ', #used same as above but is just a feminine of above words
             u'ਵਿਚ', #used as preposition, for 'inside'
             u'ਦਾ', #again used as possession
             u'ਨੂੰ', #  stop word has no meaning on its own, but used in sentence
             u'ਹੈ', # usually used at the end of sentence, shows present tense
             u'ਹੀ', #again a stop word without any meaning
             u'ਹੇ', # used in same sence as 'Oh' word
             u'ਕੇ', #same used as the for possession, but it is close to hindi
             u'ਉਸ',#used in sense of 'his/her'
             u'ਨਹੀਂ',#means no of denial
             u'ਤੇ',#used for 'on' or 'after'
             u'ਉਹ',#used as 'he'
             u'ਤੋਂ',#used as 'after this'
             u'ਨਾਲ',#means 'with'
             u'ਹੋ',#used like 'doing'
             u'ਇਹ',#means 'this'
             u'ਭੀ',# means 'also'
             u'ਨੇ', #a stop word, without meaning on its own, difficult to teach its meaning
             u'ਕਰ', #means 'doing'
             u'ਜਿਸ',# used as 'who'
             u'ਇਸ',# used as 'this' refer to an object
             u'ਆਪਣੇ',#means 'our'
             u'ਜੋ', #used like 'who' but may have different meanings at different times
             u'ਮੈਂ', #means 'me'
             u'ਕੋਈ',# used like 'any' or 'anyone'
             u'ਵਾਲਾ',#used in sense like having a property of something
             u'ਆਪ',#means 'myself'
             u'ਤੂੰ', #many meanings depend on situation, may be used for 'after sometime' or 'after some place'
             u'ਕਰਦਾ', #similar to 'doing'
             u'ਕਿ', #a type of connector connect sentences similar way as 'because' does
             u'ਉਹਨਾਂ',#used as 'they'
             u'ਜੀ',#used as 'yes' but by giving some respect
             u'ਤਾਂ',#used as 'after'
             u'ਕਰਨ',#used as 'doing'
             u'‘ਚ', # used same as ਵਿਚ
             u'ਸਭ',#means 'everyone'
             u'ਜਾ',#means 'going'
             u'ਰਹਿੰਦਾ',#means 'living' or 'live there'
             u'ਵਾਲੇ',# similar to 'ਵਾਲਾ'
             u'ਹਨ', # similar to 'ਹੈ' but used usually with plural
             u'ਹੋਰ', # used as 'and'
             u'ਪਰ', # means 'but'
             u'ਜੇ', # means 'if'
             u'ਕੀ', # various meanings like 'what'
             u'ਜਾਂਦੇ',# means 'going'
             u'ਅਤੇ',# means 'and'
             u'ਕਿਸੇ',# used as 'who' or 'whoever'
             u'ਨਾਹ', # used for denial
             u'ਹੋਇਆ', # used for 'work has done'
             u'ਰਿਹਾ', # used as 'work going on'
             u'ਜਾਂਦੀ', # used as 'going'
             u'ਮਿਲ', # means 'meet'
             u'ਉਤੇ', # used as 'above'
             u'ਹੁੰਦਾ', # a stopword used to denote present tense
             u'ਤੇਰੇ', # means 'yours'
             u'ਰਹਾਉ', # means 'liveable'
             u'ਆ',# close to meaning 'comming' but not exactly same
             u'ਹੋਏ',# close to meaning present but its not exactly same
             u'ਦੂਰ',# means 'far'
             u'ਬਿਨਾ',# means 'without'
             u'ਪੈਦਾ', # means 'birth'
             u'ਲੈਂਦਾ', # means 'taking'
             u'ਮੈਨੂੰ', # used like 'me'
             u'ਕਾ', #used like 'his' but close to hindi
             u'ਦੇਂਦਾ',# used as 'giving'
             u'ਲਈ',# no prefect meaning in engilish, but is close to 'for'
             u'ਕਿਰਪਾ', # means 'please'
             u'ਦੇਣ', # means like 'giving'
             u'ਹਰ', # used like 'every'
             u'ਰਹਿੰਦੇ', # means 'living'
             u'ਮੇਰਾ', # means 'mine'or 'my'
             u'ਜੀਵਾਂ',# means 'like'
             u'ਪੈ', # a word without any meaning, but we can say that it means like 'lie down', under some circumstances
             u'ਹਰੇਕ',# means 'everyone'
             u'ਤੇਰੀ',#means 'yours'
             u'ਤੇਰਾ',#same as above meaning
             u'ਕਰਦੇ',#used like 'they do' or 'he do'
             u'ਆਪਣਾ',#means 'our'
             u'ਸਕਦਾ',#usually used like 'able'
             u'ਜਦੋਂ',# used as 'when'
             u'ਬਣ',# usually used like 'made'
             u'ਕਰਿ',# used as 'do' but not used in modern punjabi
             u'ਹੋਈ',# usually used like 'happens'
             u'ਦੀਆਂ', # many meaning not clear but one of them is 'his possession'
             u'ਥਾਂ', # means 'place'
             u'ਆਪਣੀ',#means 'our'
             u'ਕੁਝ', # means 'something'
             u'ਪੈਂਦਾ', # no clear meaning
             u'ਵਾਲੀ',# means 'having property'
             u'ਵੇਲੇ',# used like 'saga' or 'time' or 'time of day'
             u'ਆਪੇ',# used like 'you'
             u'ਆਦਿਕ',# means like 'etc.'
             u'ਵਾਸਤੇ',# used like 'for sake of'
             u'ਇਹਨਾਂ',# used like 'their'
             u'ਕਦੇ', # used like 'ever'
             u'ਮਨੁ', # old punjabi word means 'assume'
             u'ਹੋਇ', # means 'done'
             u'ਰਹੇ', # means 'lived'
             u'ਉਹੀ', # means like 'he/she'
             u'ਰਹਿ', # no specific meaning, used with 'doing' but does not means 'doing'
             u'ਮੇਰੀ',# means 'mine'
             u'ਵਿਚੋਂ',# used like 'inside'
             u'ਤਾ', # usually used like 'submission'
             u'ਪਾਇਆ', # used for many meanins like 'wear' and 'found'
             u'ਕੀਤਾ', # means 'done'
             u'ਲੈ', # means like 'taken'
             u'ਪਾ', # used like 'worn'
             u'ਸਾਰੀ',# used like 'all'
             u'ਕਈ', # means 'many' but not know how many
             u'ਲਿਆ',# means 'taken' or used with 'done'
             u'ਦਿੱਤਾ',#means 'given'
             u'ਤਰ੍ਹਾਂ',#means 'ways'
             u'ਕੰਮ',# means 'job'
             u'ਸਮਝ',#means 'understanding'
             u'ਆਪਿ',#means 'ourselves'
             u'ਜਿਵੇਂ',# means 'like'
             u'ਉੱਤੇ',#means 'on'
             u'ਤਦੋਂ',#used like 'when' but after some event
             u'ਕੋ', #no meanings on its own
             u'ਨਾ', #used like denial or may be used 'name'
             u'ਹਾਂ', #used for ending the sentence
             u'ਮੈ', #means 'me'
             u'ਨੰ:', #no meaning on its own
             u'ਸੀ', #used to end sentence but denote past tense
             u'ਨਾਹੀ', #means no or denial
             u'ਫਿਰ', # means 'then' but this word is close to hindi
             u'ਇਉਂ', #old punjabi word close to meaning 'this way'
             u'ਉਸੇ', #old punjabi word meaning 'he/she'
             u'ਰੇ',  #used like 'Oh'
             u'ਸੇ', #no meaning on its own
             u'ਇਹੁ',#means 'this way'
             u'ਕਿਸ',#used like 'whoes' or 'who'
             u'ਵਲ' #used like 'his/her side' like 'giving edge to'
            ]

def removePunctuation(text):
    puncList = [u".",u":",u"/",u"\\",u"#",u"@",u"$",u"&",u"\""]
    for i in puncList:
            text = text.replace(i,u'')
    return text

def createSentences(text): # Sentence Tokenizing
    sentence_list = list()
    count = 0
    global headline
    global author
    for para in text:
        #print(type(para))
        #para = para.encode("utf-8")
        i = 0;
        j=0;
        while i != len(para):
            if((para[i] == u'।') or (para[i] == u'!') or (para[i] == u'?') ):
                if(para[j] == u" "):
                    #print("yes")
                    sentence_list.insert(count,para[j+1:i])
                else:
                    sentence_list.insert(count,para[j:i])
                j = i+1
                count = count + 1
            i = i+1
            if u'।' not in para:
                author = para.rstrip() # Newline Stripping
    
    return sentence_list

def createWords(text): # Word Tokenizing
    word_list = list()
    word_list = copy.deepcopy(re.split(r'[\s*]|[\,|\?][\s]|[\,]|[\?]', text))
    #print(word_list)
    return word_list

#create_PreprocessedWords(sent)

def create_PreprocessedWords(text): # Word Tokenizing STOP WORDS REMOVAL
    word_list = list()
    word_list = copy.deepcopy(re.split(r'[\s*]|[\,|\?][\s]|[\]|[\?]', text))
    
    for word in STOPS_LIST:

        if(word in word_list):
            word_list.remove(word)
        else:
            pass

    return word_list

def stemming(w): # STEMMING
    list_rule1 = [u'\u0a06\u0a02',
         u"\u0A0F",
         u"\u0a47",
         u"\u0A4B",
         u"\u0A13",
         u"\u0A06",
         u"\u0A35\u0A3E\u0A02",
         u"\u0A08",
         u"\u0A3E\u0A02",
         u'\u0A40\u0A02',
         u'\u0A4B\u0A02',
         u'\u0A3F\u0A09',
         u'\u0A3F\u0A06',
         u'\u0A3F\u0A09\u0A02'
      ]  # -------->  ਆਂ , ਏ , ੇ, ੋ , ਓ , ਆ, ਵਾਂ, ਈ, ਾਂ, ੀਂ, ੋਂ, ਿ◌ਓ,  ਿ◌ਆ, ਿਉਂ

    x = w
    
    if(len(w)>=3):
        for l in list_rule1:

            if(l == w[-3:]):  #  ----------------------------------------------> CASE 1

                if(l == u"\u0A35\u0A3E\u0A02"): # for ਵਾਂ
                    x = w[0:len(w)-3]
                    break
                elif(l == u'\u0A3F\u0A09\u0A02'):   # for ਿਉਂ
                    x = w[0:len(w)-3]+u"\u0A3E"
                    break
            
            else:
                if(l == w[-2:]):  #  ----------------------------------------------> CASE 2

                    if(l == u'\u0a06\u0a02'):      # for ਆਂ
                        if(w[-3] == u'\u0A42' or w[-3] == u'\u0A3F' or w[-3] == u'\u0A40'):
                            x = w[0:len(w)-2]
                            break
                    elif(l == u"\u0A3E\u0A02"): # for ਾਂ
                        x = w[0:len(w)-2]
                        break
                    elif(l == u'\u0A40\u0A02'): # for ੀਂ
                        x = w[0:len(w)-2]
                        break
                    elif(l == u'\u0A4B\u0A02'): # for ੋਂ
                        x = w[0:len(w)-2]
                        break
                    elif(l == u'\u0A3F\u0A09'): # for  ਿ◌ਓ
                        x = w[0:len(w)-2]+u"\u0A3E"
                        break
                    elif(l ==  u'\u0A3F\u0A06'):    # for ਿ◌ਆ
                        x = w[0:len(w)-2]+u"\u0A3E"
                        break
            
                else:
                    if(l == w[-1:]): #  ----------------------------------------------> CASE 3  

                        if(l == u"\u0a47" ):    # for ੇ
                            x = w[0:len(w)-1]+u"\u0A3E"
                            break
                        elif(l == u"\u0A4B"):    # for
                            x = w[0:len(w)-1]+u"\u0A3E"
                            break
                        elif(l == u"\u0A0F" ): # for ਏ
                            if(w[-2] == u'\u0A40'):
                                x = w[0:len(w)-1]
                                break
                        elif(l == u"\u0A13"): # for ਓ
                            if(w[-2] == u'\u0A40'):
                                x = w[0:len(w)-1]
                                break
                        elif(l == u"\u0A06"): # for ਆ
                            if(w[-2] == u'\u0A40' or w[-2] == u"\u0A08"):
                                x = w[0:len(w)-1]
                                break
                        elif(l == u"\u0a08" ):  # for ਈ
                            x = w[0:len(w)-1]
                            break
                        else:
                            pass
    
    return x

def load_VocabLists():
    global NOUNS_LIST, ADJECTIVES_LIST, VERBS_LIST, ADVERBS_LIST
    list_POS = ["NOUN.npy","ADJECTIVE.npy","VERB.npy","ADVERB.npy"]

    no_POS = 0
    for pos in list_POS:
        goal_path = os.getcwd()
        array = np.load(goal_path+"/"+pos)
        for line in array:
            #print(type(line))
            line = line.decode("utf-8").strip()
            word_list = list()
            word_list = copy.deepcopy(re.split(r'[\s*]|[\,|\?][\s]|[\,\?]', line))
            if(no_POS == 0):
                NOUNS_LIST.extend(word_list)
            elif(no_POS == 1):
                ADJECTIVES_LIST.extend(word_list)
            elif(no_POS == 2):
                VERBS_LIST.extend(word_list)
            elif(no_POS == 3):
                ADVERBS_LIST.extend(word_list)
        no_POS = no_POS + 1
           
    return

def generateKeywords(nouns,words,nouns2_original):
    all_words = list()
    tf_scores = dict()
    count = 0
    k = 0
    for i in range(0,len(nouns)):
        list_tf = list()
        for w in range(0,len(nouns[i])):
            all_words.insert(k,nouns2_original[i][w])
            list_tf.insert(k,str(words[i].count(nouns[i][w])))

            k = k + 1 # incrementing list indices

        tf_scores[i] = list_tf

    temp = copy.deepcopy(all_words)
    #print(len(all_words))

    for w in temp:
        if(all_words.count(w)>1):
            all_words.remove(w)

    #print(len(all_words))

    isf_scores = dict()
    for i in range(0,len(all_words)):
        count = 0
        for j in range(0,len(tf_scores)):
            if(all_words[i] in nouns2_original[j]):
                count = count + 1

        isf_scores[i] = count
    
    #print(len(isf_scores))

    for i in range(0,len(tf_scores)):
        for j in range(0,len(tf_scores[i])):
             for k in range(0,len(all_words)):
                if(nouns2_original[i][j] == all_words[k]):
                    x = float(len(tf_scores))/isf_scores[k]
                    x = math.log(x,10)
                    tf_scores[i][j] = float(tf_scores[i][j])*x
                    #print("Success")
                else:
                    pass
    dic1 = dict()
    dic2 = dict()
    k = 0
    for i in range(0,len(tf_scores)):
        for j in range(0,len(tf_scores[i])):
            dic1[k] = nouns2_original[i][j]
            dic2[k] = tf_scores[i][j]
            k = k + 1
 
    dict_keywords = dict()
    for x in range(0,len(all_words)/5):
        maxim = dic2[0]
        m = dic1[0]
        z = 0
        for i in range(0,len(dic2)):
            if(dic2[i]>maxim):
                maxim = dic2[i]
                m = dic1[i]
                z = i
        #print(z)
        dic2[z] = 0
        dict_keywords[x] = m
    return dict_keywords

def identifyNouns(list_w):
    listt = list()
    global index_list
    index_list[:] = []
    count = 0
    ind = 0
    for word in list_w:
        if(list_w[ind] in NOUNS_LIST):
            listt.insert(count,list_w[ind])
            index_list.insert(count,ind)
            count = count + 1
        else:
            pass
        ind = ind + 1
        
    return listt

def findPlaces(word):
    x = 0
    inst = Classifier.Locations()
    
    towns = inst.loadTowns()
    villages = inst.loadVillages()
    
    for key in towns:
        for town in inst.towns[key]:
            if(word == town):
                return True
    for key in villages:
        for village in inst.villages[key]:
            if(word == village):
                return True
    return False

def findNamedEntities(dict_pwords):
    ne = list()
    k = 0
    for i in range(len(dict_pwords)):
        for word in dict_pwords[i]:
            if(findPlaces(word)):
                ne.insert(k,word)
                k = k + 1
            else:
                pass

    return ne

# *********************************************************************     Main Function    ********************************************************************************************

def main():
    fp = open("news.txt")
    input_text = fp.readlines()
    i  = 0
    
    for para in input_text:
        para = para.decode("utf-8")
        input_text[i] = removePunctuation(para)
        i = i+1 

        
    info_no_of_paragraphs = len(input_text)
    list_sentences = list()
    list_of_sentences = copy.deepcopy(createSentences(input_text)) # List of all Sentences is build
    info_no_of_sentences = len(list_of_sentences)

    dict_words = dict() # Dictionary of words corresponding to each sentence in generated

    i = 0
    for sent in list_of_sentences:
        dict_words[i] = createWords(sent)
        i = i + 1
        
    dict_pwords = dict() # Dictionary of words afer preprocessing corresponding to each sentence

    i = 0
    for sent in list_of_sentences:
        dict_pwords[i] = create_PreprocessedWords(sent.strip())
        i = i + 1
##    for w in dict_pwords[81]:
##        print(w)
##    print("\n")
    load_VocabLists()

    dict_noun_keywords = dict() # ALso Containing empty string
    for i in range(0,len(list_of_sentences)):
        if(len(identifyNouns(dict_pwords[i])) ==0 ):
            dict_noun_keywords[i] = [u'']
        else:
            dict_noun_keywords[i] = identifyNouns(dict_pwords[i])
            dict_noun_keywords[i] = set(dict_noun_keywords[i])
            dict_noun_keywords[i] = list(dict_noun_keywords[i])

    dic_words_stemming = dict() # Dictionary of words to be Stemmed

    for i in range(len(list_of_sentences)):
        dic_words_stemming[i] = set(dict_pwords [i])-set(dict_noun_keywords[i])
        dic_words_stemming[i] = list(dic_words_stemming[i])
        
    
##    for i in dict_noun_keywords[0]:   
##        print(i)
##    print("\n\n")
####    for i in dic_words_stemming[0]:
####        print(i)

    dic_stemming_keywords = dict()  # Dictionary of words after steming corresponding to sentences

    for i in range(len(list_of_sentences)):
        li = list()
        count = 0
        for word_x in dic_words_stemming[i]:
            li.insert(count,stemming(word_x))
            count = count+1
        dic_stemming_keywords[i] = li

##    for i in range(0,len(dic_stemming_keywords[0])):
##        print(dic_stemming_keywords[0][i] + "      " + dic_words_stemming[0][i])

    dic_sm = dict()
    dic_sm2 = dict()
    dict_noun_keywords2 = dict()
    
    for i in range(len(list_of_sentences)):
        
        fake2 = copy.deepcopy(dict_noun_keywords[i])
        dict_noun_keywords2[i] = fake2
        fake = copy.deepcopy(dic_stemming_keywords[i])
        temp = copy.deepcopy(dic_stemming_keywords[i])
        for q in range(0,len(temp)):
            if(temp[q] in dic_words_stemming[i]):
                dic_stemming_keywords[i].remove(temp[q])
                
        common_words1 = copy.deepcopy(dic_stemming_keywords[i])

        if(len(identifyNouns(common_words1)) ==0 ):
            dic_sm[i] = [u'']
        else:
            dic_sm[i] = identifyNouns(common_words1)
        dict_noun_keywords[i].extend(dic_sm[i])

        global index_list

        temp1 = copy.deepcopy(dic_words_stemming[i])
        for q in range(0,len(temp1)):
            if(temp1[q] in fake):
                dic_words_stemming[i].remove(temp1[q])

        common_words2 = copy.deepcopy(dic_words_stemming[i])


            
        temp3 = list()
        temp3 = copy.deepcopy(common_words2)

        for v in range(0,len(common_words2)):
            if(v in index_list):
                pass
            else:
                common_words2.remove(temp3[v])
        dic_sm2[i] = common_words2


        dict_noun_keywords2[i].extend(dic_sm2[i])

    

    keywords = dict()
    keywords = generateKeywords(dict_noun_keywords2,dict_pwords,dict_noun_keywords)    
##    for i in range(0,len(keywords)):
##        print(keywords[i])

    ne = list()
    ne = findNamedEntities(dict_pwords)
            
    print("******** Early Information **********")
    print("No. of Paragraphs : "+ str(info_no_of_paragraphs))
    print("No. of Sentences : "+ str(info_no_of_sentences))
    print("Author : "+ author)
    print("Headline :"+ headline)
    print("Keywords :"+ str(len(keywords)))
    print("Named Entities are :")
    print "[",
    for entity in ne:
        print entity,
    print "]"
    return

main()
