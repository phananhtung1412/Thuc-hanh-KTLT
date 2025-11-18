class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


# Ví dụ sử dụng
input_text = "hello .py"
reverser = StringReverser(input_text)
output_text = reverser.reverse_words()
print(output_text)   # .py hello
