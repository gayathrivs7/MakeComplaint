import spacy
from collections import Counter

def evaluate(keywords,item,water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis,dept,nlp):
    #keyword matching 
    #water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis
    
    count_list = []
    prob_list  = []

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
    pwd_count=0
    for li in pwd_lis:
        for i in li:
            
            pwd_list.append(i)
    for i in keywords:
        
        if i in keywords:
            if i in pwd_list:
                pwd_count+=1
                pwd_predict.append(i)

    #keywords = set(keywords)
    #pwd_list = set(pwd_list)
    #pwd_predict = keywords & pwd_list
    #pwd_predict = list(pwd_predict)
                        
    print("\n\n PWD predict \n\n")
    print(pwd_count)
    print(pwd_predict)
    print(pwd_list)
    count_list.append(pwd_count)
    #water predict
    #==================================================Water
    water_predict=[]
    water_list = []
    water_count = 0
    
    for li in water_lis:
        for i in li:
            
            water_list.append(i)

    for i in keywords:
        
        if i in keywords:
            if i in water_list:
                water_count+=1
                water_predict.append(i)

                        
    print("\n\n WATER predict \n\n")  
    print(water_count)
    print(water_predict)
    print(water_list)
    count_list.append(water_count)
    #env predict
    #=======================================================ENV
    env_predict=[]
    env_list = []
    env_count = 0
    #making it as 1 d list
    for li in env_lis:
        for i in li:
            env_list.append(i)
        
    #matching  the test keywords with env_keywords
    for i in keywords:
        
        if i in keywords:
            if i in env_list:
                env_count+=1
                env_predict.append(i)

            
    
                        
    print("\n\n ENV predict \n\n") 
    print(env_count)
    print(env_predict)
    print(env_list)
    count_list.append(env_count)
    
    #kseb predict
    #=========================================================KSEB
    
    kseb_predict=[]
    kseb_list = []
    kseb_count = 0
    
    for li in kseb_lis:
        for i in li:
            
            
            kseb_list.append(i)
    for i in keywords:
        
        if i in keywords:
            if i in kseb_list:
                kseb_count+=1
                kseb_predict.append(i)

                        
    print("\n\n kseb predict \n\n")    
    print(kseb_predict)
    print(kseb_list)
    print(kseb_count)
    count_list.append(kseb_count)
    
    #ksrtc predict
    #=============================================================KSRTC
    
    ksrtc_predict=[]
    ksrtc_list = []
    ksrtc_count = 0
    
    for li in ksrtc_lis:
        for i in li:
            ksrtc_list.append(i)
    
    for i in keywords:
        
        if i in keywords:
            if i in ksrtc_list:
                ksrtc_count+=1
                ksrtc_predict.append(i)

                        
    print("\n\n ksrtc predict \n\n") 
    print(ksrtc_count)
    print(ksrtc_predict)
    print(ksrtc_list)
    count_list.append(ksrtc_count)
    print("Count list")
    print(count_list)
    for i in count_list:
        prob = i/5
        prob_list.append(prob)
    print("\n Probablity list  Predict fn ")
    print(prob_list)
    max_prob = max(prob_list)
    index = prob_list.index(max_prob)
    indices = [index for index, value in enumerate(prob_list) if value == max_prob]
    print ("Index",indices)

  
    for i in indices:


        if index == 0:
            print("Predicted class : PWD ")
        if index == 1:
            print("Predicted class : Water Authority")
        if index == 2:
            print("Predicted class : Environment and climate change")

        if index == 3:
            print("Predicted class : KSEB")

        if index == 4:

            print("Predicted class : KSRTC")
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
        flag_env =1
        
    
    if len(water_predict)==0:
        pass
    else:
        predict_dict.update({'Water Authority':len(water_predict)})
        print(" \n\n Predicted class : " + depart_dict[1])
        
        
    if len(pwd_predict)==0:
        pass
    else:
        predict_dict.update({'PWD':len(pwd_predict)})
        print(" \n\n Predicted class : " + depart_dict[2])
        
        
    if len(kseb_predict)==0:
        pass
    else:
        predict_dict.update({'KSEB':len(kseb_predict)})
        print(" \n\n Predicted class : " + depart_dict[3])
        
        
    if len(ksrtc_predict)==0:
        pass
    else:
        predict_dict.update({'KSRTC':len(ksrtc_predict)})
        print(" \n\n Predicted class : " + depart_dict[4])
        
            

    print(predict_dict)

    if len(env_predict)==0:
        flag_env = 0
    else:
        flag_env = 1
    
    if len(kseb_predict)==0:
        flag_kseb = 0
    else:
        flag_kseb = 1

    
    if len(ksrtc_predict)==0:
        flag_ksrtc = 0
    else:
        flag_ksrtc = 1
    
    if len(pwd_predict)==0:
        flag_pwd = 0
    else:
        flag_pwd = 1
    
    
    if len(water_predict) == 0:
        flag_water = 0
    else:
        flag_water = 1
    
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
    
    water_dept=[]
    pwd_dept=[]
    kseb_dept=[]
    ksrtc_dept=[]
    env_dept=[]


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
                            water_dept.append(depart_dict[1])
                        if new_mapped_word in pwd_list:
                            print("Predicted class : "+depart_dict[2])
                            pwd_dept.append(depart_dict[2])
                        if new_mapped_word in kseb_list:
                            print("Predicted class : "+depart_dict[3])
                            kseb_dept.append(depart_dict[3])
                        if new_mapped_word in ksrtc_list:
                            print("Predicted class : "+depart_dict[4])
                            ksrtc_dept.append(depart_dict[4])
                        if new_mapped_word in env_list:
                            print("Predicted class : "+depart_dict[5])
                            env_dept.append(depart_dict[5])
    water_len = len(water_dept)
    if water_len == 1:
        water_flag =1
    else:
        water_flag = 0  

    if len(pwd_dept)==1:
        pwd_flag= 1
    else:
        pwd_flag= 0
    if len(kseb_dept)==1:
        kseb_flag = 1
    else:
        kseb_flag = 0
    if len(ksrtc_dept)== 1:
        ksrtc_flag = 1
    else:
        ksrtc_flag = 0
    if len(env_dept)==1:
        env_flag = 1
    else:
        env_flag = 0

    print(water_dept,pwd_dept,kseb_dept,ksrtc_dept,env_dept)
    print(water_flag,pwd_flag,kseb_flag,ksrtc_flag,env_flag)
    return water_flag,pwd_flag,kseb_flag,ksrtc_flag,env_flag,water_dept,pwd_dept,kseb_dept,ksrtc_dept,env_dept,flag_env,flag_kseb,flag_ksrtc,flag_pwd,flag_water
    
