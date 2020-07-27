# imports
import pylab as pl
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

#Create dataframe from excel file for all states, all data categories
overall_data = pd.read_excel('~/github/gal/Analyzing-Medicare-Expansion/data/All States All Data Collected.xlsx')

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

#Welch's t-test % overweight or obese
t_score_overweight, pval_ow = stats.ttest_ind_from_stats(overweight_mean_expanded, std_overweight_expanded, n_expanded, overweight_mean_nexpanded, std_overweight_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_overweight:.4f}, P-Value: {pval_ow:.4f}, P < alpha: {pval_ow < alpha}"))

#Welch's t-test % Adults, Smoke
t_score_smoke, pval_smoke = stats.ttest_ind_from_stats(smoke_mean_expanded, std_smoke_expanded, n_expanded, smoke_mean_nexpanded, std_smoke_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_smoke:.4f}, P-Value: {pval_smoke:.4f}, P < alpha: {pval_smoke < alpha}")

#Welch's t-test Heart Disease Death Rate per 100,000
t_score_hd, pval_hd = stats.ttest_ind_from_stats(hd_mean_expanded, std_hd_expanded, n_expanded, hd_mean_nexpanded, std_hd_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_hd:.4f}, P-Value: {pval_hd:.4f}, P < alpha: {pval_hd < alpha}")

#Welch's t-test Cancer Death Rate per 100,000
t_score_cancer, pval_cancer = stats.ttest_ind_from_stats(cancer_mean_expanded, std_cancer_expanded, n_expanded, cancer_mean_nexpanded, std_cancer_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_cancer:.4f}, P-Value: {pval_cancer:.4f}, P < alpha: {pval_cancer < alpha}")

#Welch's t-test Stroke Death Rate per 100,000
t_score_stroke, pval_stroke = stats.ttest_ind_from_stats(stroke_mean_expanded, std_stroke_expanded, n_expanded, stroke_mean_nexpanded, std_stroke_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_stroke:.4f}, P-Value: {pval_stroke:.4f}, P < alpha: {pval_stroke < alpha}")

#Welch's t-test Mortality Rate per 100,000
t_score_mortality, pval_mortality = stats.ttest_ind_from_stats(mortality_mean_expanded, std_mortality_expanded, n_expanded, mortality_mean_nexpanded, std_mortality_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_mortality:.4f}, P-Value: {pval_mortality:.4f}, P < alpha: {pval_mortality < alpha}")

#Welch's t-test Suicide Rate per 100,000
t_score_suicide, pval_suicide = stats.ttest_ind_from_stats(suicide_mean_expanded, std_suicide_expanded, n_expanded, suicide_mean_nexpanded, std_suicide_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_suicide:.4f}, P-Value: {pval_suicide:.4f}, P < alpha: {pval_suicide < alpha}")

#Welch's t-test Life Expectancy
t_score_life_exp, pval_life_exp = stats.ttest_ind_from_stats(life_exp_mean_expanded, std_life_exp_expanded, n_expanded, life_exp_mean_nexpanded, std_life_exp_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_life_exp:.4f}, P-Value: {pval_life_exp:.4f}, P < alpha: {pval_life_exp < alpha}")

#Welch's t-test % Adults, Health Poor
t_score_stroke, pval_poor_health = stats.ttest_ind_from_stats(poor_health_mean_expanded, std_poor_health_expanded, n_expanded, poor_health_mean_nexpanded, std_poor_health_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_stroke:.4f}, P-Value: {pval_poor_health:.4f}, P < alpha: {pval_poor_health < alpha}")

#Welch's t-test% Adults, Health Fair
t_score_fair_health, pval_fair_health = stats.ttest_ind_from_stats(fair_health_mean_expanded, std_fair_health_expanded, n_expanded, fair_health_mean_nexpanded, std_fair_health_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_fair_health:.4f}, P-Value: {pval_fair_health:.4f}, P < alpha: {pval_fair_health < alpha}")

#Welch's t-test % Adults, Health Good
t_score_good_health, pval_good_health = stats.ttest_ind_from_stats(stroke_mean_expanded, std_good_health_expanded, n_expanded, good_health_mean_nexpanded, std_good_health_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_good_health:.4f}, P-Value: {pval_good_health:.4f}, P < alpha: {pval_good_health < alpha}")

#Welch's t-test % Adults, Health Very Good
t_score_vg_health, pval_vg_health = stats.ttest_ind_from_stats(vg_health_mean_expanded, std_vg_health_expanded, n_expanded, vg_health_mean_nexpanded, std_vg_health_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_vg_health:.4f}, P-Value: {pval_vg_health:.4f}, P < alpha: {pval_vg_health < alpha}")

