def generate_list_and_tuple(input_sequence):
    
    numbers = [int(num) for num in input_sequence.split(',')]
    
    numbers_list = list(numbers)
    numbers_tuple = tuple(numbers)
    
    return numbers_list, numbers_tuple

def main():
    input_sequence = input("Enter a sequence of comma-separated numbers: ")
    
    result_list, result_tuple = generate_list_and_tuple(input_sequence)
   
    print("Generated List:", result_list)
    print("Generated Tuple:", result_tuple)

if __name__ == "__main__":
    main()
