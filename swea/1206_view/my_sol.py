import sys
sys.stdin = open('input.txt')

T = 10

num_bld = int(input())
hght_bld = list(map(int, input().split()))

total = 0

for tc in range(1, T+1):
    for i in range(2, num_bld - 3):
        dfnc_list = [hght_bld[i] - hght_bld[i-1], hght_bld[i] - hght_bld[i-2], hght_bld[i] - hght_bld[i+1], hght_bld[i] - hght_bld[i+2]]
        if min(dfnc_list) >= 0:
            view = min(dfnc_list)
            total += view
        else:
            view = 0
            total += view

    print(f'#{tc} {total}')