class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the number of all four samples to 0
        """
        # Initialize counters for true positives, false positives, false negatives, and true negatives
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0


    def update(self, predicted_labels, true_labels):
        """
        Update the number of all four samples(true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, change the number of corresponding samples
        """
        # Iterate over predicted and true labels
        for predicted, true in zip(predicted_labels, true_labels):
            # Check if the predicted label matches the true label
            if predicted == 1 and true == 1:
                # If both are 1, increment true positives
                self.true_positives += 1
            elif predicted == 1 and true == 0:
                # If predicted is 1 and true is 0, increment false positives
                self.false_positives += 1
            elif predicted == 0 and true == 1:
                # If predicted is 0 and true is 1, increment false negatives
                self.false_negatives += 1
            else:
                # If both are 0, increment true negatives
                self.true_negatives += 1


    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        # Update counters
        self.update(predicted_labels, true_labels)
        # Calculate precision as true positives / (true positives + false positives)
        if self.true_positives + self.false_positives == 0:
            return 0
        return self.true_positives / (self.true_positives + self.false_positives)


    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        # Update counters
        self.update(predicted_labels, true_labels)
        # Calculate recall as true positives / (true positives + false negatives)
        if self.true_positives + self.false_negatives == 0:
            return 0
        return self.true_positives / (self.true_positives + self.false_negatives)


    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        # Calculate precision and recall
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        # Calculate f1 score as 2 * (precision * recall) / (precision + recall)
        if precision + recall == 0:
            return 0
        return 2 * (precision * recall) / (precision + recall)


    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        # Update counters
        self.update(predicted_labels, true_labels)
        # Calculate accuracy as (true positives + true negatives) / total samples
        total_samples = self.true_positives + self.false_positives + self.false_negatives + self.true_negatives
        if total_samples == 0:
            return 0
        return (self.true_positives + self.true_negatives) / total_samples