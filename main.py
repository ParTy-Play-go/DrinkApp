import random
import time
import tkinter as tk
window = tk.Tk()
window.resizable(False, False)
print("[Log] Program started: Done!")
print("[Log] Drink App! by Party")
window.title("Drink App!")

def handle_click(event):
    list1 = ['ром', 'пиво', 'водку', 'коньяк', "виски"]
    list2 = ['за здоровье!', 'за удачу!', 'за успех!', 'за любовь!', 'за дружбу!']
    out = "Сегодня мы будем выпивать " + random.choice(list1) + " " + random.choice(list2)
    print("[Log] Frase genearated!")
    label = tk.Label(
        text=out,
        foreground="cyan2",
        padx=5,
        pady=10
    )

    label.pack()



button = tk.Button(text="Сгенерировать тост", background="OliveDrab1", width=39, height=5, relief=tk.FLAT)

button.bind("<Button-1>", handle_click)
button.pack()
window.mainloop()
