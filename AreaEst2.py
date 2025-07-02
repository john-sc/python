import math
import ctypes
#MessageBox = ctypes.windll.user32.MessageBoxW  # MessageBoxA in Python2
#MessageBox(None, 'Message\nfor\nthe\nuser', 'Window title', 0)

n=4
start=2.0
stop=10.0 # math.pi
def fx(x):
    z = math.sqrt(x*x*x + 1.0)
    #z = math.sin(x)
    #z=(2*x-1)/(x*x+4*x+6)
    #z=4*x*math.exp(-x*x)
    #z=math.exp(-x*x)+1.0/(x+1)
    #z=math.sqrt(x*x+1)
    #z=x*math.pow(x*x+2,1.0/3.0)
    #z=(x*x-1)/math.exp(x/2.0)
    #xx=math.sqrt(x)
    #z=xx*math.sqrt(x*xx+7.0)
    #z=math.exp(-x) + 1/(x*x*x)
    #z=x/math.sqrt(x*x+1)
    #z=3.14159265359*4*math.exp(-4*x)
    return z
    

fstring = '{:.5f}'  # format string

step=(stop - start)/n
print("n=",n, "start=",start,"stop=",stop,"step=",step)

i=0
xval=0.0
#step=.0625/256
#mid=0.0
esttrap=0.0
estleft = 0.0
estrite=0.0
estmid=0.0
simp=0.0
y=0.0
ymid=0.0

i=0
sm=0.0
print("i", "xval", "midval","f(xi)","f(mid)")
xval=start
xvalmid=start+step/2.0;
estleft=fx(xval)
esttrap = 0.5*fx(xval);
simp=fx(xval)
estmid=fx(xvalmid)
print(i, fstring.format(xval), fstring.format(xvalmid),fstring.format(estleft),fstring.format(estmid))
i=1;
while (i < n):
    xval+=step
    y=fx(xval)
    estleft+=y
    estrite+=y
    esttrap+=y
    xvalmid+=step
    ymid=fx(xvalmid)
    estmid+=ymid
    if (i%2) == 0:
        sm=2.0
    else:
        sm=4.0
    simp+=sm*y
    print(i, fstring.format(xval), fstring.format(xvalmid),fstring.format(y),fstring.format(ymid))
    i += 1;
xval=stop;
y=fx(stop)
estrite+=y
esttrap += 0.5*y
simp+=y
print(i, fstring.format(xval), fstring.format(xvalmid),fstring.format(y),"n/a")

estleft=estleft*step
estrite=estrite*step
esttrap *= step;
estmid=estmid*step
simp=(simp*step)/3.0

print("step =",step)
print("left =", '{:.4f}'.format(estleft))
print("rite =", '{:.4f}'.format(estrite))
print("mid  =", '{:.4f}'.format(estmid))
print("trap =", '{:.4f}'.format(esttrap))
print("simp =", '{:.4f}'.format(simp))
