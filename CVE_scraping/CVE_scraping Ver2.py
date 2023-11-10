import requests,csv
from bs4 import BeautifulSoup
from datetime import datetime
import googletrans
import time

'''
(리포트 타입)
1. csv(.csv)
=> ,로 구분되어 excel로 볼 수 있음(단 2,3번째의 칸 길이 조절 필요)
2. line(.txt)
=> CVE-2023-????|한글내용|영어내용 으로 one line으로 구분되어있음
3. report(.txt)
=> 
keyword : ????? / Total : ?????

CVE-2023-????
한글내용
<
영어내용
>
=> 쭉 이런 내용이 문단별로 나뉘어서 기록되어있음
'''
report_type = 'csv' # csv(default), line, report
total_cve = [] # [cve, 한글, 영어]
input_keyword = ''

def make_filename():

    # 현재 날짜와 시간 가져오기
    current_datetime = datetime.now()

    # 파일 이름으로 사용할 형식 지정
    filename_format = "%Y-%m-%d_%H-%M-%S"

    # 날짜 시간을 파일 이름 형식에 맞게 포맷팅
    formatted_datetime = current_datetime.strftime(filename_format)

    filename = f'{formatted_datetime}_report_{input_keyword}'# + 뒤에 확장자
    
    return filename

def write_report_csv():
    global total_cve

    filename = make_filename()+'.csv'

    new_order = [0,2,1]
    tranport_data = []
    for row in total_cve:
        new_row = [row[i] for i in new_order]
        tranport_data.append(new_row)

    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tranport_data)
    print(f'CSV 파일 {filename}이 생성되었습니다.')

def write_report_line():
    global total_cve
    
    filename = make_filename()+'_line'+'.txt'
    filename.replace('report','line')

    with open(filename, mode='w', newline='') as f:
        for list_cve in total_cve:
            line = f"{list_cve[0]}|{list_cve[2]}|{list_cve[1]}\n"
            f.write(line)
    print(f'line형식의 txt파일 {filename}이 생성되었습니다.')
    

def write_report_report():
    global total_cve

    filename = make_filename()+'_report'+'.txt'

    with open(filename, mode='w') as f:
        f.write(f"keyword : {input_keyword} / Total : {len(total_cve)}\n\n")

        for list_cve in total_cve:
            print(list_cve)
            print(len(list_cve))
            time.sleep(1)
            f.write(f"{list_cve[0]}\n{list_cve[2]}\n<\n{list_cve[1]}\n>\n\n")
    print(f'report형식의 txt파일 {filename}이 생성되었습니다.')

def create_report(input_type):
    global total_cve

    if input_type == '':
        report_type = 'csv'
    else:
        report_type = input_type
    
    if report_type == 'csv':
        write_report_csv()
    elif report_type == 'line':
        write_report_line()
    elif report_type == 'report':
        write_report_report()
    else:
        print("잘못된 type입니다.")

# =====
def main():
    global total_cve
    global report_type
    global input_keyword

    total_cve.append(['CVE','en','ko'])

    # 지역변수
    cve_url = 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=' # +input keyword
    papago_url = 'https://papago.naver.com/?sk=en&tk=ko&hn=1&st=' # +input content

    # 1. keyword 입력
    print("CVE에서 검색할 Keyword를 입력해수세요.")
    input_keyword = input("> ")
    cve_url = cve_url + input_keyword

    res_cve = requests.get(cve_url)
    content_cve = res_cve.content # content는 무엇을 담고 있을까?
    
    soup = BeautifulSoup(content_cve, "html.parser")

    div_with_rules = soup.find('div', id='TableWithRules')

    # 2. cve content 크롤링
    if div_with_rules:
        div_contents = div_with_rules.get_text() # 내부 내용만 가져오겠다.
        list_contents = div_contents.split('\n\n\n\n')
    else:
        print("Couldn't find the specified div.")

    # content 가공
    list_cve = []
    for content in list_contents:
        if content == 'Name\nDescription' or content == '':
            continue
        
        list_content = content.split('\n') # 1 : CVE, 2 : desc
        for content in list_content:
            if content == '':
                continue

            if  content[:3] == 'CVE':
                list_cve.append(content)
            else:
                list_cve.append(content)
                total_cve.append(list_cve)
                list_cve = []
    
    translator = googletrans.Translator()
    # 파파고 돌면서 한글 번역
    for i in range(len(total_cve)):

        inStr = total_cve[i][1]

        outStr = translator.translate(inStr, dest = 'ko', src='auto')

        total_cve[i].append(outStr.text) # 영어 추가

        #print(f"{inStr} => {outStr.text}")
    
    # 번역된 cve로 보고서 생성
    create_report(report_type)


# =====
main()
