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
        self.BMI_std = [
            {"male": [20, 25]},
            {"female": [19, 24]}
        ]

    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divided by the square of height, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.get_BMI()
        21.604938271604937
        """
        BMI = self.weight / (self.height ** 2)
        return BMI

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1
        """
        BMI = self.get_BMI()
        std_range = self.BMI_std[0][self.sex] if self.sex == "male" else self.BMI_std[1][self.sex]
        
        if BMI < std_range[0]:
            return -1  # Too thin
        elif BMI > std_range[1]:
            return 1  # Too fat
        else:
            return 0  # Normal

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        BMR is calculated based on the user's height, weight, age, and sex.
        - Male: BMR = 10 * weight + 6.25 * height - 5 * age + 5
        - Female: BMR = 10 * weight + 6.25 * height - 5 * age - 161
        The calorie intake is calculated based on the BMR and the user's condition:
        - If the user is too fat, the calorie intake is BMR * 1.2
        - If the user is too thin, the calorie intake is BMR * 1.6
        - If the user is normal, the calorie intake is BMR * 1.4
        :return: calorie intake, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.calculate_calorie_intake()
        986.0
        """
        if self.sex == "male":
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        else:
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161

        condition = self.condition_judge()
        
        if condition == 1:
            return BMR * 1.2
        elif condition == -1:
            return BMR * 1.6
        else:
            return BMR * 1.4