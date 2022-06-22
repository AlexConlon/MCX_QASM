# MCX_QASM
Decomposition of 14-qubit Toffoli gate
My circuit decomposes the 14-qubit-controlled Toffoli into 4 “smaller” multi-controlled Toffoli gates. The circuit uses 20 qubits where, qubits 0,...,13 are the 
controls, qubit 14 is the target, and qubits 15,...,19 are the auxiliaries.

The first step in my circuit implements the multi-controlled Toffoli gate controlled by qubits 0,1,2,3,4,5 with target qubit 19, denoted by mcx([0,1,2,3,4,5],19).

The second step implements mcx([6,7,8,9],18).

The third step is a partial implementation of mcx([10,11,12,13],17). It is only a partial implementation since qubit 15 is not reset, this avoids some 
redundancy in the subsequent steps, however, does not affect the depth of the circuit.

The fourth step implements mcx([17,18,19],14).

Finally, the fifth step runs steps 3, 2, and 1 backwards to reset all auxiliary qubits.
