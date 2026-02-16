# 🚢 Titanic Survival Prediction Project

## 📖 About This Project

This is my machine learning project that predicts whether passengers survived the Titanic disaster. This project is perfect for beginners who want to learn about data science and machine learning!
## ⚠️ About the Dataset

**Important to Know:**

This dataset contains information about **1,309 passengers** from the Titanic, which is a subset of the full historical record (~2,224 people including crew). 

**Key Limitations:**
- **Crew members excluded** - Only passenger data is included
- **Missing values** - About 20% of ages and 77% of cabin numbers are missing
- **Cleaned data** - This is a simplified version created for learning, based on historical records from Encyclopedia Titanica and other sources
- **Survival rate differs** - Dataset shows ~38% survival (passengers only) vs ~32% historical survival rate (all people aboard)

Despite these limitations, this dataset is excellent for learning machine learning fundamentals and is one of the most popular datasets in data science education.

**Sources:** 
- Kaggle Titanic Competition
- Encyclopedia Titanica
- "Titanic: Triumph and Tragedy" by Eaton & Haas (1994)
  

### What is the Titanic Dataset?

On April 15, 1912, the RMS Titanic sank after hitting an iceberg during its first voyage. Out of 2,224 passengers and crew, more than 1,500 people died. This tragic event is now used as a learning dataset to predict survival based on passenger information like age, gender, ticket class, and more.

## 🎯 Project Goal

The main goal is to build a machine learning model that can predict if a passenger survived or not based on their characteristics. This helps us learn:
- How to clean and prepare data
- How to explore data to find patterns
- How to build and compare different machine learning models
- How to evaluate how well our models work

## 🛠️ Technologies Used

This project uses Python and several popular libraries:

- **Python 3.x** - The programming language
- **Pandas** - For working with data (like Excel, but in code)
- **NumPy** - For mathematical calculations
- **Matplotlib** - For creating charts and graphs
- **Seaborn** - For making beautiful visualizations
- **Scikit-learn** - For machine learning algorithms

## 📁 Project Structure

```
Titanic/
│
├── notebooks/           # Jupyter notebooks with code and analysis
│   ├── data_exploration.ipynb    # Looking at the data
│   ├── data_preprocessing.ipynb  # Cleaning the data
│   └── model_training.ipynb      # Building ML models
│
├── data/               # Dataset files
│   ├── train.csv      # Data for training our model
│   └── test.csv       # Data for testing our model
│
└── README.md          # This file!
```

## 🚀 Getting Started

### Prerequisites

You need to have Python installed on your computer. If you don't have it, download it from [python.org](https://www.python.org/).

### Installation

1. **Clone this repository** (download the code to your computer):
   ```bash
   git clone https://github.com/FARAH251-creator/Titanic.git
   cd Titanic
   ```

2. **Install required libraries**:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

   Or if you have a `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

4. **Open the notebooks** in the `notebooks/` folder and run them step by step!

## 📊 What's Inside the Notebooks

### 1. Data Exploration
- Looking at what data we have
- Understanding different columns (features)
- Finding missing values
- Creating visualizations to see patterns

### 2. Data Preprocessing
- Cleaning the data
- Filling in missing values
- Converting text data to numbers (like "male"/"female" to 0/1)
- Creating new useful features

### 3. Model Training
- Building different machine learning models:
  - Logistic Regression
  - Decision Trees
  - Random Forest
  - Support Vector Machines (SVM)
- Comparing which model works best
- Making predictions on new data

## 📈 Results

- **Best Model**: Random Forest
- **Accuracy**: 81.5%
- **Training Time**: ~2 seconds

### Key Findings:
- **Gender was critical**: Women survived at 74% vs men at 19%
- **Class mattered**: 1st class (63% survival) > 2nd class (47%) > 3rd class (24%)
- **Children survived more**: 59% for kids vs 38% for adults
- **Family size effect**: Small families did better than solo travelers or large groups

**Most Important Features** (by model importance):
1. Sex (Gender)
2. Pclass (Passenger Class)
3. Fare (Ticket Price)
4. Age
5. Embarked Port

## 🧠 What I Learned

- How to work with real-world messy data
- Different ways to visualize data
- How machine learning models make predictions
- The importance of data cleaning
- How to compare different models

## 🔮 Future Improvements

- [ ] Try more advanced models (like XGBoost or Neural Networks)
- [ ] Do more feature engineering
- [ ] Create a web app to make predictions
- [ ] Improve accuracy with better data preprocessing

## 📚 Resources for Beginners

If you're new to machine learning, check out these resources:

- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic) - The original competition
- [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) - Free online book
- [Scikit-learn Documentation](https://scikit-learn.org/) - Learn about ML algorithms
- [Pandas Documentation](https://pandas.pydata.org/) - Learn data manipulation

## 🤝 Contributing

This is a learning project, but suggestions are welcome! Feel free to:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is open source and available for anyone to learn from.



