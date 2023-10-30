# pip install r2pipe
import r2pipe
import os,sys
import subprocess

mode_set = "target" # default : target -> 전체 비교한다면 total
# trigger : targetlist.txt 최상단에 *를 넣으면 됨

base_path = os.getcwd()

data1_path = base_path + "/data1"
data2_path = base_path + "/data2"

list_Target = list() # 비교할 파일들이 명시되어있는 파일명
list_result = [] # 보고서 dict가 담기는 곳

# function
def is_elf_binary(file_path):
    # ELF 바이너리의 매직 넘버는 '7F 45 4C 46'입니다.
    elf_magic_number = b'\x7FELF'
    
    # 파일의 처음 4바이트를 읽어 매직 넘버를 확인합니다.
    with open(file_path, 'rb') as file:
        magic_number = file.read(4)
    
    if magic_number == elf_magic_number:
        return True
    else:
        return False

def is_shell_script(file_path):
    # 파일의 처음 2바이트를 읽어 매직 넘버를 확인합니다.
    with open(file_path, 'rb') as file:
        magic_number = file.read(2)

    # 셸 스크립트의 매직 넘버는 '#!' 입니다.
    if magic_number == b'#!':
        return True
    else:
        return False

def analysis_bin(data1_path):
    #print(data1_path)
    list_im1_path = data1_path.split("auto_radiff2")
    front_path = list_im1_path[0]
    back_path = list_im1_path[1]
    back_path = back_path[6:]
    
    data2_path = front_path + "auto_radiff2" + "/data2" + back_path
    
    rel_data1_path = data1_path.split("auto_radiff2")[1]
    rel_data2_path = data2_path.split("auto_radiff2")[1]
    
    # r2pipe를 사용하여 radare2를 시작하고 radiff2 명령 실행
    cmd = f'radiff2 -s {data1_path} {data2_path}' # s옵션 유사도 수치
    
    dict_target_result = {
        'target_path' : '',
        'similarity' : '',
        'distance' : '',
        'error' : None
    }
    target_data = "."+rel_data1_path[6:]
    dict_target_result['target_path'] = target_data
    
    try:
        
        response = subprocess.check_output(cmd, shell=True, text=True)
        
        list_response = response.split("\n")
        
        target_similarity = list_response[0].split(":")[1]
        target_distance = list_response[1].split(":")[1]
        
        dict_target_result['similarity'] = target_similarity
        dict_target_result['distance'] = target_distance
        
        # print(dict_target_result)
        mid_result = dict_target_result
        
        return mid_result
    except subprocess.CalledProcessError as e:
        
        dict_target_result['error'] = f'Error: {e.returncode}\n-> Output: {e.output}'
        
        mid_result = dict_target_result
        
        return mid_result

def explore_directory(path, cur_index): # 폴더 깊이 탐색
    rel_path = path.split("auto_radiff2")[1]
    print(f"{cur_index} - .{rel_path}")

    # 현재 경로의 파일과 폴더 목록을 얻습니다.
    list_data = os.listdir(path)
    cur_var = "v"+str(cur_index)
    
    # 폴더 깊이 탐색
    # (3) 파일일떄 list_target과 비교하여 있다면 분석 타겟으로 삼음
    # (4) 탐지된 파일 분석
    for cur_file in list_data:
        cur_path = os.path.join(path, cur_file)
        
        if (os.path.isfile(cur_path)):
            # 파일인 경우, 파일 경로를 출력하거나 다른 작업을 수행할 수 있습니다.
            
            # (3) 
            if (not cur_file in list_Target) or (mode_set == 'total'):
                # if target에 있다면?
                # print(f'Dep {cur_index} - 파일: {cur_file}')
                
                # (4)
                # radare2
                # (+) sh스크립트인지, ELF바이너리인지에 따른 diff 차별점
                result_mid = None
                
                # 파일 시그니처를 이용한 구분
                if is_shell_script(cur_path):
                    pass # sh파일에 대한 분석(파일 diff)
                elif is_elf_binary(cur_path):
                    result_mid = analysis_bin(cur_path) # ELF파일
                else:
                    print(f"{cur_path} is neither a shell script nor an ELF binary.")
                
                #result_mid = analysis_bin(cur_path) # ELF파일
                
                # (5) response 가공
                list_result.apppend(result_mid)
            else:
                rel_cur_path = "."+cur_path.split("auto_radiff2")[1]
                print(f"{rel_cur_path}는 존재하지 않습니다.\n")
            
            
        elif os.path.isdir(cur_path):
            # 폴더인 경우, 재귀적으로 해당 폴더를 탐색합니다.
            # print(f'Dep {cur_index} - 폴더: {cur_path}')
            explore_directory(cur_path, cur_index+1)
    print()

# ===

# (1) tragetlist를 통해 타겟 파일들 목록화
with open("targetlist.txt") as f:
    lines = f.readlines()
    
    for line in lines:
        if line == "*\n":
            mode_set = "total"
            break
            
        list_Target.append(line[:-1])
        #print(line[:-1])

# (2) data1폴더를 이용하여 기준으로 탐색하되 target을 찾으면 
#     data2폴더의 데이터와 비교
# => 폴더 깊이 탐색
explore_directory(data1_path, 0)

# (6) list_result 최종 가공하여 보고서 형태


# 비교기준 : data1

# (+) radare2의 추가적인 기능을 이용하면 차이가 발생했을떄 
# 좀더 많은 데이터를 얻을 수 있음