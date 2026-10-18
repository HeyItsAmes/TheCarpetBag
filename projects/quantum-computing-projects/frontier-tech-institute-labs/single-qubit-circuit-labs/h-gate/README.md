# Single-Qubit Quantum Circuit: H Gate

A beginner-level quantum computing lab using Python and Cirq to construct, simulate, and analyze a single-qubit circuit containing a Hadamard (H) gate.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments and Learning Process](#acknowledgments-and-learning-process)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a self-directed coding lab developed as an independent extension of Lab 3: Single Qubit Circuits from the _Foundations of Quantum Computing_ course, Fall 2026, offered through Frontier Technology Institute's Qubit x Qubit Program, formerly known as The Coding School.
https://www.frontier-tech.org/

The original Lab 3 assignment was delivered through the Lovable platform and provided pre-made code for students to run. For this independent extension, I recreated the assignment from scratch in Python using Cirq and Visual Studio Code (VS Code), writing and reviewing the code line by line to develop a deeper understanding of quantum circuit construction and simulation.

The circuit starts with the simulator's default initial state of |0⟩, applies a Hadamard (H) gate to create an equal superposition of the computational basis states |0⟩ and |1⟩, and measures the resulting state.

The circuit is executed 1,000 times to observe the measurement outcomes and summarize them using a histogram.

This lab reinforces foundational quantum computing concepts while providing hands-on practice with Python variables, objects, method calls, keyword arguments, and output formatting.

### Quantum Concepts

- **Qubit:** The fundamental unit of quantum information.
- **Computational basis states:** The states |0⟩ and |1⟩ used to describe the measurement outcomes in this experiment.
- **Hadamard gate:** A quantum gate that transforms a computational-basis state into an equal superposition.
- **Superposition:** A quantum state that can produce different outcomes when measured.
- **Measurement:** Produces a classical outcome from a quantum measurement.
- **Repeated execution:** Runs the circuit multiple times to collect measurement outcomes.
- **Histogram:** Summarizes the frequency of each observed outcome.

## Features

- Creates a qubit using `cirq.LineQubit(0)`.
- Constructs a quantum circuit using `cirq.Circuit()`.
- Applies a Hadamard gate using `cirq.H(qubit)`.
- Measures the qubit using the measurement key `circuit_result`.
- Runs the circuit 1,000 times using Cirq's simulator.
- Displays a text-based circuit diagram in the terminal.
- Summarizes measurement outcomes using `histogram()`.

### Expected Circuit Diagram

```text
0: ───H───M('circuit_result')───
```

### Expected Measurement Results

The histogram should show a distribution approximately evenly split between 0 and 1. For example:

```text
Counter({0: 503, 1: 497})
```

These counts are illustrative, not fixed output. Actual results will vary between runs. When the Hadamard gate is applied to the initial |0⟩ state, the theoretical probability of measuring either 0 or 1 is 50%.

## Installation

### Prerequisites

- Python 3.12
- Visual Studio Code (or another Python-compatible editor)
- A Python virtual environment

### Set Up the Environment

Activate the project's existing virtual environment and install Cirq if it is not already installed in that environment.

```bash
python -m pip install cirq
```

To verify the installed version:

```bash
python -c "import cirq; print(cirq.__version__)"
```

This project was developed using Cirq 1.7.0.

## Usage

1. Open `single_qubit_circuit_h_gate.py` in your editor.
2. Ensure the selected Python interpreter points to the project's `.venv` environment.
3. Run the Python script.
4. Review the text-based circuit diagram displayed in the terminal.
5. Review the histogram to observe the measurement outcomes.

The circuit uses `repetitions=1000` to collect 1,000 measurement outcomes. The histogram provides a concise summary instead of printing every individual measurement.

## Acknowledgments and Learning Process

### Educational Source

This independent lab was guided by Lab 3: Single Qubit Circuits from the _Foundations of Quantum Computing_ course, Fall 2026, offered through Frontier Technology Institute / The Coding School.

**Instructor:**

[Kian Jansepar](https://www.linkedin.com/in/kian-jansepar-a2849a1b9/), Quantum Education Fellow at Frontier Technical Institute (The Coding School) and researcher in quantum technologies.

The original lesson and pre-made code provided the foundation for this exercise. This project extends that learning activity by independently recreating the circuit in Python using Cirq in VS Code.

This project is an independent learning exercise and is not an official course submission or an endorsement by Frontier Technology Institute or The Coding School.

### AI-Assisted Learning

AI was used as a learning guide and coding assistant throughout this exercise. Assistance included explaining quantum computing concepts, clarifying Python and Cirq syntax, providing incremental hints, troubleshooting errors, and reviewing the meaning of the circuit's output.

I wrote and developed the code myself, working through the implementation step by step. I used AI guidance to help me understand what I was writing, why the code worked, and how to interpret the results, rather than simply copying a completed solution.

The goal of this approach was to build independent coding skills and a deeper conceptual understanding of quantum circuit simulation.

## Contributing

This project is part of a personal learning portfolio focused on quantum computing, Python, and emerging technologies.

Suggestions and corrections that support learning, code clarity, and technical accuracy are welcome.

## License

No license has been specified for this project yet. Unless a license is added, the repository's default copyright protections apply.
