import tkinter as tk
from tkinter import ttk
import time

# =========================
# FSM LOGIC
# =========================
def next_state(state, char):
    if state == "S":
        return "A" if char == "0" else "B"
    elif state == "A":
        return "C" if char == "0" else "B"
    elif state == "B":
        return "A" if char == "0" else "B"
    return "C"

# =========================
# SIMULATION
# =========================
def run_simulation():
    s = entry.get()

    if not all(c in "01" for c in s):
        status_label.config(text="Input hanya 0/1", foreground="red")
        return

    state = "S"
    path = ["S"]

    for c in s:
        state = next_state(state, c)
        path.append(state)

    step_label.config(text=" → ".join(path))

    if state == "B":
        status_label.config(text="DITERIMA ✅", foreground="#27ae60")
        result = "DITERIMA"
    else:
        status_label.config(text="DITOLAK ❌", foreground="#e74c3c")
        result = "DITOLAK"

    tree.insert("", "end", values=(s, result, state, time.strftime("%H:%M:%S")))

# =========================
# ROOT
# =========================
root = tk.Tk()
root.title("FSM Simulation")
root.geometry("1100x650")
root.configure(bg="#eef1f5")

# STYLE
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
    font=("Segoe UI", 10),
    padding=8
)

style.configure("Blue.TButton",
    background="#2d6cdf",
    foreground="white"
)

style.configure("Gray.TButton",
    background="#dcdde1"
)

style.configure("Red.TButton",
    background="#ff7675"
)

style.configure("Card.TFrame",
    background="white",
    relief="flat"
)

# =========================
# LEFT PANEL
# =========================
left = ttk.Frame(root, style="Card.TFrame", padding=15)
left.place(x=15, y=15, width=360, height=600)

ttk.Label(left, text="INPUT STRING", font=("Segoe UI", 11, "bold")).pack(anchor="w")

entry = ttk.Entry(left, font=("Segoe UI", 12))
entry.pack(fill="x", pady=10)

btn_frame = ttk.Frame(left)
btn_frame.pack(pady=5)

ttk.Button(btn_frame, text="▶ Start", style="Blue.TButton", command=run_simulation).grid(row=0, column=0, padx=3)
ttk.Button(btn_frame, text="⏸ Pause", style="Gray.TButton").grid(row=0, column=1, padx=3)
ttk.Button(btn_frame, text="⏹ Reset", style="Red.TButton").grid(row=0, column=2, padx=3)

# DETAIL
ttk.Label(left, text="DETAIL", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=10)

status_label = ttk.Label(left, text="-", font=("Segoe UI", 11))
status_label.pack(anchor="w")

# HISTORY
ttk.Label(left, text="HISTORY", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=10)

tree = ttk.Treeview(left, columns=("Input","Result","State","Time"), show="headings", height=10)

for col in ("Input","Result","State","Time"):
    tree.heading(col, text=col)

tree.pack(fill="both", expand=True)

# =========================
# RIGHT PANEL
# =========================
right = ttk.Frame(root, style="Card.TFrame", padding=15)
right.place(x=390, y=15, width=730, height=600)

ttk.Label(right, text="FINITE STATE MACHINE", font=("Segoe UI", 11, "bold")).pack()

canvas = tk.Canvas(right, width=700, height=350, bg="white", highlightthickness=0)
canvas.pack(pady=10)

# STATES
S = canvas.create_oval(50, 150, 100, 200, fill="#ecf0f1")
A = canvas.create_oval(250, 70, 300, 120, fill="#ecf0f1")
B = canvas.create_oval(250, 250, 300, 300, fill="#2ecc71")
C = canvas.create_oval(500, 150, 550, 200, fill="#ff7675")

canvas.create_text(75, 175, text="S", font=("Segoe UI", 10, "bold"))
canvas.create_text(275, 95, text="A", font=("Segoe UI", 10, "bold"))
canvas.create_text(275, 275, text="B", font=("Segoe UI", 10, "bold"))
canvas.create_text(525, 175, text="C", font=("Segoe UI", 10, "bold"))

# ARROWS
canvas.create_line(100,170,250,95,arrow=tk.LAST)
canvas.create_text(180,120,text="0")

canvas.create_line(100,180,250,275,arrow=tk.LAST)
canvas.create_text(180,240,text="1")

canvas.create_line(275,120,275,250,arrow=tk.LAST)
canvas.create_text(290,190,text="1")

canvas.create_line(260,250,260,120,arrow=tk.LAST)
canvas.create_text(240,190,text="0")

canvas.create_line(300,95,500,170,arrow=tk.LAST)
canvas.create_text(400,130,text="0")

# LOOP B
canvas.create_arc(230,260,330,340,start=140, extent=280,style=tk.ARC,width=2)
canvas.create_text(275,330,text="1")

# LOOP C
canvas.create_arc(480,160,580,240,start=140, extent=280,style=tk.ARC,width=2)
canvas.create_text(530,260,text="0,1")

# STEP
step_label = ttk.Label(right, text="", font=("Segoe UI", 10))
step_label.pack()

root.mainloop()