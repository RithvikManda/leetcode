
nums=[]
nums=list(map(input().split()))
c=nums[0]
cnt=1
for i in range(1,len(nums)):
    if nums[i]==c:
        cnt+=1
    else:
        cnt-=1
        if cnt==0:
            c=nums[i]
            cnt=1
print(c)        
        