l, r = map(int, input().split())

tmp = (r - l) // 10
ans = tmp * 4

if l % 10 != 0:
    for i in range(l, (l // 10 + 1) * 10 + 1):
        if i % 10 == 1 or i % 10 == 4 or i % 10 == 6 or i %10 == 9:
            ans += 1
if r % 10 != 0:
    for i in range(l, (l // 10) * 10 + 1):
        if i % 10 == 1 or i % 10 == 4 or i % 10 == 6 or i %10 == 9:
            ans += 1
