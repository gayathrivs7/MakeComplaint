
#data framing
def dataframing(dataset):
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
    #print(dfenv )
    return (dfwater,dfpwd,dfksrtc,dfkseb,dfenv)