# What happens to memory requirements and simulation time as we increase the number of qubits on a classical computer?

import cirq
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw() # Hides the main blank window
messagebox.showinfo("Warning", "This experiment simulates quantum circuits on a classical computer using Cirq's state-vector simulator. As the number of qubits increases, the number of state-vector amplitudes grows exponentially, increasing memory requirements. Larger simulations may require substantial system resources. \nThis version tests 10, 15, 20, and 25 qubits. Future versions may include larger tests with additional safeguards.")

#cirq.Simulator() creates the state-vector simulator
simulator = cirq.Simulator()

#cirq.LineQubit creates qubits arranged in a line
#.range(number_of_qubits) creates the current test number of qubits
#iterate through a sequence of qubit values to test
#First iteration: number_of_qubits = 10
#Second iteration: number_of_qubits = 15
#Third iteration: number_of_qubits = 20
#Fourth iteration: number_of_qubits = 25

for number_of_qubits in [10, 15, 20, 25]:
    qubits = cirq.LineQubit.range(number_of_qubits)
    
    #build empty circuit and store the circuit for each test
    circuit = cirq.Circuit()
    
    #each qubit can be represented using 2 states 0 and 1
    #apply the Hadamard gate to each qubit being tested using for loop
    #each qubit enters an equal (simulated) superposition of those 2 states
    for single_qubit in qubits:
        circuit.append(cirq.H.on(single_qubit))
        
    #.simulate() function to simulate the circuit for each qubit test
    # #simulator.simulate(circuit) calculates the final state vector for memory scaling
    #cirq simulator - example: a system of 10 qubits req 2^10 possible states each with complex amplitudes to represent its full state vector
    simulation = simulator.simulate(circuit)
    
    #print number of qubits for each test
    print(f"Which qubits were run: {number_of_qubits}")
    #print the final state vector to find out how many amplitudes it contains
    print(f"{len(simulation.final_state_vector)} amplitudes")

