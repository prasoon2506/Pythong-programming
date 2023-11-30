def generate_squared_dict(n):
    squared_dict = {i: i*i for i in range(1, n+1)}
    return squared_dict

def main():
    n = int(input("Enter a positive integer n: "))
    
    if n < 1:
        print("Please enter a positive integer.")
        return
    
    result_dict = generate_squared_dict(n)
    
    print("Generated Dictionary:")
    print(result_dict)

if __name__ == "__main__":
    main()
