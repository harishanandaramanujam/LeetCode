Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Input: [1,8,6,2,5,4,8,3,7]
Output: 49


Code:::
a = [1, 8 ,6 ,2 ,5 ,4 ,8 ,3 ,7]
b=len(a)
c=[]
m=1
for i in range(b-1):
    k=i+1
    m=1
    n=1
    for j in range (k,b):
        if a[i]>a[j]:
            d = a[j]*m
            
            c.append(d)
            #print("This is first:", d, a[i], m)
            m=m+1
        else:
            d=a[i]*m
            
            c.append(d)
            #print("This is second: ", d, a[i], m)
            m=m+1
d=max(c)
print(d)
