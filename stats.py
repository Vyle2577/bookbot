def num_words(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def char_count(text):
    count_dict = {}
    clean_text = text.lower()
    for char in clean_text:
        if char.isalpha():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return count_dict

def sort_on(items):
    return items["num"]
    
def get_sorted_list(char_count):
    sorted_list = []
    for key in char_count:
        if key not in sorted_list:
            sorted_list.append({'char': key, "num": char_count[key]})
    sorted_list.sort(reverse =True, key=sort_on)
    return sorted_list

