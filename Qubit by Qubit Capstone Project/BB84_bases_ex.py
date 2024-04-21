# Path: requirements.txt
# cirq==0.8.2
# matplotlib==3.2.1
# numpy==1.18.2
# cirq-web==0.1.0


import cirq
import cirq_web.bloch_sphere as bloch_sphere
import numpy as np
import matplotlib.pyplot as plt
from random import choices

# Alice's part
message  = input("Enter your message that you want to send to Bob: ")
string_list = [int(bit) for char in message for bit in format(ord(char), '08b')]
print(string_list)
# Create a quantum circuit
qubits = cirq.LineQubit.range(len(string_list))

# Alice chooses a random basis to encode her bits
alice_bases = choices(['Z', 'X'], k=len(string_list))
print("Alice bases: ", alice_bases)

circuit_A = cirq.Circuit()

# Prepare the qubits
for i in range(len(string_list)):
    if string_list[i] == '1':
        circuit_A.append(cirq.X(qubits[i]))

print("Alice Circuit: \n",circuit_A)

# Apply the Hadamard gate to the qubits that are encoded in the X basis
for i in range(len(string_list)):
    if alice_bases[i] == 'X':
        circuit_A.append(cirq.H(qubits[i]))

print("Alice Circuit: \n",circuit_A)

# Bob's part
#bob_bases = [choices([0, 1], k=1)[0] for _ in range(len(string_list))]
#circuit.append(cirq.measure(*qubits, key='result'))


# Bob chooses a random basis
bob_bases = choices(['Z', 'X'], k=len(string_list))
print("Bob bases:", bob_bases)
bob_circuit = cirq.Circuit()

for i in range(len(string_list)):
    if bob_bases[i] == 'X':
        bob_circuit.append(cirq.H(qubits[i]))

# Bob Measure the qubits
bob_circuit.append(cirq.measure(*qubits, key='result'))
print("Bob Circuit", bob_circuit)

# Bob creates a Key
bb84_circuit = circuit_A + bob_circuit

simulator = cirq.Simulator()
results = simulator.run(bb84_circuit)
bob_key = results.measurements['result'][0]

print('\n Bob\'s initial key:', bob_key)

# Independently ALice and Bob's randomly selected bases
final_alice_key = []
final_bob_key = []

for i in range(len(string_list)):
    if bob_key[i] == 1:
        if alice_bases[i] == 'Z':
            final_alice_key.append(0)
        if alice_bases[i] == 'X':
            final_alice_key.append(1)
        if bob_bases[i] == 'Z':
            final_bob_key.append(1)
        if bob_bases[i] == 'X':
            final_bob_key.append(0)

print('\n Alice\'s final key:', final_alice_key)
print('\n Bob\'s final key:', final_bob_key)

# Step 8 Alice and Bob compare the first bits in their key
bits_to_compare = int(len(final_alice_key) * .5)

if final_alice_key[:bits_to_compare] == final_bob_key[:bits_to_compare]:
    final_alice_key = final_alice_key[bits_to_compare:]
    final_bob_key = final_bob_key[bits_to_compare:]
    
    print('\n\n The Keys can be used!')
    print('\n Alice\'s final key:', final_alice_key)
    print('\n Bob\'s final key:', final_bob_key)

else:
    print('\n\n The keys cannot be used! Eve has tampered with the keys!')
    #exit(1)  # Exit the program if the keys cannot be used

# Sifting
same_bases = [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]
alice_key_sifted = [string_list[i] for i in same_bases]
bob_key_sifted = [bob_key[i] for i in same_bases]

# Alice encrypts her message
encrypted_message = [bit ^ key for bit, key in zip(alice_key_sifted, alice_key_sifted)]
print('\n Encrypted message:', encrypted_message)

# Bob decrypts the message
decrypted_message = [bit ^ key for bit, key in zip(encrypted_message, bob_key_sifted)]
print('\n Decrypted message:', decrypted_message)

# Convert the decrypted message back to a string
decrypted_message_string = ''.join(chr(int(''.join(map(str, decrypted_message[i:i+8])), 2)) for i in range(0, len(decrypted_message), 8))
print('\n Decrypted message string:', decrypted_message_string)