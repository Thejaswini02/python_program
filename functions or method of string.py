s=input("enter a string: ")
a=len(s)
print('the length of the string is: '+str(a))

t=' sattva '
b=t.strip()
print(b)
b=t.rstrip()
print(b)
b=t.lstrip()
print(b)

txt = "Hlo guys, welcome to my world"
x = txt.find("welcome")
print(x)
x= txt.rfind("to")
print(x)
x=txt.index('o')
print(x)
x=txt.rindex('o')
print(x)
x=txt.count('o')
print(x)
x=txt.replace('world','home')
print(x)
y=txt.split(' ')
print(y)
x=','.join(y)
print(x)
y="yeah i'm good"
c=y.upper().lower()
print(c)
c=y.istitle()
print(c)
c=y.startswith('yeah')
print(c)
c=y.endswith('yeah')
print(c)
