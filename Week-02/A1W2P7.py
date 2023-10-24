pos = input("position") 
print("black" if(int(pos[1])%2) == int(ord(pos[0])%2) else "white")