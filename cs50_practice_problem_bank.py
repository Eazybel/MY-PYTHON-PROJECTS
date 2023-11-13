greet=input("Enter your greeting: ")
name=greet.lower()
while True:
    if 'hello' in name:
        print("0$")
        break
    if 'h' in name[0]:
        print("20$")
        break
    else:
        print("100$")
        break