def encode_LZW(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # Initialize the dictionary with ASCII codes
        dictionary = {chr(i): i for i in range(256)}
        print(dictionary)
        next_code = 256

        # Read the input data
        data = input_file.read()

        # Initialize variables for encoding
        current_str = ""
        encoded_data = []
        for ch in data:
            new_str = current_str + ch
            if new_str in dictionary:
                current_str = new_str
            else:
                encoded_data.append(dictionary[current_str])
                dictionary[new_str] = next_code
                next_code += 1
                current_str = ch
        encoded_data.append(dictionary[current_str])

        # Write the encoded data to the output file
        output_file.write(" ".join(str(code) for code in encoded_data))

def decode_LZW(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # Initialize the dictionary with ASCII codes
        dictionary = {i: chr(i) for i in range(256)}
        next_code = 256

        # Read the encoded data
        encoded_data = input_file.read().split()

        # Initialize variables for decoding
        current_str = dictionary[int(encoded_data[0])]
        decoded_data = current_str
        for code in encoded_data[1:]:
            if int(code) in dictionary:
                new_str = dictionary[int(code)]
            # else:
            #     new_str = current_str + current_str[0]
            decoded_data += new_str
            print(decoded_data)
            dictionary[next_code] = current_str + new_str[0]
            next_code += 1
            current_str = new_str

        # Write the decoded data to the output file
        output_file.write(decoded_data)



input_file_path = "input.txt"
encoded_file_path = "encoded.txt"
decoded_file_path = "decoded.txt"

encode_LZW(input_file_path, encoded_file_path)
decode_LZW(encoded_file_path, decoded_file_path)

