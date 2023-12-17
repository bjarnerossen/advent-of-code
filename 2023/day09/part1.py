import re

def sequence_differences(sequence):
    return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]

def extrapolate_next_value(history):
    sequences = [history]
    while not all(value == 0 for value in sequences[-1]):
        sequences.append(sequence_differences(sequences[-1]))
    
    extrapolated_value = 0
    for sequence in reversed(sequences):
        extrapolated_value += sequence[-1]
    return extrapolated_value

def sum_of_extrapolated_values(histories):
    extrapolated_values = [extrapolate_next_value(history) for history in histories]
    return sum(extrapolated_values)

def read_input_file(file_name):
    with open(file_name, 'r') as file:
        return [[int(value) for value in re.findall(r'-?\d+', line)] for line in file.readlines()]

def main():
    data = read_input_file("input.txt")
    histories = data
    result = sum_of_extrapolated_values(histories)
    print("Sum of extrapolated values:", result)

if __name__ == "__main__":
    main()
