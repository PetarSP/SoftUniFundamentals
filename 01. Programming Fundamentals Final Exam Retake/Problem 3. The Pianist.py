number_of_pieces = int(input())

pieces_dict = {}
for pieces in range(number_of_pieces):
    each_piece = input().split("|")
    piece_title = each_piece[0]
    piece_composer = each_piece[1]
    piece_key = each_piece[2]

    pieces_dict[piece_title] = {"piece_composer": piece_composer, "piece_key": piece_key}

command = input()

while not command == "Stop":
    command = command.split("|")
    instruction = command[0]
    piece = command[1]

    if instruction == "Add":
        composer = command[2]
        key = command[3]
        if piece in pieces_dict:
            print(f"{piece} is already in the collection!")
        else:
            pieces_dict[piece] = {"piece_composer": composer, "piece_key":key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif instruction == "Remove":
        if piece in pieces_dict:
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif instruction == "ChangeKey":
        new_key = command[2]
        if piece in pieces_dict:
            pieces_dict[piece]["piece_key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()
# sorted by their name and by the name of their composer in alphabetical order
sorted_dict = sorted(pieces_dict.items(), key=lambda x: (x[0], x[1]["piece_composer"]))

for piece, data in sorted_dict:
    print(f"{piece} -> Composer: {data['piece_composer']}, Key: {data['piece_key']}")