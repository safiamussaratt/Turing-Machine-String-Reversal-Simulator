# Turing Machine String Reversal Simulator

A visual Turing Machine simulator built with Python Tkinter that demonstrates string reversal for strings consisting of 'a' and 'b' characters.

### How It Works

The Turing Machine uses a multi-state algorithm to reverse the input string:

1. **Phase 1 (State 0)** - Moves right to find end of input
2. **Phase 2 (State 1)** - Finds and marks characters to move
3. **Phase 3 (States 2-4)** - Transports characters to output position
4. **Phase 4 (State 5)** - Completion

The machine uses 'X' as a marker for processed characters and appends reversed characters to the right side.

## Features

- **Visual Tape Display** - Shows current tape contents with highlighted head position
- **Step-by-Step Simulation** - Watch each transition in real-time
- **Adjustable Speed** - Control simulation speed with a slider
- **Input Validation** - Only accepts 'a' and 'b' characters
- **Reset Functionality** - Clear and start over
- **State Display** - Shows current machine state (q0-q5)

## Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/safiamussaratt/Turing-Machine-String-Reversal-Simulatorl.git
cd Turing-Machine-String-Reversal-Simulator
```

2. Run the application:
```bash
python turing_machine.py
```

## Usage Guide
- Enter Input: Type a string containing only 'a' and 'b' characters (e.g., "aabb", "abba", "aaa")
- Start: Click "Start" to begin the simulation
- Adjust Speed: Use the slider to control animation speed (0.1x to 2.0x)
- Reset: Click "Reset" to clear and start over
