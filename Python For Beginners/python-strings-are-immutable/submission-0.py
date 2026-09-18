def remove_fourth_character(word: str) -> str:
    temp1 = word[:3]
    temp2 = word[4:]
    return temp1+temp2
# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
