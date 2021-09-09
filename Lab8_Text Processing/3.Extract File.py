path_file = input().split("\\")

file_name = (path_file[-1].split("."))[0]
file_ext = (path_file[-1].split("."))[1]
print(f"File name: {file_name}\n"
      f"File extension: {file_ext}")