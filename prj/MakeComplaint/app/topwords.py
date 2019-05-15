from gensim.summarization import keywords
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.tokenize import word_tokenize 


def most_repeated_keywords(dfwater,dfpwd,dfksrtc,dfkseb,dfenv,water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq,status ):
    if status == 'manual':      
        #print("\n\n Water Freq newwwwwwwwww")
        #print(water_freq)
        #=================================================   Water 
        water_lis =[]
        
        
        items = [(v, k) for k, v in water_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        #print(items)

        water_dict=(items[:5])
        water_lis.append(water_dict)            
        #print("\n\nKEYWORDS  WATER\n\n")
        #print(water_lis) 
        
        #==================================================  PWd       
        #print("\n\n PWD Freq newwwwwwwwww")
        #print(pwd_freq)
        
        pwd_lis =[]
        
        
        items = [(v, k) for k, v in pwd_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        #print(items)

        pwd_dict=(items[:5])
        pwd_lis.append(pwd_dict)

        #print("\n\nKEYWORDS  PWD\n\n")
        #print(pwd_lis)
        
        
        #===================================================  KSEB
        #print("\n\n KSEB Freq newwwwwwwwww")
        #print(kseb_freq)
        
        
        kseb_lis =[]   
        items = [(v, k) for k, v in kseb_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        #print(items)



        kseb_dict=(items[:5])
        kseb_lis.append(kseb_dict)

        #print("\n\nKEYWORDS  KSEB\n\n")
        #print(kseb_lis)
        
        

        
        # ========================================================= KSRTC

        #print("\n\n KSRTC Freq newwwwwwwwww")
        #print(ksrtc_freq)
        
        
        ksrtc_lis =[]
   
        
        items = [(v, k) for k, v in ksrtc_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        
        #print(items)



        ksrtc_dict=(items[:5])
        ksrtc_lis.append(ksrtc_dict)

        #print("\n\nKEYWORDS  KSRTC\n\n")
        #print(ksrtc_lis)
    
    

    
        # ===================================================== ENV
        #print("\n\n ENV Freq newwwwwwwwww")
        #print(env_freq)
        
        
        env_lis =[]
 
    
        items = [(v, k) for k, v in env_freq.items()]
        items.sort()
        items.reverse()
        items = [k  for v, k in items]
        #print(items)



        env_dict=(items[:5])
        env_lis.append(env_dict)

        #print("\n\nKEYWORDS  ENV \n\n")
        #print(env_lis)
        
    
    
        return(water_lis,pwd_lis,ksrtc_lis,kseb_lis,env_lis )
    #water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq
    #dfenv,dfwater,dfpwd,dfksrtc,dfkseb
            
    if status == "lib" :
        #env keyword
        
        env_keyword = []
        env_summary = []
        
        stopwords = list(STOP_WORDS)
        
        #print("\n\nKEYWORD : LIB : ENV\n\n")
        #print(dfenv)
        
        for i, row in dfenv.iterrows():
            env_token = word_tokenize(row['Subject_and_Complaint'])

            result = [i for i in env_token if not i in stopwords]
            #print(result)
            env_keyword.append(result)
            
            str1 = ' '.join(result)
            #map(bytes,env_keyword)
            #print(str1)
            #break
        #print(type(env_token))
            env_summary.append(keywords(str1).split('\n'))
               
        #print(type(env_token[0][0]))
        #print(env_summary)
        
        # water Keyword
        
        water_keyword = []
        water_summary = []
        
        stopwords = list(STOP_WORDS)
        
        #print("\n\nKEYWORD : LIB : Water\n\n")
        
        
        for i, row in dfwater.iterrows():
            water_token = word_tokenize(row['Subject_and_Complaint'])

            result = [i for i in water_token if not i in stopwords]
            #print(result)
            water_keyword.append(result)
            
            str1 = ' '.join(result)
            #map(bytes,env_keyword)
            #print(str1)
            #break
        #print(type(env_token))
            water_summary.append(keywords(str1).split('\n'))
               
        #print(type(env_token[0][0]))
        #print(water_summary)
        
        
        #pwd keyword
        
        pwd_keyword = []
        pwd_summary = []
        
        stopwords = list(STOP_WORDS)
        
        #print("\n\nKEYWORD : LIB : PWD\n\n")
        #print(dfenv)
        
        for i, row in dfpwd.iterrows():
            pwd_token = word_tokenize(row['Subject_and_Complaint'])

            result = [i for i in pwd_token if not i in stopwords]
            #print(result)
            pwd_keyword.append(result)
            
            str1 = ' '.join(result)
            #map(bytes,env_keyword)
            #print(str1)
            #break
        #print(type(env_token))
            pwd_summary.append(keywords(str1).split('\n'))
               
        #print(type(env_token[0][0]))
        #print(pwd_summary)
        
        #env keyword
        
        ksrtc_keyword = []
        ksrtc_summary = []
        
        stopwords = list(STOP_WORDS)
        
        #print("\n\nKEYWORD : LIB : KSRTC\n\n")
        #print(dfenv)
        
        for i, row in dfksrtc.iterrows():
            ksrtc_token = word_tokenize(row['Subject_and_Complaint'])

            result = [i for i in ksrtc_token if not i in stopwords]
            #print(result)
            ksrtc_keyword.append(result)
            
            str1 = ' '.join(result)
            #map(bytes,env_keyword)
            #print(str1)
            #break
        #print(type(env_token))
            ksrtc_summary.append(keywords(str1).split('\n'))
               
        #print(type(env_token[0][0]))
        #print(ksrtc_summary)
        
        #env keyword
        
        kseb_keyword = []
        kseb_summary = []
        
        stopwords = list(STOP_WORDS)
        
        #print("\n\nKEYWORD : LIB : KSEB\n\n")
        #print(dfkseb)
        
        for i, row in dfkseb.iterrows():
            kseb_token = word_tokenize(row['Subject_and_Complaint'])

            result = [i for i in kseb_token if not i in stopwords]
            #print(result)
            kseb_keyword.append(result)
            
            str1 = ' '.join(result)
            #map(bytes,env_keyword)
            #print(str1)
            #break
        #print(type(env_token))
            kseb_summary.append(keywords(str1).split('\n'))
               
        #print(type(env_token[0][0]))
        #print("\n KSEB summary \n")
        #print(kseb_summary)
        return(env_summary,water_summary,pwd_summary,ksrtc_summary,kseb_summary)
        