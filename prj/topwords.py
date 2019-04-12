
def most_repeated_keywords(water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq,status ):
    if status == 'manual':      
        print("\n\n Water Freq newwwwwwwwww")
        print(water_freq)
        #=================================================   Water 
        water_lis =[]
        
        
        items = [(v, k) for k, v in water_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        print(items)

        water_dict=(items[:5])
        water_lis.append(water_dict)            
        print("\n\nKEYWORDS  WATER\n\n")
        print(water_lis) 
        
        #==================================================  PWd       
        print("\n\n PWD Freq newwwwwwwwww")
        print(pwd_freq)
        
        pwd_lis =[]
        
        
        items = [(v, k) for k, v in pwd_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        print(items)

        pwd_dict=(items[:5])
        pwd_lis.append(pwd_dict)

        print("\n\nKEYWORDS  PWD\n\n")
        print(pwd_lis)
        
        
        #===================================================  KSEB
        print("\n\n KSEB Freq newwwwwwwwww")
        print(kseb_freq)
        
        
        kseb_lis =[]   
        items = [(v, k) for k, v in kseb_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        print(items)



        kseb_dict=(items[:5])
        kseb_lis.append(kseb_dict)

        print("\n\nKEYWORDS  KSEB\n\n")
        print(kseb_lis)
        
        

        
        # ========================================================= KSRTC

        print("\n\n KSRTC Freq newwwwwwwwww")
        print(ksrtc_freq)
        
        
        ksrtc_lis =[]
   
        
        items = [(v, k) for k, v in ksrtc_freq.items()]
        items.sort()
        items.reverse()
        items = [k for v, k in items]
        
        print(items)



    ksrtc_dict=(items[:5])
    ksrtc_lis.append(ksrtc_dict)

    print("\n\nKEYWORDS  KSRTC\n\n")
    print(ksrtc_lis)
    
    

    
    # ===================================================== ENV
    print("\n\n ENV Freq newwwwwwwwww")
    print(env_freq)
    
    
    env_lis =[]
 
    
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
            
