def pascal_triangle(n):
    """Generate Pascal's Triangle up to the n-th row.
    
    Args:
        n (int): The number of rows in the Pascal's Triangle.
        
    Returns:
        list of lists: A list of lists representing the Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

# Test the function
if __name__ == "__main__":
    def print_triangle(triangle):
        """Print the Pascal's Triangle."""
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
