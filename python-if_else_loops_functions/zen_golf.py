"""
Zen Golf: Balancing Readability and Brevity in Python
File 1 Submission: Verbose vs. Pythonic Functions
"""

# =====================================================================
# FUNCTION 1: Sum of Even Numbers
# =====================================================================

def sum_even_verbose(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total


def sum_even_pythonic(numbers):
    # Zen of Python: "Simple is better than complex."
    # Built-in sum() with a generator expression avoids explicit accumulator state.
    return sum(num for num in numbers if num % 2 == 0)


# =====================================================================
# FUNCTION 2: Find the Longest Word
# =====================================================================

def longest_word_verbose(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def longest_word_pythonic(words):
    # Zen of Python: "Readability counts."
    # Using max() with the key=len parameter replaces imperative loop comparison.
    return max(words, key=len, default="")


# =====================================================================
# FUNCTION 3: Filter Positive Numbers
# =====================================================================

def filter_positive_verbose(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result


def filter_positive_pythonic(numbers):
    # Zen of Python: "Flat is better than nested."
    # A list comprehension flattens the loop-and-append logic into a single idiomatic construct.
    return [num for num in numbers if num > 0]


# =====================================================================
# STEP 3: Measurement & Equivalence Tests
# =====================================================================

def count_characters(code):
    """Calculates code length excluding spaces and newlines."""
    return len(code.replace(" ", "").replace("\n", ""))


def avg_line_length(code):
    """Calculates average line length for non-empty lines as a proxy for readability."""
    lines = [l for l in code.split("\n") if l.strip()]
    return sum(len(l) for l in lines) / len(lines) if lines else 0


def test_equivalence():
    """Verifies that both verbose and pythonic versions produce identical results."""
    # Test 1: Sum of evens
    nums = [1, 2, 3, 4, 5, 6]
    assert sum_even_verbose(nums) == sum_even_pythonic(nums) == 12

    # Test 2: Longest word
    words = ["cat", "elephant", "dog", "whale"]
    assert longest_word_verbose(words) == longest_word_pythonic(words) == "elephant"

    # Test 3: Filter positives
    mixed = [-3, -1, 0, 2, 5, -7]
    assert filter_positive_verbose(mixed) == filter_positive_pythonic(mixed) == [2, 5]

    print("All equivalence tests passed successfully!")


if __name__ == "__main__":
    test_equivalence()