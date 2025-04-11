def sha1_hash(input_str:str) -> str:
    blocks_size_bits = 512
    words_per_block = 16
    words_size_bits = 32

    input_str = input_str.encode('utf-8')

    input_bits = ''.join(f'{byte:08b}' for byte in input_str)

    input_size_bits = len(input_bits)

    input_bits +=  '1' + '0' * ((448 - (len(input_bits) + 1) % blocks_size_bits) % blocks_size_bits)

    input_bits += f'{input_size_bits:064b}'

    blocks = [input_bits[i:i + blocks_size_bits] for i in range(0, len(input_bits), blocks_size_bits)]

    blocks = [[int(block[i:i + words_size_bits], 2) for i in range(0, blocks_size_bits, words_size_bits)] for block in blocks]

    for block in blocks:
        for i in range(16, 80):
            new_word = lrot((block[i - 3] ^ block[i - 8] ^ block[i - 14] ^ block[i - 16]))
            block.append(new_word)

    registers = [
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0
    ]

def lrot(word:int) -> int:
    return (word << 1 | (word >> 31)) & 0xFFFFFFFF