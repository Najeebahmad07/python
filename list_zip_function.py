l=[10,20,30,40]
l1=[50,60,70,80,90] #zip function sirf barabar element ko hi print karega isme error nhi aayega
for a,b in  zip(l,l1):
    print(a,b)

    #ab dusre method se bhi list ko print kar sakte hai
    print("--------------------")

t=len(l)
for h in range(t):
    print(l[h],l1[h])
