import sys
even, odd = 0, 0
while True: 
    try: 
        line = int(input())
        if line%2 == 0: 
            even = even+line 
        else: 
            odd = odd+line 
    except EOFError: 
        print("odd:{} even:{}".format(odd,even)) 
        break  