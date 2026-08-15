##1. Basic function fibonacci
# def fibonacci(n):
#     #base case
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     #recursive case
#     return fibonacci(n-1) + fibonacci(n-2)

##2. Add type hints
# def fibonacci(n: int) -> int:
#     #base case
#     if n < 0:
#         raise ValueError("Value input must be more than 0")
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     #recursive case
#     return fibonacci(n-1) + fibonacci(n-2)

##3. Kiem tra Type Hints bang mypy
def fibonacci(n: int) -> int:
    #base case
    if n < 0:
        raise ValueError("Value input must be more than 0")
    if n == 0:
        return 0
    if n == 1:
        return 1

    #recursive case
    return fibonacci(n-1) + fibonacci(n-2)

def main() -> None:

    fibonacci("acv")

if __name__ == "__main__":
    main()