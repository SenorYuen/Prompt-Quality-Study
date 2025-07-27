class MetricsCalculator:
    def __init__(self):
        # Initialize the number of all four samples to 0
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        # Update the number of all four samples
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                self.true_positives += 1  # Correctly predicted positive
            elif predicted == 1 and true == 0:
                self.false_positives += 1  # Incorrectly predicted positive
            elif predicted == 0 and true == 1:
                self.false_negatives += 1  # Missed positive
            else:
                self.true_negatives += 1  # Correctly predicted negative

    def precision(self):
        # Calculate precision: true positives / (true positives + false positives)
        if self.true_positives + self.false_positives == 0:
            return 0  # Avoid division by zero
        return self.true_positives / (self.true_positives + self.false_positives)

    def recall(self):
        # Calculate recall: true positives / (true positives + false negatives)
        if self.true_positives + self.false_negatives == 0:
            return 0  # Avoid division by zero
        return self.true_positives / (self.true_positives + self.false_negatives)

    def f1_score(self):
        # Calculate f1 score: harmonic mean of precision and recall
        precision_value = self.precision()
        recall_value = self.recall()
        if precision_value + recall_value == 0:
            return 0  # Avoid division by zero
        return 2 * precision_value * recall_value / (precision_value + recall_value)

    def accuracy(self):
        # Calculate accuracy: (true positives + true negatives) / total
        total = self.true_positives + self.false_positives + self.false_negatives + self.true_negatives
        if total == 0:
            return 0  # Avoid division by zero
        return (self.true_positives + self.true_negatives) / total