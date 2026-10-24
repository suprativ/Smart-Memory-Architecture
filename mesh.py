"""
Smart Memory Architecture (SMA) Simulation
Models shortest-path energy routing across an active 1-bit NAND crossbar grid.
"""

import numpy as np
import time
import math

class SmartMemoryGrid1Bit:
    def __init__(self, is_starving=False):
        """
        Initializes the Smart Memory Substrate.
        :param is_starving: Boolean flag mapping the internal state override.
        """
        self.is_starving = is_starving
        
        # 1. Dedicated 1-bit NAND memory blocks (1 = Active/Ready, 0 = Idle)
        # Each node is physically mapped to spatial coordinates (X, Y) on a 10x10 crossbar
        self.nand_nodes = {
            "EAT IT":        {"bit": 1, "x": 1, "y": 1, "outcome": "Direct Energy Sustenance"},
            "MAKE JUICE":    {"bit": 1, "x": 2, "y": 1, "outcome": "Liquid State Transformation"},
            "PLANT SEEDS":   {"bit": 1, "x": 9, "y": 8, "outcome": "New Apple Tree Ecosystem Expansion"},
            "SELL IT":       {"bit": 1, "x": 8, "y": 9, "outcome": "External Currency Generation"},
            "EPOXY ANTIQUE": {"bit": 1, "x": 9, "y": 9, "outcome": "Preserved Aesthetic Sculpture"}
        }
        
        # 2. Sensor Input Origin Point (Where the sensory data hits the wire grid)
        self.input_x = 0
        self.input_y = 0
        
        # 3. Ambient Button Battery Power System
        self.ambient_battery_voltage = 5.0  # Constant baseline voltage tension
        self.results = {}

    def process_shortest_path_routing(self):
        """
        Calculates electrical current flow over the absolute shortest wire pathways.
        Applies physical conductance scaling and internal state overrides.
        """
        print("======================================================================")
        print(f"Executing Core SMA Substrate Analysis | Internal Starvation = {self.is_starving}")
        print("======================================================================")
        print("Sensory input 'APPLE ON GROUND' hit origin grid coordinates (0,0).")
        print("Current is tracking shortest-path interconnects to minimize energy loss...\n")
        
        for action, node in self.nand_nodes.items():
            # Calculate the absolute straight-line shortest path distance to the node
            # Formula: Geometric Hypotenuse on the crossbar matrix
            distance = math.sqrt((node["x"] - self.input_x)**2 + (node["y"] - self.input_y)**2)
            
            # Physical Law: Conductance is inversely proportional to distance (Longer wire = more energy loss)
            wire_conductance = 1.0 / distance
            
            # --- DYNAMIC HARDWARE OVERRIDE PATHWAYS ---
            # If the internal state shifts, the system changes physical wire resistance rules
            if self.is_starving:
                if action in ["EAT IT", "MAKE JUICE"]:
                    # Survival paths drop in resistance and become highly conductive
                    wire_conductance *= 4.0  
                else:
                    # Distant creative pathways lock up and block the current
                    wire_conductance *= 0.1  
            
            # Arriving voltage at the target 1-bit NAND gate
            arriving_voltage = self.ambient_battery_voltage * wire_conductance * node["bit"]
            
            # Clip voltage signals to realistic hardware limits (0.1V to 5.0V max)
            self.results[action] = np.clip(arriving_voltage, 0.1, 5.0)
            
            print(f" -> Path to NAND [{action:13}] | Grid Distance: {distance:4.2f} units | Signal: {self.results[action]:.2f}V")
            time.sleep(0.1)

    def evaluate_hardware_output(self):
        """
        Evaluates which 1-bit NAND node achieved the highest voltage profile.
        Outputs the system decision and the resulting transformation layer.
        """
        chosen_action = max(self.results, key=self.results.get)
        final_voltage = self.results[chosen_action]
        created_entity = self.nand_nodes[chosen_action]["outcome"]
        
        print("\n=======================================================")
        print("            SMART MEMORY SYSTEM HARDWARE OUTPUT        ")
        print("=======================================================")
        print(f"Input Source Component : SENSORY FEED TRIGGER")
        print(f"Selected Memory Gateway: 1-Bit NAND [{chosen_action}]")
        print(f"Peak Signal Voltage    : {final_voltage:.2f}V")
        print(f"Physical Action Route  : Shortest Path Energy Line")
        print(f"Target Outcome Shift   : {created_entity}")
        print("=======================================================\n")


if __name__ == "__main__":
    # Test Case 1: Evaluate grid decision when system is under starvation override
    active_chip = SmartMemoryGrid1Bit(is_starving=True)
    active_chip.process_shortest_path_routing()
    active_chip.evaluate_hardware_output()
