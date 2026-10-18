# Frontier Technology Institute Labs

A collection of foundational quantum computing and programming projects developed alongside the _Foundations of Quantum Computing_ course, Fall 2026, offered through offered through Frontier Technology Institute Qubit x Qubit Program and formally known as The Coding School.  
https://www.frontier-tech.org/

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments and Learning Process](#acknowledgments-and-learning-process)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This folder contains independent coding exercises and projects associated with my study of quantum computing through the _Foundations of Quantum Computing_ course, Fall 2026, offered through Frontier Technology Institute.

The projects provide hands-on practice translating foundational quantum computing concepts into code, using Python and relevant quantum computing tools and libraries. They complement the course materials by allowing me to independently implement examples, explore how quantum circuits work, and build practical programming skills.

As I develop my knowledge of Python and quantum computing, this folder will serve as an organized record of my progress, experiments, and growing understanding of quantum technologies.

### Learning Objectives

- Develop a foundational understanding of quantum computing concepts.
- Apply Python programming skills to quantum computing exercises.
- Build and simulate quantum circuits using Cirq.
- Explore quantum gates, qubit measurements, and simulation outcomes.
- Practice independent implementation, debugging, and technical documentation.
- Establish a foundation for exploring more advanced quantum computing topics.

## Features

- Organizes independent coding exercises associated with quantum computing coursework.
- Uses Python and quantum computing libraries to explore foundational concepts.
- Includes documented implementations and simulation results.
- Emphasizes hands-on experimentation and understanding the underlying code.
- Tracks ongoing learning and project development.

## Project Structure

```text
frontier-tech-institute-labs/
│
├── README.md
│
└── single-qubit-circuit-labs/
    ├── README.md
    └── single_qubit_circuit_x_gate.py
```

_Note: This structure illustrates the current lab organization. Update it as additional folders or files are added._

### Project Folders

- **[single-qubit-circuit-labs](./single-qubit-circuit-labs/README.md)** — Foundational exercises exploring single-qubit quantum circuits using Python and Cirq, beginning with a Pauli-X gate circuit.

- **Single-Qubit Circuit: H Gate** — Constructs and simulates a circuit with a Hadamard gate, then measures the qubit over 1,000 repetitions.

## Installation

### Prerequisites

- Python 3.12
- Visual Studio Code (or another Python-compatible editor)
- Python virtual environment
- Cirq 1.7.0 for the current single-qubit circuit lab

### Set Up the Environment

This project uses a Python virtual environment named `.venv` configured within the `frontier-tech-institute-labs` folder.

Activate the existing environment and install Cirq if it is not already installed.

```bash
python -m pip install cirq
```

To verify the installed Cirq version:

```bash
python -c "import cirq; print(cirq.__version__)"
```

Additional dependencies may be required as new projects are added.

## Usage

1. Open the `frontier-tech-institute-labs` folder within your development workspace in Visual Studio Code.
2. Select the Python interpreter associated with the project's `.venv` environment.
3. Navigate to the relevant project folder.
4. Open and run the Python script for the exercise you want to explore.
5. Review the code comments, circuit diagrams, and simulation results.
6. Refer to each project's README for its specific concepts, instructions, and expected outcomes.

Projects are developed incrementally, with an emphasis on understanding the code and concepts rather than simply executing pre-written examples.

## Acknowledgments and Learning Process

### Educational Source

This project collection is associated with the _Foundations of Quantum Computing_ course, Fall 2026, offered through Frontier Technology Institute / The Coding School.

**Instructor:**
[Kian Jansepar](https://www.linkedin.com/in/kian-jansepar-a2849a1b9/), Quantum Education Fellow at Frontier Technical Institute (The Coding School) and researcher in quantum technologies.

The original lesson and pre-made code provided the foundation for this exercise. This project extends that learning activity by independently recreating the circuit in Python using Cirq in VS Code.

This project is an independent learning exercise and is not an official course submission or an endorsement by Frontier Technology Institute or The Coding School.

### AI-Assisted Learning

AI is used as a learning guide and coding assistant to help explain concepts, clarify Python and library syntax, provide incremental hints, troubleshoot errors, and interpret results.

The emphasis is on developing and understanding the code step by step, with AI assistance supporting the learning process rather than replacing independent implementation and problem-solving.

## Contributing

This folder is part of a personal learning portfolio focused on quantum computing, Python, and emerging technologies.

Suggestions and corrections that support learning, code clarity, and technical accuracy are welcome.

## License

No license has been specified for this project yet. Unless a license is added, the repository's default copyright protections apply.
