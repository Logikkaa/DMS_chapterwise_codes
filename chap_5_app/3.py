def generate_bit_sequences(n, sequence=''):
    if n == 0:
        print(sequence)
        return
    generate_bit_sequences(n-1, sequence+'1')
    if sequence == '' or sequence[-1] != '0':
        generate_bit_sequences(n-1, sequence+'0')

n = 3  # Length of bit sequences
generate_bit_sequences(n)
