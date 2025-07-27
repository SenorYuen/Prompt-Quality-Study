import time

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
        """
        Get the target temperature of an instance of the Thermostat class.
        :return self.target_temperature: float
        """
        return self.target_temperature

    def set_target_temperature(self, temperature):
        """
        Set the target temperature
        :param temperature: float, the target temperature
        """
        self.target_temperature = temperature

    def get_mode(self):
        """
        Get the current work mode
        :return mode: str, working mode. only ['heat', 'cool']
        """
        return self.mode

    def set_mode(self, mode):
        """
        Set the current work mode
        :param mode: str, working mode. only ['heat', 'cool']
        """
        if mode in ['heat', 'cool']:
            self.mode = mode

    def auto_set_mode(self):
        """
        Automatically set the operating mode by comparing with the current temperature and target temperature. 
        If the current temperature is lower than the target temperature, the operating mode is set to 'heat', 
        otherwise it is set to 'cool'.
        """
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        """
        Check if there is a conflict between the operating mode and the relationship between the current temperature 
        and the target temperature. If there is a conflict, the operating mode will be adjusted automatically.
        :return: True if mode isn't conflict with the relationship between the current temperature and the target temperature, or False otherwise.
        """
        if (self.current_temperature < self.target_temperature and self.mode != 'heat') or \
           (self.current_temperature >= self.target_temperature and self.mode != 'cool'):
            self.auto_set_mode()
            return False
        return True

    def simulate_operation(self):
        """
        Simulate the operation of Thermostat. It will automatically start the auto_set_mode method to set the operating mode,
        and then automatically adjust the current temperature according to the operating mode until the target temperature is reached.
        :return time: int, the time it took to complete the simulation.
        """
        self.auto_set_mode()
        start_time = time.time()

        while self.current_temperature != self.target_temperature:
            if self.mode == 'heat':
                self.current_temperature += 0.1  # Simulate heating
            elif self.mode == 'cool':
                self.current_temperature -= 0.1  # Simulate cooling

            # Ensure that the temperature does not overshoot
            if self.mode == 'heat' and self.current_temperature > self.target_temperature:
                self.current_temperature = self.target_temperature
            elif self.mode == 'cool' and self.current_temperature < self.target_temperature:
                self.current_temperature = self.target_temperature

            time.sleep(0.1)  # Simulate time delay for temperature change
        
        end_time = time.time()
        return int(end_time - start_time)