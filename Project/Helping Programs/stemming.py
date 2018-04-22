##The objective of any stemmer is to get the
##root of those words which are not in their basic forms and
##are not present in morph/dictionary. After stemming, if
##word is found in morph/dictionary, then it is correct
##word, otherwise it can be name or some incorrect word.

words = [u"ਲੜਕੀਆਂ",
         u"ਮੁੰਡੇ",
         u"ਪੀਲੋ",
         u"ਦੇਖੀਏ",
         u"ਵਡੀਆ",
         u"ਵਡਈਆ",
         u"ਦੇਖੀਓ",
         u"ਿਫਰੋਜ਼ਪੁਰੋਂ",
         u"ਫੁੱਲਾਂ",
         u"ਮਾਂਵਾਂ",
         u"ਮਾਈ",
         u"ਸ਼ਹਿਉ",
         u"ਗਠਿਆ",
         u"ਕੋਠਿਉਂ"
         ]

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


print(repr(u"ਸ਼ਹਿਉ".encode("utf8").decode("utf-8")))



for w in words:
    if(len(w)>=3):
        for l in list_rule1:

            if(l == w[-3:]):  #  ----------------------------------------------> CASE 1

                if(l == u"\u0A35\u0A3E\u0A02"): # for ਵਾਂ
                    print(w[0:len(w)-3])
                    break
                elif(l == u'\u0A3F\u0A09\u0A02'):   # for ਿਉਂ
                    print(w[0:len(w)-3]+u"\u0A3E")
                    break
            
            else:
                if(l == w[-2:]):  #  ----------------------------------------------> CASE 2

                    if(l == u'\u0a06\u0a02'):      # for ਆਂ
                        if(w[-3] == u'\u0A42' or w[-3] == u'\u0A3F' or w[-3] == u'\u0A40'):
                            print(w[0:len(w)-2])
                            break
                    elif(l == u"\u0A3E\u0A02"): # for ਾਂ
                        print(w[0:len(w)-2])
                        break
                    elif(l == u'\u0A40\u0A02'): # for ੀਂ
                        print(w[0:len(w)-2])
                        break
                    elif(l == u'\u0A4B\u0A02'): # for ੋਂ
                        print(w[0:len(w)-2])
                        break
                    elif(l == u'\u0A3F\u0A09'): # for  ਿ◌ਓ
                        print(w[0:len(w)-2]+u"\u0A3E")
                        break
                    elif(l ==  u'\u0A3F\u0A06'):    # for ਿ◌ਆ
                        print(w[0:len(w)-2]+u"\u0A3E")
                        break
            
                else:
                    if(l == w[-1:]): #  ----------------------------------------------> CASE 3  

                        if(l == u"\u0a47" ):    # for ੇ
                            print(w[0:len(w)-1]+u"\u0A3E")
                            break
                        elif(l == u"\u0A4B"):    # for
                            print(w[0:len(w)-1]+u"\u0A3E")
                            break
                        elif(l == u"\u0A0F" ): # for ਏ
                            if(w[-2] == u'\u0A40'):
                                print(w[0:len(w)-1])
                                break
                        elif(l == u"\u0A13"): # for ਓ
                            if(w[-2] == u'\u0A40'):
                                print(w[0:len(w)-1])
                                break
                        elif(l == u"\u0A06"): # for ਆ
                            if(w[-2] == u'\u0A40' or w[-2] == u"\u0A08"):
                                print(w[0:len(w)-1])
                                break
                        elif(l == u"\u0a08" ):  # for ਈ
                            print(w[0:len(w)-1])
                            break
                        else:
                            pass        
            
