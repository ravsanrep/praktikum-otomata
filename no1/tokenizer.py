import re

# ========================
# DATA
# ========================
RESERVED_WORDS = {
    "if", "else", "for", "while", "int", "float", "return"
}

SYMBOLS = r"[+\-*/=(){};,]"

# ========================
# FUNCTION TOKENIZER
# ========================
def tokenize(code):
    tokens = re.findall(r"[A-Za-z_]\w*|\d+|[+\-*/=(){};,]", code)

    result = {
        "reserved": [],
        "symbol": [],
        "variable": [],
        "math_expr": []
    }

    for token in tokens:
        if token in RESERVED_WORDS:
            result["reserved"].append(token)

        elif re.match(SYMBOLS, token):
            result["symbol"].append(token)

        elif re.match(r"[A-Za-z_]\w*", token):
            result["variable"].append(token)

    # Deteksi ekspresi matematika (simple)
    lines = code.split("\n")
    for line in lines:
        if re.search(r"[=+\-*/]", line):
            result["math_expr"].append(line.strip())

    return result