# train_model.py
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# Sample data (5 features)
np.random.seed(0)
X = np.random.rand(1000,5) * 10  # features: amount, location, merchant_type, previous_frauds, hour
y = np.random.randint(0,2,1000)  # target: 0 = safe, 1 = fraud

# Train RandomForest model
model = RandomForestClassifier()
model.fit(X, y)

# Save as model.pkl in the same folder as app.py
pickle.dump(model, open('model.pkl', 'wb'))


print(" model.pkl created successfully")
