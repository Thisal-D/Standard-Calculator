import customtkinter as ctk
import pygame

pygame.init()

root = ctk.CTk()

root.title("Calculator")
root.iconbitmap("source/main2.ico")
root.maxsize(345,505)
root.minsize(345,505)
root.config(bg="#000000")
root.attributes('-alpha',0.97)

#out disaply
out_frame = ctk.CTkFrame(root ,fg_color="#172017" ,border_width=2 ,border_color="#ffffff" ,corner_radius=8, width=335, height=70)
out_frame.place(y=5 ,x=5)
out_display = ctk.CTkLabel(out_frame ,text="0" ,font=('arial',17,'bold') , fg_color="#172017" ,corner_radius=6 ,bg_color = "#172017", width=335-12 ,anchor="e", height=70-6)
out_display.place(y=3,x=6)


def clrscr():
    pygame.mixer.music.load("source/s2.mp3")
    pygame.mixer.music.play(loops=1)
    out_display.configure(text='')

def display(input_v):
    input_v = str(input_v)
    pygame.mixer.music.load("source/s6.mp3")
    pygame.mixer.music.play(loops=1)

    if input_v == ".":
        if len(str(out_display.cget("text"))) == 0 :
            out_text = input_v
        else:
            if "." not in str(out_display.cget("text")):
                out_text = input_v
            else:
                split_success = False
                for i in maths:
                    try:
                        n,m = str(out_display.cget("text")).split(i)
                        split_success = True
                        break
                    except:
                        pass
                if split_success:
                    if "." in m:
                        out_text = ""
                    else:
                        out_text = input_v
                else:
                    if "." in str(out_display.cget("text")):
                        out_text = ""
                    else:
                        out_text = input_v
    
    if input_v in maths :
        if len(str(out_display.cget("text"))) != 0 :
            if str(out_display.cget("text"))[-1] == " ":
                remove()
                out_text = input_v
            else:
                cal_success = False
                for i in maths :
                    try:
                        n,m = str(out_display.cget("text")).split(i)
                        calculate()
                        cal_success = True
                        out_text = input_v
                        break
                    except:
                        pass
                if not(cal_success):
                    if str(out_display.cget("text"))[-1] == ".":
                        out_text = ''
                    else:
                        out_text = input_v
        else:
            out_text = ''
    if input_v in [str(x) for x in nums] :
        out_text = input_v

    out_display.configure(text=str(out_display.cget("text")) + str(out_text))   

def remove():
    pygame.mixer.music.load("source/s4.mp3")
    pygame.mixer.music.play(loops=1)
    if len(str(out_display.cget("text"))) > 0:
        if str(out_display.cget("text"))[-1] == " ":
            out_display.configure(text=str(out_display.cget("text"))[:-3])
        else:
            out_display.configure(text=str(out_display.cget("text"))[:-1])

def convert(type):
    pygame.mixer.music.load("source/s5.mp3")
    pygame.mixer.music.play(loops=1)

    ope_code_in = False
    for i in maths :
        if i in str(out_display.cget("text")):
            ope_code_in = True
            break

    if ope_code_in :
        for i in maths :
            try:
                n,m = str(out_display.cget("text")).split(i)
                calculate()
                ope_code_in = False
                break
            except:
                pass
    if not(ope_code_in) :
        if type == int:
            out_display.configure(text=int(float(out_display.cget("text"))))
        else:
            out_display.configure(text=float(out_display.cget("text")))

def calculate():
    pygame.mixer.music.load("source/s3.mp3")
    pygame.mixer.music.play(loops=1)
    done = False
    error = False
    op = out_display.cget("text")
    count = 0
    for i in maths :
        try:
            num1,num2  = op.split(i)
            done = True
            break
        except:
            pass
        count += 1
    if count == 0 :
        try:
            val = (int(num1) / int(num2))
        except:
            try:
                val = (float(num1) / float(num2))
            except:
                error = True
    elif count == 1 :
        try:
            val = (int(num1) * int(num2))
        except:
            try:
                val = (float(num1) * float(num2))
            except:
                error = True
    elif count == 2:
        try:
            val = (int(num1) - int(num2))
        except:
            try:
                val = (float(num1) - float(num2))
            except:
                error = True
    else:
        try:
            val = (int(num1) + int(num2))
        except:
            try:
                val = (float(num1) + float(num2))
            except:
                error = True
    if done and not error:
        out_display.configure(text=val)
