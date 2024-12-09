hbar=197.329
pi=3.141592653

AP=16
ZP=8
AT=152
ZT=62

R1=1.2*AP**(1./3.)-0.09
R2=1.2*AT**(1./3.)-0.09
A0=1.17*(1.+0.53*(AP**(-1./3.)+AT**(-1./3.)))
A0=1/A0
R0=(R1+R2)
R12=R1*R2/(R1+R2)
GAMMA=0.95*(1-1.8*(AP-2*ZP)/AP*(AT-2*ZT)/AT)
V0=16*pi*GAMMA*R12*A0

RC=1.3*(AP**(1/3)+AT**(1/3))
r0=R0*((AP**(1/3)+AT**(1/3))**(-1))
print(V0,R0,A0,RC,r0)
