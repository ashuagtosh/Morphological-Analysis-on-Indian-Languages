class Person:
    def __init__(self):
        pass

    def loadFamous(self):
        punjabi_categories = list()
        punjabi_categories = [
                        u"ਨੋਬਲ ਵਿਜੇਤਾ", # Nobel laureate
                        u"ਨੋਬਲ ਐਲੀਵਰਟ",  # Nobel laureate
                        
                        u"ਮਿਲਟਰੀ ਲੀਡਰ",  # Military leader
                        u"ਮਿਲਟਰੀ ਅਵਾਰਡ", # Military award
                        u"ਮਿਲਟਰੀ",   #  Military
                        u"ਹਵਾਈ ਸੈਨਾ", # Air force
                        u"ਫੌਜ",      # Army
                        u"ਨੇਵੀ",        # Navy
                        u'ਵਿਕਟੋਰੀਆ ਕਰਾਸ',    # Victoria Cross
                        u'ਪਰਮਵੀਰ ਚੱਕਰ',     # Param Veer Chakra
                        u'ਮਹਾ ਵੀਰ ਚੱਕਰ',     # Maha Veer Chakra
                        
                        u"ਕਾਰੋਬਾਰ",                   # Business 
                        u"ਕਾਰੋਬਾਰੀ",                   # Businessmen
                        u"ਬਿਜਨੈਸਪਰਸਨ",               # Businessperson
                        
                        u"ਕਲਾਕਾਰ",                   # Artist
                        
                        u"ਖੋਜਕਰਤਾ",                   # Researcher
                        u"ਖੋਜਕਾਰ",                    # Researcher
                        u"ਖੋਜ",                       # Research
                               
                        u"ਐਸਟ੍ਰੌਨੋਟ",                   # Astronaut
                        u"ਪੁਲਾੜ ਯਾਤਰੀ",                # Astronaut
                        
                        u"ਬਾਲੀਵੁੱਡ",                    #Bollywood
                        u'ਆਨੰਦ',                       # Anand
                        u'ਚੋਪੜਾ',                       # Chopra
                        u'ਦਿਓਲ',                       # Deol
                        u'ਦੇਵਗਨ',                      # Devgan
                        u'ਦੱਤ',                         # Dutt
                        u'ਓਬਰਾਏ',                       # Oberoi
                        u'ਪੇਂਟਲ',                        # Paintal
                        u'ਪੁਰੀ',                         # Puri
                        u'ਸਾਹਨੀ',                       # Sahni
                        u'ਕਲਾਕਾਰ',                      # Artist
                        u'ਫਿਲਮ ਨਿਰਮਾਤਾ',                 # Film maker
                        u'ਨਿਰਮਾਤਾ',                      # Maker
                        u'ਡਾਇਰੈਕਟਰ' ,                    #Director
                        
                        u"ਇਤਿਹਾਸ",                      #History
                        
                        u"ਲੋਕਤੋਰ",                       #Folklore
                        
                        u"ਧਾਰਮਿਕ ਅਤੇ ਆਤਮਿਕ ਅੰਕੜੇ",        # Religious and spiritual figure
                        
                        u"ਲੇਖਕ",                              #Writer
                        u'ਪੰਜਾਬੀ ਲੇਖਕ',                        # Punjabi writer
                        u'ਹਿੰਦੀ ਲੇਖਕ',                         # Hindi writer
                        u'ਉਰਦੂ ਲੇਖਕ',                         # Urdu writer                        
                        u'ਅੰਗਰੇਜ਼ੀ ਲੇਖਕ',                       # English writer

                        u"ਪੱਤਰਕਾਰ",                      # Journalist
                        
                        u"ਤਾਮਿਲ ਸਿਨੇਮਾ",                  # Tamil cinema

                        u"ਮਾਡਲ",                         # Model

                        u"ਸੰਗੀਤਕਾਰ",                      # Musician
                        u"ਸੰਗੀਤ",                         # Song
                        u"ਗਾਇਕ",                        # Singer
                        u"ਕਲਾਸੀਕਲ",                      # Classical
                        u"ਬਾਲੀਵੁੱਡ",                        # Bollywood
                        u"ਗਜ਼ਲ",                         # Ghazal
                        u"ਭੰਗੜਾ",                         # Bhangra
                        u"ਪੌਪ",                           # Pop
                        u"ਰਾਕ",                           # Rock

                        u"ਇਨਕਲਾਬੀ ਅਤੇ ਆਜ਼ਾਦੀ ਘੁਲਾਟੀਏ",      # Revolutionary and freedom fighter

                        u"ਨੇਤਾ",                          # Politicians
                        u"ਸਿਆਸਤਦਾਨ",                    #Politicians
                        u"ਰਾਜਨੀਤੀ",                       # Politics

                        u"ਖੇਡਾਂ",                          # Sports
                        u"ਸਪੋਰਟਸ",                       # Sports            
                        u"ਖੇਡ",                          # Sport
                        u"ਖਿਡਾਰੀ",                         # Sportsperson
                        u"ਕ੍ਰਿਕੇਟ",                       # Cricket
                        u"ਹਾਕੀ",                        # Hockey
                        u"ਐਥਲੈਟਿਕਸ",                    # Athletics
                        u'ਐਥਲੀਟ',                      # Athlete
                        u'ਗੋਲਫ',                       # Golf
                        u'ਕੁਸ਼ਤੀ',                        # Wrestling
                        u'ਪਹਿਲਵਾਨ',                     # Wrestler
                        u'ਲੜਾਕੂ',                        # Fighters
                        u'ਨਿਸ਼ਾਨੇਬਾਜ਼ੀ',                    # Shooting
                        u'ਬਾਸਕਟਬਾਲ'                     # Basketball  
                        
                    ]
        
        
        punjabi_subcategories = dict()
        punjabi_subcategories = { u"ਮਿਲਟਰੀ ਲੀਡਰ" : [                   # Military leader  
                                            u'ਹਵਾਈ ਸੈਨਾ',               # Air force
                                            u'ਫੌਜ',                    # Army
                                            u'ਨੇਵੀ'                     # Navy
                                            ],
                        
                                  u"ਮਿਲਟਰੀ ਅਵਾਰਡ" : [                   # Military award
                                            u'ਵਿਕਟੋਰੀਆ ਕਰਾਸ',            # Victoria Cross
                                            u'ਪਰਮਵੀਰ ਚੱਕਰ',              # Param Veer Chakra
                                            u'ਮਹਾ ਵੀਰ ਚੱਕਰ'              # Maha Veer Chakra         
                                            ],

                                  u"ਬਾਲੀਵੁੱਡ" : [                             # Bollywood
                                            u'ਆਨੰਦ',                       # Anand
                                            u'ਚੋਪੜਾ',                       # Chopra
                                            u'ਦਿਓਲ',                       # Deol
                                            u'ਦੇਵਗਨ',                       # Devgan
                                            u'ਦੱਤ',                         # Dutt
                                            u'ਓਬਰਾਏ',                       # Oberoi
                                            u'ਪੇਂਟਲ',                        # Paintal
                                            u'ਪੁਰੀ',                         # Puri
                                            u'ਸਾਹਨੀ',                       # Sahni
                                            u'ਕਲਾਕਾਰ',                      # Artist
                                            u'ਫਿਲਮ ਨਿਰਮਾਤਾ',                 # Film maker
                                            u'ਨਿਰਮਾਤਾ',                      # Maker
                                            u'ਡਾਇਰੈਕਟਰ'                     #Director
                                            ],
                                   u"ਲੇਖਕ" : [                              # Writer
                                            u'ਪੰਜਾਬੀ ਲੇਖਕ',                        # Punjabi writer
                                            u'ਹਿੰਦੀ ਲੇਖਕ',                         # Hindi writer
                                            u'ਉਰਦੂ ਲੇਖਕ',                         # Urdu writer                        
                                            u'ਅੰਗਰੇਜ਼ੀ ਲੇਖਕ',                       # English writer
                                          ],
                                   u"ਸੰਗੀਤਕਾਰ" : [
                                            u"ਸੰਗੀਤਕਾਰ",                      # Musician
                                            u"ਸੰਗੀਤ",                         # Song
                                            u"ਗਾਇਕ",                        # Singer
                                            u"ਕਲਾਸੀਕਲ",                      # Classical
                                            u"ਬਾਲੀਵੁੱਡ",                        # Bollywood
                                            u"ਗਜ਼ਲ",                         # Ghazal
                                            u"ਭੰਗੜਾ",                         # Bhangra
                                            u"ਪੌਪ",                           # Pop
                                            u"ਰਾਕ"                           # Rock
                                        ],
                                  
                                    u"ਖਿਡਾਰੀ" : [                              # Sportsperson
                                            u"ਖੇਡਾਂ",                         # Sports
                                            "ਖੇਡ",                          # Sport
                                            "ਸਪੋਰਟਸ",                       # Sports
                                            u"ਕ੍ਰਿਕੇਟ",                         # Cricket
                                            u"ਹਾਕੀ",                          # Hockey
                                            u"ਐਥਲੈਟਿਕਸ",                      # Athletics
                                            u'ਐਥਲੀਟ',                        # Athlete
                                            u'ਗੋਲਫ',                          # Golf
                                            u'ਕੁਸ਼ਤੀ',                          # Wrestling
                                            u'ਪਹਿਲਵਾਨ',                       # Wrestler
                                            u'ਲੜਾਕੂ',                          # Fighters
                                            u'ਨਿਸ਼ਾਨੇਬਾਜ਼ੀ',                       # Shooting
                                            u'ਬਾਸਕਟਬਾਲ'                       # Basketball                                
                                        ]
                        
                                 }
                   
x = Person()
x.loadFamous()
