from nltk.corpus import stopwords 
import nltk
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

def tokenisation(dfwater,dfpwd,dfksrtc,dfkseb,dfenv):

    stop_words = set(stopwords.words('english'))
    water_token = []
    water_list=[]

    #Tokenising water data
    
    
    for i, row in dfwater.iterrows():
            #print(i,row['Subject'], row['Complaint'])
            
        water_token = word_tokenize(row['Subject_and_Complaint'])
        result = [i for i in water_token if not i in stop_words]
        #lemmatized_output = [i for i in lemmatizer.lemmatize(i) for i in result]
    
        water_list.append(result)
    print("\n==================Tokenisation=================\n")
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
        
    #print("\n\nPWD Tokens\n\n")
    #print(pwd_list)
        
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
   
    #print("\n\nfor Stemming \n\n")
    env_inner=[]
    for li in env_list:
        env_inner=[]
        for j in li:
            #st=porter.stem(j)
            st=stemmer.stem(j)
            
            env_inner.append(st)
        env_stem.append(env_inner)
    #print("\n==================Stemming=================\n")
    #print(env_stem)
    
    #lemma
    env_lemm = []
    
    # ps.stem(w)) 
    print("\n==================Stemming=================\n")
    #print("\n\nfor Lemmatisation\n\n")
    env_inner=[]
    for li in env_stem:
        env_inner=[]
        for j in li:
            
            lm = lemmatizer.lemmatize(j)
            
            env_inner.append(lm)
        env_lemm.append(env_inner)
    #print(env_lemm)
#======================================================  water
    water_stem = []
    
    # ps.stem(w)) 
    #print("\n==================Stemming=================\n")
 
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
    #print("\n\nfor Lemmatisation\n\n")
    water_inner=[]
    for li in water_stem:
        water_inner=[]
        for j in li:
            
            lm = lemmatizer.lemmatize(j)
            
            water_inner.append(lm)
        water_lemm.append(water_inner)
    print("\n==================Lemmatisation=================\n")
    print(water_lemm)
    #======================================================  pwd
    pwd_stem = []
    
    # ps.stem(w)) 
    #print("\n\nfor Stemming \n\n")
    pwd_inner=[]
    for li in pwd_list:
        pwd_inner=[]
        for j in li:
            #st=porter.stem(j)
            st=stemmer.stem(j)
            
            pwd_inner.append(st)
        pwd_stem.append(pwd_inner)
    #print(pwd_stem)
    
    #lemma
    pwd_lemm = []
    
    # ps.stem(w)) 
    #print("\n\nfor Lemmatisation\n\n")
    pwd_inner=[]
    for li in pwd_stem:
        pwd_inner=[]
        for j in li:
            
            lm = lemmatizer.lemmatize(j)
            
            pwd_inner.append(lm)
        pwd_lemm.append(pwd_inner)
    #print(pwd_lemm)
    #======================================================  kseb
    kseb_stem = []
    
    # ps.stem(w)) 
    #print("\n\nfor Stemming \n\n")
    pwd_inner=[]
    for li in kseb_list:
        kseb_inner=[]
        for j in li:
            #st=porter.stem(j)
            st=stemmer.stem(j)
            
            kseb_inner.append(st)
        kseb_stem.append(kseb_inner)
    #print(kseb_stem)
    
    #lemma
    kseb_lemm = []
    
    # ps.stem(w)) 
    #print("\n\nfor Lemmatisation\n\n")
    kseb_inner=[]
    for li in kseb_stem:
        kseb_inner=[]
        for j in li:
            
            lm = lemmatizer.lemmatize(j)
            
            kseb_inner.append(lm)
        kseb_lemm.append(kseb_inner)
    #print(kseb_lemm)
        #======================================================  ksrtc
    ksrtc_stem = []
    
    # ps.stem(w)) 
    #print("\n\nfor Stemming \n\n")
    ksrtc_inner=[]
    for li in ksrtc_list:
        ksrtc_inner=[]
        for j in li:
            #st=porter.stem(j)
            st=stemmer.stem(j)
            
            ksrtc_inner.append(st)
        ksrtc_stem.append(ksrtc_inner)
    #print(ksrtc_stem)
    
    #lemma
    ksrtc_lemm = []
    
    # ps.stem(w)) 
    #print("\n\nfor Lemmatisation\n\n")
    ksrtc_inner=[]
    for li in ksrtc_stem:
        ksrtc_inner=[]
        for j in li:
            
            lm = lemmatizer.lemmatize(j)
            
            ksrtc_inner.append(lm)
        ksrtc_lemm.append(ksrtc_inner)
    #print(ksrtc_lemm)
        
    return(water_lemm,pwd_lemm,ksrtc_lemm,kseb_lemm,env_lemm)
    #return(water_list,pwd_list,ksrtc_list,kseb_list,env_list)
