#Case Study 6
import matplotlib.pyplot as plt

a=[]
b=[]
c=[]
case=open('caseStudy6.txt','r')
for i in case:
    k=i.split(' ')
    a.append(float(k[1]))
    b.append(float(k[2]))
    #c.append(float(k[2]))
#plt.subplot(1,2,1)
plt.hist(a)
plt.show()
#plt.subplot(1,2,2)
plt.hist(b)
#plt.gcf().clear()
