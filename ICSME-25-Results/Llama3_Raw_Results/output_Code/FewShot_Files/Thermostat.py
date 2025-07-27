class Thermostat:
    """
    The class manages temperature control, including setting and retrieving the target temperature, adjusting the mode, and simulating temperature operation.
    """

    def __init__(self, current_temperature, target_temperature, mode):
        """
        initialize instances of the Thermostat class, including the current temperature, target temperature, and operating mode.
        :param current_temperature: float
        :param target_temperature: float
        :param mode: str, the work mode
        """
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode

    def get_target_temperature(self):
        # Return the target temperature of the thermostat
        return self.target_temperature

    def set_target_temperature(self, temperature):
        # Set the target temperature of the thermostat
        self.target_temperature = temperature

    def get_mode(self):
        # Return the current operating mode of the thermostat
        return self.mode

    def set_mode(self, mode):
        # Set the operating mode of the thermostat
        if mode in ['heat', 'cool']:
            self.mode = mode
        else:
            raise ValueError("Invalid mode. Mode should be either 'heat' or 'cool'.")

    def auto_set_mode(self):
        # Automatically set the operating mode based on the current and target temperatures
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        # Check if there is a conflict between the operating mode and the temperature relationship
        if (self.mode == 'heat' and self.current_temperature >= self.target_temperature) or \
           (self.mode == 'cool' and self.current_temperature <= self.target_temperature):
            self.auto_set_mode()
            return False
        return True

    def simulate_operation(self):
        # Simulate the operation of the thermostat
        start_time = time.time()
        self.auto_set_mode()
        while abs(self.current_temperature - self.target_temperature) > 0.1:
            if self.mode == 'heat':
                self.current_temperature += 0.1
            else:
                self.current_temperature -= 0.1
            time.sleep(1)  # Simulate a 1-second delay
        end_time = time.time()
        return int(end_time - start_time)