# imports
import pylab as pl
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

#Create dataframe from excel file for all states, all data categories
overall_data = pd.read_excel('~/github/gal/Analyzing-Medicare-Expansion/data2/All States All Data Collected.xlsx')

#Subset dataframe to only include states that have expanded Medicare
mask = overall_data.Expanded == 'Expanded'
expanded = overall_data[mask]

#Subset dataframe to only include states that have not expanded Medicare
mask = overall_data.Expanded != 'Expanded'
not_expanded = overall_data[mask]

#Get sample means for all categories for states with expanded medicare
overweight_mean_expanded = expanded['% overweight or obese'].mean()
smoke_mean_expanded = expanded['% Adults, Smoke'].mean()
hd_mean_expanded= expanded['Heart Disease Death Rate per 100,000'].mean()
cancer_mean_expanded = expanded['Cancer Death Rate per 100,000'].mean()
stroke_mean_expanded = expanded['Stroke Death Rate per 100,000'].mean()
mortality_mean_expanded = expanded['Mortality Rate per 100,000'].mean()
suicide_mean_expanded = expanded['Suicide Rate per 100,000'].mean()
life_exp_mean_expanded = expanded['Life Expectancy'].mean()
poor_health_mean_expanded = expanded['% Adults, Health Poor'].mean()
fair_health_mean_expanded = expanded['% Adults, Health Fair'].mean()
good_health_mean_expanded = expanded['% Adults, Health Good'].mean()
vg_health_mean_expanded = expanded['% Adults, Health Very Good'].mean()
ex_health_mean_expanded = expanded['% Adults, Health Excellent'].mean()
ex_mentalh_mean_expanded = expanded['Excellent Mental Health (0 Poor days)'].mean()
good_mental_mean_expanded = expanded['Good Mental Health (1-4 Poor Days)'].mean()
fair_mental_mean_expanded = expanded['Fair Mental Health (5-13 Days Poor)'].mean()
bad_mental_mean_expanded = expanded['Bad Mental Health (14+ Days Poor)'].mean()
no_care_mean_expanded = expanded['% Adults, No care due to cost'].mean()
trouble_mean_expanded = expanded['% Adults, Trouble Paying Medical Bills'].mean()
uninsured_mean_expanded = expanded['% Adults Uninsured'].mean()

#Get sample means for all categories for states without expanded medicare
overweight_mean_nexpanded = not_expanded['% overweight or obese'].mean()
smoke_mean_nexpanded = not_expanded['% Adults, Smoke'].mean()
hd_mean_nexpanded= not_expanded['Heart Disease Death Rate per 100,000'].mean()
cancer_mean_nexpanded = not_expanded['Cancer Death Rate per 100,000'].mean()
stoke_mean_nexpanded = not_expanded['Stroke Death Rate per 100,000'].mean()
mortality_mean_nexpanded = not_expanded['Mortality Rate per 100,000'].mean()
suicide_mean_nexpanded = not_expanded['Suicide Rate per 100,000'].mean()
life_exp_mean_nexpanded = not_expanded['Life Expectancy'].mean()
poor_health_mean_nexpanded = not_expanded['% Adults, Health Poor'].mean()
fair_health_mean_nexpanded = not_expanded['% Adults, Health Fair'].mean()
good_health_mean_nexpanded = not_expanded['% Adults, Health Good'].mean()
vg_health_mean_nexpanded = not_expanded['% Adults, Health Very Good'].mean()
ex_health_mean_nexpanded = not_expanded['% Adults, Health Excellent'].mean()
ex_mentalh_mean_nexpanded = not_expanded['Excellent Mental Health (0 Poor days)'].mean()
good_mental_mean_nexpanded = not_expanded['Good Mental Health (1-4 Poor Days)'].mean()
fair_mental_mean_nexpanded = not_expanded['Fair Mental Health (5-13 Days Poor)'].mean()
bad_mental_mean_nexpanded = not_expanded['Bad Mental Health (14+ Days Poor)'].mean()
no_care_mean_nexpanded = not_expanded['% Adults, No care due to cost'].mean()
trouble_mean_nexpanded = not_expanded['% Adults, Trouble Paying Medical Bills'].mean()
uninsured_mean_nexpanded = not_expanded['% Adults Uninsured'].mean()

