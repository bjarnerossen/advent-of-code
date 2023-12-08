def main():
    with open("test.txt") as file:
        data = file.readlines()

    result = sum_part_numbers(data)

def is_part_number(data, row, col):

        symbols = "*+#$@&" 
        neighbors = [
            (-1, -1), (-1, 0), 
            (-1, 1), (0, -1), 
            (0, 1), (1, -1), 
            (1, 0), (1, 1)
        ]

        if not data[row][col].isdigit():
            return False
        
        for dr, dc in neighbors:
            new_row, new_col = row + dr, col + dc
            if (
                0 <= new_row < len(data) and
                0 <= new_col < len(data[0]) and
                data[new_row][new_col] in symbols
            ):
                return True

        return False

def sum_part_numbers(data):
        for row in range(len(data)):
            for col in range(len(data[row])):
                if is_part_number(data, row, col):
                    total += int(data[row][col])
        return total

    


if __name__ == "__main__":
    main()