#buttons
bt_frame = ctk.CTkFrame(root , fg_color="#000000")
bt_frame.place(relwidth=1 ,y=80 ,x=5 ,relheight=1)
c_bt = ctk.CTkButton(bt_frame ,text="C",font=('arial',11,'bold') ,border_width=2 ,border_color="#707070" ,
                fg_color="#202020" ,text_color="#cccccc" ,hover_color="#303030" ,
                command=clrscr ,width=80 ,height=80)
c_bt.grid(row=1 ,column=1,pady=2 ,padx=2)

row_ = 2
column_ = 1
nums = [7 ,8 ,9 ,4 ,5 ,6 ,1 ,2 ,3, 0]
for i in range(10):
    if column_> 3:
        column_ = 1
        row_ += 1
    globals()['bt_no'+str(i)] = ctk.CTkButton(bt_frame ,text=nums[i] ,font=('arial',14,'bold') 
                                            ,border_width=2 ,border_color="#707070" ,
                                            command = lambda x =  nums[i] : display(x) ,
                                            width=80 ,height=80 ,
                                            fg_color="#000000" ,text_color="#ffffff" ,hover_color="#202020") 
    globals()['bt_no'+str(i)].grid(row=row_ ,column=column_ ,pady=2 ,padx=2)
    column_ += 1


float_bt =  ctk.CTkButton(bt_frame ,text="." ,font=('arial',14,'bold') 
                                        ,border_width=2 ,border_color="#707070" ,
                                        command = lambda x =  "." : display(x) ,
                                        width=80 ,height=80 ,
                                        fg_color="#202020" ,text_color="#cccccc" ,hover_color="#303030")
float_bt.grid(row = 1 ,column = 3 ,pady=2 ,padx=2)


column_ = 4
row_ = 1
maths = [" / " , " x " ," - " ," + " ]
for i in maths :
    globals()['maths'+str(i)]  = ctk.CTkButton(bt_frame ,text=i ,font=('arial',13,'bold') 
                                        ,border_width=2 ,border_color="#707070" ,
                                        command = lambda x =  i : display(x) ,
                                        width=80 ,height=80 ,
                                        fg_color="#101010" ,text_color="#00ff00" ,hover_color="#172017")
    globals()['maths'+str(i)].grid(row = row_ ,column = column_,pady=2 ,padx=2)
    row_ += 1



cal_bt = ctk.CTkButton(bt_frame ,text="=",font=('arial',11,'bold') ,border_width=2 ,border_color="#707070" ,
                command=calculate,width=80 ,height=80 ,fg_color="#202020" ,text_color="#cccccc" ,hover_color="#171725")
cal_bt.grid(row=5 ,column=4,pady=2 ,padx=2)

rem_bt = ctk.CTkButton(bt_frame ,text="<<<",font=('arial',11,'bold') ,border_width=2 ,border_color="#707070" ,
                command=remove , width=80 ,height=80 ,fg_color="#202020" ,text_color="#cccccc" ,hover_color="#303030")
rem_bt.grid(row=1 ,column=2,pady=2 ,padx=2)

con_float = ctk.CTkButton(bt_frame ,text="float",font=('arial',11,'bold') ,border_width=2 ,border_color="#707070" ,
                command=lambda x = float :convert(x),width=80 ,height=80 ,
                fg_color="#202020" ,text_color="#ff0000" ,hover_color="#201717" ,)
con_float.grid(row=5 ,column=2,pady=2 ,padx=2)
con_int = ctk.CTkButton(bt_frame ,text="int",font=('arial',11,'bold') ,border_width=2 ,border_color="#707070" ,
                command=lambda x = int :convert(x),width=80 ,height=80,
                fg_color="#202020" ,text_color="#ff0000" ,hover_color="#201717" ,)
con_int.grid(row=5 ,column=3,pady=2 ,padx=2)


def display_e(e):
    mods =  ["/" , "x" ,"-" ,"+" ]
    key_val = str(e.char)
    if key_val == "*" :
        key_val = " x "
    if key_val in mods:
        key_val = " {} ".format(key_val)
    else:
        key_val = key_val
    display(key_val)

def calculate_e(e):
    calculate()

def remove_e(e):
    remove()

for num_key in  nums+maths+["."]:
    if num_key == " x ":
        num_key = " * "
    root.bind(str(num_key),lambda key_val=num_key:display_e(key_val))

root.bind('<Return>',calculate_e)
root.bind('<BackSpace>',remove_e)

root.mainloop()