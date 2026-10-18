# Single-Qubit Circuit Labs

A collection of foundational quantum computing labs exploring single-qubit circuits through hands-on implementation and simulation using Python and Cirq.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments and Learning Process](#acknowledgments-and-learning-process)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This folder contains practical coding exercises exploring the fundamentals of single-qubit quantum circuits. The labs provide an opportunity to translate quantum computing concepts into Python code using Cirq, a Python framework for creating and simulating quantum circuits.

The exercises are part of an independent coding practice effort associated with Lab 3: Single Qubit Circuits from the _Foundations of Quantum Computing_ course, Fall 2026, offered through Frontier Technology Institute Qubit x Qubit Program and formally known as The Coding School.  
https://www.frontier-tech.org/

The goal is to develop a practical understanding of how quantum circuits are constructed, how gates affect qubits, how measurements produce classical outcomes, and how simulation results can be interpreted.

### Learning Objectives

- Understand the basic structure of a single-qubit quantum circuit.
- Represent qubits and quantum operations using Cirq.
- Apply quantum gates and explore their effects on qubit states.
- Add measurement operations and interpret classical results.
- Execute quantum circuit simulations and summarize outcomes.
- Strengthen Python programming skills through hands-on implementation.

## Features

- Organizes single-qubit quantum circuit exercises in one location.
- Uses Python and Cirq to construct and simulate quantum circuits.
- Explores quantum gates, measurements, and simulation results.
- Includes code comments to document concepts and implementation decisions.
- Supports incremental learning through independent coding and experimentation.

### Current Labs

- **Single-Qubit Circuit: X Gate** — Constructs and simulates a circuit with a Pauli-X gate, then measures the qubit over 1,000 repetitions.

- **Single-Qubit Circuit: H Gate** — Constructs and simulates a circuit with a Hadamard gate, then measures the qubit over 1,000 repetitions.

## Installation

### Prerequisites

- Python 3.12
- Cirq 1.7.0
- Visual Studio Code (or another Python-compatible editor)
- A Python virtual environment

### Set Up the Environment

The labs use the Python virtual environment configured for the `frontier-tech-institute-labs` project. Activate that environment and install Cirq if it is not already installed.

```bash
python -m pip install cirq
```

To verify the installed Cirq version:

```bash
python -c "import cirq; print(cirq.__version__)"
```

## Usage

1. Open the `single-qubit-circuit-labs` folder in Visual Studio Code as part of the parent project.
2. Ensure the selected Python interpreter points to the parent project's `.venv` environment.
3. Open the Python file for the lab you want to explore.
4. Run the script and review the circuit diagram and simulation output.
5. Review the code comments and experiment with the circuit to reinforce your understanding.

Each lab may have its own implementation details and expected results. Refer to the individual lab's README, when available, for specific instructions and explanations.

## Acknowledgments and Learning Process

### Educational Source

These exercises are informed by Lab 3: Single Qubit Circuits from the _Foundations of Quantum Computing_ course, Fall 2026, offered through Frontier Technology Institute / The Coding School.

**Instructor:**
[Kian Jansepar](https://www.linkedin.com/in/kian-jansepar-a2849a1b9/), Quantum Education Fellow at Frontier Technical Institute (The Coding School) and researcher in quantum technologies.

The original lesson and pre-made code provided the foundation for this exercise. This project extends that learning activity by independently recreating the circuit in Python using Cirq in VS Code.

This project is an independent learning exercise and is not an official course submission or an endorsement by Frontier Technology Institute or The Coding School.

### AI-Assisted Learning

AI was used as a learning guide and coding assistant to help explain quantum concepts, clarify Python and Cirq syntax, troubleshoot errors, and interpret simulation results.

The exercises are developed incrementally, with an emphasis on writing and understanding the code rather than simply copying completed solutions. The goal is to strengthen independent programming skills and build a deeper understanding of quantum computing.

## Contributing

This folder is part of a personal learning portfolio focused on quantum computing, Python, and emerging technologies.

Suggestions and corrections that support learning, code clarity, and technical accuracy are welcome.

## License

No license has been specified for this project yet. Unless a license is added, the repository's default copyright protections apply.
