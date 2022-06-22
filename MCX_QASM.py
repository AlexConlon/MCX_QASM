from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

def q_QASM(i=int):
    return """q[""" + str(i) + """]"""

def h_QASM(i=int):
    return """h """ + q_QASM(i) + """;"""

def t_QASM(i=int):
    return  """t """ + q_QASM(i) + """;"""

def tdg_QASM(i=int):
    return """tdg """ + q_QASM(i) + """;"""

def cx_QASM(i=int, j=int):
    return """cx """ + q_QASM(i) + """,""" + q_QASM(j) + """;"""

def toff_QASM(i=int, j=int, t=int):
    return """ccx """ +q_QASM(i) + """,""" + q_QASM(j) + """,""" + q_QASM(t) + """;"""

def toff_decomp(a=int,b=int,t=int):
    return \
        h_QASM(t) \
        + cx_QASM(b,t) \
        + tdg_QASM(t) \
        + cx_QASM(a,t) \
        + t_QASM(t) \
        + cx_QASM(b,t) \
        + t_QASM(b) \
        + tdg_QASM(t) \
        + cx_QASM(b,t) \
        + t_QASM(t) \
        + h_QASM(t) \
        + cx_QASM(a,b) \
        + t_QASM(a) \
        + tdg_QASM(b) \
        + cx_QASM(a,b)

## decomposed circuit
qasm_str = """OPENQASM 2.0;
   include "qelib1.inc";
   qreg q[20];
   """
# implement mcx([0,1,2,3,4,5],19)
qasm_str = qasm_str \
           + toff_decomp(0,1,15) \
           + toff_decomp(2,3,16) \
           + toff_decomp(4,5,17) \
           + toff_decomp(15,16,18) \
           + toff_decomp(17,18,19)
# reset work qubits 15,16,17,18
qasm_str = qasm_str \
           + toff_decomp(15,16,18) \
           + toff_decomp(4,5,17) \
           + toff_decomp(2,3,16) \
           + toff_decomp(0,1,15)


qc = QuantumCircuit.from_qasm_str(qasm_str)
qc.draw('mpl')

## high-level circuit uing ccx gates
hl_qasm_str = """OPENQASM 2.0;
   include "qelib1.inc";
   qreg q[20];
   """
# implement mcx([0,1,2,3,4,5],19)
hl_qasm_str = hl_qasm_str \
              + toff_QASM(0, 1, 15) \
              + toff_QASM(2, 3, 16) \
              + toff_QASM(4, 5, 17) \
              + toff_QASM(15, 16, 18) \
              + toff_QASM(17, 18, 19)
# reset work qubits 15,16,17,18
hl_qasm_str = hl_qasm_str \
           + toff_QASM(15, 16, 18) \
           + toff_QASM(4, 5, 17) \
           + toff_QASM(2, 3, 16) \
           + toff_QASM(0, 1, 15)
hl_qc = QuantumCircuit.from_qasm_str(hl_qasm_str)
hl_qc.draw('mpl')

plt.show()
exit()

# reset work qubits 15,16,17,18
toff_decomp(4,17,18)
toff_decomp(3,16,17,fd)
toff_decomp(2,15,16,fd)
toff_decomp(0,1,15,fd)

# implement mcx([6,7,8,9,10],18)
toff_decomp(6,7,15,fd)
toff_decomp(8,15,16,fd)
toff_decomp(9,16,17,fd)
toff_decomp(10,17,18,fd)
# reset work qubits 15,16,17
toff_decomp(9,16,17,fd)
toff_decomp(8,15,16,fd)
toff_decomp(6,7,15,fd)

# implement mcx([11,12,13,18,19],14)
toff_decomp(11,12,15,fd)
toff_decomp(13,15,16,fd)
toff_decomp(16,18,17,fd)
toff_decomp(17,19,14,fd)
# reset work qubits 15,16,17
toff_decomp(16,18,17,fd)
toff_decomp(13,15,16,fd)
toff_decomp(11,12,15,fd)

# reset work qubit 18
# implement mcx([6,7,8,9,10],18)
toff_decomp(6,7,15,fd)
toff_decomp(8,15,16,fd)
toff_decomp(9,16,17,fd)
toff_decomp(10,17,18,fd)
# reset work qubits 15,16,17
toff_decomp(9,16,17,fd)
toff_decomp(8,15,16,fd)
toff_decomp(6,7,15,fd)

# reset work qubit 19
# implement mcx([0,1,2,3,4,5],19)
toff_decomp(0,1,15,fd)
toff_decomp(2,15,16,fd)
toff_decomp(3,16,17,fd)
toff_decomp(4,17,18,fd)
toff_decomp(5,18,19,fd)
# reset work qubits 15,16,17,18
toff_decomp(4,17,18,fd)
toff_decomp(3,16,17,fd)
toff_decomp(2,15,16,fd)
toff_decomp(0,1,15,fd)

qc = QuantumCircuit.from_qasm_str(qasm_str)

qc.draw('mpl')
plt.show()