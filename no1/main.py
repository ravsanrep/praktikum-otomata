from tokenizer import tokenize

print("=== TOKENIZER PROGRAM ===")
print("Masukkan kode (ketik 'END' untuk selesai):")

lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

code = "\n".join(lines)

result = tokenize(code)

print("\n=== HASIL TOKEN ===")

print("\n[Reserved Words]")
print(result["reserved"])

print("\n[Symbols]")
print(result["symbol"])

print("\n[Variables]")
print(result["variable"])

print("\n[Math Expressions]")
for expr in result["math_expr"]:
    print(expr)