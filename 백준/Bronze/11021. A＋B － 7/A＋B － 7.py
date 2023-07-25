# 테스트 케이스의 개수 T를 입력받음
T = int(input())

# T번 반복하며 A와 B를 입력받고, 결과를 출력
for i in range(1, T+1):
    A, B = map(int, input().split())
    result = A + B
    print("Case #{}: {}".format(i, result))
