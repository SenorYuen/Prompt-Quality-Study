class FitnessTracker:
    """
    This is a class as fitness tracker that implements to calculate BMI (Body Mass Index) and calorie intake based on the user's height, weight, age, and sex.
    """

    def __init__(self, height, weight, age, sex) -> None:
        """
        Initialize the class with height, weight, age, and sex, and calculate the BMI standard based on sex, and male is 20-25, female is 19-24.
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.BMI_std = {
            "male": [20, 25],
            "female": [19, 24]
        }  # Simplified the BMI_std dictionary

    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divide by the square of height, float.
        """
        # Calculate BMI using the formula: BMI = weight / height^2
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        # Get the BMI standard for the user's sex
        bmi_std = self.BMI_std[self.sex]
        
        # Calculate the BMI
        bmi = self.get_BMI()
        
        # Judge the condition based on the BMI standard
        if bmi > bmi_std[1]:
            return 1  # Too fat
        elif bmi < bmi_std[0]:
            return -1  # Too thin
        else:
            return 0  # Normal

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        :return: calorie intake, float.
        """
        # Calculate BMR based on the user's sex
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        
        # Judge the condition
        condition = self.condition_judge()
        
        # Calculate calorie intake based on the condition
        if condition == 1:  # Too fat
            return bmr * 1.2
        elif condition == -1:  # Too thin
            return bmr * 1.6
        else:  # Normal
            return bmr * 1.4