# Sentiment-Analysis-Using-LSTM
A deep learning-based sentiment analysis project using Long Short-Term Memory (LSTM) to classify IMDb movie reviews as positive or negative. Built with Python, TensorFlow, Keras, and Scikit-learn.
# 🎬 Sentiment Analysis Using Long Short-Term Memory (LSTM)

A Deep Learning-based Natural Language Processing (NLP) project that classifies IMDb movie reviews as **Positive** or **Negative** using a Long Short-Term Memory (LSTM) neural network.

---

##  Project Overview

Sentiment Analysis is an NLP technique used to determine the emotional tone of textual data. This project uses an LSTM model to analyze movie reviews from the IMDb dataset and predict whether a review expresses a positive or negative sentiment.

The model is trained using TensorFlow and Keras with text preprocessing techniques such as tokenization, sequence padding, and label encoding.

---

##  Features

-  IMDb Movie Review Dataset
-  Text Preprocessing
-  Tokenization
-  Sequence Padding
-  LSTM Deep Learning Model
-  Model Evaluation
-  Predicts Positive or Negative Sentiment
-  Model Saving for Future Predictions

---

##  Technologies Used

- Python 3.12
- TensorFlow
- Keras
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- NLTK

---

##  Project Structure

```
Sentiment-Analysis-Using-LSTM/
│
├── dataset/
│   └── archive (14)/
│       └── IMDB_Dataset.csv
│
├── models/
│   ├── lstm_model.keras
│   └── tokenizer.pkl
│
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dataset

**Dataset:** IMDb Movie Reviews Dataset

- 50,000 Movie Reviews
- Binary Classification
- Positive Reviews
- Negative Reviews

Dataset Columns:

| Column | Description |
|---------|-------------|
| review | Movie Review Text |
| sentiment | Positive / Negative |

---

##  Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Sentiment-Analysis-Using-LSTM.git
```

Move into the project folder

```bash
cd Sentiment-Analysis-Using-LSTM
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Train the model

```bash
python train.py
```

---

## 💬 Example Prediction

Input

```
This movie is fantastic. I loved every scene.
```

Output

```
😊 Positive Review
```

Input

```
Worst movie I have ever watched.
```

Output

```
😞 Negative Review
```

---

## 🧠 Model Architecture

```
Input Review
      │
      ▼
Text Cleaning
      │
      ▼
Tokenizer
      │
      ▼
Sequence Padding
      │
      ▼
Embedding Layer
      │
      ▼
LSTM Layer
      │
      ▼
Dense Layer
      │
      ▼
Sigmoid Activation
      │
      ▼
Positive / Negative
```

---

##  Model Performance

| Metric | Value |
|---------|--------|
| Algorithm | LSTM |
| Epochs | 3 |
| Batch Size | 32 |
| Test Accuracy | ~80% |

> **Note:** Accuracy may vary depending on the dataset size, train-test split, and training parameters.

---

## Future Improvements

- Add Streamlit Web Application
- Improve Accuracy using Bidirectional LSTM
- Hyperparameter Tuning
- Multi-Class Sentiment Classification
- Deploy the Model on the Cloud

---

## Contributing

Contributions are welcome. Feel free to fork this repository and submit a pull request with improvements.

---

## License

This project is licensed under the MIT License.

---

## Author

**Monika R**

**B.Tech Artificial Intelligence and Data Science**

**GitHub:** https://github.com/Monika843

---

⭐ If you found this project useful, consider giving it a Star!
