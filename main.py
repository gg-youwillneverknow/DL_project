
import numpy as np
import pandas as pd

#import loan dataset
df = pd.read_csv('spaceship-titanic/train').dropna(axis=1,how='any')