def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_character_counts(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    # Sort list from greatest to least by count
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    
    return sorted_list
