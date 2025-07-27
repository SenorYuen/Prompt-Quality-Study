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
        self.BMI = self.get_BMI()

    def get_BMI(self):
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        if self.sex == "male":
            if self.BMI < self.BMI_std["male"][0]:
                return -1
            elif self.BMI > self.BMI_std["male"][1]:
                return 1
            else:
                return 0
        elif self.sex == "female":
            if self.BMI < self.BMI_std["female"][0]:
                return -1
            elif self.BMI > self.BMI_std["female"][1]:
                return 1
            else:
                return 0

    def calculate_calorie_intake(self):
        if self.sex == "male":
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.sex == "female":
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        condition = self.condition_judge()
        if condition == 1:
            return BMR * 1.2
        elif condition == -1:
            return BMR * 1.6
        else:
            return BMR * 1.4