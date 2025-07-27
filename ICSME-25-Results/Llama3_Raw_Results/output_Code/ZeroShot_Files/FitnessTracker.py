class FitnessTracker:
    def __init__(self, height, weight, age, sex) -> None:
        """
        Initialize the class with height, weight, age, and sex, and calculate the BMI standard based on sex, and male is 20-25, female is 19-24.
        """
        # Initialize the attributes
        self.height = height  # height in cm
        self.weight = weight  # weight in kg
        self.age = age
        self.sex = sex.lower()  # convert sex to lowercase
        
        # Define the BMI standard based on sex
        if self.sex == 'male':
            self.bmi_standard = (20, 25)
        elif self.sex == 'female':
            self.bmi_standard = (19, 24)
        else:
            raise ValueError("Invalid sex. Please enter 'male' or 'female'.")

    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divide by the square of height, float.
        """
        # Calculate the BMI
        bmi = self.weight / ((self.height / 100) ** 2)
        return bmi

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        # Get the BMI
        bmi = self.get_BMI()
        
        # Judge the condition based on the BMI standard
        if bmi > self.bmi_standard[1]:
            return 1  # too fat
        elif bmi < self.bmi_standard[0]:
            return -1  # too thin
        else:
            return 0  # normal

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate), 
        BMR is calculated based on the user's height, weight, age, and sex, 
        male is 10 * self.weight + 6.25 * self.height - 5 * self.age + 5, 
        female is 10 * self.weight + 6.25 * self.height - 5 * self.age - 161, 
        and the calorie intake is calculated based on the BMR and the user's condition, 
        if the user is too fat, the calorie intake is BMR * 1.2, 
        if the user is too thin, the calorie intake is BMR * 1.6, 
        if the user is normal, the calorie intake is BMR * 1.4.
        :return: calorie intake, float.
        """
        # Calculate the BMR based on sex
        if self.sex == 'male':
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.sex == 'female':
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        
        # Judge the condition
        condition = self.condition_judge()
        
        # Calculate the calorie intake based on the condition
        if condition == 1:  # too fat
            calorie_intake = bmr * 1.2
        elif condition == -1:  # too thin
            calorie_intake = bmr * 1.6
        else:  # normal
            calorie_intake = bmr * 1.4
        
        return calorie_intake

# Example usage
tracker = FitnessTracker(170, 60, 25, 'male')
print("BMI:", tracker.get_BMI())
print("Condition:", tracker.condition_judge())
print("Calorie intake:", tracker.calculate_calorie_intake())