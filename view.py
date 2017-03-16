#!/usr/bin/python3

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#:set fileformat=unix
#!!!!!!!!!!!!!!!!!!!!!!!!!!!

'''
*Michal Chorobik 0937145
*CIS 2750 Assignment2
*mchorobi@uofguelph.mail.ca
*February 19, 2017
'''

if __name__ == "__main__":

    import sys
    import glob
    import os
    import curses

def writeFile(postNum,user,stream):#{

    oldPosNum="0"
    #os.chdir("./messages/")
    fileName=stream+"StreamUsers.txt"
    list=[]

    with open(fileName,'r') as f:
       for line in f:
           list.append(line)

    file = open(fileName,'w')
    for line in list:
        if user in line:

            a=line.split(" ")
            oldPosNum=a[1][:-1]
            #print("="+oldPosNum+"=")
            if(len(oldPosNum)>0):
                if(int(oldPosNum)>postNum):
                    postNum=oldPosNum

            line=user+" "+str(postNum)+"\n"
        file.write(line)
    file.close()

#}

def main(m,var,var2,var3,var4,postNum):#{

    lastRead=0
    lastPost=0
    userName = sys.argv[1]
    choice = sys.argv[2]

    #print("1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10")
    thePost="<br>"
    array=[]
    array2=[]

    if var=="0":
        os.chdir("./messages/")
    list=[]

    for file in glob.glob("*StreamUsers.txt"):
        with open(file,'r') as f:
           for line in f:
              for word in line.split():
                  if word==userName:
                      file = file[:-15]
                      list.append(file)

    if not list:
        print("<br>This user is not in any streams")
        sys.exit()

    #print(" ".join(list) ,"all ")
    if choice=="all":
        print("0")
        sys.exit()

    if var=="0":
        pas=0
        while pas==0:
            for x in range(len(list)):
                if choice == list[x]:
                    pas=1
                if choice == "all":
                    pas=1
            if pas==0:
                print("0")
                sys.exit()

    else:
        choice=var

    if var2=="1":
        pas=0
        while pas==0:
            choice = input()
            for x in range(len(list)):
                if choice == list[x]:
                    pas=1
                if choice == "all":
                    pas=1
            if pas==0:
                print("This is not a possible option")

    if choice!="all":
        #finding the last read line
        file=choice+"StreamUsers.txt"
        with open(file,'r') as f:
           for line in f:
               line.strip()
               line=line.rstrip('\n')
               if userName in line:
                    viewLine=line.split()
        viewLine=viewLine[1]

        messageList=[]
        file=choice+"StreamData.txt"
        with open(file,'r') as f:
           for line in f:
               for word in line.split():
                   messageList.append(word)

    #curses
    mypad_pos = 0

    count=0
    dateList=[]
    senderList=[]
    oldLine=0
    nextLoop=0
    authorLine=""

