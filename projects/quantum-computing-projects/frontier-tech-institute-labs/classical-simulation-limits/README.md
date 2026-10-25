# Classical Simulation Limits: Qubit Scaling Experiment

A Python experiment using Google Cirq to explore how the memory requirements of classical quantum-circuit simulation grow as the number of qubits increases.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project explores the resource requirements of simulating quantum circuits on a classical computer.

Using Cirq's state-vector simulator, the program creates quantum circuits with increasing numbers of qubits and applies a Hadamard gate to each qubit. It then simulates each circuit and reports the number of amplitudes in the resulting state vector.

The experiment demonstrates how the size of a state-vector representation grows exponentially with the number of qubits, illustrating one of the challenges of classical quantum simulation.

## Features

- **Progressive qubit scaling:** Tests circuits containing 10, 15, 20, and 25 qubits.
- **Quantum circuit construction:** Uses Cirq to create qubits and apply Hadamard gates.
- **State-vector simulation:** Simulates each circuit on a classical computer.
- **Amplitude counting:** Reports the number of state-vector amplitudes for each test.
- **Resource awareness:** Provides a starting point for investigating how increasing circuit size affects classical computing resources.

## Project Structure

frontier-tech-institute-labs/
│
└── classical-simulation-limits/
├── README.md
└── qubit_scaling_experiment.py

## Project Folders

- Classical Simulation Limits — Explores how the memory requirements of classical quantum-circuit simulation grow as the number of qubits increases, using Python and Cirq.

- Qubit Scaling Experiment — Builds and simulates quantum circuits containing 10, 15, 20, and 25 qubits. Applies a Hadamard gate to each qubit and reports the number of amplitudes in the resulting state vector to demonstrate exponential growth as qubit count increases.

## Installation

### Prerequisites

- Python 3.12 or a compatible Python version
- Cirq

Install Cirq using pip:

```bash
python -m pip install cirq
```

### Clone the Repository

```bash
git clone https://github.com/HeyItsAmes/TheCarpetBag.git
```

Navigate to the project directory:

```bash
cd TheCarpetBag/projects/quantum-computing-projects/frontier-tech-institute-labs/classical-simulation-limits
```

## Usage

Run the experiment from the project directory:

```bash
python qubit_scaling_experiment.py
```

The program simulates circuits with 10, 15, 20, and 25 qubits and prints the number of amplitudes in each resulting state vector.

Example output:

```text
Which qubits were run: 10
1024 amplitudes
Which qubits were run: 15
32768 amplitudes
Which qubits were run: 20
1048576 amplitudes
Which qubits were run: 25
33554432 amplitudes
```

The number of amplitudes doubles with each additional qubit. This experiment focuses on state-vector size; it does not yet measure actual execution time or system memory usage.

**Note:** Larger simulations can require substantial memory and computing resources. Available resources vary by computer.

## Acknowledgments and Learning Process

### Educational Source

This project collection is associated with the _Foundations of Quantum Computing_ course, Fall 2026, offered through Frontier Technology Institute / The Coding School.

**Instructor:**
[Kian Jansepar](https://www.linkedin.com/in/kian-jansepar-a2849a1b9/), Quantum Education Fellow at Frontier Technical Institute (The Coding School) and researcher in quantum technologies.

This project extends a learning lab originally assigned to the class by independently recreating the circuit in Python using Cirq in VS Code.

This project is an independent learning exercise and is not an official course submission or an endorsement by Frontier Technology Institute or The Coding School.

### AI-Assisted Learning

AI is used as a learning guide and coding assistant to help explain concepts, clarify Python and library syntax, provide incremental hints, troubleshoot errors, and interpret results.

The emphasis is on developing and understanding the code step by step, with AI assistance supporting the learning process rather than replacing independent implementation and problem-solving.

## Contributing

This folder is part of a personal learning portfolio focused on quantum computing, Python, and emerging technologies.

Suggestions and corrections that support learning, code clarity, and technical accuracy are welcome.

## License

No license has been specified for this project yet. Unless a license is added, the repository's default copyright protections apply.
