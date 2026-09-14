def second_largest(numbers: list[float]) -> float:
  
    unique_sorted = sorted(set(numbers), reverse=True)
    if len(unique_sorted) < 2:
        raise ValueError("נדרשים לפחות 2 ערכים שונים")
    return unique_sorted[1]


print(second_largest([3, 1, 4, 1, 5, 9, 2]))  # 5

# 3 Test Cases for second_largest
print(second_largest([10, 20, 30, 40]))  # Expected output: 30
print(second_largest([5, 5, 5, 2, 1]))  # Expected output: 2
print(second_largest([-10, -5, -20]))  # Expected output: -10