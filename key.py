def correct_ans():
    corectans=["A","B","C","D","A","C","B","D","A","D","A","B","C","D","D"]
correct_ans()
name=input("Please Enter your name:-  ")
fname=input("Enter your File name:-  ")
print('Students name is:',name)
print('your filename is:',fname)
print("The student answers List ")
file1 = open("myfile.txt","w")
L = ["['1.A,2.B,3.C']\n", " ['4.D,5.C,6.D']\n","['7.C,8.D,9.B']\n","['10.B,11.B,12.D']\n","['13.B,14.D ,15.B']\n"]

file1.write("This is my final answers\n")
file1.writelines(L)
file1.close()

file1 = open("myfile.txt","r+")

print("Output of Read function is ")
print(file1.read())
print()
file1.seek(0)
file1.close()


#correct answers for the student

for k in range(len(correct_ans)):
    for n in range(len(L)):
         
