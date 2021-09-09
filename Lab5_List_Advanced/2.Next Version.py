# "{n1}.{n2}.{n3}"

# 1.2.3

soft_ver = input().split(".")
joined = "".join(soft_ver)

if int(joined) < 999:
    next_ver = int(joined) + 1
# 124
    next_ver_as_str = [str(i) for i in str(next_ver)]
    print(f"{next_ver_as_str[0]}.{next_ver_as_str[1]}.{next_ver_as_str[2]}")
