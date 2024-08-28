def even_or_odd_check():
    """Prompt the user for a number and check if each number is even or odd."""
    n = int(input("Enter your range: "))
    
    for i in range(1, n + 1):
        num = int(input(f"Enter number {i}: "))
        if num % 2 == 0:
            print("even")
        else:
            print("odd")

if __name__ == "__main__":
    even_or_odd_check()
