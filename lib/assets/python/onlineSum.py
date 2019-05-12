
# coding: utf-8

# In[19]:


import bs4 as bs
import urllib.request
import re
import nltk
import heapq


# In[20]:


nltk.download('stopwords')
nltk.download('punkt')


# In[21]:


# here we have our url
url_text = urllib.request.urlopen("https://www.rte.ie/news/munster/2019/0512/1048926-dingle-rescue/").read()
# the beautiful soup library to help extract from html
soup = bs.BeautifulSoup(url_text, 'lxml')
print(url_text)  # print the page


# In[22]:


print(soup.prettify)


# In[23]:


text = ""
# find the paragraph tag
for paragraph in soup.find_all('p'):
    text += paragraph.text
print(text)


# In[24]:


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


# In[25]:


stop_words  # get the list


# In[26]:


word_dict = {}  # line 1
for word in nltk.word_tokenize(clean):  # line 2
    if word not in stop_words:  # line 3
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1
for key in word_dict.keys():  # line 4
    word_dict[key] = word_dict[key] / max(word_dict.values())


# In[27]:


print(word_dict, '\n')


# In[28]:


word_score = {}
for sentence in token_sentences:
      for word in nltk.word_tokenize(sentence.lower()):
        if word in word_dict.keys():
            if len(sentence.split(' ')) < 30:
                if sentence not in word_score.keys():
                    word_score[sentence] = word_dict[word]
                else:
                    word_score[sentence] += word_dict[word]


# In[29]:


best_sentences = heapq.nlargest(7, word_score, key=word_score.get)


# In[30]:


for sentences in best_sentences:
    print(sentences, '\n')

