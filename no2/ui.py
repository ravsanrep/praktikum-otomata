import tkinter as tk

# =========================
# FSM TRANSITION
# =========================
def next_state(state, char):
    if state == "S":
        return "A" if char == "0" else "B"
    elif state == "A":
        return "C" if char == "0" else "B"
    elif state == "B":
        return "A" if char == "0" else "B"
    elif state == "C":
        return "C"


# =========================
# ANIMATION
# =========================
def run_simulation():
    s = entry.get()

    # validasi
    if not all(c in "01" for c in s):
        result_label.config(text="❌ Input hanya 0 dan 1!", fg="red")
        return
    

    global path
    path = ["S"]
    state = "S"

    for char in s:
        state = next_state(state, char)
        path.append(state)

    step_text.set(" → ".join(path))

    # simpan history
    final = path[-1]
    history.insert(tk.END, f"{s} → {final} → {'ACCEPT' if final == 'B' else 'REJECT'}")

    animate(0)


def animate(i):
    if i >= len(path):
        final = path[-1]
        if final == "B":
            result_label.config(text="DITERIMA ✅", fg="green")
        else:
            result_label.config(text="DITOLAK ❌", fg="red")
        return

    update_visual(path[i])
    root.after(700, lambda: animate(i + 1))


# =========================
# VISUAL UPDATE
# =========================
def update_visual(state):
    for s in states:
        canvas.itemconfig(states[s], fill="lightgray")

    canvas.itemconfig(states[state], fill="lightgreen")


# =========================
# UI
# =========================
root = tk.Tk()
root.title("FSM Simulation")
root.geometry("700x500")

tk.Label(root, text="Input String (0 & 1):").pack()

entry = tk.Entry(root, width=30)
entry.pack()

tk.Button(root, text="Start Simulation", command=run_simulation).pack()

step_text = tk.StringVar()
tk.Label(root, textvariable=step_text).pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# =========================
# CANVAS (FSM DIAGRAM)
# =========================
canvas = tk.Canvas(root, width=650, height=300)
canvas.pack()

# =========================
# HISTORY
# =========================
tk.Label(root, text="History").pack()

history = tk.Listbox(root, height=8)
history.pack(fill="both", expand=True)

# STATE POSITIONS
states = {
    "S": canvas.create_oval(50, 120, 100, 170, fill="lightgray"),
    "A": canvas.create_oval(200, 40, 250, 90, fill="lightgray"),
    "B": canvas.create_oval(200, 200, 250, 250, fill="lightgray"),
    "C": canvas.create_oval(450, 120, 500, 170, fill="lightgray"),
}

# LABEL STATE
canvas.create_text(75, 145, text="S")
canvas.create_text(225, 65, text="A")
canvas.create_text(225, 225, text="B")
canvas.create_text(475, 145, text="C")

# =========================
# DRAW ARROWS
# =========================

# S → A (0)
canvas.create_line(100, 140, 200, 65, arrow=tk.LAST)
canvas.create_text(150, 90, text="0")

# S → B (1)
canvas.create_line(100, 150, 200, 225, arrow=tk.LAST)
canvas.create_text(150, 190, text="1")

# A → B (1)
canvas.create_line(225, 90, 225, 200, arrow=tk.LAST)
canvas.create_text(240, 145, text="1")

# B → A (0)
canvas.create_line(210, 200, 210, 90, arrow=tk.LAST)
canvas.create_text(195, 145, text="0")

# A → C (0)
canvas.create_line(250, 65, 450, 140, arrow=tk.LAST)
canvas.create_text(350, 100, text="0")

# B loop (1)
canvas.create_arc(190, 210, 260, 270, start=140, extent=270, style=tk.ARC)
canvas.create_text(230, 280, text="1")

# C loop (0,1)
canvas.create_arc(440, 130, 510, 190, start=140, extent=270, style=tk.ARC)
canvas.create_text(480, 200, text="0,1")

root.mainloop()