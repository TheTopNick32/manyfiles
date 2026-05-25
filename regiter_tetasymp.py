from sympy import *
x = symbols("x")
q = { 1: [[1]] }
def decompose(n):
    try:
        return q[n]
    except:
        pass
    result = [[n]]
    for i in range(1, n):
        a = n-i
        R = decompose(i)
        for r in R:
            if r[0] <= a:
                result.append([a] + r)
    q[n] = result
    return result
def perms(l):
    s={}
    for i in l:
        try:
            s[i]+=1
        except:
            s[i]=1
    ans=factorial(len(l))
    for i in s.values():
        ans/=factorial(i)
    return ans
t=[-complex(N(conjugate(LambertW(-1)),20))]
for i in range(16):
    t.append(t[0])
decompose(len(t)-1)
a=[t[0],1]
for v in range(2,len(t)):
    ans=0
    for n in range(2,v+1):
        ans2=0
        for p in q[v]:
            ans3=1
            if len(p)!=n:
                continue
            for i in p:
                ans3*=a[i]
            ans2+=ans3*perms(p)
            ans3*perms(p)
        ans+=complex(ans2*t[n]/factorial(n))
    a.append(ans/(t[1]**v-t[1]))
print(a)