import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import *

#Table Initialization
paperlist = Workbook(encoding = 'utf-8')
table = paperlist.add_sheet('data')
table.write(0, 0, 'Title')
table.write(0, 1, 'URL')
table.write(0, 2, 'Authors')
table.write(0, 3, 'Snippet')
table.write(0, 4, 'Venue')
table.write(0, 5, 'Citation')
line = 1

#Scrape paper
keyword = "Annotation+AR"
maxCount = 30
for start in range(0, maxCount+1, 10):
    print(start)
    url = "https://scholar.google.com/scholar?start="+str(start)+"&q="+keyword+"&hl=en&as_sdt=0,22"
    print(url)
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    f = requests.get(url)
    soup = BeautifulSoup(f.content, 'lxml')
    paperTags = soup.find_all("div",{
       'class': 'gs_r gs_or gs_scl'
     })
    print(f)
    for anchor in paperTags:
        print("paper")
        paper = anchor.find_next("div", {
            'class': 'gs_ri'
        })
        title = paper.find_next("h3").get_text()
        paperUrl = paper.find_next("h3").find_next("a")["href"]
        authorTag = paper.find_next("div",{'class': 'gs_a'}).get_text().split('-')
        author = authorTag[0]
        venue = authorTag[1]
        snippet = paper.find_next("div",{'class': 'gs_rs'}).get_text()
        resultId = anchor["data-cid"]
        citationUrl = "https://scholar.google.com/scholar?output=cite&q=info:"+resultId+":scholar.google.com"
        print(title)
        print(paperUrl)
        print(author)
        print(snippet)
        print(venue)
        print(citationUrl)
        #Write to table
        table.write(line, 0, title)
        table.write(line, 1, paperUrl)
        table.write(line, 2, author)
        table.write(line, 3, snippet)
        table.write(line, 4, venue)
        table.write(line, 5, citationUrl)
        line += 1


paperlist.save('AR_Annotation_paperList.xls')
