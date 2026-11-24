#0
x=float(input('lotfan adad khod ra vared konin?:'))
if x>0:
    print('ada + hast')
else:
    print('adad - hast')

x=float(input('lotfan adad khod ra vared konin?:'))
if x>0:
    if x%2==0:
       print('zoj ast adad')
    else:
       print('fard ast adad')
else:
    print('lotfan adad mosbat intekha konin')
#------------------------------------------------------------------------------
#1
x=float(input('lotfan darsad batri khod ra benevisid:'))
if x>20:
    print('sharje shoma khob ast')
else:
    print('shajer ra motasel konin')
print('baresi tamam shod')
#------------------------------------------------------------------------------
#2
x=float(input('lotfan mogodi mahsol ra beghoeid?:'))
if x>0:
    print('emkan kharid vojod darad')
else:
    print('mahsol namojod ast')
#------------------------------------------------------------------------------
#3
x= float(input('lotfan mablagh ra beghoeid(be toman):'))    
if x>1000000:
    z='rayeghan'
elif x>500000:
    z='30000toman'
else: 
    z='60000toman'   
print(f'hazineh arsal baraye soma {z} hast')
#------------------------------------------------------------------------------
#4
#چند if مستقل :
x = input('lotfan ramz obor ra benevisid: ')
y = len(x)
z = x.isdecimal()
if y < 8:
    print('ramz kotah ast')
if z == True:
    print('ramz faghat adad ast lotfan avaz konid')
if ' ' in x:
    print('ramz daraye fasele ast lotfan avaz konid')  
    
    
#if های تو در تو:  
x = input('lotfan ramz obor ra benevisid: ')
y = len(x)
z = x.isdecimal()
if y < 8:
    print('ramz kotah ast')
    if z == True:
        print('ramz faghat adad ast lotfan avaz konid')
    if ' ' in x:
        print('ramz daraye fasele ast lotfan avaz konid')
else:
    if z == True:
        print('ramz faghat adad ast lotfan avaz konid')
    if ' ' in x:
        print('ramz daraye fasele ast lotfan avaz konid')
        
        
# با ساختار if / elif:
x = input('lotfan ramz obor ra benevisid: ')
y = len(x)
z = x.isdecimal()

if y < 8:
    print('ramz kotah ast')

elif z == True:
    print('ramz faghat adad ast lotfan avaz konid')

elif ' ' in x:
    print('ramz daraye fasele ast lotfan avaz konid')

else:
    print('ramz shoma moshkeli nadarad')
#------------------------------------------------------------------------------
#5
name= ['ali' , 'mohamad' , 'reza' , 'yasin']
username= input('lotfan name khod ra benevisid:')    
pasvord= input('lotfan pasvoed khod ra benevisid:')    
if username in name :
   if pasvord == 'python123' : 
       print('khosh amadid :)')
   else:
       print('ramz ashtebah ast:/')
else:
     print('karbar peyda nashod:(')  
#------------------------------------------------------------------------------
#6
x= float(input('lotfan adad aval khod ra entekhab konin:'))    
y= float(input('lotfan adad dovom khod ra entekhab konin:'))    
z= input('lotfan amalghard khod ra antekhab konin(+,-,*,/):')
if z== '+':  
   A= x+y
   print(A)    
elif z== '-':   
    B= x-y
    print(B)
elif z== '*':   
    C= x*y
    print(C)
else: 
    D= x/y
    print(D)    
    
    
    
    
    
    
    
    
    
    
    
    