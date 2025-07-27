import time

class Thermostat:
    def __init__(self, current_temperature, target_temperature, mode):
        # Initialize instances of the Thermostat class
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode

    def get_target_temperature(self):
        # Get the target temperature of an instance of the Thermostat class
        return self.target_temperature

    def set_target_temperature(self, temperature):
        # Set the target temperature
        self.target_temperature = temperature

    def get_mode(self):
        # Get the current work mode
        return self.mode

    def set_mode(self, mode):
        # Set the current work mode
        if mode in ['heat', 'cool']:
            self.mode = mode
        else:
            raise ValueError("Invalid mode. Mode should be either 'heat' or 'cool'.")

    def auto_set_mode(self):
        # Automatically set the operating mode by comparing with the current temperature and target temperature
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        # Check if there is a conflict between the operating mode and the relationship between the current temperature and the target temperature
        if (self.mode == 'heat' and self.current_temperature >= self.target_temperature) or (self.mode == 'cool' and self.current_temperature <= self.target_temperature):
            return False
        else:
            return True

    def simulate_operation(self):
        # Simulate the operation of Thermostat
        start_time = time.time()
        self.auto_set_mode()
        while self.current_temperature != self.target_temperature:
            if self.mode == 'heat':
                self.current_temperature += 1
            else:
                self.current_temperature -= 1
            # Check for conflict and adjust mode if necessary
            if not self.auto_check_conflict():
                self.auto_set_mode()
            # Simulate time passing
            time.sleep(0.1)
        end_time = time.time()
        return end_time - start_time


# Example usage:
thermostat = Thermostat(20, 25, 'heat')
print(thermostat.get_mode())  # Output: heat
print(thermostat.get_target_temperature())  # Output: 25
thermostat.set_target_temperature(28)
print(thermostat.get_target_temperature())  # Output: 28
print(thermostat.auto_check_conflict())  # Output: True
print(thermostat.simulate_operation())  # Output: time it took to complete the simulation