###################################################################################################
    p=1

    if var3=="1":
        if choice == "all":
            for i in range(len(list)):
                file=list[i]+"Stream.txt"
                with open(file,'r') as f:
                   for line in f:
                       line.strip()
                       line=line.rstrip('\n')

                       if nextLoop==1:
                          senderList.append(authorLine+" "+line)
                          senderList.sort()
                          nextLoop=0

                       if "Sender" in line:
                           nextLoop=1
                           authorLine=line[8:]

            newLine=""
            for x in range(len(senderList)):
                for i in range(len(list)):
                    file=list[i]+"Stream.txt"
                    with open(file,'r') as f:
                       for line in f:
                           line.strip()
                           line=line.rstrip('\n')
                           if "Sender" in line:
                              authorLine=line[8:]
                              ok=0
                           if ok==1:
                              thePost+="<br>"
                              thePost+=line
                              array.append(thePost)
                              thePost=""
                              count+=1

                           newLine= authorLine+" "+line
                           if senderList[x] in newLine:
                               thePost+="<br>"
                               thePost+=line
                               array.append(thePost)
                               thePost=""
                               count+=1
                               thePost+="<br>"
                               thePost+=line
                               array.append(thePost)
                               thePost=""
                               count+=1
                               ok=1
                           oldLine=line
        else:
            file=choice+"Stream.txt"
            with open(file,'r') as f:
               for line in f:
                   line.strip()
                   line=line.rstrip('\n')

                   if nextLoop==1:
                      senderList.append(authorLine+" "+line)
                      senderList.sort()
                      nextLoop=0

                   if "Sender" in line:
                       nextLoop=1
                       authorLine=line[8:]

            newLine=""
            for x in range(len(senderList)):
                    file=choice+"Stream.txt"
                    with open(file,'r') as f:
                       for line in f:
                           line.strip()
                           line=line.rstrip('\n')
                           if "Sender" in line:
                              authorLine=line[8:]
                              ok=0
                           if ok==1:
                              thePost+="<br>"
                              thePost+=line
                              array.append(thePost)
                              thePost=""
                              count+=1

                           newLine= authorLine+" "+line
                           if senderList[x] in newLine:
                               thePost+="<br>"
                               thePost+=oldLine
                               array.append(thePost)
                               thePost=""
                               count+=1
                               thePost+="<br>"
                               thePost+=line
                               array.append(thePost)
                               thePost=""
                               count+=1
                               ok=1
                           oldLine=line
    elif choice=="all":
        for i in range(len(list)):
            file=list[i]+"Stream.txt"
            with open(file,'r') as f:
               for line in f:
                   line.strip()
                   line=line.rstrip('\n')
                   if "Date" in line:
                       dateList.append(line[-16:-14]+line[-13:-11]+line[-10:-8]+line[-7:-5])
                       sorted(dateList, key=int)
        newLine=""
        for x in range(len(dateList)):
            for i in range(len(list)):
                file=list[i]+"Stream.txt"
                with open(file,'r') as f:
                   for line in f:
                       line.strip()
                       line=line.rstrip('\n')
                       if "Sender" in line:
                          ok=0
                       if ok==1:
                          thePost+="<br>"
                          thePost+=line
                          array.append(thePost)
                          thePost=""
                          count+=1

                       newLine=line[-4:]+line[-16:-14]+line[-13:-11]+line[-10:-8]+line[-7:-5]
                       if dateList[x] in newLine:
                           thePost+="<br>"
                           thePost+=oldLine
                           array.append(thePost)
                           thePost=""
                           count+=1
                           thePost+="<br>"
                           thePost+=line
                           array.append(thePost)
                           thePost=""
                           count+=1
                           ok=1
                       oldLine=line
    else:
        file=choice+"Stream.txt"
        with open(file,'r') as f:
           for line in f:
               line.strip()
               line=line.rstrip('\n')
               thePost+="<br>"
               thePost+=line
               array.append(thePost)
               thePost=""
               count+=1
        #here i move the text down to the last read line of that us
        mypad_pos = mypad_pos + int(viewLine)

    ###################################################################################################
    post=""

    for i in range(len(array)):
        if((i!=0)and(array[i].find("Sender")==-1)):
            post+=array[i]
        else:
            if(i!=0):
                array2.append(post)
            post=""
            post+=array[i]
        if(i==len(array)-1):
            array2.append(post)
    ###################################################################################################

    postNum+=int(viewLine)

    array2[0]=array2[0][4:]
    array2.append("<br>no unread messages left")

    if(m=="1"):
        postNum=len(array2)-1

    if((postNum>=0)and(postNum<len(array2))):
        array2[postNum]=array2[postNum].replace("~",' ')
        array2[postNum]=array2[postNum].replace("\"<br>\"",'<br>')
        print(array2[postNum])


    #print(thePost)

        #here i add 23 to the seen lines because as its printed you can see all 23 lines at first
        #if int(viewLine)!=0:
        #    mypad_pos=mypad_pos+1
        #viewLine = 24 + int(viewLine)
        #prev=0
        #for pos in messageList:
        #    if int(pos)>int(viewLine):
        #            lastPost=prev
        #            break
        #    prev=pos
        #print(lastPost)

    if(int(viewLine)>=len(array2)):
        viewLine=len(array2)-2

    if(postNum>=len(array2)):
        postNum=len(array2)-2

    if(var4=='100'):
        writeFile(postNum,userName,choice)
    else:
        writeFile(int(viewLine),userName,choice)

    return 0;

    '''cmd=2
    #while cmd != -123 :
    p=0
    if (p==0):
        p=2
#        print("")
        #print(cmd)
        if  cmd == 113:
#            print(" ")
            #break
        if  cmd == 66:
            mypad_pos += 1
            if choice!="all":
                viewLine = 1 + int(viewLine)

                for pos in messageList:
                    if int(pos)>int(viewLine):
                        if int(prev)<int(viewLine):
                            lastPost=prev
                            #break
                    prev=pos
        elif cmd == 65:
            mypad_pos -= 1
        elif (cmd == 109 or cmd == 77):#m
            if choice!="all":
                lastPost=int(messageList[-1])
        elif (cmd == 99 or cmd == 67):#c
            main(choice,"0","0")
            #break
        elif (cmd == 115 or cmd == 83):#s
            main(choice,"1","0")
            #break
        elif (cmd == 111 or cmd == 79):#o
            curses.endwin()
            if var3 == "1":
                main(choice,"0","0")
            else:
                main(choice,"0","1")
            #break


    if choice!="all":
        if lastPost==0:
            lastPost=int(messageList[-1])
        writeFile(lastPost,userName,choice)
    return 0;'''
    #}

postNum = sys.argv[3]

#areg4 is mark read all option
# sys.argv[6] is sort

main(sys.argv[5],"0","0",sys.argv[6],sys.argv[4],int(postNum))
