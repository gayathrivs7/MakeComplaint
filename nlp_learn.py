{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "LookupError",
     "evalue": "\n**********************************************************************\n  Resource \u001b[93mpunkt\u001b[0m not found.\n  Please use the NLTK Downloader to obtain the resource:\n\n  \u001b[31m>>> import nltk\n  >>> nltk.download('punkt')\n  \u001b[0m\n  Attempted to load \u001b[93mtokenizers/punkt/PY3/english.pickle\u001b[0m\n\n  Searched in:\n    - '/home/user/nltk_data'\n    - '/usr/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n    - ''\n**********************************************************************\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mLookupError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-8-48e15c0cd87e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m#function to split text into word\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m \u001b[0mtokens\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mword_tokenize\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"The quick brown fox jumps over the lazy dog\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/usr/local/lib/python3.5/dist-packages/nltk/tokenize/__init__.py\u001b[0m in \u001b[0;36mword_tokenize\u001b[0;34m(text, language, preserve_line)\u001b[0m\n\u001b[1;32m    141\u001b[0m     \u001b[0;34m:\u001b[0m\u001b[0mtype\u001b[0m \u001b[0mpreserve_line\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    142\u001b[0m     \"\"\"\n\u001b[0;32m--> 143\u001b[0;31m     \u001b[0msentences\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mpreserve_line\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0msent_tokenize\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlanguage\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    144\u001b[0m     return [\n\u001b[1;32m    145\u001b[0m         \u001b[0mtoken\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0msent\u001b[0m \u001b[0;32min\u001b[0m \u001b[0msentences\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mtoken\u001b[0m \u001b[0;32min\u001b[0m \u001b[0m_treebank_word_tokenizer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtokenize\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msent\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.5/dist-packages/nltk/tokenize/__init__.py\u001b[0m in \u001b[0;36msent_tokenize\u001b[0;34m(text, language)\u001b[0m\n\u001b[1;32m    102\u001b[0m     \u001b[0;34m:\u001b[0m\u001b[0mparam\u001b[0m \u001b[0mlanguage\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mthe\u001b[0m \u001b[0mmodel\u001b[0m \u001b[0mname\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mthe\u001b[0m \u001b[0mPunkt\u001b[0m \u001b[0mcorpus\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    103\u001b[0m     \"\"\"\n\u001b[0;32m--> 104\u001b[0;31m     \u001b[0mtokenizer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'tokenizers/punkt/{0}.pickle'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlanguage\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    105\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mtokenizer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtokenize\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    106\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.5/dist-packages/nltk/data.py\u001b[0m in \u001b[0;36mload\u001b[0;34m(resource_url, format, cache, verbose, logic_parser, fstruct_reader, encoding)\u001b[0m\n\u001b[1;32m    866\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    867\u001b[0m     \u001b[0;31m# Load the resource.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 868\u001b[0;31m     \u001b[0mopened_resource\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_open\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresource_url\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    869\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    870\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mformat\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'raw'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.5/dist-packages/nltk/data.py\u001b[0m in \u001b[0;36m_open\u001b[0;34m(resource_url)\u001b[0m\n\u001b[1;32m    991\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    992\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mprotocol\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mprotocol\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'nltk'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 993\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mfind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpath_\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpath\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m''\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    994\u001b[0m     \u001b[0;32melif\u001b[0m \u001b[0mprotocol\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'file'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    995\u001b[0m         \u001b[0;31m# urllib might not use mode='rb', so handle this one ourselves:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.5/dist-packages/nltk/data.py\u001b[0m in \u001b[0;36mfind\u001b[0;34m(resource_name, paths)\u001b[0m\n\u001b[1;32m    697\u001b[0m     \u001b[0msep\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'*'\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m70\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    698\u001b[0m     \u001b[0mresource_not_found\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'\\n%s\\n%s\\n%s\\n'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0msep\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msep\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 699\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0mLookupError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresource_not_found\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    700\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    701\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mLookupError\u001b[0m: \n**********************************************************************\n  Resource \u001b[93mpunkt\u001b[0m not found.\n  Please use the NLTK Downloader to obtain the resource:\n\n  \u001b[31m>>> import nltk\n  >>> nltk.download('punkt')\n  \u001b[0m\n  Attempted to load \u001b[93mtokenizers/punkt/PY3/english.pickle\u001b[0m\n\n  Searched in:\n    - '/home/user/nltk_data'\n    - '/usr/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n    - ''\n**********************************************************************\n"
     ]
    }
   ],
   "source": [
    "#using NLTK library, we can do lot of text preprocesing\n",
    "import nltk\n",
    "from nltk.tokenize import word_tokenize\n",
    "\n",
    "#function to split text into word\n",
    "\n",
    "tokens = word_tokenize(\"The quick brown fox jumps over the lazy dog\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk\n",
    "nltk.download()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to /home/user/nltk_data...\n",
      "[nltk_data]   Unzipping tokenizers/punkt.zip.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['All', 'work', 'and', 'no', 'play', 'makes', 'jack', 'a', 'dull', 'boy', ',', 'all', 'work', 'and', 'no', 'play']\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "from nltk.tokenize import sent_tokenize, word_tokenize\n",
    "nltk.download('punkt')\n",
    "data = \"All work and no play makes jack a dull boy, all work and no play\"\n",
    "print(word_tokenize(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['All', 'work', 'and', 'no', 'play', 'makes', 'jack', 'a', 'dull', 'boy', ',', 'all', 'work', 'and', 'no', 'play']\n"
     ]
    }
   ],
   "source": [
    "from nltk.tokenize import sent_tokenize, word_tokenize\n",
    "data = \"All work and no play makes jack a dull boy, all work and no play\"\n",
    "print(word_tokenize(data))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
