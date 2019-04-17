import spacy
from collections import Counter

def evaluate(keywords,item,water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis,dept,nlp):
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
                        keywords_string   = nlp(keywords_string)
                        similarity_string = nlp(similarity_string)
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

