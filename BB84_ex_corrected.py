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
print("Message in bits: ", string_list)


# Create a quantum circuit
qubits = cirq.LineQubit.range(len(string_list))
circuit = cirq.Circuit()

# Prepare the qubits
for i in range(len(string_list)):
    if string_list[i] == 1:
        circuit.append(cirq.X(qubits[i]))

print(circuit)

# Alice chooses a random basis to encode her bits
alice_bases = [choices([0, 1], k=1)[0] for _ in range(len(string_list))]
for i in range(len(string_list)):
    if alice_bases[i] == 1:
        circuit.append(cirq.H(qubits[i]))

print(circuit)

# Bob's part
bob_bases = [choices([0, 1], k=1)[0] for _ in range(len(string_list))]
print("Bob bases: ", bob_bases)

circuit.append(cirq.measure(*qubits, key='result'))
print(circuit)

simulator = cirq.Simulator()
results = simulator.run(circuit, repetitions=1)

# Get the measurement results
bob_results = list(map(int, results.measurements['result'][0]))
print(bob_results) 

# Alice and Bob discard the bits where they used different bases
key = [bob_results[i] for i in range(len(string_list)) if alice_bases[i] == bob_bases[i]]
print("Key after alice and bob discarded bits with different bases: ", key)

# Using One time Pad encryption, decryption phenomena and Pad the key with zeros until it's the same length as the string_list
key += [0] * (len(string_list) - len(key))

# Use the key to encrypt the message
encrypted_message = [string_list[i] ^ key[i] for i in range(len(string_list))]
print("Encrypted message: ", encrypted_message)

# Bob uses the same key to decrypt the message
decrypted_message = [encrypted_message[i] ^ key[i] for i in range(len(string_list))]
print("Decrypted Message: ", decrypted_message)

# Convert the decrypted message back to a string
decrypted_string = ''.join(map(str, decrypted_message))
print("Decrypted String: ", decrypted_string)
binary_chunks = [decrypted_string[i:i+8] for i in range(0, len(decrypted_string), 8)]
print("Binary chunks: ", binary_chunks)

ascii_string = ''.join([chr(int(chunk, 2)) for chunk in binary_chunks])

print("Decrypted message: ", ascii_string)

if message == ascii_string:
    print("The message has been successfully decrypted")
else:
    print("The message has not been successfully decrypted")

# Assuming alice_bases, bob_bases, and bob_results are defined as in your original code

# Find the bits where Alice and Bob used the same basis
same_basis_indices = [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]

# Extract those bits from Bob's results
same_basis_results = [bob_results[i] for i in same_basis_indices]

# Extract those bits from the original message
same_basis_message = [string_list[i] for i in same_basis_indices]

# Calculate the number of bits that are different
num_errors = sum([same_basis_results[i] != same_basis_message[i] for i in range(len(same_basis_results))])

# Calculate the QBER
qber = num_errors / len(same_basis_results)

print("Quantum Bit Error Rate: ", qber)

plt.figure(figsize=(10, 5))
plt.plot(encrypted_message, label='Encrypted message', color='red', linestyle='dashdot', marker='|', markersize=6)
plt.plot(decrypted_message, label='Decrypted message', color='blue', linestyle='dotted', marker='o', markersize=4)
plt.xlabel('Bit index')
plt.ylabel('Bit value')
plt.title("Encrypted and Decrypted Message Comparison in bits via indexing")
plt.legend(loc='upper right', shadow=True)
plt.show()
#bob_results = list(map(int, results.measurements['result'][0]))

# Alice and Bob discard the bits where they used different bases
#key = [bob_results[i] for i in range(len(string_list)) if alice_bases[i] == bob_bases[i]]


# Use the key to encrypt the message
#encrypted_message = [string_list[i] ^ key[i] for i in range(len(string_list))]

# Bob uses the same key to decrypt the message
#decrypted_message = [encrypted_message[i] ^ key[i] for i in range(len(string_list))]

# Convert the decrypted message back to a string
#decrypted_string = ''.join(map(str, decrypted_message))
#binary_chunks = [decrypted_string[i:i+8] for i in range(0, len(decrypted_string), 8)]
#ascii_string = ''.join([chr(int(chunk, 2)) for chunk in binary_chunks])

#print("Decrypted message: ", ascii_string)

#if message == ascii_string:
#    print("The message has been successfully decrypted")
#else:
#    print("The message has not been successfully decrypted")