import matplotlib.pyplot as plt
import numpy as np
f=open('caseStudy6.txt','r')
a=[]
for i in f:
    a.append(i.split(' '))
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
timestamps=[]
for i in a:
    b.append(float(i[1]))
    c.append(float(i[2]))
    d.append(float(i[3]))
    e.append(float(i[4]))
    f.append(float(i[5]))
    g.append(float(i[6]))
mb=np.mean(b)
sb=np.std(b)

mc=np.mean(c)
sc=np.std(c)
md=np.mean(d)
sd=np.std(d)
me=np.mean(e)
se=np.std(e)
mf=np.mean(f)
sf=np.std(f)
mg=np.mean(g)
sg=np.std(g)
for j in range(len(b)):
    b[j]=(b[j]-mb)/sb
    c[j]=(c[j]-mc)/sc
    d[j]=(d[j]-md)/sd
    e[j]=(e[j]-me)/se
    f[j]=(f[j]-mf)/sf
    g[j]=(g[j]-mg)/sg
    
x=np.arange(312) 
   
plt.plot(x,b)
plt.plot(x,c)

for i in range(312):
    if i%22==0:
        string=a[i][0]
        timestamps.append(string[2:7])
    else:
        timestamps.append('')
#plt.plot(x,d)
#plt.plot(x,e)
#plt.plot(x,f)
#plt.plot(x,g)
plt.xticks(x,timestamps)