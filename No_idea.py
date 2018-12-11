# Enter your code here. Read input from STDIN. Print output to STDOUT
def search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return 1

    return -1
str=input()
n=int(str[0])
m=int(str[2])
arr=list(map(int, input().split()))
print(arr)

a=list(map(int, input().split()))
b=list(map(int, input().split()))
print(a)
print(b)
happiness=0


for i in range(n):
    if search(a,arr[i])==1:
        happiness+=1
    elif search(b,arr[i])==1:
        happiness-=1

print(happiness)