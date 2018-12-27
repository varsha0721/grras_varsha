import os
import shutil
def Create_file():
        f = input("please enter FULL and VALID path:")
        if os.path.exists(f):
            fp = open(f,'w')
            print("type 'quit' to save file")
            while True:
                d = input("write ur text from here\n")
                if d.lower() == 'quit':
                    fp.close()
                    break
                fp.write(d)
                fp.write('\n')
                print("ur file has been created")
        else:
            print("please enter valid path\ntry again")
        choice()
def Read_file():
        f = input("please enter FULL and VALID path:")
        if os.access(f,os.F_OK) and os.access(f,os.R_OK):
            fp = open(f,'r')
            data = fp.read()
            fp.close()
            print(data)
        else:
            print("invalid path\n Try Again")
def Append_file():
       f = input("please enter FULL and VALID path:")
       if os.access(f,os.F_OK) and os.access(f,os.R_OK):
            fp = open(f,'a')
            print("type 'quit' to save file")
            print("write your text from here")
            while True:
                d = input()
                if d.lower() == 'quit':
                    fp.close()
                    break
                fp.write(d)
                fp.write('\n')
       else:
           print("invalid path\n Try Again")
       option()
def Copy_file():
       s = print("please enter path of SOURCE")
       d = print("please enter path of DESTINTION")
       if os.path.exists(s) and os.path.exists(d):
           shutil.copytree(s,d)
       else:
           print("path does not exist\ntry again")
       option()
def Move_file():
       s = print("please enter path of SOURCE")
       d = print("please enter path of DESTINTION")
       if s == d:
           print("error!")
           print("sourse and destination are same")
       elif os.path.exists(s) and os.path.exists(d):
           shutil.move(s,d)
       else:
           print("path does not exist\ntry again")
       option()




def option():
    print("\n1.Create File \n2.Read File \n3.Append File \n4.Copy File \n5.Move File \n6.Exit")
    ch=int(input("enter ur choice:"))
    if ch == 1:
        Create_file()
    elif ch == 2:
        Read_file()
    elif ch == 3:
        Append_file()
    elif ch == 4:
        Copy_file()
    elif ch == 5:
        Move_file()
    elif ch == 6:
        exit(0)
    else:
        print("invalid choice\ntry again")
        option()


if __name__ == "__main__" :
    option()
            
    
