from fsm import check_string

print("=== FSM CHECKER ===")
s = input("Masukkan string (0 & 1): ")

if check_string(s):
    print("✅ STRING DITERIMA")
else:
    print("❌ STRING DITOLAK")