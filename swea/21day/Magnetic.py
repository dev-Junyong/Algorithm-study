
for tc in range(1, 10+1):
    N = int(input())
    magnet = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0  # 교착상태
    for c in range(N):  # 세로 방향으로만 움직이니깐 가로방향말고 세로부터
        idx = 0  # 자성체 체크
        for r in range(N):  # 세로로 확인
            if magnet[r][c] == 1 and idx == 0:  # 붉은색
                idx = 1  # 붉은색 존재 확인
            elif magnet[r][c] == 2 and idx == 1:  # 파란색
                idx = 0  # 값 리셋
                cnt += 1  # 교착 체크
    print("#{} {}".format(tc, cnt))
