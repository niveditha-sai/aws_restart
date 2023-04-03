'''import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of user to add: ")
        print("use the username '" + username +  "'? (Y/N)")
        confirm = input().upper()
        if confirm == "Y":
            print("code run succes ")
        else:
            print("No ")
        
        
    os.system("sudo adduser " +  username)
    
new_user()
'''

'''import subprocess
import os
os.system("ls")


subprocess.run(["ls"])

subprocess.run(["ls","-l"])

subprocess.run(["ls","-l","README.md"])


command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
'''


'''import os
def remove_user(): 
    confirm = "N"
    while confirm != "Y": 
         username = input("Enter the name of the user to remove: ")
         print("Remove the user : '" + username + "'? (Y/N)") 
         confirm = input().upper()
         if confirm == "Y":
            print(" removed successfully ")
         else:
            print("Not removed ")
        
    os.system("sudo userdel -r " + username)

remove_user()
'''

'''import os

def add_user_to_group(): 
    username = input("Enter the name of the user that you want to add to a group: ") 
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0] 
    print("Enter a list of groups to add the user to") 
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3") 
    print("The available groups are:\r\n " + output) 
    chosenGroups = str(input("Groups: "))
    
add_user_to_group()
'''









        
    
    
    
    
    
        