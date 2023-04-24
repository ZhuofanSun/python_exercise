import time
print("-" * 80)
print("Remember The Word")
print("-" * 80)

file = open("instructions.txt","r")
x = file.read()
file.close()
print(x)

input("Press enter key to display the words.")
print("orange")
time.sleep(2)
print("chair")
time.sleep(2)
print("sandwich")
time.sleep(2)


