import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    with open(filename) as f:
        reader = csv.DictReader(f)
        evidence = []
        label = []
        for row in reader:
            e = []
            e.append(int(row["Administrative"]))
            e.append(float(row["Administrative_Duration"]))
            e.append(int(row["Informational"]))
            e.append(float(row["Informational_Duration"]))
            e.append(int(row["ProductRelated"]))
            e.append(float(row["ProductRelated_Duration"]))
            e.append(float(row["BounceRates"]))
            e.append(float(row["ExitRates"]))
            e.append(float(row["PageValues"]))
            e.append(float(row["SpecialDay"]))
            months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            for i in range(len(months)):
                if months[i] == row["Month"]:
                    e.append(i)
                    break
            e.append(int(row["OperatingSystems"]))
            e.append(int(row["Browser"]))
            e.append(int(row["Region"]))
            e.append(int(row["TrafficType"]))
            e.append(int(1 if row["VisitorType"] == "Returning_Visitor" else 0))
            e.append(int(1 if row["Weekend"] == "TRUE" else 0))
            evidence.append(e)
            label.append(int(1 if row["Revenue"] == "TRUE" else 0))
        
    tuple = (evidence, label)
    return tuple


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    trainer = KNeighborsClassifier(n_neighbors=1)
    trained = trainer.fit(evidence, labels)
    return trained


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    buys = 0
    leaves = 0
    predicted_buys = 0
    predicted_leaves = 0
    for prediction, label in zip(predictions, labels):
        if label == 0:
            buys += 1
        else:
            leaves += 1

        if prediction == label:
            if label == 0:
                predicted_buys += 1
            else:
                predicted_leaves += 1
    specificity = predicted_buys / buys
    sensitivity = predicted_leaves / leaves
    tuple = (sensitivity, specificity)
    return tuple 


if __name__ == "__main__":
    main()
