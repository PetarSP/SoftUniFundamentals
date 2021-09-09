cookies = input().split(", ")

command = input()

while not command == "Eat":
    command = command.split()
    instruction = command[0]
    biscuit = command[1]

    if instruction == "Update-Any":
        for el in range(len(cookies)):
            if cookies[el] == biscuit:
                cookies[el] = "Out of stock"
    elif instruction == "Replace":
        index = int(command[2])
        if index < len(cookies):
            cookies[index] = biscuit
    elif instruction == "Update-Last":
        cookies.pop()
        cookies.append(biscuit)
    elif instruction == "Rearrange":
        for el in range(len(cookies)):
            if cookies[el] == biscuit:
                biscuit_popped = cookies.pop(el)
                cookies.append(biscuit_popped)
    command = input()

new_list = [biscuit for biscuit in cookies if not biscuit == "Out of stock"]
print(" ".join(new_list))