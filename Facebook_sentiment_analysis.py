#VADER -  Valance Aware Dictionary and sentiment Reasoner
import pandas as pd
import nltk
from nltk.sentiment.vader impost SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file = 'data_file.xslsx'
#Read from Excel
xl = pd.ExcelFile(file)
#Parsng the Excel sheet to data frame
dfs = xl.parse(x1.sheet_names[0])
#removes blank rows from the data frame
dfs = list(dfs['Timeline'])
print(dfs)
sid = SentimentInteensityAnalyzer()
str1 = "UTC+5:30"
for data in dfs:
    a = data.find(str1)
    if a==-1:
        ss = sid.polarity_scored(data)
        for k in ss:
            print(k,ss[k])
