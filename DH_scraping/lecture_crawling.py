import requests
from bs4 import BeautifulSoup
import time

base_path = 'https://dreamhack.io/lecture/courses'

length = 700
total_result = ['' for j in range(length)]

for i in range(length):
    if i%10 ==0:
        print(f"{i} 진행중")

    lecture_num = i
    target_path = base_path + '/' + str(lecture_num)

    r = requests.get(target_path)
    #print(r.status_code, r.text) 
    result = r.text
    if 'error-search-no-result' in result: # X
        continue
    else:
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.select_one('#__layout > div > main > section > section > header > div > div.information > h2 > span')
        title = str(title).split(">")[1].replace('</span>','').replace('</span','')
        total_result[i] = title
    #print(lecture_num,title)
    time.sleep(0.1)

#print(total_result)

with open('./test.txt','wt',encoding='utf-8') as f:
    for j in range(len(total_result)):
        line = f"{j} => {total_result[j]}\n"
        if total_result[j] != '':
            f.write(line)
            #print(line)
        else:
            #print(line)
            continue