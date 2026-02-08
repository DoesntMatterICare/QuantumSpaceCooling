# Quantum Space Cooling - Feasibility Simulator
# Author: Rehan
# Purpose: Calculate required radiator surface area for space-based quantum cooling.

import math

def calculate_radiator_size(heat_watts, target_temp_kelvin):
    # Constants
    STEFAN_BOLTZMANN = 5.67e-8  # Physical constant
    SPACE_TEMP = 2.7            # Temperature of deep space (Kelvin)
    EMISSIVITY = 0.9            # Efficiency of the black radiator material (0-1)

    # Physics Check: You can't cool below space temperature passively!
    if target_temp_kelvin <= SPACE_TEMP:
        return "IMPOSSIBLE (Target is colder than space itself)"

    # The Math: Rearranging Stefan-Boltzmann Law to find Area
    # Power = sigma * Area * epsilon * (T_rad^4 - T_space^4)
    # Area = Power / (sigma * epsilon * (T_rad^4 - T_space^4))
    
    delta_t_factor = (target_temp_kelvin**4) - (SPACE_TEMP**4)
    required_area = heat_watts / (STEFAN_BOLTZMANN * EMISSIVITY * delta_t_factor)

    return round(required_area, 4)

# --- SIMULATION ---
print("--- QUANTUM SPACE COOLING SIMULATOR ---")
print(f"Background Space Temp: 2.7 Kelvin")

# Scenario 1: Dumping heat from a Cryo-cooler (Hotter radiator)
heat_load = 100 # Watts (Typical cryo-cooler waste heat)
rad_temp = 300  # Kelvin (Room temp radiator)
area = calculate_radiator_size(heat_load, rad_temp)
print(f"\n[Scenario 1] Standard Radiator (300K):")
print(f"To dump {heat_load} Watts, you need: {area} m^2")

# Scenario 2: Direct Passive Cooling (Cold radiator)
heat_load = 0.1 # Watts (Tiny heat leak)
rad_temp = 4    # Kelvin (Liquid Helium temp)
area = calculate_radiator_size(heat_load, rad_temp)
print(f"\n[Scenario 2] Deep Cryogenic Radiator (4K):")
print(f"To dump {heat_load} Watts, you need: {area} m^2")
