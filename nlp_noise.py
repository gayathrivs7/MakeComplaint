#prg to remove stopwords 
noise_list = [ "is", "a", " this",".","of","in","an","the","as","but","was",";",":","were","am","are","I","at","on","under","over","it"]

def remove_noise(input_text):
    words=input_text.split()
    noise_free_words=[word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

text=remove_noise("this is a sample text of .  gayathri was ; in : it in ")
print(text)