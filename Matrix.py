'''
print("Welcome  You Can Logn in ")
print("------------------------")
New_username = input("Enter The New UserName : ")
New_Password = input("Enter The New Password : ")
print("Check Your UserName And Password")
print("--------------------------------")
Retype_username = input("Enter The Retype_UserName : ")
Retype_password = input("Enter The Retype_Password : ")
print("----------------------------------------------------")
if New_username == Retype_username and New_Password == Retype_password:
    print("Hello ",New_username, " Then Register")
else:
    print("You Are Not ",New_username)
'''
'''
Number = eval(input("Enter The Number : "))
list=[1 , 3 , 4 , 5 , 19 , 10]
count = 0
for i in range(Number , max(list)):
    count = count +1
    if Number+count in list:
        print(Number+count)
        break
    if Number-count in list:
        print(Number-count)
        break
'''
string = input("Enter The String : ").split(" ")
Word = ""
for i in range(len(string)):
    print(chr(ord(string[i][0]) - 32))
    Word = Word + chr(ord(string[i][0])-32)
    for m in range(len())
print(string)
print(Word)








