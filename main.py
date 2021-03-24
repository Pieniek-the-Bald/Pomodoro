from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
""" Constants commented out since user is choosing these. """
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
reps = 0
mark = ""
timer = None


def reset_timer():
    """ --- TIMER RESET --- """
    global reps, mark
    window.after_cancel(timer)
    reps = 0
    mark = ""
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text=mark)
    canvas.itemconfig(timer_text, text="00:00")


def start_timer():
    """ --- TIMER MECHANISM --- """
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        time = int(long_break_entry.get()) * 60
    elif reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        time = int(work_time_entry.get()) * 60
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        time = int(short_break_entry.get()) * 60
    count_down(time)


def count_down(count):
    """ --- COUNTDOWN MECHANISM --- """
    global mark, reps, timer
    minutes = int(count / 60)
    seconds = int(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > -1:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark += "✔"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=3)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=2)
check_mark = Label(text=mark, fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=5)

work_time_label = Label(text="Enter work time", bg=YELLOW, font=(FONT_NAME, 10, "bold"))
work_time_label.grid(column=0, row=0)
short_time_label = Label(text="Enter short break time", bg=YELLOW, font=(FONT_NAME, 10, "bold"))
short_time_label.grid(column=1, row=0)
long_time_label = Label(text="Enter long break time", bg=YELLOW, font=(FONT_NAME, 10, "bold"))
long_time_label.grid(column=2, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=4)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=4)

work_time_entry = Entry(width=10)
work_time_entry.grid(column=0, row=1)
short_break_entry = Entry(width=10)
short_break_entry.grid(column=1, row=1)
long_break_entry = Entry(width=10)
long_break_entry.grid(column=2, row=1)

window.mainloop()
