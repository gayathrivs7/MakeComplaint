import pandas as pd
from nltk.corpus import stopwords 
import nltk
from nltk.tokenize import word_tokenize 
from collections import Counter
from gensim.summarization import keywords
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import spacy
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer




global dataset


class Main:
         
    global departments
    
    
    def __init__(self,dataset,nlp):
        #/home/gayathri/project/MakeComplaint/data.csv
        self.dataset=dataset
        #print(self.dataset)
        self.dataset= pd.read_csv(self.dataset)
        self.nlp =nlp
         
        
        pass
    
    def department_class(self):
        departments=self.dataset['Departments'].unique()
        return departments
        
    
    def punctuate(self):
        punctuations = '''!()-[]{};:'"\,.<>/?@#$%^&*_~'''
        text=self.dataset['Subject']

        # To take input from the user
        # my_str = input("Enter a string: ")

        # remove punctuation from the string
        no_punct = ""
        no_punctuate =[]
        for char in  self.dataset['Subject']:

            if char not in punctuations:
                no_punct = no_punct + char
                no_punctuate.append(no_punct)

        # display the unpunctuated string
        #print(no_punctuate)
        return(no_punctuate)

        
    def data_clean(self):
        
        
       
        print(self.dataset.head())
        # unpunctuate and lower case
        self.dataset['Subject'] = self.dataset['Subject'].str.replace('[^\w\s]','').str.lower()


            # unpunctuate and lower case
        self.dataset['Complaint'] =  self.dataset['Complaint'].str.replace(',',' ').str.lower() 
        self.dataset['Subject'] = self.dataset['Subject'].str.replace('[^\w\s]','').str.lower()
        self.dataset['Complaint'] = self.dataset['Complaint'].str.replace('[^\w\s]','').str.lower()
        self.dataset['Subject'] = self.dataset['Subject'].str.replace('[^\P{P}-]','').str.lower()
        #print( self.dataset.head())



        #rRemoving new lines in the subject field
        self.dataset['Subject'] =  self.dataset['Subject'].str.rstrip('\n')

        #removing Numeric 
        self.dataset['Complaint'] =  self.dataset['Complaint']
        print( self.dataset.head())
        
    def dataframing(self,dataset):
        # creating dataframe for each departments
        water = dataset.loc[dataset['Departments'] == 'Water Authority']
        pwd = dataset.loc[dataset['Departments'] == 'PWD']
        ksrtc = dataset.loc[dataset['Departments'] == 'KSRTC']
        kseb = dataset.loc[dataset['Departments'] == 'KSEB']
        env = dataset.loc[dataset['Departments'] == 'Environment and climate change']
        print(env.shape)    #(30, 4)
        #print(water.shape)  #(39, 4)
        #print(pwd.shape)    #(42, 4)
        #print(ksrtc.shape)  #(17, 4)
        #print(kseb.shape)   #(22, 4)
        #dataset.head()
        #print(pwd)

  

        #Filtering out Subjects and complaints from the dataframe
        df_water = water[['Subject','Complaint']]
        df_pwd   = pwd[['Subject','Complaint']]
        df_ksrtc = ksrtc[['Subject','Complaint']]
        df_kseb  = kseb[['Subject','Complaint']]
        df_env   = env[['Subject','Complaint']]

        dfwater  = df_water[['Subject','Complaint']]
        dfpwd    = df_pwd[['Subject','Complaint']]
        dfksrtc  = df_ksrtc[['Subject','Complaint']]
        dfkseb   = df_kseb[['Subject','Complaint']]
        dfenv    = df_env[['Subject','Complaint']]

        
        dfwater['Subject_and_Complaint'] = df_water['Subject'] + " "+ df_water['Complaint']
        dfwater=dfwater[['Subject_and_Complaint']]
        
        dfpwd['Subject_and_Complaint'] = df_pwd['Subject'] + " "+ df_pwd['Complaint']
        dfpwd=dfpwd[['Subject_and_Complaint']]
        
        dfksrtc['Subject_and_Complaint'] = df_ksrtc['Subject'] + " "+ df_ksrtc['Complaint']
        dfksrtc=dfksrtc[['Subject_and_Complaint']]
        
        dfkseb['Subject_and_Complaint'] = df_kseb['Subject'] + " "+ df_kseb['Complaint']
        dfkseb=dfkseb[['Subject_and_Complaint']]
        
        dfenv ['Subject_and_Complaint'] = df_env['Subject'] + " "+ df_env['Complaint']
        dfenv =dfenv [['Subject_and_Complaint']]
        print(dfenv )
        return (dfwater,dfpwd,dfksrtc,dfkseb,dfenv)
        
        
    def tokenisation(self,dfwater,dfpwd,dfksrtc,dfkseb,dfenv):
        water_token = []
        water_list=[]
            #Tokenising water data
            
        #lemmatizer = WordNetLemmatizer()
        
        #lemmatizer.lemmatize("corpora")
        stop_words = set(stopwords.words('english'))
        for i, row in dfwater.iterrows():
                #print(i,row['Subject'], row['Complaint'])
                
            water_token = word_tokenize(row['Subject_and_Complaint'])
            result = [i for i in water_token if not i in stop_words]
            #lemmatized_output = [i for i in lemmatizer.lemmatize(i) for i in result]
        
            water_list.append(result)
        print("\n\nWater Tokens\n\n")
        print(water_list)
    #water_token.append(tokenizer.tokenize(row['Subject_and_Complaint']))
        pwd_token = []

        pwd_list = []
        #Tokenising pwd data  
        
        for i, row in dfpwd.iterrows():
        #print(i,row['Subject'], row['Complaint'])
            pwd_token = word_tokenize(row['Subject_and_Complaint'])

            result1 = [i for i in pwd_token if not i in stop_words]
            pwd_list.append(result1)
            
        print("\n\nPWD Tokens\n\n")
        print(pwd_list)
            
            #print( pwd_token)


        ksrtc_token =[]
        ksrtc_list =[]
        #Tokenising ksrtc data    
        for i, row in dfksrtc.iterrows():
            #print(i,row['Subject'], row['Complaint'])
            ksrtc_token = word_tokenize(row['Subject_and_Complaint'])
            result = [i for i in ksrtc_token if not i in stop_words]
            ksrtc_list.append(result)
            #print(ksrtc_list)
            #print( ksrtc_token)
            
            
            
        kseb_token = []
        kseb_list= []
        #Tokenising kseb data    
        for i, row in dfkseb.iterrows():
        #print(i,row['Subject'], row['Complaint'])
            kseb_token = word_tokenize(row['Subject_and_Complaint'])
            result = [i for i in kseb_token if not i in stop_words]
            kseb_list.append(result)
        #print(kseb_list)
        #print(kseb_token)
        
        
        env_token = []
        env_list = []
        #Tokenising env data  
        
        for i, row in dfenv.iterrows():
            #print(i,row['Subject'], row['Complaint'])
            env_token = word_tokenize(row['Subject_and_Complaint'])
            result = [i for i in env_token if not i in stop_words]
            env_list.append(result)
            
        
        #print(env_list)
        
        porter=PorterStemmer()
        stemmer = SnowballStemmer("english")
        lemmatizer = WordNetLemmatizer()
        ############################################ENV lemm
        env_stem = []
        
        # ps.stem(w)) 
        print("\n\nfor Stemming \n\n")
        env_inner=[]
        for li in env_list:
            env_inner=[]
            for j in li:
                #st=porter.stem(j)
                st=stemmer.stem(j)
                
                env_inner.append(st)
            env_stem.append(env_inner)
        print(env_stem)
        
        #lemma
        env_lemm = []
        
        # ps.stem(w)) 
        print("\n\nfor Lemmatisation\n\n")
        env_inner=[]
        for li in env_stem:
            env_inner=[]
            for j in li:
                
                lm = lemmatizer.lemmatize(j)
                
                env_inner.append(lm)
            env_lemm.append(env_inner)
        print(env_lemm)
