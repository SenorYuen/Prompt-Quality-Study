import time

class Thermostat:
    def __init__(self, current_temperature, target_temperature, mode):
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode

    def get_target_temperature(self):
        return int(self.target_temperature)

    def set_target_temperature(self, temperature):
        self.target_temperature = temperature

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        if mode in ['heat', 'cool']:
            self.mode = mode
        else:
            raise ValueError("Invalid mode. Mode should be 'heat' or 'cool'.")

    def auto_set_mode(self):
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        if self.mode == 'heat' and self.current_temperature >= self.target_temperature:
            self.mode = 'cool'
            return False
        elif self.mode == 'cool' and self.current_temperature <= self.target_temperature:
            self.mode = 'heat'
            return False
        return True

    def simulate_operation(self):
        start_time = time.time()
        self.auto_set_mode()
        while self.current_temperature != self.target_temperature:
            if self.mode == 'heat':
                self.current_temperature += 0.1
            else:
                self.current_temperature -= 0.1
            time.sleep(0.1)
            self.auto_check_conflict()
        end_time = time.time()
        return int(end_time - start_time)