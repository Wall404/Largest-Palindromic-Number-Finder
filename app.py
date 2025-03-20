def is_palindrome(n: int) -> bool:
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]


def largest_palindrome_in_range(start: int, end: int) -> int:
    """Find the largest palindromic number strictly between two numbers."""
    # Check if the range has numbers between them (exclusive)
    if end - start <= 1:
        return -1

    for num in range(end - 1, start, -1):
        if is_palindrome(num):
            return num
    return -1  # Return -1 if no palindromic number is found


if __name__ == "__main__":
    # Accept user input
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    result = largest_palindrome_in_range(start, end)
    if result != -1:
        print(f"The largest palindromic number between {start} and {end} is: {result}")
    else:
        print(f"There is no palindromic number between {start} and {end}.")
