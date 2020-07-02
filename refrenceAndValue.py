def double(arg):
    print('before arg ',arg)
    arg = arg *2;
    print('after arg ',arg)

def change(arg):
    print('before arg ',arg)
    arg.append('more data')
    print('after arg ',arg)

def changetuple(arg):
    print('before arg ',arg)
    arg = (4)
    print('after arg ',arg)

x = 5
print('before function call x= ',x)
double(x)
print('after function call x= ',x)

y = [1,2,3]
print('before function call y= ',y)
change(y)
print('after function call x= ',y)

tuplez = (1,2,3)
print('before function call z= ',tuplez)
changetuple(tuplez)
print('after function call z= ',tuplez)
