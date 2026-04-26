def check_string(s):
    state = "S"

    for char in s:
        if state == "S":
            if char == "0":
                state = "A"
            elif char == "1":
                state = "B"
            else:
                return False

        elif state == "A":
            if char == "0":
                state = "C"
            elif char == "1":
                state = "B"

        elif state == "B":
            if char == "0":
                state = "A"
            elif char == "1":
                state = "B"

        elif state == "C":
            state = "C"

    return state == "B"