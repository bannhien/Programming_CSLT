myPets = ["Zophie","Pooka","Fat-tail"]
print("Enter a pet name:")
name=input()
if name not in myPets:
    print(f"I do not have a pet named")
else:
    print(f"{name} is may pet")