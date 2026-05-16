import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from dotenv import load_dotenv
from statistics import mode
from func import *

load_dotenv()

engine = get_engine()

start = time.perf_counter()

dfc = pd.read_csv('Teen_Mental_Health_Dataset.csv')

dfc.index = np.arange(1, len(dfc) + 1)

or_col_name = dfc.columns.to_list()
col_name = list(map(correct_title, or_col_name))

for i in range(len(or_col_name)):
    dfc.rename(columns = {or_col_name[i] : col_name[i]}, inplace = True)

slpdf = pd.read_sql("SELECT * FROM acper_slphrs", engine)
slpdf.index = np.arange(1, len(slpdf) + 1)

dsmhdf = pd.read_sql("SELECT * FROM acper_dsmh", engine)

slpdf.rename(columns ={'sleep_hours': col_name[4],
                       'academic_performance': col_name[6],
                       'min_per': 'Weakest GPA',
                       'max_per': 'Strongest GPA',
                       'number_of_students' : 'Number of Students'},
                        inplace = True)

dsmhdf.rename(columns ={'daily_social_media_hours': col_name[2],
                       'academic_performance': col_name[6]},
                        inplace = True)

bar_plot(dsmhdf, col_name[2], 'Academic Performance')

print(dfc.head())
end_time = time.perf_counter()
print(f"{end_time - start:.4f} seconds")

plt.show()