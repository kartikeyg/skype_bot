def scraper(url,t):
    try:
        os.remove('RAW_1.txt')
        os.remove('RAW_2.txt')
        print('Cleared Chached Data')
    except:
        print('Cleared Chached Data')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    file = open('RAW_1.txt','wb')
    file.write(str(soup.findAll()).encode("utf-8"))
    file.close()
    print('Fetched')
    time.sleep(t)
    file2 = open('RAW_2.txt','wb')
    file2.write(str(soup.findAll()).encode("utf-8"))
    file2.close()
    print('Started Comparing')
    f1 = open('RAW_1.txt', 'rb')
    a = str(f1)
    c = a.split()
    f1.close()
    f2 = open('RAW_2.txt','rb')
    b = str(f2)
    d = b.split()
    f2.close()
    if len(a)<len(b):
        l=len(d)
    else:
        l=len(c)
    with open("RAW_1.txt",'rb') as f:
      lines = f.read()
    with open("RAW_2.txt",'rb') as f:
      lines2 = f.read()
    l1 = []
    l2 = []
    for a in lines:
        c = str(a)
        words = c.strip().split()
        l1.append(words)
    for b in lines2:
        d = str(b)
        w = d.strip().split()
        l2.append(w)
    print('Compared')
    if l1!=l2:
        return yes
    os.remove('RAW_1.txt')
    os.remove('RAW_2.txt')
    time.sleep(1)
    
def skype(sk,content):
    ch = sk.contacts[contact].chat
    ch.sendMsg(content)

#main_block
import os
import time
try:
    import requests
    import urllib.request
    from bs4 import BeautifulSoup
    from skpy import Skype
    print('All Libraries Installed.\nStarting Scraper')
except:
    print('All Libraries not installed')
    print('Started Installing Libraries')
    os.system('pip install -r req.txt --user')
    print('Starting Scraper')
url = input('Enter The URL To Scrape\n>>')
ask  = input('Do you Want To Run The Script Infinetly(y/n)\n>>')
username = input('Enter Your Username')
password = input('Enter your Password')
sk = Skype(username, password)
content = 'A Change Was Detected On Given URL'

if ask == 'y' or ask == 'Y' or ask == 'Yes':
    t = int(input('Enter Time Interval B/W 2 Scraps(in sec):\n>>'))
    while True:
        if scraper(url,t)=='Yes':
            print('Changes Detected')
            print('Sending Skype MSG')
            skype(sk,content)
        
else:
    print("Default Time Interval Is 10 Sec")
    if scraper(url,10)=='Yes':
            print('Changes Detected')
            print('Sending Skype MSG')
            #skype()
            a = input('Hit Enter To Exit')
    else:
        a = input('Hit Enter To Exit')


