def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    chars = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            chars[char] = chars.get(char, 0) + 1
    return chars
def char_sort(char_dict):
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
