
def data_clean(dataset):
  
    # unpunctuate and lower case
    dataset['Subject'] = dataset['Subject'].str.replace('[^\w\s]','').str.lower()
    dataset['Complaint'] = dataset['Complaint'].str.replace('[^\w\s]','').str.lower()

    dataset['Complaint'] =  dataset['Complaint'].str.replace(',',' ').str.lower() 
    
    dataset['Subject'] =  dataset['Subject'] .str.replace('\d+', ' ')
    dataset['Complaint'] =  dataset['Complaint'] .str.replace('\d+', ' ')
    dataset['Subject'] =  dataset['Subject'].str.rstrip('\n')
    #print(dataset['Complaint'])
    return dataset


    

    
