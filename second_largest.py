def second_largest(numbers: list[float]) -> float:
    """מחזיר את המספר השני-בגודלו ברשימה. מניח לפחות 2 ערכים שונים"""
    unique_sorted = sorted(set(numbers), reverse=True)
    if len(unique_sorted) < 2:
        raise ValueError("נדרשים לפחות 2 ערכים שונים")
    return unique_sorted[1]


# 3 Test Cases
print(second_largest([10, 20, 30, 40]))  # 30
print(second_largest([5, 5, 5, 2, 1]))  # 2
print(second_largest([-10, -5, -20]))  # -10