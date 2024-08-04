import nltk
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
import os
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
nltk.download('vader_lexicon')
root=os.path.abspath("../..")

df=pd.read_excel(root+"\\data\\messages\\dataset.xlsx")
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

# 创建VADER情感分析器
sia = SentimentIntensityAnalyzer()
result=[]

# 分析情感极性
for chat in df['text']:
    chat = chat.lower()
    chat = re.sub(r'[^a-z\s]', '', chat)
    # 使用TextBlob分析情感
    blob = TextBlob(chat)
    blob_polarity = blob.sentiment.polarity
    blob_subjectivity = blob.sentiment.subjectivity

    # 使用VADER分析情感
    sia_scores = sia.polarity_scores(chat)
    sia_compound = sia_scores['compound']
    result.append({'文本':chat,'TextBlob极性':blob_polarity,'TextBlob主观性':blob_subjectivity,'VADER综合得分': sia_compound})

df_result = pd.DataFrame(result)
df_result=df_result[(df_result['VADER综合得分']<0) & (df_result['TextBlob极性']<0)]

with open(root+'\\data\\messages\\messages.txt', 'a') as file:
    for text in df_result['文本']:
       file.write(text + '\n')
text = open(root+'\\data\\messages\\messages.txt', 'r', encoding='utf-8').read()
stopwords = open(root+'\\data\\messages\\stopwords.txt', 'r', encoding='utf-8').read().split('\n')

text = text.lower()
text = re.sub(r'[^a-z\s]', '', text)
wc = WordCloud(width=600, 
               height=400, 
               background_color="white", 
               max_words=1000, 
               stopwords=stopwords)

wc.generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()      
try:      
    wc.to_file(root+'\\result\\wordcloud.png')
except:
    os.mkdir(root+"\\result")
    wc.to_file(root+'\\result\\wordcloud.png')