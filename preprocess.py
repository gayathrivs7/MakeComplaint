


def punctuate(dataset):
    punctuations = '''!()-[]{};:'"\,.<>/?@#$%^&*_~'''
    text = dataset['Subject']

       

    # remove punctuation from the string
    no_punct = ""
    no_punctuate =[]
    for char in  dataset['Subject']:

        if char not in punctuations:
            no_punct = no_punct + char
            no_punctuate.append(no_punct)

        # display the unpunctuated string
    #print(no_punctuate)
    return(no_punctuate)

