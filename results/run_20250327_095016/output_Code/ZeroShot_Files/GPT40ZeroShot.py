class FitnessTracker:
    def __init__(self, height, weight, age, sex) -> None:
        """
        Initialize the class with height, weight, age, and sex, and calculate the BMI standard based on sex, and male is 20-25, female is 19-24.
        """
        self.height = height  # Height in meters
        self.weight = weight  # Weight in kilograms
        self.age = age  # Age in years
        self.sex = sex  # Sex as 'male' or 'female'

        # Set BMI standards based on sex
        if self.sex == 'male':
            self.bmi_standard = (20, 25)
        elif self.sex == 'female':
            self.bmi_standard = (19, 24)
        else:
            raise ValueError("Sex must be 'male' or 'female'")

    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divided by the square of height, float.
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        bmi = self.get_BMI()
        lower, upper = self.bmi_standard
        if bmi < lower:
            return -1  # Too thin
        elif bmi > upper:
            return 1  # Too fat
        else:
            return 0  # Normal

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        BMR is calculated based on the user's height, weight, age, and sex:
        - Male: BMR = 10 * weight + 6.25 * height - 5 * age + 5
        - Female: BMR = 10 * weight + 6.25 * height - 5 * age - 161
        The calorie intake is calculated based on the BMR and the user's condition:
        - If the user is too fat, the calorie intake is BMR * 1.2
        - If the user is too thin, the calorie intake is BMR * 1.6
        - If the user is normal, the calorie intake is BMR * 1.4
        :return: calorie intake, float.
        """
        if self.sex == 'male':
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161

        condition = self.condition_judge()
        if condition == 1:
            return bmr * 1.2
        elif condition == -1:
            return bmr * 1.6
        else:
            return bmr * 1.4