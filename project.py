class StringReverse:
    def __init__(self, text):
        self.text = text
    def reverse_words(self):
        return " ".join(self.text.split()[::-1])
s = StringReverse("hello world this is python")
print(s.reverse_words())
