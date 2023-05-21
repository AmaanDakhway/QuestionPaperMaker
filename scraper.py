#Pakage Imports
import requests
from bs4 import BeautifulSoup
import csv 
import random as r

#Requesting Source of the website
page_name = "interview-questions/"
page = requests.get(
   "https://intellipaat.com/blog/"+page_name)
#Getting the HTML source code of the website
soup = BeautifulSoup(page.content, 'html.parser')

#Variable Declarations
href_links = []
questions = []

#Searching the website for potential webpages
for element in soup.select('ul li a'):
  href_links.append(element.get('href'))

#Searching through all the webpages for questions
for i in href_links:
  page = requests.get(i)
  soup = BeautifulSoup(page.content, 'html.parser')
  for ql in soup.select('h3 strong'):
    x = ql.text
    x = x.lstrip(" .1234567890")
    questions.append(x)

#Declaring Variables for CVS related operations
fields = ['Questions','Difficulty']
rows = []

#Creating and writing a CSV file
for i in questions:
  rows.append([i])

filename = "all_questions.csv"
with open(filename, 'w') as csvfile:
  csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
  csvwriter.writerow(fields) 
          
    # writing the data rows 
  csvwriter.writerows(rows)

#Flag: End of Execution
print("Dataset in CSV format created.")