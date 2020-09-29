f=open("assembly.txt","r")
f1=open("table.txt","w")
f2=open("symtab.txt","w")
f3=open("littable.txt","w")
f4=open("pooltable.txt","w")
stop="STOP"
lc=set()
v=list()
l=0 
flag=0 
ltindex=poolindex=0
ltcount=precount=0
f1.write("L.C."+" "+"MO"+" "+"RO"+" "+"INSTRUCTION"+"\n")
f2.write("Add."+" "+"Ln"+"  "+"Vl"+"  "+"Symbol"+"\n")
f3.write("Sr"+" "+"Lit"+" "+"Add."+"\n")

sym=[":","DC","DS","EQU"]
for line in f:
    string=line
    words=line.split()
    if "START" in words:
        x=int(words[-1])
        x=x-1
        #print(x)
    if stop in string:
        f1.write(str(x)+" ")
        f1.write("00"+" ")
        f1.write("00"+" ")
        f1.write(string)
    if "LTORG" in words : 
        continue
    if flag == 0:
        if "ADD" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("01"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                f1.write(str(x)+" ")
                f1.write("01"+" ")
                f1.write("02"+" ")
                f1.write(string)
                
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("01"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("01"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(x)+" ")
                f1.write("01"+" ")
                f1.write("na"+" ")
                f1.write(string)
        elif "SUB" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("02"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                f1.write(str(x)+" ")
                f1.write("02"+" ")
                f1.write("02"+" ")
                f1.write(string)
            
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("02"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("02"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(x)+" ")
                f1.write("02"+" ")
                f1.write("na"+" ")
                f1.write(string)
        elif "MULT" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("03"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                #f1.write(string+" ")
                f1.write(str(x)+" ")
                f1.write("03"+" ")
                f1.write("02")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("03"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("03"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(x)+" ")
                f1.write("03"+" ")
                f1.write("na"+" ")
                f1.write(string)
        elif "MOVER" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("04"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                f1.write(str(x)+" ")
                f1.write("04"+" ")
                f1.write("02"+" ")
                f1.write(string)
                
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("04"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("04"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(x)+" ")
                f1.write("04"+" ")
                f1.write("na"+" ")
                f1.write(string)
        elif "MOVEM" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("05"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                f1.write(str(x)+" ")
                f1.write("05"+" ")
                f1.write("02"+" ")
                f1.write(string)
                
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("05"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("05"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(x)+" ")
                f1.write("05"+" ")
                f1.write("na"+" ")
                f1.write(string)
        elif "COMP" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("06"+" ")
                f1.write("01"+" ")
                f1.write(string)
            
            elif "BREG" in words:
                f1.write(str(x)+" ")
                f1.write("06"+" ")
                f1.write("02"+" ")
                f1.write(string)
                
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("06"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("06"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(x)+" ")
                f1.write("06"+" ")
                f1.write("na"+" ")
                f1.write(string)
        elif "BC" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("07"+" ")
                f1.write("01"+" ")
                f1.write(string)
            elif "BREG" in words:
                f1.write(str(x)+" ")
                f1.write("07"+" ")
                f1.write("02"+" ")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("07"+" ")
                f1.write("03"+" ")
                f1.write(string)
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("07"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(x)+" ")
                f1.write("07"+" ")
                f1.write("na"+" ")
                f1.write(string)
        elif "DIV" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("08"+" ")
                f1.write("01"+" ")
                f1.write(string)
            elif "BREG" in words:
                f1.write(str(x)+" ")
                f1.write("08"+" ")
                f1.write("02"+" ")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("08"+" ")
                f1.write("03"+" ")
                f1.write(string)
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("08"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(x)+" ")
                f1.write("08"+" ")
                f1.write("na"+" ")
                f1.write(string)
        elif "READ" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("09"+" ")
                f1.write("01"+" ")
                f1.write(string)
            elif "BREG" in words:
                f1.write(str(x)+" ")
                f1.write("09"+" ")
                f1.write("02"+" ")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("09"+" ")
                f1.write("03"+" ")
                f1.write(string)
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("09"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(x)+" ")
                f1.write("09"+" ")
                f1.write("na"+" ")
                f1.write(string)
        elif "PRINT" in words:
            if "AREG" in words:
                f1.write(str(x)+" ")
                f1.write("10"+" ")
                f1.write("01"+" ")
                f1.write(string)
            elif "BREG" in words:
                f1.write(str(x)+" ")
                f1.write("10"+" ")
                f1.write("02"+" ")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(x)+" ")
                f1.write("10"+" ")
                f1.write("03"+" ")
                f1.write(string)
            elif "DREG" in words:
                f1.write(str(x)+" ")
                f1.write("10"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(x)+" ")
                f1.write("10"+" ")
                f1.write("na"+" ")
                f1.write(string)
        
    elif flag == 1:
         x=x-1
         if "ADD" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("01"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                f1.write(str(z)+" ")
                f1.write("01"+" ")
                f1.write("02"+" ")
                f1.write(string)
                
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("01"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("01"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(z)+" ")
                f1.write("01"+" ")
                f1.write("na"+" ")
                f1.write(string)
         elif "SUB" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("02"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                f1.write(str(z)+" ")
                f1.write("02"+" ")
                f1.write("02"+" ")
                f1.write(string)
            
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("02"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("02"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(z)+" ")
                f1.write("02"+" ")
                f1.write("na"+" ")
                f1.write(string)
         elif "MULT" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("03"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                #f1.write(string+" ")
                f1.write(str(z)+" ")
                f1.write("03"+" ")
                f1.write("02")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("03"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("03"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(z)+" ")
                f1.write("03"+" ")
                f1.write("na"+" ")
                f1.write(string)
         elif "MOVER" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("04"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                f1.write(str(z)+" ")
                f1.write("04"+" ")
                f1.write("02"+" ")
                f1.write(string)
                
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("04"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("04"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(z)+" ")
                f1.write("04"+" ")
                f1.write("na"+" ")
                f1.write(string)
         elif "MOVEM" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("05"+" ")
                f1.write("01"+" ")
                f1.write(string)
                
            elif "BREG" in words:
                f1.write(str(z)+" ")
                f1.write("05"+" ")
                f1.write("02"+" ")
                f1.write(string)
                
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("05"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("05"+" ")
                f1.write("04"+" ")
                f1.write(string)
                
            else:
                f1.write(str(z)+" ")
                f1.write("05"+" ")
                f1.write("na"+" ")
                f1.write(string)
         elif "COMP" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("06"+" ")
                f1.write("01"+" ")
                f1.write(string)
            
            elif "BREG" in words:
                f1.write(str(z)+" ")
                f1.write("06"+" ")
                f1.write("02"+" ")
                f1.write(string)
                
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("06"+" ")
                f1.write("03"+" ")
                f1.write(string)
                
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("06"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(z)+" ")
                f1.write("06"+" ")
                f1.write("na"+" ")
                f1.write(string)
         elif "BC" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("07"+" ")
                f1.write("01"+" ")
                f1.write(string)
            elif "BREG" in words:
                f1.write(str(z)+" ")
                f1.write("07"+" ")
                f1.write("02"+" ")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("07"+" ")
                f1.write("03"+" ")
                f1.write(string)
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("07"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(z)+" ")
                f1.write("07"+" ")
                f1.write("na"+" ")
                f1.write(string)
         elif "DIV" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("08"+" ")
                f1.write("01"+" ")
                f1.write(string)
            elif "BREG" in words:
                f1.write(str(z)+" ")
                f1.write("08"+" ")
                f1.write("02"+" ")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("08"+" ")
                f1.write("03"+" ")
                f1.write(string)
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("08"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(z)+" ")
                f1.write("08"+" ")
                f1.write("na"+" ")
                f1.write(string)
         elif "READ" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("09"+" ")
                f1.write("01"+" ")
                f1.write(string)
            elif "BREG" in words:
                f1.write(str(z)+" ")
                f1.write("09"+" ")
                f1.write("02"+" ")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("09"+" ")
                f1.write("03"+" ")
                f1.write(string)
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("09"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(z)+" ")
                f1.write("09"+" ")
                f1.write("na"+" ")
                f1.write(string)
         elif "PRINT" in words:
            if "AREG" in words:
                f1.write(str(z)+" ")
                f1.write("10"+" ")
                f1.write("01"+" ")
                f1.write(string)
            elif "BREG" in words:
                f1.write(str(z)+" ")
                f1.write("10"+" ")
                f1.write("02"+" ")
                f1.write(string)
            elif "CREG" in words:
                f1.write(str(z)+" ")
                f1.write("10"+" ")
                f1.write("03"+" ")
                f1.write(string)
            elif "DREG" in words:
                f1.write(str(z)+" ")
                f1.write("10"+" ")
                f1.write("04"+" ")
                f1.write(string)
            else:
                f1.write(str(z)+" ")
                f1.write("10"+" ")
                f1.write("na"+" ")
                f1.write(string)
    if "ORIGIN" in words:
            y=int(words[-1])
            for ele in lc:
                if ele in words:
                    z=v[l]+y 
                    l=0 
                    flag=1
                   # f1.write("0000"+" "+"00"+" "+string+"\n")
                    break
                l=l+1 
    for ele in sym:
        if ele in words:
          lc=words[0]
          v.append(x)
          f2.write(str(x)+" ")
          #f1.write(str(x)+" ")
          if words[1]==":" or words[1]=="EQU":
            f2.write("na"+"  ")
            f2.write("na"+"   ")
          elif words[1]=="DS":
            f2.write(words[-1]+"  ")
            f2.write("na"+"   ")
          elif words[1]=="DC":
            f2.write("na"+"  ")
            f2.write(words[-1]+"  ")
          f2.write(words[0]+"\n")
          
    if "=" == words[0]:
        ltindex=ltindex+1
        ltcount=ltcount+1 
        f3.write(str(ltindex)+" ")
        f3.write(words[-1]+" ")
        f3.write(str(x)+"\n")
    if "=" != words[0]:
        if ltcount != 0:
          poolindex=poolindex+1 
          precount=ltindex-ltcount+1 
          f4.write(str(poolindex)+" ")
          f4.write(str(precount)+" ")
          f4.write(str(ltcount)+"\n")
          ltcount=0 
    
        
    x=x+1

f.close()
f1.close()
f2.close()
f3.close()
f4.close()
flag=0

f1=open("table.txt","r")
f2=open("symtab.txt","r")
f3=open("littable.txt","r")
f4=open("pooltable.txt","r")
f5=open("pass2.txt","w")

f5.write("DefAdd"+" "+"UseAdd"+" "+"Sym/Lit"+"\n")
for line in f2:
    words=line.split()
    if "Add." in words:
        continue
    f1.seek(0)
    for line1 in f1:
        words1=line1.split()
        if words1[-1] == words[-1]:
            f5.write(words[0]+"   "+words1[0]+"   "+words[-1]+"\n")
            flag=1  
             
    if flag == 0:
        f5.write(words[0]+"   "+"----"+"   "+words[-1]+"\n")
    flag=0
x=0
y=1 


for line2 in f3:
    flag=0 
    words2=line2.split()
    if "Add." in words2:
        continue
    f1.seek(0)
    f4.seek(y)
    for line1 in f1:
        words1=line1.split()
        if words1[-1] == words2[1]:
            f5.write(words2[-1]+"   "+words1[0]+"   "+words2[1]+"\n")
            flag=1
            x=x+1 
        for line4 in f4:
         
         words4=line4.split()
         z=int(words4[-1])
         if x == z:
            y=y+1 
            x=0 
            break
    if flag == 0:
        f5.write(words2[-1]+"   "+"----"+"   "+words2[1]+"\n")
    
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
flag=1 
f=open("assembly.txt","r")
f1=open("table.txt","r")
f2=open("symtab.txt","r")
f3=open("littable.txt","r")
f4=open("pooltable.txt","r")
f5=open("pass2.txt","r")
f6=open("machinecode.txt","w")
f6.write("L.C."+" "+"MO"+" "+"RO"+" "+"AOR."+" "+"INSTRUCTION"+"\n")
for line2 in f:
    words2 = line2.split()
    if "START" in words2:
        continue
    for line in f1:
        words=line.split()
        if "INSTRUCTION" in words:
                 continue
        if words2[-1] == words[-1]:
            
            for line1 in f5:
                words1=line1.split()
                if words2[-1] == words1[-1]:
                     f6.write(words[0]+" "+words[1]+" "+words[2]+" "+words1[0]+" ")
                     f6.write(str(line[11:])+"\n")
                     flag=1
                     break
            
            break
    if flag==0:
         f6.write(words[0]+" "+"00"+" "+"00"+" "+"----"+" ")
         f6.write(str(line2)+"\n")
         print(words[3:])
         flag=1
         break
    f1.seek(0)    
    f5.seek(0)
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()