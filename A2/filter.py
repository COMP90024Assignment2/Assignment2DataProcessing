import pandas as pd

homeless = pd.read_csv("homeless_19.csv")
income = pd.read_csv("income_2021.csv")
unemp = pd.read_csv("unemployment_2021.csv")
all_data = pd.read_csv("homeless_19.csv")
all_data = all_data.drop('fin_yr', axis=1)

all_data = all_data.merge(income,how='left', left_on=" gccsa_code", right_on=" gccsa_code_2021")
all_data = all_data.drop(' gccsa_code_2021', axis = 1)
all_data = all_data.merge(unemp,how='left', left_on=" gccsa_code", right_on=' gccsa_code_2016')
all_data = all_data.drop(' gccsa_code_2016', axis = 1)

all_data.to_csv('all_data.csv', index=False)