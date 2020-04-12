n = int(input())
su = 0
temp = 0
run = True

# while temp != n+1 :
#
#     su = su + temp
#     if temp<10:
#      su = su * 10
#      print(su)
#     if temp>9:
#         su = su *100
#     temp = temp + 1
#
#
# print(int(su/10))
while temp==n+1 :
    su = su*10
    su=su+temp
    temp+=1
    print(su)

print(su)