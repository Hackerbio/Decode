import base64

def print_title():
    title = """
==============================
        Uncoder by ymfw
==============================
    """
    print(title)

def try_decode_base(name, decode_func, encoded):
    try:
        decoded_bytes = decode_func(encoded)
        decoded_str = decoded_bytes.decode('utf-8')
        print(f"[+] {name} decoded: {decoded_str}")
    except Exception as e:
        print(f"[-] {name} failed: {e}")

def decode_all_bases(encoded_input):
    print(f"Trying to decode: {encoded_input}\n")
    try_decode_base("Base64", base64.b64decode, encoded_input)
    try_decode_base("Base32", base64.b32decode, encoded_input)
    try_decode_base("Base16 (Hex)", base64.b16decode, encoded_input)
    try_decode_base("Base85", base64.b85decode, encoded_input)
    try_decode_base("Ascii85", base64.a85decode, encoded_input)

if __name__ == "__main__":
    print_title()
    user_input = input("Enter encoded shit: ").strip()
    decode_all_bases(user_input)
