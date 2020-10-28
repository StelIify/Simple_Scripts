with open(r"C:\Users\x0658602\Desktop\cupcakes.txt", "r") as raw_text:
    text_string = ""
    for word in raw_text:
        text_string += word


filted_text = text_string.replace(".", "").replace("\n", "").split(" ")


def count_number(word_list):
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


not_sorted_dict = count_number(filted_text)
sorted_dict = {key: value for key, value in sorted(not_sorted_dict.items(),
               key=lambda item: item[1], reverse=True) if len(key) > 2}

for key, value in sorted_dict.items():
    print(f"{key} occurs {value} times")



