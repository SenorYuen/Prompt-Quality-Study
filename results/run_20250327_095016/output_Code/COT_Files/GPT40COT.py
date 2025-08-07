class FitnessTracker:
    def __init__(self, height, weight, age, sex) -> None:
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
        if self.sex in self.BMI_std:
            std_range = self.BMI_std[self.sex]
            if BMI < std_range[0]:
                return -1
            elif BMI > std_range[1]:
                return 1
            else:
                return 0
        else:
            raise ValueError("Invalid sex provided")

    def calculate_calorie_intake(self):
        if self.sex == "male":
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        elif self.sex == "female":
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
        else:
            raise ValueError("Invalid sex provided")

        condition = self.condition_judge()
        if condition == 1:
            return BMR * 1.2
        elif condition == -1:
            return BMR * 1.6
        else:
            return BMR * 1.4