# pip install r2pipe
import r2pipe
import os,sys
import subprocess

base_path = os.getcwd()

data1_path = base_path + "/data1"
data2_path = base_path + "/data2"

list_Target = list() # 비교할 파일들이 명시되어있는 파일명

# function
def analysis_bin(data1_path):
    print(data1_path)
    list_im1_path = data1_path.split("auto_radiff2")
    front_path = list_im1_path[0]
    back_path = list_im1_path[1]
    back_path = back_path[6:]
    
    data2_path = front_path + "auto_radiff2" + "/data2" + back_path
    
    rel_data1_path = data1_path.split("auto_radiff2")[1]
    rel_data2_path = data2_path.split("auto_radiff2")[1]
    
    # r2pipe를 사용하여 radare2를 시작하고 radiff2 명령 실행
    cmd = f'radiff2 -s {data1_path} {data2_path}'
    
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f'Error: {e.returncode}, Output: {e.output}'

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
        
        if os.path.isfile(cur_path):
            # 파일인 경우, 파일 경로를 출력하거나 다른 작업을 수행할 수 있습니다.
            
            # (3) 
            if not cur_file in list_Target:
                # if target에 있다면?
                # print(f'Dep {cur_index} - 파일: {cur_file}')
                
                # (4)
                # radare2
                # (+) sh스크립트인지, ELF바이너리인지에 따른 diff 차별점
                
                
                
                result = analysis_bin(cur_path) # ELF파일
                
                # (5) 결과 가공
                print(result)
            else:
                print(f"{cur_path}는 존재하지 않습니다.")
            
            
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
        list_Target.append(line[:-1])
        #print(line[:-1])

# (2) data1폴더를 이용하여 기준으로 탐색하되 target을 찾으면 
#     data2폴더의 데이터와 비교
# => 폴더 깊이 탐색
explore_directory(data1_path, 0)


# 비교기준 : data1