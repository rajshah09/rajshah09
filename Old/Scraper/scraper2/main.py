import os
import requests
from bs4 import BeautifulSoup

file_path ='/home/rextron/websites/LF-Directory/www.locatefamily.com/Street-Lists/India/'

for b in os.listdir('/home/rextron/websites/LF-Directory/www.locatefamily.com/Street-Lists/India/'):
    file_path2=file_path+b
    try:
        with open(file_path2, 'r', encoding='utf-8') as file: 
            html_content = file.read()
    except:continue
    soup =BeautifulSoup(html_content, "html.parser")

    with open('output.txt','a',encoding='utf-8') as output_file:
        for numbers in soup.find_all(itemprop='telephone'):
            if(len(numbers.text.replace(" ",""))==12):
                output_file.write(numbers.text.replace(" ","")+'\n')
            #else: continue
            #print(numbers.text, end='\n')