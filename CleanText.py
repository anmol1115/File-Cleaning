fname=input('Enter the file name: ')
try:
    fh=open(fname)
except:
    print('file',fname,'not present in the given directory')
    quit()

inp=fh.read()
fout=open('intro2','w')
inp2=''
i=0
pos1=0
pos2=0


while i<len(inp):
    if inp[i]=='[':
        pos1=inp.find('[',pos2,len(inp))
        pos2=inp.find(']',pos1,len(inp))
        i=pos2
    else:
        inp2=inp2+inp[i]
    i=i+1

fout.write(inp2)
fout.close()