"""สลากกินแบ่ง"""
A_all, N_all = map(str, input().split())
B_me, N_me = map(str, input().split())

if A_all == B_me and N_all == N_me:
    print(1000000)
elif N_all == N_me:
    print(100000)
elif A_all == B_me and N_all[2:5] == N_me[2:5]:
    print(2000)
elif A_all == B_me and N_all[3:5] == N_me[3:5]:
    print(1000)
elif N_all[2:5] == N_me[2:5]:
    print(200)
elif N_all[3:5] == N_me[3:5]:
    print(100)
elif A_all == B_me:
    print(20)
else:
    print(0)
