from sklearn.tree import DecisionTreeClassifier

class DecisionTreeAlgorithm:
    def __init__(self):
        self.model = DecisionTreeClassifier()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, data):
        return self.model.predict(data)