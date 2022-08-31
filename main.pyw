import tkinter
#import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    start.config(state=tkinter.ACTIVE)
    timer_txt.config(text="TIMER", fg=GREEN)
    checks.set("")
    canvas.itemconfig(time_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    start.config(state=tkinter.DISABLED)
    reps += 1
    if reps % 2 != 0:
        #playsound.playsound('./start.mp3')
        count_down(60 * WORK_MIN)
        timer_txt.config(text="WORK")
    elif reps == 8:
        count_down(60 *  LONG_BREAK_MIN)
        timer_txt.config(text="LONG BREAK", fg=RED)
    else:
        count_down(60 * SHORT_BREAK_MIN)
        #playsound.playsound('./break.mp3')
        timer_txt.config(text="BREAK", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    m = "0"+str(int(count/60)) if int(count/60) < 10 else int(count/60)
    s = "0"+str(count%60) if count%60 < 10 else count%60
    canvas.itemconfig(time_text, text=f"{m}:{s}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_count()
        if reps % 2 == 0:
            c = checks.get()
            c = c + "✔"
            checks.set(c)



# ---------------------------- UI SETUP ------------------------------- #
#WINDOWS
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

#Canvas
canvas = tkinter.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
time_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

#Label
timer_txt = tkinter.Label(text="TIMER", fg=GREEN, font=(FONT_NAME,35,"bold"), bg=YELLOW)
timer_txt.grid(column=1, row=0)

#Button Start
start = tkinter.Button(width=6, height=1, text="Start", command=start_count)
start.grid(column=0, row=2)

#Button Reset
reset = tkinter.Button(width=6, height=1, text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

#Check Label
checks = tkinter.StringVar(value="")
check = tkinter.Label(textvariable=checks, fg=GREEN, font=(FONT_NAME,15,"bold"), bg=YELLOW)
check.grid(column=1, row=2)

window.mainloop()

