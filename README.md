# 🛒AI-Aided-Product-Recommendation-Analytics-of-E-Commerce

An intelligent product recommendation system built using **Python, Streamlit, and Association Rule Mining (Apriori Algorithm)**. This project analyzes customer purchasing behavior using the Instacart Market Basket Analysis dataset and recommends products that are frequently purchased together.

---

## 📌 Project Overview

# 🛒 AI-Aided Product Recommendation Analytics of E-Commerce is a recommendation system that analyzes customer purchasing behavior using the Instacart Market Basket Analysis Dataset. It identifies products that are frequently purchased together using the Apriori Algorithm and provides intelligent product recommendations through an interactive Streamlit web application.

Instead of recommending products randomly, the system identifies purchasing patterns using **Association Rule Mining (Apriori Algorithm)** and provides accurate product recommendations through an interactive Streamlit web application.

This project demonstrates practical applications of **Data Analytics**, **Machine Learning**, and **Business Intelligence** in E-Commerce.

---

## ✨ Features

- 🔍 Product Recommendation using Apriori Algorithm
- 🛍️ Dropdown-based Product Selection
- 📊 Top Purchased Products Analysis
- 📈 Product Frequency Visualization
- 📋 Product Frequency Table
- ⚡ Interactive Streamlit Web Interface
- 🧹 Data Preprocessing using Pandas
- 📦 Association Rule Generation

---

## 📸 Application Preview

### Product Recommendation

> Select a product from the dropdown and receive products frequently purchased together.

![Recommendation System](images/recommendation.png)

---

### Top Purchased Products

Displays the most frequently purchased products using a bar chart.

![Top Products](images/top_products.png)

---

### Product Frequency Table

Displays purchase frequency for each product.

![Frequency Table](images/frequency_table.png)

---

## 🧠 How It Works

1. Load the Instacart dataset.
2. Clean and preprocess transaction data.
3. Convert transactions into basket format.
4. Apply the Apriori Algorithm.
5. Generate Association Rules.
6. Store the generated rules.
7. User selects a product.
8. System recommends associated products based on confidence and lift values.

---

## 📂 Project Structure

```
AI-Aided-Product-Recommendation-Analytics-of-E-Commerce/
│
├── app/
│   └── app.py
│
├── data/
│   ├── association_rules.csv
│   ├── cleaned_data.csv
│   ├── order_products__prior.csv
│   ├── orders.csv
│   └── products.csv
│
├── notebooks/
│   ├── data_analysis.ipynb
│   └── data_preprocessing.ipynb
│
├── utils/
│   ├── recommender.py
│   └── __init__.py
│
├── models/
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Streamlit
- mlxtend

### Development Tools

- VS Code
- Jupyter Notebook

### Dataset

- Instacart Market Basket Analysis Dataset (Kaggle)

---

## 📊 Machine Learning Technique

This project uses **Association Rule Mining** with the **Apriori Algorithm**.

Evaluation metrics include:

- Support
- Confidence
- Lift

These metrics help identify strong relationships between products purchased together.

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Tripti1020/ai-aided-product-recommenation-analytics-of-e-commerce.git
```

Move into the project

```bash
cd your-repository
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app/app.py
```

---

## 📈 Dataset

The project uses the **Instacart Market Basket Analysis Dataset** available on Kaggle.

Dataset includes:

- Products
- Orders
- Prior Orders
- Customer Purchase History

---

## 💡 Future Enhancements

- Personalized User Recommendations
- Hybrid Recommendation System
- Collaborative Filtering
- Product Images
- Real-time Recommendation API
- Cloud Deployment
- User Login & Authentication
- Recommendation Dashboard

---

## 🎯 Learning Outcomes

Through this project I learned:

- Data Cleaning & Preprocessing
- Association Rule Mining
- Apriori Algorithm
- Market Basket Analysis
- Streamlit Web Application Development
- Data Visualization
- Python Programming
- Recommendation System Design

---

## 👩‍💻 Author

**Tripti**

MCA Student

Interested in

- Data Analytics
- Machine Learning
- Python Development
- Business Intelligence

GitHub: https://github.com/tripti1020

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.

It helps motivate further improvements and supports my portfolio.