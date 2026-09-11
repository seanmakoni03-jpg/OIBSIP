import random 
import string

def Genertaor():
    pass_len= int(input("Enter the length of your password: "))
    char_value= string.ascii_letters + string.digits + string.punctuation 

    password=""


    for i in range(pass_len):

        password+= random.choice(char_value)
    return password


print("-----***RANDOM PASSWORD GENERATOR***-----\n")
password= Genertaor()
print("Your random password is:",password)   
while True:
    Review1= input("Are you satisfied with your password?? [Press 'Yes' __or__ 'No' to answer]\n")
    if(Review1 == "Yes" or Review1 == "yes") :
        print("Your Generated Password is:",password)
        break
    elif(Review1== "No" or Review1 == "no"):

            Review2= input("PRESS 'Yes' To Regenerate your Password __OR__ PRESS 'No' To Quit the process...??\n")
            if(Review2 == "Yes" or Review2 == "yes"):

              print("Your Random Regenerated Password is:",Genertaor(), "\nThankyou!!\n")
              break   
            elif(Review2 == "No" or Review2 == "no"):
             
              print("Thankyou")
              break
            else:
              print("ENTER A VALID OPTION \n")
    else:
        print("ENTER A VALID OPTION \n")   


print("-----PROCESS FINISHED-----\n")        