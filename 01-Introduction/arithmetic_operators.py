def calculate_metrics(num1: int, num2: int) -> tuple[int, int, int]:
    """
    Recebe dois inteiros e retorna uma tupla contendo: (soma, diferença, produto).
    """
    return (num1 + num2, num1 - num2, num1 * num2)

if __name__ == '__main__':
    """
    Task
    The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
    1. The first line contains the sum of the two numbers.
    2. The second line contains the difference of the two numbers (first - second).
    3. The third line contains the product of the two numbers.
    
    Example
    a = 3, b = 5
    Print: 8, -2, 15
    
    Constraints
    1 <= a <= 10^10
    1 <= b <= 10^10
    """
    
    a = int(input().strip())
    b = int(input().strip())
    
    soma, diferenca, produto = calculate_metrics(a, b)
    
    print(soma)
    print(diferenca)
    print(produto)