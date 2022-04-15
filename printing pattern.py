lines=int(input())
if lines%2!=0:
    half_len=int((lines+1)/2)
    i=1
    while i<=half_len:
        print(i*'#')
        i+=1
    j=half_len-1
    while j>=1:
        print(j*'#')
        j-=1
else:
    print('even number')
