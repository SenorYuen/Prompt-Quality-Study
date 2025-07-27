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
                self.true_positives += 1
            elif predicted == 1 and true == 0:
                self.false_positives += 1
            elif predicted == 0 and true == 1:
                self.false_negatives += 1
            elif predicted == 0 and true == 0:
                self.true_negatives += 1

    def precision(self, predicted_labels, true_labels):
        # Calculate precision
        # Initialize the number of all four samples to 0
        tp = 0
        fp = 0
        fn = 0
        tn = 0
        # Update the number of all four samples
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                tp += 1
            elif predicted == 1 and true == 0:
                fp += 1
            elif predicted == 0 and true == 1:
                fn += 1
            elif predicted == 0 and true == 0:
                tn += 1
        # Calculate precision
        if tp + fp == 0:
            return 0.0
        else:
            return tp / (tp + fp)

    def recall(self, predicted_labels, true_labels):
        # Calculate recall
        # Initialize the number of all four samples to 0
        tp = 0
        fp = 0
        fn = 0
        tn = 0
        # Update the number of all four samples
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                tp += 1
            elif predicted == 1 and true == 0:
                fp += 1
            elif predicted == 0 and true == 1:
                fn += 1
            elif predicted == 0 and true == 0:
                tn += 1
        # Calculate recall
        if tp + fn == 0:
            return 0.0
        else:
            return tp / (tp + fn)

    def f1_score(self, predicted_labels, true_labels):
        # Calculate f1 score
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        # Calculate f1 score
        if precision + recall == 0:
            return 0.0
        else:
            return 2 * (precision * recall) / (precision + recall)

    def accuracy(self, predicted_labels, true_labels):
        # Calculate accuracy
        # Initialize the number of all four samples to 0
        tp = 0
        fp = 0
        fn = 0
        tn = 0
        # Update the number of all four samples
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                tp += 1
            elif predicted == 1 and true == 0:
                fp += 1
            elif predicted == 0 and true == 1:
                fn += 1
            elif predicted == 0 and true == 0:
                tn += 1
        # Calculate accuracy
        total = tp + fp + fn + tn
        if total == 0:
            return 0.0
        else:
            return (tp + tn) / total