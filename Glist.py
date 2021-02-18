import os
os.system('printf "\033[3;32m" ')
list=input('Entre Name The List : ')
os.system('clear') 
os.system('printf "\033[3;36m"') 
os.system('figlet Glitch - Team')
print('BY : Glitch Team✓') 
print('>'*30)
file=open(list,'w') 
aa=set([]) 
oio=set([])
kk=1
while True :
    b=input('Entre {} : '.format(kk))
    if b=='exit' :
        print('\033[3;36m')
        file.close()
        qq=open(list, 'r' )
        ll=len(qq.readlines())
        os.system('printf "\033[3;31m"')
        print('-'*60)
        print('>> {} Passwords in ====>> {} '.format(ll, list))
        print('-'*60) 
        break ;
    aa.add(b)
    for i in aa:
        if len(i) >= 6 and i not in oio :
            oio.add(i)
            file.write(i)
            file.write('\n')
        c=b+i
        d=i+b
        if len(c) >= 6 :
            file.write(c)
            file.write('\n') 
        if c != d and len(d) >= 6:
            file.write(d)
            file.write('\n')
    kk=int(kk)+1
    print('-'*40)
