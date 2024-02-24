import requests
from bs4 import BeautifulSoup
# https://www.w3schools.com/python/ref_requests_response.asp
# https://dictionary.cambridge.org/vi/dictionary/english/hello
website = 'https://www.w3schools.com/python/ref_requests_response.asp'
result = requests.get(website)
content = result.text
print(content)
print(result.status_code)
# content = result.text
# soup = BeautifulSoup(content,'lxml')
# #title = soup.find("article",class_ = "main-article")
# #print(title)
# print(soup.find("h1").get_text())
# <span class="hw dhw">ease</span>
# //span[@class = "hw dhw"]/text()
# <div class="def ddef_d db">to make or <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/become" title="become" rel="">become</a> less <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/severe" title="severe" rel="">severe</a>, <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/difficult" title="difficult" rel="">difficult</a>, <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/unpleasant" title="unpleasant" rel="">unpleasant</a>, <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/pain" title="painful" rel="">painful</a>, etc.: </div>
# //div[@class = "def ddef_d db"]
//span/h1/text()
<div class="pos-header dpos-h"><div class="di-title"><span class="headword hdb tw-bw dhw dpos-h_hw "><span class="hw dhw">hello</span></span></div><div class="posgram dpos-g hdib lmr-5"><span class="pos dpos" title="A word or phrase that you say loudly or suddenly to express strong feelings.">exclamation</span>, <span class="pos dpos" title="A word that refers to a person, place, idea, event or thing.">noun</span></div> <div></div><span class="uk dpron-i "><span class="region dreg">uk</span><span class="daud">                    
 //div[@class = "pos-header dpos-h"]/*/text()
 //*[@id="page-content"]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div[1]/span[@class = "hw dhw"]/text()
 //*[@id="page-content"]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div[1]/span/span
 /html/body/div[2]/div/div[1]/div[2]/article/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div[1]/span/span

 //*[@id="page-content"]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div[1]/span/span/text()   # id get 
 //*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[@class = "def ddef_d db"]/text()
 <div class="def ddef_d db">used as an <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/informal" title="informal" rel="">informal</a> <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/greeting" title="greeting" rel="">greeting</a>, usually to <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/people" title="people" rel="">people</a> who you <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/know" title="know" rel="">know</a>: </div>