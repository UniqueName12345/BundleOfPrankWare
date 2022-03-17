import tkinter as tk

window = tk.Tk()
window.title("You are an IDIOT!")
window.geometry("400x400")
window.configure(background='#FFFFFF')
window.mainloop()

# make the screen loop im.gif
image = tk.PhotoImage(file="im.gif")
label = tk.Label(window, image=image)
label.pack()
window.mainloop()
