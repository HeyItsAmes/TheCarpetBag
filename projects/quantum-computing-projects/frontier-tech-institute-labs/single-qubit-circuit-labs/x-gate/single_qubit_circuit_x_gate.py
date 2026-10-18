##Code a single-qubit circuit with one X gate using Cirq.

#An X gate is the quantum equivalent of a NOT gate for a computational-basis qubit: it flips 0 to 1 and 1 to 0
#import the cirq library
import cirq

# create a qubit. 
  
# Cirq class "LineQubit" represents a qubit positioned on a one-dimensional line (horizontal circuit wire)
# cirq.LineQubit(0) creates a qubit identified by the index 0
#(0) position of a qubit (it does not mean the qubit is in the quantum state)
#syntax is variable_name = library.class(position)
#stores a qubit object in a variable
#this is not initializing the qubit
#Cirq simulator starts in the computational basis 0, by default when simulating a circuit, unless a different initial state is specified. 
qubit = cirq.LineQubit(0)

#create the quantum circuit
#Circuit represents a quantum circuit that can contain operations.
circuit = cirq.Circuit()

#apply an X gate for the operation to flip the qubit from |0> to |1>
#cirq.X is how Cirq represents the X gate
#circuit.append(...) adds that operation to the circuit.
#.on(qubit) creates an operation that applies the X gate to your qubit.

circuit.append(cirq.X.on(qubit))

#apply a measurement operation to the circuit which will produce a classical outcome (1 or 0 state)
#cirq.measure() Cirq function for measurement operation
#key='' is a label for the measurement (circuit_result)
circuit.append(cirq.measure(qubit, key='circuit_result'))

#create a quantum simulator to execute circuit
simulator = cirq.Simulator()

#tell simulator to execute circuit 1,000 times and store result
circuit_output = simulator.run(circuit, repetitions=1000)

#Display ASCII based text diagram of output
print("Circuit diagram:\n", circuit)

#The measurement returns the classical bit 1 which is the expected result for an ideal simulation of this circuit
# print(circuit_output)

#Instead of the print(circuit_output) - a Histogram() will return a count of how many times each measurement outcome occured as a summary in the terminal instead of 1000 indiv measurements

#Histogram() will display the count of each measurement outcome instead of all 1,000 individual results
print("Histogram:\n", circuit_output.histogram(key='circuit_result'))

## How to read teh ASCII based Cirq text diagram of the output:
# 0: ───X───M('circuit_result')───
# #
# 0: identifies your qubit, LineQubit(0).
# X is the Pauli-X gate that flips the qubit from \(|0\rangle\) to \(|1\rangle\).
# M('result') is the measurement operation, with 'result' as its measurement key.
# The horizontal line represents the qubit's path through the circuit, from left to right as operations are applied.

