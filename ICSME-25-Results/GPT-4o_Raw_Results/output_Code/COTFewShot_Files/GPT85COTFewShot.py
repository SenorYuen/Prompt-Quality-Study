import time

class Thermostat:
    def __init__(self, current_temperature, target_temperature, mode):
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode

    def get_target_temperature(self):
        return self.target_temperature

    def set_target_temperature(self, temperature):
        self.target_temperature = temperature

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        if mode in ['heat', 'cool']:
            self.mode = mode

    def auto_set_mode(self):
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        if (self.mode == 'heat' and self.current_temperature >= self.target_temperature) or \
           (self.mode == 'cool' and self.current_temperature <= self.target_temperature):
            self.auto_set_mode()
            return False
        return True

    def simulate_operation(self):
        self.auto_set_mode()
        time_elapsed = 0
        while not self.auto_check_conflict():
            if self.mode == 'heat':
                self.current_temperature += 1
            elif self.mode == 'cool':
                self.current_temperature -= 1
            time.sleep(1)
            time_elapsed += 1
        return time_elapsed