import tkinter as tk
from tkinter import ttk, messagebox
import time

class Transition:
    def __init__(self, fromstate, tostate, oldchar, newchar, direction):
        self.fromstate = fromstate
        self.tostate = tostate
        self.oldchar = oldchar
        self.newchar = newchar
        self.direction = direction

class TuringMachineGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Turing Machine - String Reversal")
        self.root.geometry("800x600")
        
        self.tape = []
        self.transitionTable = []
        self.tracker = 1
        self.current_state = 0
        
        self.setup_gui()
        
    def setup_gui(self):
        # Input Frame
        input_frame = ttk.Frame(self.root, padding="20")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(input_frame, text="Enter string (a's and b's only):").grid(row=0, column=0, padx=5)
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(input_frame, textvariable=self.input_var)
        self.input_entry.grid(row=0, column=1, padx=5)
        
        ttk.Button(input_frame, text="Start", command=self.start_simulation).grid(row=0, column=2, padx=5)
        ttk.Button(input_frame, text="Reset", command=self.reset).grid(row=0, column=3, padx=5)
        
        # Tape Display Frame
        self.tape_frame = ttk.Frame(self.root, padding="10")
        self.tape_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # State Display
        self.state_label = ttk.Label(self.root, text="Current State: q0")
        self.state_label.grid(row=2, column=0, pady=10)
        
        # Speed Control
        speed_frame = ttk.Frame(self.root, padding="10")
        speed_frame.grid(row=3, column=0)
        ttk.Label(speed_frame, text="Speed:").grid(row=0, column=0)
        self.speed_var = tk.DoubleVar(value=1.0)
        self.speed_scale = ttk.Scale(speed_frame, from_=0.1, to=2.0, orient=tk.HORIZONTAL, 
                                   variable=self.speed_var)
        self.speed_scale.grid(row=0, column=1)
        
    def create_tape_cells(self):
        for widget in self.tape_frame.winfo_children():
            widget.destroy()
            
        for i, symbol in enumerate(self.tape):
            cell = ttk.Label(self.tape_frame, text=symbol, width=3, 
                           relief="solid", padding=5)
            cell.grid(row=0, column=i, padx=2)
            if i == self.tracker:
                cell.configure(background='yellow')
                
    def validate_input(self):
        input_str = self.input_var.get()
        if not all(c in ['a', 'b'] for c in input_str):
            messagebox.showerror("Error", "Invalid input. Please use only 'a' and 'b' characters.")
            return False
        return True
        
    def start_simulation(self):
        if not self.validate_input():
            return
            
        self.tape = ['#'] + list(self.input_var.get()) + ['#']
        self.tracker = 1
        self.current_state = 0
        self.transitionTable = []
        self.create_tape_cells()
        self.root.after(100, self.run_simulation)
        
    def reset(self):
        self.input_var.set("")
        self.tape = []
        self.tracker = 1
        self.current_state = 0
        self.transitionTable = []
        for widget in self.tape_frame.winfo_children():
            widget.destroy()
        self.state_label.configure(text="Current State: q0")
        
    def add_transition(self, fromstate, tostate, direction, newchar, oldchar):
        self.transitionTable.append(Transition(fromstate, tostate, oldchar, newchar, direction))
        
    def run_simulation(self):
        if self.current_state == -1:
            messagebox.showinfo("Complete", "Simulation finished!")
            return
            
        delay = int(1000 / self.speed_var.get())  # Convert speed to milliseconds
        
        if self.current_state == 0:
            if self.tracker < len(self.tape) - 1 and self.tape[self.tracker] != '#':
                self.add_transition(self.current_state, self.current_state, 'R', 
                                  self.tape[self.tracker], self.tape[self.tracker])
                self.tracker += 1
            else:
                self.add_transition(self.current_state, self.current_state + 1, 'L', 
                                  self.tape[self.tracker], self.tape[self.tracker])
                self.tracker -= 1
                self.current_state = 1
                
        elif self.current_state == 1:
            while self.tape[self.tracker] == 'X':
                self.add_transition(self.current_state, self.current_state, 'L', 
                                  self.tape[self.tracker], self.tape[self.tracker])
                self.tracker -= 1
                
            if self.tape[self.tracker] == '#':
                self.add_transition(self.current_state, 4, 'R', 
                                  self.tape[self.tracker], self.tape[self.tracker])
                self.tracker += 1
                self.current_state = 5
            elif self.tape[self.tracker] == 'a':
                temp = self.tape[self.tracker]
                self.tape[self.tracker] = 'X'
                self.add_transition(self.current_state, self.current_state + 1, 'R', 'X', temp)
                self.tracker += 1
                self.current_state = 2
            elif self.tape[self.tracker] == 'b':
                temp = self.tape[self.tracker]
                self.tape[self.tracker] = 'X'
                self.add_transition(self.current_state, self.current_state + 3, 'R', 'X', temp)
                self.tracker += 1
                self.current_state = 4
                
        elif self.current_state == 2:
            if self.tape[self.tracker] != '#':
                self.add_transition(self.current_state, self.current_state, 'R', 
                                  self.tape[self.tracker], self.tape[self.tracker])
                self.tracker += 1
            else:
                self.tape[self.tracker] = 'a'
                self.tape.append('#')
                self.add_transition(self.current_state, self.current_state + 1, 'L', '#', 'a')
                self.tracker -= 1
                self.current_state = 3
                
        elif self.current_state == 3:
            if self.tape[self.tracker] != 'X':
                self.add_transition(self.current_state, self.current_state, 'L', 
                                  self.tape[self.tracker], self.tape[self.tracker])
                self.tracker -= 1
            else:
                self.add_transition(self.current_state, self.current_state, 'L', 
                                  self.tape[self.tracker], self.tape[self.tracker])
                self.tracker -= 1
                self.current_state = 1
                
        elif self.current_state == 4:
            if self.tape[self.tracker] != '#':
                self.add_transition(self.current_state, self.current_state, 'R', 
                                  self.tape[self.tracker], self.tape[self.tracker])
                self.tracker += 1
            else:
                self.tape[self.tracker] = 'b'
                self.tape.append('#')
                self.add_transition(self.current_state, self.current_state + 1, 'L', '#', 'b')
                self.tracker -= 1
                self.current_state = 3
                
        elif self.current_state == 5:
            self.current_state = -1
            
        self.state_label.configure(text=f"Current State: q{self.current_state}")
        self.create_tape_cells()
        
        if self.current_state != -1:
            self.root.after(delay, self.run_simulation)
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    tm_gui = TuringMachineGUI()
    tm_gui.run() 