#Welch's t-test % Adults, Health Excellent
t_score_ex_health, pval_ex_health = stats.ttest_ind_from_stats(ex_health_mean_expanded, std_ex_health_expanded, n_expanded, ex_health_mean_nexpanded, std_ex_health_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_ex_health:.4f}, P-Value: {pval_ex_health:.4f}, P < alpha: {pval_ex_health < alpha}")

#Welch's t-test Excellent Mental Health (0 Poor days)
t_score_ex_mentalh, pval_ex_mentalh = stats.ttest_ind_from_stats(ex_mentalh_mean_expanded, std_ex_mentalh_expanded, n_expanded, ex_mentalh_mean_nexpanded, std_ex_mentalh_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_ex_mentalh:.4f}, P-Value: {pval_ex_mentalh:.4f}, P < alpha: {pval_ex_mentalh < alpha}")

#Welch's t-test Good Mental Health (1-4 Poor Days)
t_score_good_mental, pval_good_mental = stats.ttest_ind_from_stats(good_mental_mean_expanded, std_good_mental_expanded, n_expanded, good_mental_mean_nexpanded, std_good_mental_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_good_mental:.4f}, P-Value: {pval_good_mental:.4f}, P < alpha: {pval_good_mental < alpha}")

#Welch's t-test Fair Mental Health (5-13 Days Poor)
t_score_fair_mental, pval_fair_mental = stats.ttest_ind_from_stats(fair_mental_mean_expanded, std_fair_mental_expanded, n_expanded, fair_mental_mean_nexpanded, std_fair_mental_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_fair_mental:.4f}, P-Value: {pval_fair_mental:.4f}, P < alpha: {pval_fair_mental < alpha}")

#Welch's t-test Bad Mental Health (14+ Days Poor)
t_score_bad_mental, pval_bad_mental = stats.ttest_ind_from_stats(bad_mental_mean_expanded, std_bad_mental_expanded, n_expanded, bad_mental_mean_nexpanded, std_bad_mental_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_bad_mental:.4f}, P-Value: {pval_bad_mental:.4f}, P < alpha: {pval_bad_mental < alpha}")

#Welch's t-test % Adults, No care due to cost
t_score_no_care, pval_no_care = stats.ttest_ind_from_stats(no_care_mean_expanded, std_no_care_expanded, n_expanded, no_care_mean_nexpanded, std_no_care_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_no_care:.4f}, P-Value: {pval_no_care:.4f}, P < alpha: {pval_no_care < alpha}")

#Welch's t-test % Adults, Trouble Paying Medical Bills
t_score_trouble, pval_trouble = stats.ttest_ind_from_stats(trouble_mean_expanded, std_trouble_expanded, n_expanded, trouble_mean_nexpanded, std_trouble_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_trouble:.4f}, P-Value: {pval_trouble:.4f}, P < alpha: {pval_trouble < alpha}")

#Welch's t-test % Adults Uninsured
t_score_uninsured, pval_uninsured = stats.ttest_ind_from_stats(uninsured_mean_expanded, std_uninsured_expanded, n_expanded, uninsured_mean_nexpanded, std_uninsured_nexpanded, n_not_expanded, equal_var=False)
print(f"T-Statistic: {t_score_uninsured:.4f}, P-Value: {pval_uninsured:.4f}, P < alpha: {pval_uninsured < alpha}")

# Correlation Heatmap For All States all Data
corrs = overall_data.corr()
mask = np.zeros_like(corrs)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(corrs, cmap='Spectral_r', square=True)

plt.title('Correlation Heatmap For All States All Data')
plt.savefig('Heatmap_all_states_all_data.png')

#Histograms for all states all data
overall_data.hist(figsize = (20,20))
pl.suptitle("All States Histograms" , y = .92)
plt.savefig("All_States_All_Data_Histograms.png")

#Histograms of All Data Categories for States with Expanded Medicare
expanded.hist(figsize = (20,20))
pl.suptitle("Histograms of All Data Categories for States with Expanded Medicare" , y = .92)
plt.savefig("Expanded_Histograms.png")

#Correlation Heatmap For States with Expanded Medicare
corrs = expanded.corr()
mask = np.zeros_like(corrs)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(corrs, cmap='Spectral_r', square=True)

plt.title('Correlation Heatmap For States with Expanded Medicare')
plt.savefig('Heatmap_expanded.png')

