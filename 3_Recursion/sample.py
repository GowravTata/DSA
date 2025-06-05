

def check_gfg(n):
    if not n:
        return "Done"
    print("GFG")
    check_gfg(n-1)

print(check_gfg(5))