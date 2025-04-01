import threading

def write_characters(input_text):
    with open("output_file1.txt", "w") as f:
        for char in input_text:
            if char.isalpha():  
                f.write(char)

def write_numbers(input_text):
    with open("output_file2.txt", "w") as f:
        for char in input_text:
            if char.isdigit():  
                f.write(char)

def write_special_characters(input_text):
    with open("output_file3.txt", "w") as f:
        for char in input_text:
            if not char.isalnum() and not char.isspace():  
                f.write(char)


with open("in.txt", "r") as file:
    data = file.read()


thread1 = threading.Thread(target=write_characters, args=(data,))
thread2 = threading.Thread(target=write_numbers, args=(data,))
thread3 = threading.Thread(target=write_special_characters, args=(data,))


thread1.start()
thread2.start()
thread3.start()


thread1.join()
thread2.join()
thread3.join()

print("Processing complete. Check output files: output_file1.txt, output_file2.txt, output_file3.txt")