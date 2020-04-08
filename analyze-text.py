import pandas as pd
import os
import csv

os.getcwd()

dfs = []

for file in os.listdir("/Applications/MAMP/htdocs/newsroom-homepages/"):
    if file.endswith(".tsv"):
        print file
        df = pd.read_csv(file,delimiter='\t', quoting=csv.QUOTE_NONE, encoding='utf-8')
        df['date_of_screenshot'] = file.replace(".tsv","").replace(".jpeg-output","")
        df = df[df.text.notnull()]
        dfs.append(df)
merge = pd.concat(dfs)
print merge



# df = pd.read_csv('202031.tsv',delimiter='\t', quoting=csv.QUOTE_NONE, encoding='utf-8')
# df['date_of_screenshot'] = '202031'
# print df
# df2 = pd.read_csv('202032.tsv',delimiter='\t', quoting=csv.QUOTE_NONE, encoding='utf-8')
#
# #add dates to column
#
# merge = pd.concat([df,df2])
# print merge.shape
