import pandas as pd #import pandas
import os #import
import glob #import glob
path = '/Volumes/Passport/ocr-test/cnn' #name filepath to relevant directory

#check for keyword string by file

data = {} #declare a new dictionary

for filename in glob.glob(os.path.join(path, '*.txt')): #for .txt file in pytesseract folder
    if "climate" in open(filename).read(): #find "climate" and
        #print("true")
        data.update({filename: 1}) #add key, value to dictionary
    else: #if no match found,
        #print("false")
        data.update({filename: 0}) #add key, value to dictionary

dataDF = pd.DataFrame(list(data.items()))  #convert dictionary to pandas dataframe
dataDF.to_csv("6am_cnn.csv") #convert dataframe to csv
