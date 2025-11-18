class RomanToInteger:
    def __init__(self, roman: str):
        self.roman = roman.upper()
        self.values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convert(self) -> int:
        total = 0
        prev_value = 0

        for char in reversed(self.roman):
            value = self.values.get(char, 0)

            if value < prev_value:
                total -= value
            else:
                total += value

            prev_value = value

        return total


# Ví dụ sử dụng
converter = RomanToInteger("MCMXCIV")
print(converter.convert())   # 1994
