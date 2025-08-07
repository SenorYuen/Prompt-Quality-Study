class FitnessTracker:
    def __init__(self, height, weight, age, sex):
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.BMI_std = {
            "male": [20, 25],
            "female": [19, 24]
        }

    def get_BMI(self):
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        BMI = self.get_BMI()
        if self.sex not in self.BMI_std:
            return None
        lower, upper = self.BMI_std[self.sex]
        if BMI < lower:
            return -1
        elif BMI > upper:
            return 1
        else:
            return 0

    def calculate_calorie_intake(self):
        if self.sex == "male":
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        elif self.sex == "female":
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
        else:
            return None

        condition = self.condition_judge()
        if condition == 1:
            return BMR * 1.2
        elif condition == -1:
            return BMR * 1.6
        elif condition == 0:
            return BMR * 1.4
        else:
            return None