#======================================================  water
        water_stem = []
        
        # ps.stem(w)) 
        print("\n\nfor Stemming \n\n")
        water_inner=[]
        for li in water_list:
            water_inner=[]
            for j in li:
                #st=porter.stem(j)
                st=stemmer.stem(j)
                
                water_inner.append(st)
            water_stem.append(water_inner)
        print(water_stem)
        
        #lemma
        water_lemm = []
        
        # ps.stem(w)) 
        print("\n\nfor Lemmatisation\n\n")
        water_inner=[]
        for li in water_stem:
            water_inner=[]
            for j in li:
                
                lm = lemmatizer.lemmatize(j)
                
                water_inner.append(lm)
            water_lemm.append(water_inner)
        print(water_lemm)
        #======================================================  pwd
        pwd_stem = []
        
        # ps.stem(w)) 
        print("\n\nfor Stemming \n\n")
        pwd_inner=[]
        for li in pwd_list:
            pwd_inner=[]
            for j in li:
                #st=porter.stem(j)
                st=stemmer.stem(j)
                
                pwd_inner.append(st)
            pwd_stem.append(pwd_inner)
        print(pwd_stem)
        
        #lemma
        pwd_lemm = []
        
        # ps.stem(w)) 
        print("\n\nfor Lemmatisation\n\n")
        pwd_inner=[]
        for li in pwd_stem:
            pwd_inner=[]
            for j in li:
                
                lm = lemmatizer.lemmatize(j)
                
                pwd_inner.append(lm)
            pwd_lemm.append(pwd_inner)
        print(pwd_lemm)
        #======================================================  kseb
        kseb_stem = []
        
        # ps.stem(w)) 
        print("\n\nfor Stemming \n\n")
        pwd_inner=[]
        for li in kseb_list:
            kseb_inner=[]
            for j in li:
                #st=porter.stem(j)
                st=stemmer.stem(j)
                
                kseb_inner.append(st)
            kseb_stem.append(kseb_inner)
        print(kseb_stem)
        
        #lemma
        kseb_lemm = []
        
        # ps.stem(w)) 
        print("\n\nfor Lemmatisation\n\n")
        kseb_inner=[]
        for li in kseb_stem:
            kseb_inner=[]
            for j in li:
                
                lm = lemmatizer.lemmatize(j)
                
                kseb_inner.append(lm)
            kseb_lemm.append(kseb_inner)
        print(kseb_lemm)
         #======================================================  ksrtc
        ksrtc_stem = []
        
        # ps.stem(w)) 
        print("\n\nfor Stemming \n\n")
        ksrtc_inner=[]
        for li in ksrtc_list:
            ksrtc_inner=[]
            for j in li:
                #st=porter.stem(j)
                st=stemmer.stem(j)
                
                ksrtc_inner.append(st)
            ksrtc_stem.append(ksrtc_inner)
        print(ksrtc_stem)
        
        #lemma
        ksrtc_lemm = []
        
        # ps.stem(w)) 
        print("\n\nfor Lemmatisation\n\n")
        ksrtc_inner=[]
        for li in ksrtc_stem:
            ksrtc_inner=[]
            for j in li:
                
                lm = lemmatizer.lemmatize(j)
                
                ksrtc_inner.append(lm)
            ksrtc_lemm.append(ksrtc_inner)
        print(ksrtc_lemm)


      
        


        
        
            
        return(water_lemm,pwd_lemm,ksrtc_list,kseb_lemm,env_lemm)
        #return(water_list,pwd_list,ksrtc_list,kseb_list,env_list)


   
    def word_frequency(self,water_list,pwd_list,ksrtc_list,kseb_list,env_list):
        
        #word frequencies  Environment department

        wordfreq = []
       
    
        for word  in env_list:
            for i in word:
                wordfreq.append(i)
        env_count =Counter(wordfreq)
        env_count= dict(env_count)
        print("\n\n Env Count \n\n")
        print(type(env_count))
        
    
        #word frequencies  KSEB department
        wordfreq = []
        for word  in kseb_list:
            for i in word:
                wordfreq.append(i)
        kseb_count = Counter(wordfreq)
        kseb_count= dict(kseb_count) 
        print("\n\n KSEB Count \n\n")
        print(kseb_count)
    

        
        #word frequencies  KSRTC department

        wordfreq = []
        
        for word  in ksrtc_list:
            
            for i in word:
                wordfreq.append(i)
        ksrtc_count =Counter(wordfreq)
        ksrtc_count= dict(ksrtc_count)
        print("\n\n KSRTC Count \n\n")
        print(ksrtc_count)
    
        
        #word frequencies  pwd department

        for word  in pwd_list:
            
            for i in word:
                wordfreq.append(i)
        pwd_count =Counter(wordfreq)
        pwd_count = dict(pwd_count)
        print("\n\n PWD Count \n\n")
        print(type(pwd_count))
        
        
        #word frequencies  water department

        wordfreq = []
        for word  in water_list:
            
            for i in word:
                wordfreq.append(i)
        water_count =Counter(wordfreq)
        water_count= dict(water_count)
        print("\n\n KSRTC Count \n\n")
        print(type(water_count))
        return(water_count,pwd_count,ksrtc_count,kseb_count,env_count)


    def most_repeated_keywords(self,water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq ):
        
        
        
        print("\n\n Water Freq newwwwwwwwww")
        print(water_freq)
        
        #print sorted(prices.iteritems(), lambda x, y : cmp(x[1], y[1]))

        
        water_lis =[]
        water_freq_list = { }
        
        items = [(v, k) for k, v in water_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        print(items)



        water_dict=(items[:5])
        water_lis.append(water_dict)


        
            
        print("\n\nKEYWORDS  WATER\n\n")
        print(water_lis)
        
        
        
        print("\n\n PWD Freq newwwwwwwwww")
        print(pwd_freq)
        
        
        pwd_lis =[]
        pwd_freq_list = { }
        
        items = [(v, k) for k, v in pwd_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        print(items)



        pwd_dict=(items[:5])
        pwd_lis.append(pwd_dict)

        print("\n\nKEYWORDS  PWD\n\n")
        print(pwd_lis)
        
        
        # Finding the most repeated words kseb
        print("\n\n KSEB Freq newwwwwwwwww")
        print(pwd_freq)
        
        
        kseb_lis =[]
        kseb_freq_list = { }
        
        items = [(v, k) for k, v in kseb_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        print(items)



        kseb_dict=(items[:5])
        kseb_lis.append(kseb_dict)

        print("\n\nKEYWORDS  KSEB\n\n")
        print(kseb_lis)
        
        

        
        # Finding the most repeated words ksrtc

        print("\n\n KSRTC Freq newwwwwwwwww")
        print(ksrtc_freq)
        
        
        ksrtc_lis =[]
        ksrtc_freq_list = { }
        
        items = [(v, k) for k, v in ksrtc_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        
        print(items)



        ksrtc_dict=(items[:5])
        ksrtc_lis.append(ksrtc_dict)

        print("\n\nKEYWORDS  KSRTC\n\n")
        print(ksrtc_lis)
        
        

        
        # Finding the most repeated words env
        print("\n\n ENV Freq newwwwwwwwww")
        print(env_freq)
        
        
        env_lis =[]
        env_freq_list = { }
        
        items = [(v, k) for k, v in env_freq.items()]
        items.sort()
        items.reverse()
        items = [k  for v, k in items]
        print(items)



        env_dict=(items[:5])
        env_lis.append(env_dict)

        print("\n\nKEYWORDS  ENV \n\n")
        print(env_lis)
       
        
        
        return(water_lis,pwd_lis,ksrtc_lis,kseb_lis,env_lis )
                
        
    def most_repeated_keyword_lib(self,dfenv,dfwater,dfpwd,dfksrtc,dfkseb):
        
        #env keyword
        
        env_keyword = []
        env_summary = []
        
        stopwords = list(STOP_WORDS)
        
        print("\n\nKEYWORD : LIB : ENV\n\n")
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
        print(env_summary)
        
        # water Keyword
        
        water_keyword = []
        water_summary = []
        
        stopwords = list(STOP_WORDS)
        
        print("\n\nKEYWORD : LIB : Water\n\n")
        
        
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
        print(water_summary)
        
        
        #pwd keyword
        
        pwd_keyword = []
        pwd_summary = []
        
        stopwords = list(STOP_WORDS)
        
        print("\n\nKEYWORD : LIB : PWD\n\n")
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
        print(pwd_summary)
        
        #env keyword
        
        ksrtc_keyword = []
        ksrtc_summary = []
        
        stopwords = list(STOP_WORDS)
        
        print("\n\nKEYWORD : LIB : KSRTC\n\n")
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
        print(ksrtc_summary)
        
        #env keyword
        
        kseb_keyword = []
        kseb_summary = []
        
        stopwords = list(STOP_WORDS)
        
        print("\n\nKEYWORD : LIB : KSEB\n\n")
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
        print(kseb_summary)
        return(env_summary,water_summary,pwd_summary,ksrtc_summary,kseb_summary)
        
        
        
    def jump(self,status):
        if status == 1:
            env_summary,water_summary,pwd_summary,ksrtc_summary,kseb_summary=self.most_repeated_keyword_lib(dfenv,dfwater,dfpwd,dfksrtc,dfkseb)
        else:
            
            water_lis,pwd_lis,ksrtc_lis,kseb_lis,env_lis = self.most_repeated_keywords(water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq )
        return(water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis)
            
    def test(self):
        text_data = input("Enter complaint")
        text_data= text_data.replace('[^\w\s]','').lower()
        
        
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  
        for x in text_data.lower(): 
            if x in punctuations: 
                text_data = text_data.replace(x, " ") 
  
   
        print(text_data) 
        
            
        test_token = word_tokenize(text_data)
        print(test_token)
        test_list =[]
        
        stop_words = set(stopwords.words('english'))
        for i in test_token:
            
            
            if i not in stop_words:
        
                test_list.append(i)
        print(test_list)
        
        #frequency : 
        

        
        counts = Counter(test_list)
        count = dict(counts)
        print(count)  # word frequency
    
        items = [(v, k) for k, v in counts.items()]
        items.sort()
        items.reverse() 
        item = [(k,v) for v, k in items]
        items = [k for v, k in items]
        print(items)  # sorted high to low
        test_dict=(items[0:5])
        print(test_dict)  #key only
        
        return(test_dict,item)
    
    
    
    
    def evaluate(self,keywords,item,water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis,dept):
        #keyword matching 
        #water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis
        
        
        print("frequent list.................")
            
        print(item)
        
        print("\n\nTest Keywords \n \n")
        print(keywords)
        #items = [k for v, k in water_lis]
        #===============================================PWD
        #pwd_lis=dict(pwd_lis)
        #pwd predict
        pwd_predict=[]
        pwd_list = []
        count=0
        for li in pwd_lis:
            for i in li:
                
                pwd_list.append(i)
        for i in keywords:
            
            if i in keywords:
                if i in pwd_list:
                    count+=1
                    pwd_predict.append(i)
        #keywords = set(keywords)
        #pwd_list = set(pwd_list)
        #pwd_predict = keywords & pwd_list
        #pwd_predict = list(pwd_predict)
                            
        print("\n\n PWD predict \n\n")
        print(count)
        print(pwd_predict)
        print(pwd_list)
        
        #water predict
        #==================================================Water
        water_predict=[]
        water_list = []
        count = 0
        
        for li in water_lis:
            for i in li:
                
                water_list.append(i)
    
        for i in keywords:
            
            if i in keywords:
                if i in water_list:
                    count+=1
                    water_predict.append(i)

                            
        print("\n\n WATER predict \n\n")  
        print(count)
        print(water_predict)
        print(water_list)
        
        #env predict
        #=======================================================ENV
        env_predict=[]
        env_list = []
        count =0
        #making it as 1 d list
        for li in env_lis:
            for i in li:
                env_list.append(i)
         
        #matching  the test keywords with env_keywords
        for i in keywords:
            
            if i in keywords:
                if i in env_list:
                    count+=1
                    env_predict.append(i)

                
       
                            
        print("\n\n ENV predict \n\n") 
        print(count)
        print(env_predict)
        print(env_list)
        
        #kseb predict
        #=========================================================KSEB
        
        kseb_predict=[]
        kseb_list = []
        count = 0
        
        for li in kseb_lis:
            for i in li:
                
                
                kseb_list.append(i)
        for i in keywords:
            
            if i in keywords:
                if i in kseb_list:
                    count+=1
                    kseb_predict.append(i)

                            
        print("\n\n kseb predict \n\n")    
        print(kseb_predict)
        print(kseb_list)
        
        #ksrtc predict
        #=============================================================KSRTC
        
        ksrtc_predict=[]
        ksrtc_list = []
        count = 0
        
        for li in ksrtc_lis:
            for i in li:
                ksrtc_list.append(i)
        
        for i in keywords:
            
            if i in keywords:
                if i in ksrtc_list:
                    count+=1
                    ksrtc_predict.append(i)

                            
        print("\n\n ksrtc predict \n\n") 
        print(count)
        print(ksrtc_predict)
        print(ksrtc_list)
     
        department = dept
        dept_values =[1,2,3,4,5]
        depart_dict = dict(zip(dept_values,department))
        print(depart_dict)
        
        predict_dict={}
        env_length = len(env_predict)
        water_length = len(water_predict)
        pwd_length = len(pwd_predict)
        kseb_length = len(kseb_predict)
        ksrtc_length = len(ksrtc_predict)
        
        #================================================================= class mapping
        
        if len(env_predict)==0:
            pass
        else:
            predict_dict.update({'Environment and Climate change':len(env_predict)})
            
            print(" \n\n Predicted class : " +depart_dict[5])
            
        
        if len(water_predict)==0:
            pass
        else:
            predict_dict.update({'Water Authority':len(env_predict)})
            print(" \n\n Predicted class : " + depart_dict[1])
            
        if len(pwd_predict)==0:
            pass
        else:
            predict_dict.update({'PWD':len(env_predict)})
            print(" \n\n Predicted class : " + depart_dict[2])
            
        if len(kseb_predict)==0:
            pass
        else:
            predict_dict.update({'KSEB':len(env_predict)})
            print(" \n\n Predicted class : " + depart_dict[3])
            
        if len(ksrtc_predict)==0:
            pass
        else:
            predict_dict.update({'KSRTC':len(env_predict)})
            print(" \n\n Predicted class : " + depart_dict[4])

        print(predict_dict)
        
        #===========================================================Converting to string
        
        
        
        keywords_string = ' '.join(keywords)
        ksrtc_string    = ' '.join(ksrtc_list)
        kseb_string    = ' '.join(kseb_list)
        water_string    = ' '.join(water_list)
        pwd_string    = ' '.join(pwd_list)
        env_string    = ' '.join(env_list)
        
        print("Joining keywords  " + keywords_string)
        print("Joining KSRTC keywords  " + ksrtc_string)
        print("Joining KSEB keywords  " + kseb_string)
        print("Joining Water keywords  " + water_string)
        print("Joining ENV keywords  " + env_string)
        
        #======================================================================



        
        
        #sorting in desecnding order
        counts = Counter(predict_dict)
        count = dict(counts)
        print(count)  # word frequency
    
        items = [(v, k) for k, v in counts.items()]
        items.sort()
        items.reverse()
        items = [(k,v) for v, k in items]
        print(items)  # sorted high to low
        
       #==================================================================Similarity if no match
       #spacy work
        
        similarity_string = water_string + " " + pwd_string+ " "+env_string+ " "+kseb_string+" "+ksrtc_string+ " "
        print("\n\n Similarity string \n \n ")
        print(similarity_string)
        
    
    
    
        if env_length ==0 :
            if water_length == 0:
                if pwd_length == 0:
                    if kseb_length == 0:   
                        if ksrtc_length == 0:
                            keywords_string   = self.nlp(keywords_string)
                            similarity_string = self.nlp(similarity_string)
                            similarity_list=[]
                            for keyword in keywords_string:
                                for word in similarity_string:
                                    print(keyword.text, word.text, keyword.similarity(word))
                                    similarity_list.append(keyword.similarity(word))
                                    similarity_max = max(similarity_list)
                            print("\nSimilarity List\n")        
                            print(similarity_list)
                            print("\nSimilarity Max\n")
                            print(similarity_max )
                            for keyword in keywords_string:
                                for word in similarity_string:

                                    if similarity_max==keyword.similarity(word):
                                        new_mapped_word = word.text
                                        print(keyword.text,word.text)

                                    #if keyword.similarity(word)>= 0.35038363:
                                      #  print("\nThresh higher"+keyword.text,word.text)

                            print("\n New mapped word "+new_mapped_word)
                            if new_mapped_word in water_list:
                                print("Predicted class : "+depart_dict[1])
                            if new_mapped_word in pwd_list:
                                print("Predicted class : "+depart_dict[2])
                            if new_mapped_word in kseb_list:
                                print("Predicted class : "+depart_dict[3])
                            if new_mapped_word in ksrtc_list:
                                print("Predicted class : "+depart_dict[4])
                            if new_mapped_word in env_list:
                                print("Predicted class : "+depart_dict[5])


                            







                            
                                    
        
                            
                            



                            


                            
                        
                            
                            
                            
                            
                            
        
  
            
        
                  
        
        
file =   '/home/gayathri/project/MakeComplaint/data.csv'   
nlp = spacy.load('en_core_web_md')

x= Main(file,nlp)
x.punctuate()
x.data_clean()
dfwater,dfpwd,dfksrtc,dfkseb,dfenv=x.dataframing(x.dataset)

water_list,pwd_list,ksrtc_list,kseb_list,env_list = x.tokenisation(dfwater,dfpwd,dfksrtc,dfkseb,dfenv)

water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq = x.word_frequency(water_list,pwd_list,ksrtc_list,kseb_list,env_list)
#x.most_repeated_keywords(water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq)
#x.most_repeated_keyword_lib(dfenv) 

water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis=x.jump(0)

keywords,item=x.test()
dept=x.department_class()
x.evaluate(keywords,item,water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis,dept)