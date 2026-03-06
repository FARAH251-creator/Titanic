# Titanic Survival Prediction Project

## 📖 About This Project
This is my machine learning project that predicts whether passengers survived the Titanic disaster. This project is perfect for beginners who want to learn about data science and machine learning!

## ⚠️ About the Dataset

**Important to Know:**

This dataset contains information about 1,309 passengers from the Titanic, which is a subset of the full historical record (~2,224 people including crew).

**Key Limitations:**
- **Crew members excluded** - Only passenger data is included
- **Missing values** - About 20% of ages and 77% of cabin numbers are missing
- **Cleaned data** - This is a simplified version created for learning, based on historical records from Encyclopedia Titanica and other sources
- **Survival rate differs** - Dataset shows ~38% survival (passengers only) vs ~32% historical survival rate (all people aboard)

Despite these limitations, this dataset is excellent for learning machine learning fundamentals and is one of the most popular datasets in data science education.

**Sources:**
- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)
- [Encyclopedia Titanica](https://www.encyclopedia-titanica.org/)
- "Titanic: Triumph and Tragedy" by Eaton & Haas (1994)

## What is the Titanic Dataset?
On April 15, 1912, the RMS Titanic sank after hitting an iceberg during its first voyage. Out of 2,224 passengers and crew, more than 1,500 people died. This tragic event is now used as a learning dataset to predict survival based on passenger information like age, gender, ticket class, and more.

## 🎯 Project Goal
The main goal is to build a machine learning model that can predict if a passenger survived or not based on their characteristics. This helps us learn:
- How to clean and prepare data
- How to explore data to find patterns
- How to build and compare different machine learning models
- How to evaluate how well our models work

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python 3.x | Programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Mathematical calculations |
| Matplotlib | Charts and graphs |
| Seaborn | Statistical visualizations |
| Scikit-learn | Machine learning algorithms |

## 📁 Project Structure
```
Titanic/
│
├── titanic_analysis.py   # Main analysis script (run this!)
├── notebooks/            # Jupyter notebooks with detailed analysis
│   ├── data_exploration.ipynb
│   ├── data_preprocessing.ipynb
│   └── model_training.ipynb
│
├── data/                 # Dataset files
│   ├── train.csv         # Training data (891 passengers)
│   └── test.csv          # Testing data
│
├── feature_importance.png # Generated chart
├── requirements.txt       # Python dependencies
└── README.md              # This file!
```

## 🚀 Getting Started

### Prerequisites
You need Python 3.x installed. Download it from [python.org](https://www.python.org/).

### Installation

1. Clone this repository:
```bash
git clone https://github.com/FARAH251-creator/Titanic.git
cd Titanic
```

2. Create a virtual environment and activate it:
```bash
python -m venv titanic_env
# Windows:
titanic_env\Scripts\activate
# Mac/Linux:
source titanic_env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the analysis:
```bash
python titanic_analysis.py
```

## 📊 Results

### Dataset Overview
- **Total passengers:** 891
- **Features:** 12 columns
- **Survival rate:** 38.4%

### Model Comparison

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 79.9% |
| Decision Tree | 79.3% |
| **Random Forest** | **82.1%** ⭐ |
| SVM | 67.0% |

**Best Model: Random Forest with 82.1% accuracy**

### Feature Importance (Random Forest)

![Feature Importance](feature_importance.png)

The chart above shows which passenger features had the most impact on survival prediction:

| Rank | Feature | Importance | Explanation |
|------|---------|-----------|-------------|
| 1 | **Sex** | Highest | Women survived at much higher rates ("women and children first") |
| 2 | **Fare** | Very High | Higher fare = better cabin location and lifeboat access |
| 3 | **Age** | High | Children had higher survival rates |
| 4 | **Pclass** | Medium | 1st class survived more than 3rd class |
| 5 | **FamilySize** | Low-Medium | Small families did better than solo travelers or large groups |
| 6 | **SibSp** | Low | Number of siblings/spouses aboard |
| 7 | **Embarked** | Low | Port of embarkation had minor effect |
| 8 | **Parch** | Lowest | Number of parents/children aboard |

### Key Findings
- **Gender was critical:** Women survived at significantly higher rates than men, reflecting the "women and children first" protocol
- **Class mattered:** 1st class passengers had the best survival chances, while 3rd class had the lowest
- **Age played a role:** Children were prioritized during evacuation
- **Wealth indicator:** Higher ticket fares correlated strongly with survival, likely due to cabin proximity to lifeboats

## 🧠 What I Learned
- How to work with real-world messy data (handling missing values, encoding categorical features)
- Different ways to visualize data using Matplotlib and Seaborn
- How machine learning models make predictions using different algorithms
- The importance of data cleaning and preprocessing
- How to compare and evaluate different models using accuracy metrics

## 🔮 Future Improvements
- [ ] Try more advanced models (XGBoost, Neural Networks)
- [ ] Perform deeper feature engineering
- [ ] Create a web app for interactive predictions
- [ ] Improve accuracy with cross-validation and hyperparameter tuning
- [ ] Add more visualizations (survival by class, age distribution, etc.)

## 📚 Resources for Beginners
- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic) - The original competition
- [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) - Free online book
- [Scikit-learn Documentation](https://scikit-learn.org/) - ML algorithms reference
- [Pandas Documentation](https://pandas.pydata.org/) - Data manipulation guide

## 🤝 Contributing
This is a learning project, but suggestions are welcome! Feel free to:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📝 License
This project is open source and available for anyone to learn from.
