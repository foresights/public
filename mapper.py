# -*- coding: utf-8 -*-
"""mapper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zE3h_VS5sxVjBmLOvoxnbquTOGaTsJ1Q
"""

#! /usr/bin/env python3

"""
import io,re,sys,nltk
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords as sw
puncts='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
stopWords=set(sw.words('english'))
stream_input=io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8') # non latin1
for line in stream_input:
	Line_Data=line.strip()
  Line_Data=re.sub(r'[^\w\s]','',Line_Data)
  Line_Data=Line_Data.lower()
  for x in Line_Data:
    if x in puncts:
      Line_Data=Line_Data.replace(x," ")
  tokens=Line_Data.split()
  for token in tokens:
    if token not in stopWords:
      print('%s\t%s' % (token, 1))
 """

import sys
## Reading [System's] Standard-Input for [each] Line
for line in sys.stdin:
  ## Assigning Data in Array, Stripping-off New Line Whitespace & Splitting on Comma/Tab
  Line_Data=line.strip().split(",") # .split("\t") # .split()
  
  #Multiple-Assigning Line_Data Item(s)
  #Wban,YearMonthDay,Time,StnType,Indicator,Conditions,Visibility,WeatherType,DryBulbTemp=Line_Data
  
  if Line_Data[8]!="-":
	try:
		Key=Line_Data[1] #  YearMonthDay
		Value=int(Line_Data[8]) # Dry Bulb Temp
		## Passing on Data from Mapper to Reducer
		print("%s\t%s" % (Key,Value)) # ("{0}\t{1}".format(Key,Value))
	except ValueError:
		continue