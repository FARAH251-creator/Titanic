# Test script 
import sys
print("Python Path:", sys.executable)
print("Virtual Environment Active:", 'titanic_env' in sys.executable)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

print("All imports successful!")
print("Setup complete! ")