#Get sample standard deviations for states with expanded medicare
std_overweight_expanded = expanded['% overweight or obese'].std()
std_smoke_expanded = expanded['% Adults, Smoke'].std()
std_hd_expanded= expanded['Heart Disease Death Rate per 100,000'].std()
std_cancer_expanded = expanded['Cancer Death Rate per 100,000'].std()
std_stoke_expanded = expanded['Stroke Death Rate per 100,000'].std()
std_mortality_expanded = expanded['Mortality Rate per 100,000'].std()
std_suicide_expanded = expanded['Suicide Rate per 100,000'].std()
std_life_exp_expanded = expanded['Life Expectancy'].std()
std_poor_health_expanded = expanded['% Adults, Health Poor'].std()
std_fair_health_expanded = expanded['% Adults, Health Fair'].std()
std_good_health_expanded = expanded['% Adults, Health Good'].std()
std_vg_health_expanded = expanded['% Adults, Health Very Good'].std()
std_ex_health_expanded = expanded['% Adults, Health Excellent'].std()
std_ex_mentalh_expanded = expanded['Excellent Mental Health (0 Poor days)'].std()
std_good_mental_expanded = expanded['Good Mental Health (1-4 Poor Days)'].std()
std_fair_mental_expanded = expanded['Fair Mental Health (5-13 Days Poor)'].std()
std_bad_mental_expanded = expanded['Bad Mental Health (14+ Days Poor)'].std()
std_no_care_expanded = expanded['% Adults, No care due to cost'].std()
std_trouble_expanded = expanded['% Adults, Trouble Paying Medical Bills'].std()
std_uninsured_expanded = expanded['% Adults Uninsured'].std()

#Get sample standard deviations for states without expanded medicare
std_overweight_nexpanded = not_expanded['% overweight or obese'].std()
std_smoke_nexpanded = not_expanded['% Adults, Smoke'].std()
std_hd_nexpanded= not_expanded['Heart Disease Death Rate per 100,000'].std()
std_cancer_nexpanded = not_expanded['Cancer Death Rate per 100,000'].std()
std_stoke_nexpanded = not_expanded['Stroke Death Rate per 100,000'].std()
std_mortality_nexpanded = not_expanded['Mortality Rate per 100,000'].std()
std_suicide_nexpanded = not_expanded['Suicide Rate per 100,000'].std()
std_life_exp_nexpanded = not_expanded['Life Expectancy'].std()
std_poor_health_nexpanded = not_expanded['% Adults, Health Poor'].std()
std_fair_health_nexpanded = not_expanded['% Adults, Health Fair'].std()
std_good_health_nexpanded = not_expanded['% Adults, Health Good'].std()
std_vg_health_nexpanded = not_expanded['% Adults, Health Very Good'].std()
std_ex_health_nexpanded = not_expanded['% Adults, Health Excellent'].std()
std_ex_mentalh_nexpanded = not_expanded['Excellent Mental Health (0 Poor days)'].std()
std_good_mental_nexpanded = not_expanded['Good Mental Health (1-4 Poor Days)'].std()
std_fair_mental_nexpanded = not_expanded['Fair Mental Health (5-13 Days Poor)'].std()
std_bad_mental_nexpanded = not_expanded['Bad Mental Health (14+ Days Poor)'].std()
std_no_care_nexpanded = not_expanded['% Adults, No care due to cost'].std()
std_trouble_nexpanded = not_expanded['% Adults, Trouble Paying Medical Bills'].std()
std_uninsured_nexpanded = not_expanded['% Adults Uninsured'].std()

#critical value, with bonferroni correction due to multiple tests
alpha = .05/20

#sample size of each category
n_expanded = 31
n_not_expanded = 19

#Welch's t-test Heart Disease Death Rate per 100,000
t_score_hd, pval_hd = stats.ttest_ind_from_stats(hd_mean_expanded, std_hd_expanded, len(medicare_expanded['Heart Disease Death Rate per 100,000']), hd_mean_ne, hd_std_ne, len(not_expanded['Heart Disease Death Rate per 100,000']), equal_var=False)
print(f"t-Statistic: {t_score_hd}, P-Value: {pval_hd}, P < alpha: {pval_hd < alpha1}")

