T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    a_cnt = 0
    b_cnt = 0
    page_l = 1
    page_r = P
    while page_l < page_r:
        mid_page = int((page_l + page_r) / 2)
        a_cnt += 1
        if mid_page == Pa:
            break
        elif mid_page < Pa:
            page_l = mid_page
        elif mid_page > Pa:
            page_r = mid_page

    page_l = 1
    page_r = P
    while page_l < page_r:
        mid_page = int((page_l + page_r) / 2)
        b_cnt += 1
        if mid_page == Pb:
            break
        elif mid_page < Pb:
            page_l = mid_page
        elif mid_page > Pb:
            page_r = mid_page

    if a_cnt > b_cnt:
        print("#{} B".format(tc))
    elif b_cnt > a_cnt:
        print("#{} A".format(tc))
    else:
        print("#{} 0".format(tc))

