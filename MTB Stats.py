from tkinter import *

# Creating Framework
window = Tk()
window.geometry('1000x1000')
window.title("My Team Stats")
window.configure(background = "white")

# Creating a Logo 
#logo = PhotoImage(file="Volleyball Stats.gif")
#Label (window, image=logo, bg = "white").grid( row = 0, columnspan = 3)

#entry = Entry(window, width = 100, bg = "LightGrey", fg = "white", borderwidth= 4)
#entry.grid(row = 0, column = 0, columnspan= 5)

def add():
    return 

# Serve  Button
ser_btn0 = Button(window, text = "0", width = 12, command = add)
ser_btn1 = Button(window, text = "1", width = 12, command = add)
ser_btn2 = Button(window, text = "2", width = 12, command = add)
ser_btn3 = Button(window, text = "3", width = 12, command = add)

# Serve Receive Button
sr_btn0 = Button(window, text = "0", width = 12, command = add)
sr_btn1 = Button(window, text = "1", width = 12, command = add)
sr_btn2 = Button(window, text = "2", width = 12, command = add)
sr_btn3 = Button(window, text = "3", width = 12, command = add)

# Dig Button
dig_btn0 = Button(window, text = "0", width = 12, command = add)
dig_btn1 = Button(window, text = "1", width = 12, command = add)
dig_btn2 = Button(window, text = "2", width = 12, command = add)
dig_btn3 = Button(window, text = "3", width = 12, command = add)

# Assits Button
assist_btn0 = Button(window, text = "0", width = 12, command = add)
assist_btn1 = Button(window, text = "1", width = 12, command = add)
assist_btn2 = Button(window, text = "2", width = 12, command = add)
assist_btn3 = Button(window, text = "3", width = 12, command = add)

# Attacks Button
att_btn0 = Button(window, text = "0", width = 12, command = add)
att_btn1 = Button(window, text = "1", width = 12, command = add)
att_btn2 = Button(window, text = "2", width = 12, command = add)
att_btn3 = Button(window, text = "3", width = 12, command = add)

# Blocks Button
bl_btn0 = Button(window, text = "0", width = 12, command = add)
bl_btn1 = Button(window, text = "1", width = 12, command = add)
bl_btn2 = Button(window, text = "2", width = 12, command = add)
bl_btn3 = Button(window, text = "3", width = 12, command = add)

# Serve Packing
ser_btn0.grid(row= 2 , column = 1)
ser_btn1.grid(row= 2 , column = 2)
ser_btn2.grid(row= 2 , column = 3 )
ser_btn3.grid(row= 2 , column = 4)


# Serve Receive Button
sr_btn0.grid(row= 3 , column = 1)
sr_btn1.grid(row= 3 , column = 2)
sr_btn2.grid(row= 3 , column = 3)
sr_btn3.grid(row= 3 , column = 4)

# Dig Button
dig_btn0.grid(row= 4 , column = 1)
dig_btn1.grid(row= 4 , column = 2)
dig_btn2.grid(row= 4 , column = 3)
dig_btn3.grid(row= 4 , column = 4)

# Assits Button
assist_btn0.grid(row= 5 , column = 1)
assist_btn1.grid(row= 5 , column = 2)
assist_btn2.grid(row= 5 , column = 3)
assist_btn3.grid(row= 5 , column = 4)

# Attacks Button
att_btn0.grid(row= 6 , column = 1)
att_btn1.grid(row= 6 , column = 2)
att_btn2.grid(row= 6 , column = 3)
att_btn3.grid(row= 6 , column = 4)

# Blocks Button
bl_btn0.grid(row= 7 , column = 1)
bl_btn1.grid(row= 7 , column = 2)
bl_btn2.grid(row= 7 , column = 3)
bl_btn3.grid(row= 7 , column = 4)

# Labels 
sr_lbl = Label(window, text = "Serve Recive", font = "arial 12 bold", bg = "white").grid(row = 3, column = 0)
ser_lbl = Label(window, text = "Serve", font = "arial 12 bold", bg = "white").grid(row = 2, column = 0)
dig_lbl = Label(window, text = "Digs", font = "arial 12 bold", bg = "white").grid(row = 4, column = 0)
assit_lbl = Label(window, text = "Assists", font = "arial 12 bold", bg = "white").grid(row = 5, column = 0)
att_lbl = Label(window, text = "Attacks", font = "arial 12 bold", bg = "white").grid(row = 6, column = 0)
bl_lbl = Label(window, text = "Blocks", font = "arial 12 bold", bg = "white").grid(row = 7, column = 0)

# Instructions / Key Button

def instructions():
    key_win = Toplevel()
    key_win.geometry("500x500")
    key_win.title("Key / Instructions")
    
  # Key Descriptions  
    key = Label(key_win, text = "Key / Instuctions", font = "arial 15 bold", bg = "white")
    key.grid(row = 0, column = 0, sticky = W)
    instructions = Label(key_win, text = "Serve Grading Code:\n0: Serve in the net or out of bounds\n1: Easily Playable Serve(Rainbow)\n2: Harder Serve but Playable(btwn top and mid of attenna / deep serve, depends on each team)\n3:Ace or Hard Serve (btwn mid attenna and tape)\n" 
    + "\nServe Receive Grading Code:\n0: Shanked Pass or ball touches ground (player attempts to pass)\n1: Pass high enough to be played but not near setter\n2: Pass within 4 - 6 steps from setter (setter can still take with their hands)\n3: Pass within 1-3 from setter (perfect pass)\n"
    + "\nDigs Grading Code:\n0:Shanked or hits ground during attempt\n1: Playable dig \n2: Setter can play with hands\n3: High in the middle perfect ball for setter\n"
    + "\nAssist Grading Code:\n0:Not Playable(goes over the net, out of bounds, or in the net)\n1:Playable ball in the court, but can't attack\n2:Ball in the right area to attack but too tight or too far off\n3: Ball 5 feet in and 5 feet off\n" 
    + "\nAttack Grading Code:\n0:In the net or out of bounds\n1:Playable ball but easily read by other team(not strategic)\n2:Strategic play when not able to swing 100% (placing ball deep corners, roll shots over block, smartly placed tips / pushes)\n3: 100% swing into the court \n" 
    + "\nBlocking Grading Code:\n0:Out of Bounds or lands on our side in front of block\n1:Touch and played by one of our players\n2: Played by a player on the other team\n3:Successful block (not able to be played by the other team)\n", 
    font = "arial 12", bg = "white")
    instructions.grid(row = 1 , column = 1, sticky = W)

key_bttn = Button(window, text = "Key", width = 30, command = instructions)
key_bttn.grid(row = 8, column = 1, columnspan= 3)



window.mainloop()
