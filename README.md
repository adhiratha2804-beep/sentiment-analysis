# sentiment-analysis
📌 Project Overview

The goal of this project is to:

Preprocess raw text data

Convert text into numerical features using TF-IDF

Train a Logistic Regression classifier

Evaluate the model using standard classification metrics

Visualize results with a confusion matrix

📂 Dataset

The dataset is loaded from a CSV file named data.csv

The CSV file must contain the following columns:

text → raw text data

label → sentiment label (e.g., 0 = Negative, 1 = Positive)

Example:

text	label
I love this movie	1
This is terrible	0
⚙️ Libraries Used

pandas – data handling

nltk – stopword removal

re – text cleaning with regular expressions

scikit-learn – ML models and evaluation

matplotlib & seaborn – data visualization
