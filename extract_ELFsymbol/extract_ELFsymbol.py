import r2pipe
import os, sys

base_path = '/home/rd/Greedun/Project/exitless'
libc_path = base_path + '/_hda1.extracted/usr/lib'

list_allow_exp = ['so','7','1','2','6']
isPoint = True
list_point = ['class', 'method']
isOk = False

# filtering data list
list_filter_word = [] # fcn.*, entry.*, segment.*
with open(base_path+'/filter.txt','r') as g:
    lines = g.readlines()
    
    for line in lines:
        list_filter_word.append(line[:-1])
#print(list_filter_word)

count = 0
with open(base_path+'/export_libc.txt','w') as f:
    list_dir = os.listdir(libc_path)
    
    total_libc = dict()
    
    print(f"Total file : {len(list_dir)}")
    for libc in list_dir:
        count += 1
        target_path = libc_path + '/' + libc
        
        list_export_symbols = [] # libc file : []
        
        # 분석할 파일 구분
        # 확장자 구분
        list_test = libc.split('.')
        if not list_test[-1] in list_allow_exp:
            continue
        
        # 심볼릭 링크 구분
        if os.path.islink(target_path):
            # 심볼릭 링크라면 continue
            continue
            
        
        print(f"[{count}] target file => {libc}")
        
        # Radare2 프로세스 시작
        r2 = r2pipe.open(target_path)  # 분석할 이진 파일 경로를 지정하세요.
        
        # 분석 명령 실행
        r2.cmd("aaa")  # 분석 명령을 실행하여 함수와 기타 정보를 분석합니다.
        
        # 심볼 테이블 정보 추출 (fs: 함수 심볼)
        symbol_table = r2.cmdj("fj")
        
        # 심볼 정보 출력
        for symbol in symbol_table:
            symbol_name = symbol["name"]
            symbol_offset = symbol["offset"]
            # print(f"Symbol Name: {symbol_name}, Offset: 0x{symbol_offset:x}")
            
            # confirm_filter - 함수화 하기엔 오버헤드 과다
            # 1. 리스트 점검
            if symbol_name in list_filter_word:
                continue
            
            # 2. 와일드 카드 점검
            # fcn.*, entry.*, segment.*
            list_wild = ['fcn', 'entry', 'segment', 'case', 'section', 'switch','str','reloc','obj']
            list_test = symbol_name.split(".")
            if list_test[0] in list_wild:
                continue
            
            # target이 있다면 선택적 저장 시전
            if isPoint:
                for point in list_point:
                    i_point = symbol_name.find(point)
                    #print(i_point)
                    if i_point > -1 :
                        isOk = True
                
                if isOk:    
                    list_export_symbols.append(symbol_name)
                    isOk = False
                    continue
            else:
                list_export_symbols.append(symbol_name)
        total_libc[libc] = list_export_symbols
        # Radare2 프로세스 종료
        r2.quit()
        
        if len(list_export_symbols) == 0:
            continue
        
        f.write(f"[{count}] Name : {libc}\n")
        for symbol in total_libc[libc]:
            f.write(symbol+'\n')
        f.write(f"\n========== - ========== - ========== - ==========\n")
        
        del r2
        del list_export_symbols
        #print(libc)
        #print(total_libc[libc])
        
        #print("========== - ========== - ========== - ==========\n")
        

