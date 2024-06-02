class lichthi:
    def __init__(self,day,hour,room,subject,group,number,code):
        self.day=day
        self.hour=hour
        self.room=room
        self.subject=subject
        self.group=group
        self.number=number
        self.code=code
    def __repr__(self):
        return self.day+' '+self.hour+' '+self.room+' '+self.subject+' '+self.group+' '+self.number
if __name__=='__main__':
    cnt=0
    mh=dict()
    ca=dict()
    ds=[]
    with open('MONTHI.in','r') as f:
        line=int(f.readline().rstrip('\n'))
        for i in range(1,line+1):
            ma=f.readline().rstrip('\n')
            ten=f.readline().rstrip('\n')
            hinhthuc=f.readline().rstrip('\n')
            mh[ma]=ten
    f.close()
    with open('CATHI.in','r') as f:
        line=int(f.readline().rstrip('\n'))
        for i in range(1,line+1):
            ngay=f.readline().rstrip('\n')
            gio=f.readline().rstrip('\n')
            phong=f.readline().rstrip('\n')
            s=ngay+" "+gio+" "+phong
            ca[str.format("C%03d"%i)]=s
    f.close()
    with open('LICHTHI.in','r') as f:
        line=int(f.readline().rstrip('\n'))
        for i in range(1,line+1):
            dv=f.readline().rstrip('\n')
            l=dv.split()
            gg=ca[l[0]].split()
            ds.append(lichthi(gg[0],gg[1],gg[2],mh[l[1]],l[2],l[3],l[0]))
    f.close()
    ds.sort(key=lambda x:(x.day,x.hour,x.code))
    for i in ds:
        print(i)