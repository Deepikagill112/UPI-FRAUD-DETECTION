# UPI-FRAUD-DETECTION
UPI Fraud Detection system uses a RandomForest model from scikit-learn. It trains on five features: amount, location, merchant type, previous frauds, and transaction hour. The model classifies transactions as safe (0) or fraud (1). After training, it is saved as model.pkl using pickle for real-time fraud prediction in a web app.
