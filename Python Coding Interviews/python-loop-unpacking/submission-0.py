from typing import List, Tuple



def best_student(scores: List[Tuple[str, int]]) -> str:
    maximum=0
    student_name=""
    for name,score in scores:
        if score > maximum:
            maximum=score
            student_name=name
    return student_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
