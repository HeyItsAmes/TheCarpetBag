#What to expect from a Hadamard Gate: H	\(|0\rangle\)	Approximately 50% 0, 50% 1. The H gate creates an equal superposition when applied to \(|0\rangle\). That means a measurement has equal theoretical probabilities of returning 0 or 1.

#import Cirq library
import cirq

#create a qubit with its position
#Cirq's simulator uses the |0⟩ state by default for this circuit
qubit = cirq.LineQubit(0)

#create a circuit
circuit = cirq.Circuit()

#apply an H gate operation on qubit and add that operation to the circuit
#Before measurement, the qubit is in a quantum state that gives equal probabilities for measuring 0 or 1
#Superposition is a quantum state
circuit.append(cirq.H(qubit))

# create a measurement operation on the qubit, add it to the circuit, and label the result
#measurement produces an outcome of 0 or 1
circuit.append(cirq.measure(qubit, key='circuit_result'))

#create a simulator to run the quantum circuit
simulator = cirq.Simulator()

#tell simulator to execute circuit 1,000 times and store result
#repeating the experiment produces an approx 50/50 distribution
circuit_output = simulator.run(circuit, repetitions=1000)

#Display ASCII based text diagram of output
print("Circuit diagram:\n", circuit)

#H gate should produce approximately 50% zeros and 50% ones when measuring the initial \(|0\rangle\) state
#print(circuit_output)

#Histogram() will display the count of each measurement outcome instead of all 1,000 individual results
print("Histogram:\n", circuit_output.histogram(key='circuit_result'))

