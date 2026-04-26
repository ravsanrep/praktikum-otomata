import tkinter as tk
from tokenizer import tokenize

def process():
    code = text_input.get("1.0", tk.END)
    result = tokenize(code)

    output.delete("1.0", tk.END)

    output.insert(tk.END, "=== RESERVED ===\n")
    output.insert(tk.END, str(result["reserved"]) + "\n\n")

    output.insert(tk.END, "=== SYMBOL ===\n")
    output.insert(tk.END, str(result["symbol"]) + "\n\n")

    output.insert(tk.END, "=== VARIABLE ===\n")
    output.insert(tk.END, str(result["variable"]) + "\n\n")

    output.insert(tk.END, "=== MATH EXPRESSION ===\n")
    for expr in result["math_expr"]:
        output.insert(tk.END, expr + "\n")

# UI
root = tk.Tk()
root.title("Tokenizer App")

tk.Label(root, text="Input Code:").pack()

text_input = tk.Text(root, height=10)
text_input.pack()

tk.Button(root, text="Process", command=process).pack()

tk.Label(root, text="Output:").pack()

output = tk.Text(root, height=10)
output.pack()

root.mainloop()