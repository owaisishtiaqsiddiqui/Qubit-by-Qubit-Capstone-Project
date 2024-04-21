**Qubit x Qubit Capstone Project**
All the important files can be located here Github Directory path to file [Qubit by-Qubit-Capstone-Project/BB84_ex_corrected.py](https://github.com/owaisishtiaqsiddiqui/Qubit-by-Qubit-Capstone-Project/Qubit-by-Qubit-Capstone-Project/BB84_ex_corrected.py)
# :space_invader: Encryption in Python

- [Personal Introduction](#Personal-introduction)
- [Problem Statement](#ProblemStatement)
  - [Description](#description)
- [Acknowledgement](#Acknowledgement)
- [References](#references)

## Personal Introduction
**Name:** Owais Ishtiaq Siddiqui 

**Project Name:** Qubit x Qubit Capstone Project
|   **Member Names**| **Owais Ishtiaq Siddiqui** |
|----------------|-------------------------------|
| **Discord ID** | Owais Ishtiaq Siddiqui#4549  |
| **GitHub ID**  | owaisishtiaqsiddiqui       |

----------------------


## Problem Statement
Implement any encryption protocol in python using python libraries.

## Description 
The Project describes the implementation the BB84 quantum key distribution protocol using the Cirq library. The BB84 protocol is a method for two parties, Alice and Bob, to create a shared secret key that they can use for secure communication.

The first protocol for quantum key distribution was introduced by H. Bennet and Gilles Brassard in 1984 and named BB84 \citeref{1, 2}. It was based on the Heisenberg Uncertainty Principle (HUP) and all protocols based on this principle are variants of the BB84 idea, where the basic concept for such protocols is that Alice can transmit a random secret key to Bob by sending a string of photons where the secret key bits are encoded in the polarization of the photons. The uncertainty principle verifies that an eavesdropper can't measure the photon's state and transmit it to Bob without disturbing the system thus indicating the eavesdropper's presence. The No-cloning theorem makes sure that eave cannot make a replica of a particle of an unknown state. BB84 has two phases, in the first phase Alice will communicate with Bob over the quantum channel. Alice begins by choosing random strings while Bob will notify over any insecure channel what bases he used to measure each photon.

The major drawback of quantum key distribution is that it usually relies on authentic classical communication channels. Unlike QKD, which is a family of method-based physical principles, Classical communication enables two peers to build a common secret key through a dialogue taking place on public channels. In modern cryptography, having an authenticated channel means exchanging a symmetric key of appropriate length or public keys of sufficient security level \citeref{3}. Classical cryptography has two branches: secret or symmetric cryptography and public key cryptography, also known as asymmetric cryptography. Secret key cryptography represents the most traditional form of cryptography in which two parties encrypt and decrypt their messages using the same shared secret key. While some secret key schemes like one-time pads are perfectly secure against an attacker with arbitrary computational power, their practical disadvantage is that the key distribution is based on public key cryptography before they share their secret key.
There are two channels:
*	`Quantum Channel` – a communication channel with properties controlled at a physical level. It is usually an optical fiber or an atmospheric link with a direct line of sight, on this channel for QKD to work, optical losses and noise cannot be too high, but more importantly, there must be no device interacting with the information exchanged.
*	A regular digital network link, which carries QKD signaling.

**Quantum Transmission**:
Quantum Transmission involves encoding information in quantum states or qubits, compared to classical transmission. Usually, photons are utilized for these quantum states. QKD exploits certain properties of quantum states to ensure security. There are several different protocols for quantum key distribution, but they can be divided into two main categories,
1.	Prepare and Measure protocols,
2.	Entanglement based protocols.

**Prepare and Measure protocols**:
Their prime focus is on measuring the quantum states that can detect eavesdropping as much as how much data or information is intercepted.
**Entanglement based protocols**:
They focus on quantum states where two objects are linked together, forming a combined quantum state. In entanglement-based protocols, if an entangled pair of objects is shared between two parties and anyone tries to intercept either object can disturb the entire system revealing the presence of a third party and the amount of information they gained.
These protocols are further divided into families of protocols,
*	Discrete Variable protocols e.g., BB84, EK91,
*	Continuous Variable protocols.

### Discrete variable protocols:
Discrete variable protocols were invented first and remain the most widely implemented. The other families of protocols focused on overcoming the practical limitations of experiments. Information is encoded in photon polarization states or weak coherent pulses phase simulating true single states of a photon, such implementation requires single photon detection techniques. Protocols like BB84 is one example.

1. `Alice's Part`: Alice starts by taking a message as input from the user. This message is then converted into a binary string, where each character is represented by its 8-bit ASCII value.

2. `Quantum Circuit Preparation`: A quantum circuit is created with as many qubits as there are bits in the message. If a bit in the message is 1, an X gate (which flips the state of a qubit from |0⟩ to |1⟩) is applied to the corresponding qubit.

3. `Alice's Bases`: Alice randomly chooses a basis (either 0 or 1) for each qubit. If the chosen basis is 1, a Hadamard gate (which puts a qubit into a superposition of states) is applied to the corresponding qubit.

4. `Bob's Part`: Bob also randomly chooses a basis for each qubit. The qubits are then measured, collapsing their superposition of states into a definite state of either 0 or 1.

5. `Key Extraction`: Alice and Bob discard the bits where they used different bases, leaving them with a shared secret key.

6. `One-Time Pad Encryption`: The key is padded with zeros until it's the same length as the original message. The message is then encrypted by taking the XOR of the message and the key.

7. `Decryption`: Bob uses the same key to decrypt the message by taking the XOR of the encrypted message and the key.

8. `Conversion to ASCII`: The decrypted message is converted back into a string by interpreting each 8-bit chunk as an ASCII character.

9. `Verification`: The decrypted message is compared with the original message to verify that the decryption was successful.

10. `Quantum Bit Error Rate` (QBER): The QBER is calculated as the number of bits that are different between Bob's results and the original message, divided by the total number of bits.

11. `Visualization`: A plot is created to compare the encrypted and decrypted messages. The x-axis represents the bit index, and the y-axis represents the bit value. The encrypted message is shown in red, and the decrypted message is shown in blue.

[This](https://github.com/owaisishtiaqsiddiqui/Qubit-by-Qubit-Capstone-Project/Qubit by Qubit Capstone Project/BB84_ex_corrected.py) script demonstrates the use of quantum mechanics for secure communication. The BB84 protocol ensures that any attempt by an eavesdropper to intercept the key will be detected, as it will introduce errors that can be detected when Alice and Bob compare their bases.




## Acknowledgement 
This work is done as a project for the Qubit by Qubit. I
Team members would like to thank the organizers and Mentors for teaching the state of the art of quantum key distribution and quantum networking.

## References
1. C. H. Bennett, and G. Brassard, "Quantum Cryptography: Public Key Distribution and Coin Tossing," 1984. 
2. C. H. Bennett, and G. Brassard, "Quantum cryptography: public key distribution and coin tossing," Theoret. Comput. Sci., vol. 56, pp. 7-11, 2014.
3. Slavisa Aleksic, Florian Hipp, Dominic Winkler, Andreas Poppe, Bernhard Schrenk, and Gerald Franzl, "Perspectives and limitations of QKD integration in metropolitan area networks," Opt. Express, vol. 23, pp. 10359-10373, 2015. 
