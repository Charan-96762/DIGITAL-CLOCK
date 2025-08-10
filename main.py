from tkinter import *
import time  # This line is correct — no syntax error

def update_time():
    current_time = time.strftime("%d-%m-%y , %H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every second

# Create main window
dc = Tk()
dc.title("DIGITAL CLOCK")
dc.geometry("500x100")  # Correct geometry format

# Create and pack the label
label = Label(dc, font=("Arial", 25), bg="black", fg="yellow")
label.pack(fill=BOTH, expand=True)

# Start updating time
update_time()

# Run the Tkinter event loop
dc.mainloop()
