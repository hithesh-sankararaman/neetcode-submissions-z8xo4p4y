from typing import List

def contains_duplicate(words: List[str]) -> bool:
    temp = {}
    for word in words:
        temp[word] = temp.get(word,0)+1
    for i,val in temp.items():
        if val>1:
            return True
    return False


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
