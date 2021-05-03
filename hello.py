print("hello world")
#게임을 만든다
#딕셔너리 ,함수 ,리스트

# 1. 딕셔너리 생성
d = {'a': 123123}
 
# (2. 값 추가)
d[999] = 10                 # 숫자 키, 숫자 값
d['99'] = 111               # 문자 키, 숫자 값
d['BlockDMask'] = "blog"    # 문자 키, 문자 값
d['wow'] = [1, 2, 3, 4, 5] # 문자 키, 리스트 값
d[(1, 2)] = "this is value # 튜플 키, 문자 값
d[1] = (3, 'a', 5)         # 숫자 키, 튜플 값
 
 
# (3. 값 접근)
print("3. 딕셔너리 값 접근)
print(f'd["a"] = {d["a"]}')
print(f'd[999] = {d[999]}')
print(f'd[1] = {d[1]}')        # 숫자 키는 index와 헷갈릴 수 있음
print(f'd[(1,2)] = {d[(1,2)]}')
print(f'd["wow"] = {d["wow"]}')
print(f'd["BlockDMask"] = {d["BlockDMask"]}')
 
# (4. 값 변경)
print()
print("4. 딕셔너리 값 변경")
print(f'before : d["BlockDMask"] = {d["BlockDMask"]}')
d["BlockDMask"] = 'boy'
print(f'after  : d["BlockDMask"] = {d["BlockDMask"]}')
 
print(f'before : d["a"] = {d["a"]}')
d["a"] = 'asdf1234'
print(f'after  : d["a"] = {d["a"]}')

# 2.함수내에서 i, mylist 값 변경
def f(i, mylist):
    i = i + 1
    mylist.append(0)
 
k = 10       # k는 int (immutable)
m = [1,2,3]  # m은 리스트 (mutable)
 
f(k, m)      # 함수 호출
print(k, m)  # 호출자 값 체크
# 출력: 10 [1, 2, 3, 0]

# 리스트 인덱싱
# 길이 8인 리스트
a = [101, 102, 'b', 'l', 'o', 103, 104, 105]
 
# 인자 접근
print(f'a[0] : {a[0]}')
print(f'a[1] : {a[1]}')
print(f'a[2] : {a[2]}')
# ...
print(f'a[7] : {a[7]}')
 
# print(f'a[8] : {a[8]}') - error
 
 
# 그럼 마이너스로 접근이 가능?
print(f'a[-1] : {a[-1]}')
print(f'a[-2] : {a[-2]}')
# ...
print(f'a[-8] : {a[-8]}')
 
# print(f'a[-9] : {a[-9]}') - error
