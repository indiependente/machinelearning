import pandas as pd
import numpy as np

data = pd.read_csv('Steph_Curry_2015_Shooting_Data.csv')

tpp = data['ThreePP']
print 'Steph Curry''s three point percentage mean',
print np.mean([i for i in tpp])
print 'Steph Curry''s three point low percentage mean',
print np.mean([i for i in tpp if i <= .2])