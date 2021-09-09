some_str = input().split()  # some input: str casted to list

print("".join([el * len(el) for el in some_str]))
