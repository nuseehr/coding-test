import sys

'''

기준 배열 [[2, 1], [3, 4], [1, 2], [1, 3], [3, 2]]

1. 첫번째 값 기준 정렬.
Arr.sort(key=lambda x:x[0])

결과 : [[1, 2], [1, 3], [2, 1], [3, 4], [3, 2]]
0번째 인덱스에 대해서 오름차순 정렬은 되었지만
동일한 0번째 인덱스를 가진 1번째 인덱스에 대해서는 정렬이 되지 않았음을 알 수 있다.

2. 두번째 값 기준 정렬.
Arr.sort(key=lambda x:( x[0], -x[1] ))

결과 : [[1, 3], [1, 2], [2, 1], [3, 4], [3, 2]]
여기서는 먼저 0번째 인덱스에 대해서 오름차순으로 정렬한 뒤,
동일한 값의 경우 내림차순으로 재정렬된다.

3. 기본 정렬.
Arr.sort()

결과 : [[1, 2], [1, 3], [2, 1], [3, 2], [3, 4]]
위에서 했던 작업이 무색하게 0번째 인덱스를 오름차순 정렬하고,
같은 값의 경우 오름차순으로 재정렬까지 시켜준다

4. 딕셔너리 이용 정렬.
sorted(Dict.items(), key=lambda x:x[0])
'''

N = int(sys.stdin.readline())
Arr = [[0]*2 for _ in range(N)]

for i in range(N):
    Arr[i] = list(map(int, sys.stdin.readline().split()))
    
Arr.sort()

for i in range(N):
    print(Arr[i][0], Arr[i][1])

