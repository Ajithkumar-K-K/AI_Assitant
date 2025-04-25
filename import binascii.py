import binascii
import os

def compute_crc(data: bytes, poly: int = 0x1021):
    crc = 0xFFFF
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0xFFFF  # Keep CRC to 16 bits
    return crc

def append_crc_to_file(file_path: str, output_path: str):
    with open(file_path, 'rb') as file:
        data = file.read()
    crc = compute_crc(data)
    with open(output_path, 'wb') as output_file:
        output_file.write(data)
        output_file.write(crc.to_bytes(2, byteorder='big'))  # Append CRC as 2 bytes
    print(f"CRC checksum {hex(crc)} appended to file: {output_path}")

def verify_crc(file_path: str):
    with open(file_path, 'rb') as file:
        data = file.read()
    received_crc = int.from_bytes(data[-2:], byteorder='big')
    original_data = data[:-2]
    computed_crc = compute_crc(original_data)
    if computed_crc == received_crc:
        print(f"File integrity verified. CRC: {hex(computed_crc)}")
        return True
    else:
        print(f"File corruption detected! Computed CRC: {hex(computed_crc)}, Received CRC: {hex(received_crc)}")
        return False

def main():
    print("Choose a file type:")
    print("1. Text File (.txt)")
    print("2. CSV File (.csv)")
    print("3. Image File (.jpg)")
    option = input("Enter your choice (1/2/3): ")

    file_extension = ""
    if option == "1":
        file_extension = ".txt"
    elif option == "2":
        file_extension = ".csv"
    elif option == "3":
        file_extension = ".jpg"
    else:
        print("Invalid option! Exiting.")
        return

    file_path = input(f"Enter the path of the {file_extension} file: ").strip()

    if not os.path.exists(file_path) or not file_path.endswith(file_extension):
        print("Invalid file path or file type mismatch. Exiting.")
        return

    output_path = f"transmitted_{os.path.basename(file_path)}"

    print("\nPerforming checksum operation:")
    append_crc_to_file(file_path, output_path)
    print("Checksum appended to the file.")

    print("\nVerifying checksum...")
    if verify_crc(output_path):
        print("File transmission verified successfully!")
    else:
        print("File transmission failed! Data integrity compromised.")

if __name__ == "__main__":
    main()