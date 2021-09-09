class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


pesho_comment = Comment("Pesho", "e pich", 5)
print(pesho_comment.username)
print(pesho_comment.content)
print(pesho_comment.likes)