#Histograms of All Data Categories for States that Did Not Expand Medicare
not_expanded.hist(figsize = (20,20))
pl.suptitle("Histograms of All Data Categories for States that Did Not Expand Medicare" , y = .92)
plt.savefig("Not_Histograms.png")

#Correlation Heatmap For States that Did Not Expand Medicare
corrs = not_expanded.corr()
mask = np.zeros_like(corrs)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(corrs, cmap='Spectral_r', square=True)

plt.title('Correlation Heatmap For States that Did Not Expand Medicare')
plt.savefig('Heatmap_not.png')

# % Adults Uninsured Boxplots with means labeled
col = '% Adults Uninsured'
sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Are Uninsured in States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Uninsured.png")

#% Adults, Trouble Paying Medical Bills Boxplots with means labeled
col = '% Adults, Trouble Paying Medical Bills'
sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Have Trouble Paying Medical Bills in States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Trouble.png")

#% Adults, No care due to cost Boxplots with means labeled

col= '% Adults, No care due to cost'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Do Not Recieve Care Due to Cost for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_No_care.png")

# Bad Mental Health (14+ Days Poor) Boxplots with means labeled
col= 'Bad Mental Health (14+ Days Poor)'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Reported Bad Mental Health (14+ Days Poor) for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_BADMH.png")

#Fair Mental Health (5-13 Days Poor) Boxplots with means labeled
col= 'Fair Mental Health (5-13 Days Poor)'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Reported Fair Mental Health (5-13 Days Poor) for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_FairMH.png")

#Good Mental Health (1-4 Poor Days) Boxplots with means labeled
col= 'Good Mental Health (1-4 Poor Days)'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Reported Good Mental Health (1-4 Poor Days) for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_GoodMH.png")

# Excellent Mental Health (0 Poor days) Boxplots with means labeled
col= 'Excellent Mental Health (0 Poor days)'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Reported Excellent Mental Health (0 Poor days) for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_EXCMH.png")

# % Adults, Health Excellent Boxplots with means labeled
col= '% Adults, Health Excellent'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Reported Excellent Health' for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_ExcH.png")

# % Adults, Health Very Good Boxplots with means labeled
col= '% Adults, Health Very Good'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Reported Very Good Health for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_VGHealth.png")

# % Adults, Health Good Boxplots with means labeled
col= '% Adults, Health Good'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Reported Good Health for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Good_Health.png")

# % Adults, Health Fair Boxplots with means labeled
col= '% Adults, Health Fair'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Reported Fair Health for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Fair_Health.png")

# % Adults, Health Poor Histogram Boxplots with means labeled
col= '% Adults, Health Poor'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults Who Reported Poor Health for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Poor_Health.png")


# Life Expectancy Boxplots with means labeled
col= 'Life Expectancy'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Life Expectancy for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_LE.png")

# Boxplots with means labeled for 'Suicide Rate per 100,000'
col= 'Suicide Rate per 100,000'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Suicide Rate per 100,000 for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_suicide.png")

# Boxplots with means labeled for Mortality Rate per 100,000'
col= 'Mortality Rate per 100,000'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Mortality Rate per 100,000 for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Mortality.png")

#Boxplots with means labeled Stroke Death Rate per 100,000
col= 'Stroke Death Rate per 100,000'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Stroke Death Rate per 100,000 for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Stroke.png")

#Boxplots with means labeled Cancer Death Rate per 100,000
col= 'Cancer Death Rate per 100,000'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Cancer Death Rate per 100,000 for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Cancer.png")

#Boxplots with means labeled Heart Disease Death Rate per 100,000
col= 'Heart Disease Death Rate per 100,000'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Heart Disease Death Rate per 100,000 for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_HD.png")

#Boxplots with means labeled % Adults, Smoke
col= '% Adults, Smoke'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title("Percentage of Adults that Smoke for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Smoke.png")

#Boxplots with means labeled % overweight or obese
col=  '% overweight or obese'

sns.set(style="whitegrid")

box_plot= sns.boxplot(x="Expanded", y=col, data=overall_data,
                 order=["Expanded", "Not Expanded"],width = .95 ,meanline = True, showmeans =True)

means = overall_data.groupby(['Expanded'])[col].mean()
vertical_offset = overall_data[col].mean() * 0.01 # offset from median for display

for xtick in box_plot.get_xticks():
    box_plot.text(xtick,means[xtick] + vertical_offset,means[xtick],
            horizontalalignment='center',size='x-small',color='w',weight='semibold')

plt.title(" Percentage of Adults that are Overweight or Obese for States with Expanded vs Non-Expanded Medicare")
plt.savefig("Box_Overweight.png")

