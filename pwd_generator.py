from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

#Randome Password 생성
def password_generate () :
    input_pwd.delete(0, END)

    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","t","u","v","w","x","y","z"]
    number = ["1","2","3","4","5","6","7","8","9","0"]
    char = ["!","@","#","$","%","^"]

    random_letter = [random.choice(letter) for i in range(random.randint(7, 10))]
    random_number = [random.choice(number) for i in range(random.randint(2,4))]
    random_char = [random.choice(char) for i in range(random.randint(1,2))]


    new_password = random_char+random_letter+random_number
    random.shuffle(new_password)
    final_password = "".join(new_password)

    input_pwd.insert(0, final_password)
    


#데이타 저장하기
data_list = []


def save_data():
    mail_address = input_mail.get()
    web_name = input_web.get()
    password = input_pwd.get()
    data = f"{web_name} | {mail_address} | {password}"
    data_list.append(data)
    # print(data_list)

    if (web_name == "") or (password == "") : 
        error_message = messagebox.showinfo(title="Alert", message="Please input the all information")

    
    
    else : 
        check_message = messagebox.askokcancel(title="Please check if your input is corret", message=f"Web page is {web_name} \n your email is {mail_address} \n your password is {password}")
        if check_message == True :
    
            print(data_list)
            with open("data file", "a") as data_file :
                data_file.write (f"{web_name} | {mail_address} | {password} \n" )  
                input_web.delete(0,END)
                input_pwd.delete(0,END)


canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1, row=1)

label_1 = Label(text="Website:")
label_1.grid(column=0,row=2)


label_2 = Label(text="Email/Username:")
label_2.grid(column=0,row=3)



label_3 = Label(text="Password :")
label_3.grid(column=0,row=4)

input_web = Entry(width=35)
input_web.grid(column=1, row=2,columnspan=2)
input_web.focus()


input_mail = Entry(width=35)
input_mail.grid(column=1, row=3,columnspan=2)
input_mail.insert(0,"legendson20@naver.com")

gen_pwd = Button(text="Generate Password" , command=password_generate)
gen_pwd.grid(column=2, row=4)


input_pwd = Entry(width=21)
input_pwd.grid(column=1, row=4)


add_button = Button(text="Add",width=36, command=save_data)
add_button.grid(column=1, row=5,columnspan=2)



window.mainloop()

