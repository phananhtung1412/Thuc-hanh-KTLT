# import the modules
import tkinter
import random

# list of possible colour.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0
# ==========================
# Bước 2: đổi thời gian 30s → 120s
# ==========================
timeleft = 120

# function that will start the game.
def startGame(event):
    if timeleft == 120:   # thời điểm bắt đầu
        countdown()
        nextColour()

# Function to choose and display the next colour.
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        # ======================
        # Bước 3: cộng 2 và trừ 1 điểm
        # ======================
        if e.get().lower() == colours[1].lower():
            score += 2
        elif e.get() != "":
            score -= 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # change the colour and text
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # update the score.
        scoreLabel.config(text="Score: " + str(score))

# Countdown timer function
def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time left: " + str(timeleft))

        timeLabel.after(1000, countdown)

# Driver Code
root = tkinter.Tk()
root.title("COLOR GAME")
root.geometry("450x250")

instructions = tkinter.Label(root, text="Type the COLOR of the word, not the text!",
                             font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press ENTER to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft),
                          font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()
n
