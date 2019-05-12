
# coding: utf-8

# In[129]:


import bs4 as bs
import urllib.request
import re
import nltk
import heapq


# In[130]:


nltk.download('stopwords')
nltk.download('punkt')


# In[131]:


# here we have our url
url_text = urllib.request.urlopen("https://en.wikipedia.org/wiki/Artificial_intelligence").read()
# the beautiful soup library to help extract from html
soup = bs.BeautifulSoup(url_text, 'lxml')
print(url_text)  # print the page


# In[132]:


print(soup.prettify)


# In[133]:


text = ""
# find the paragraph tag
for paragraph in soup.find_all('p'):
    text += paragraph.text
print(text)


# In[134]:


# remove referencing e.g. [1]
text = re.sub(r'\[[0-9]*\]', ' ', text)
text = re.sub(r'\s+', ' ', text)

# now we begin cleaning the text

# we put it to lower, remove the punctuation and spaces
clean = text.lower()
clean = re.sub(r'\W', ' ', clean)
clean = re.sub(r'\d', ' ', clean)
clean = re.sub(r'\s+', ' ', clean)
# use sent_tokenize to break the text into sentences
token_sentences = nltk.sent_tokenize(text)
# import the english stopwords
stop_words = nltk.corpus.stopwords.words('english')
print(token_sentences)


# In[135]:


stop_words  # get the list


# In[136]:


print(clean)


# In[143]:


# using regexp to remove the stop words
stop = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
text = stop.sub('', clean)


# In[142]:


amount = 5
print("\nThe {} most commons words are: \n".format(amount))
word_counter = collections.Counter(newly_clean)
top_five = []
for word, count in word_counter.most_common(amount):
    top_five.append(word)
    print(word, ": ", count)
print("\n")

# the final array list with the top five words   
print(top_five)

