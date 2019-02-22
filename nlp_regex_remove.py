import re

def remove_regex(input_text,regex_pattern):
	urls=re.finditer(regex_pattern,input_text)
	for i in urls:
		input_text = re.sub(i.group().strip(), '', input_text)
	return input_text

regex_pattern = "#[\w]*" 
rem=remove_regex("remove this #hashtag from analytics vidhya", regex_pattern)
print(rem)
