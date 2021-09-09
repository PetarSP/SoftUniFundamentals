words = input().split(" ")
even_words = [i for i in words if len(i) % 2 == 0]
for word in even_words:
    print(word)
