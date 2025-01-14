




def character_count(the_book):
    char_dict = {}
    for char in the_book.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict




def number_of_words(whole_book):
    
    
    
    
    return len(whole_book.split())

def book_report(char_dict):
    char_tuple_list = list(char_dict.items())
    char_tuple_list.sort(key=lambda item: item[1], reverse=True)
    for key, value in char_tuple_list:
        if key == "\n":
            print(f"The '\\n' character was found {value} times")
        else:
            print(f"The '{key}' character was found {value} times")

    
   

    
        


def main():

    

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()



    character_dictionary = character_count(file_contents)
    book_report(character_dictionary)







if __name__ == "__main__":
    main()



