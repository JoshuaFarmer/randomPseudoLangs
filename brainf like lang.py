memory = [0] * 4096
pointer = 0
tmp = ""
while True:
    inp = input()
    index = 0
    while index < len(inp):
        # advnace pointer
        if inp[index]==">":
            pointer+=1
        # advance pointer (backwards)
        elif inp[index]=="<":
            pointer-=1
        # increment current location
        elif inp[index]=="+":
            memory[pointer]+=1
        # decrement current location
        elif inp[index]=="-":
            memory[pointer]-=1
        # set to value
        # the fuck i do wrong
        elif inp[index]==":":
            # ah
            index += 1
            tmp = ""
            while inp[index]!=":":
                tmp+=inp[index]
                index+=1
            #print("DEBUG, SET TO VALUE: " + str(tmp))
            if tmp.isnumeric():
                memory[pointer] = int(tmp)
            else:
                # one char per memory thing :trollface:
                memory[pointer] = int(ord(tmp))
        # output
        elif inp[index]==".":
            print(chr(memory[pointer]))
        # input (chr)
        elif inp[index]==",":
            memory[pointer]=ord(input())
        # input chunk
        elif inp[index]=="I":
            n=0
            tmp=input() + "\0"
            while tmp[n]!="\0":
                memory[pointer]=ord(tmp[n])
                pointer+=1
                n+=1
            while n>0:
                n-=1
                pointer-=1
        # set [x] to current pos
        elif inp[index]==";":
            index+=1
            tmp=""
            while inp[index]!=":":
                tmp+=inp[index]
                index+=1
            memory[int(tmp)] = memory[pointer]
        # set chunk{x} to current chunk
        elif inp[index]=="c":  
            index+=1
            tmp=""
            while inp[index]!=":":
                tmp+=inp[index]
                index+=1
            loc=int(tmp)
            n=0
            while memory[pointer]!=0:
                memory[loc]=memory[pointer]
                pointer+=1
                loc+=1
                n+=1
            while n>0:
                pointer-=1
                n-=1
        # comment
        elif inp[index]=="#":
            index=len(inp)
        # print chunk
        elif inp[index]=="P":
            n=0
            tmp=""
            while memory[pointer]!=0:
                #print("DEBUG: ")
                # nvm
                tmp+=str(chr(memory[pointer]))
                pointer+=1
                n+=1
            while n>0:
                pointer-=1
                n-=1
            print(tmp)
        # set chunk
        elif inp[index]=="S":
            n=0
            tmp=""
            index+=1
            while inp[index]!=":":
                memory[pointer]=ord(str(inp[index]))
                #print("debug: " + str(memory[pointer]))
                pointer+=1
                n+=1
                index+=1
            while n>0:
                #print("ptr: "+ str(pointer))
                pointer-=1
                n-=1
        # jump
        elif inp[index]=="j":
            index+=1
            tmp=""
            while inp[index]!=":":
                tmp+=str(inp[index])
                index+=1
            index=int(tmp) - 1
        # jump (if)
        elif inp[index]=="J":
            index+=1
            tmp=""
            while inp[index]!=":":
                tmp+=str(inp[index])
                index+=1
            index+=1
            # idk if this will work, i have never used eval()
            if eval(tmp):
                tmp=""
                while inp[index]!=":":
                    tmp+=str(inp[index])
                    index+=1
                index=int(tmp) - 1
        # exit
        elif inp[index]=="e":
            exit()
        index+=1
