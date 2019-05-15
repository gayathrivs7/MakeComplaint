from collections import Counter

def word_frequency(water_list,pwd_list,ksrtc_list,kseb_list,env_list):
    
    #word frequencies  Environment department

    wordfreq = []
    

    for word  in env_list:
        for i in word:
            wordfreq.append(i)
    env_count =Counter(wordfreq)
    env_count= dict(env_count)
    #print("\n\n Env Count \n\n")
    #print(type(env_count))
    

    #word frequencies  KSEB department
    wordfreq = []
    for word  in kseb_list:
        for i in word:
            wordfreq.append(i)
    kseb_count = Counter(wordfreq)
    kseb_count= dict(kseb_count) 
    #print("\n\n KSEB Count \n\n")
    #print(kseb_count)


    
    #word frequencies  KSRTC department

    wordfreq = []
    
    for word  in ksrtc_list:
        
        for i in word:
            wordfreq.append(i)
    ksrtc_count =Counter(wordfreq)
    ksrtc_count= dict(ksrtc_count)
    #print("\n\n KSRTC Count \n\n")
    #print(ksrtc_count)

    
    #word frequencies  pwd department

    for word  in pwd_list:
        
        for i in word:
            wordfreq.append(i)
    pwd_count =Counter(wordfreq)
    pwd_count = dict(pwd_count)
    #print("\n\n PWD Count \n\n")
    #print(type(pwd_count))
    
    
    #word frequencies  water department

    wordfreq = []
    for word  in water_list:
        
        for i in word:
            wordfreq.append(i)
    water_count =Counter(wordfreq)
    water_count= dict(water_count)
    #print("\n\n KSRTC Count \n\n")
    #print(type(water_count))
    return(water_count,pwd_count,ksrtc_count,kseb_count,env_count)

