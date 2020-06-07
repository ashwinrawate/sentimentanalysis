from textblob import TextBlob
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from textblob.sentiments import NaiveBayesAnalyzer
import csv
#import nltk
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')




my_url = 'https://inshorts.com/en/read'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


title_news = page_soup.findAll("div",{"class":"news-card z-depth-1"})
content_news = page_soup.findAll("div",{"class":"news-card-content news-right-box"})

file1 = 'news1.csv'
file2 = 'news2.csv'

f1 = open(file1, "w",encoding="utf-8")
f2 = open(file2, "w",encoding="utf-8")

headers1 = "Title\n"
headers2 = "Content\n"

f1.write(headers1)
f2.write(headers2)



for x in title_news:
    title = x.a.text.strip()
    f1.write(title.replace(",","|") + "\n")

for y in content_news:
    content = y.div.text.strip()
    f2.write(content.replace(",","|") + "\n")


f1.close()
f2.close()

while True:
    
    print('\nHello! Welcome to the News Analysis \nSelect from the following Categories.\n\n 1. See Title of News \n 2. See Content of News \n 3. See Sentiment Analysis of Title \n 4. See Sentiment Analysis of Content \n')
    check = input("Enter the number: ")
    
    
    if check =='1':
    
        for x in title_news:
            title = x.a.text.strip()
            print("Title: " + title + "\n")
    
    
    elif check =='2':
    
        for y in content_news:
            content = y.div.text.strip()
            print("\t Content:  " + content + "\n")
    
    
    elif check =='3':
    
        with open(file1,'r',encoding ='utf-8') as csv2:
                rows2 = csv.reader(csv2)
                for row in rows2:
                    sentence = row[0]
                    blob = TextBlob(sentence, analyzer = NaiveBayesAnalyzer())
                    subj = TextBlob(sentence)
                    pol = blob.polarity
                    subjectivity = subj.sentiment.subjectivity
                    positive = blob.sentiment.p_pos
                    negative = blob.sentiment.p_neg
                    
    #                sid = SentimentIntensityAnalyzer()
    #                pos_words = []
    #                neg_words = []
    #                neutral_words = []
    #                
    #                for words in rows2:
    #                    
    #                    sentence.encode('utf-8')
    #                    if(sid.polarity_scores(sentence)['compound']) >= 0.5:
    #                        pos_words.append(sentence)
    #                    elif(sid.polarity_scores(sentence)['compound']) <= -0.5:
    #                        neg_words.append(sentence)
    #                    else:
    #                        neutral_words.append(sentence)
                    print(sentence)
                    print("Polarity is ",pol,"\n Subjectivity is ",subjectivity,"\n Positive Words :",positive,"\n Negative Words : ",negative)
                    if pol < 0:
                        print("Negative Sentiment")
                    elif pol == 0:
                        print("Neutral Sentiment")
                    else:
                        print("Positive Sentiment")
                        
                    if subjectivity < 0.5:
                        print("Objective News \n")
                    else:
                        print("Subjective News \n")
                    
                        
                        
    
    elif check =='4':
        
        with open(file2,'r',encoding ='utf-8') as csv2:
                rows2 = csv.reader(csv2)
                for row in rows2:
                    sentence = row[0]
                    blob = TextBlob(sentence, analyzer = NaiveBayesAnalyzer())
                    subj = TextBlob(sentence)
                    pol = blob.polarity
                    subjectivity = subj.sentiment.subjectivity
                    positive = blob.sentiment.p_pos
                    negative = blob.sentiment.p_neg
                    print(sentence)
                    print("Polarity is ",pol,"\n Subjectivity is ",subjectivity,"\n Positive Words :",positive,"\n Negative Words : ",negative)
                    if pol < 0:
                        print("Negative Sentiment")
                    elif pol == 0:
                        print("Neutral Sentiment")
                    else:
                        print("Positive Sentiment")
                        
                    if subjectivity <0.5:
                        print("Objective News \n")
                    else:
                        print("Subjective News \n")
                        
                        
    ch = input("Do you want to continue?(y/n)")
    if ch == 'n':
        break
                 
                    
