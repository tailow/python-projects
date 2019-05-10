a,b,gap=float(input("a:")),float(input("b:")),float(input("gap:"))
while abs(b-a)>gap:
    c=1/2*(a+b)
    if(a**2-5)*(c**2-5)<0:b=c
    else:a=c
print(c)