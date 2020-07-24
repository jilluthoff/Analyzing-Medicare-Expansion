# Is there a difference? Analyzing if Medicare expansion helped increase health characteristics in a state.  
With the 2020 election on the horizon and healthcare reform as a major discussion point, this project intended to better understand if the Affordable Care Act (ACA) which gave states the option to expand their Medicaid programs to cover more low-income adults aged 19-64, actually helped to increase the populations health. 

Health is a strong indicator of quality of life, and provides insight into access to nutrition, economic challenges and other barriers to health that may persist within a state's population, and can best be measured by looking at the state's public health (rate of disease), access to healthcare, and quality of care. 

## Table of contents
* [Technologies](#technologies)
* [Data Acquisition](#data-acquisition)
* [Data Processing](#data-processing)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Hypothesis Testing](#hypothesis-testing)
* [Conclusion](#conclusion)
* [Future Steps](#future-steps)

## Technologies
Project created with:
 - Python
 - Pandas
 - Matplotlib/Seaborn
 - Excel
 - Pingouin
 - Scipy

## Data Acquisition
The data used for analysis in this project was pulled from CDC WONDER and the United States Census Bureau, and included the following datasets:

  - Public Health Datasets:
    - State Heart Disease Death Rate per 100,000
    - State Cancer Death Rate per 100,000 
    - Adult's Reporting Poor Mental Health Status in the Last 30 Days
    - Adult's Self Reported Fair or Poor Health Status
      
  - Access to Healthcare Datasets:
    - State Uninsured Rates
    - Rates of individuals who had trouble paying off medical bills during past twelve month
    - Percent of adults who could not get medical care when needed due to cost by Total
 
 - State's Stance on Adoption of Expanded Medicare Coverage


## Data Processing
The data was pulled from each website and loaded into a single excel file:
  - All states All Data Collected.xlsx contains alll data collected for every state  
  - All states Correlation Data.xlsx has cleaned data 
  
Since the datasets are all from 2018 and contained data for all states, they were then split into two sets:

   - 31 states that have adpoted and expanded Medicare coverage: HEALTH DATA Adopted.xlsx
   - 19 states that have either not adopted Medicare expansion (13 states) or have not expanded it (6 states) prior to 2018 when: Health Data Not Adopted.xlsx


## Exploratory Data Analysis

Pairwise correlations show a range of correlations from negative to positive. 

![alt text](https://github.com/jilluthoff.png)

A Correlations Heatmap Matrix better shows positive correlations values in red and zero correlations in shades of blue.


![alt text](https://github.com/jilluthoff.png)

A scatter matrix plot of the data in states that have expanded medicare coverage shows positive correlations with the data and that most the data is normally distributed.


A scatter matrix plot of the data in states that have not expanded medicare coverage shows a few positive correlations with the data and that most the data is normally distributed.


## Hypothesis Testing

Welch's t-test was used to answer if the means of the two samples (states with expanded medicare coverage vs states without expanded medicare coverage) were equal, since the populations differ in size, therefore the variance is unequal. It was also assumed the two sample distributions of each category were normally distributed, which can be inferred from the analysis above. 

![formula](https://render.githubusercontent.com/render/math?math=\alpha=0.05)

Question: Do states that have expanded Medicaid Coverage differ in public health characteristics?
  
  NOTE: A Bonferroni correction is used to compensates for testing each individual hypothesis simultaneously. Therefore, the following 4 tests will use a significance level of ![formula](https://render.githubusercontent.com/render/math?math=\alpha/4).
  ![formula](https://render.githubusercontent.com/render/math?math=\alpha=0.0125)
  
  1. Death rates due to heart disease:
  
        Mean_expanded,hd: 160 deaths per 100,000
       
        Mean_not_expanded,hd: 171 deaths per 100,000
  
       ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean death rate due to heart disease for states that expanded coverage = Mean death rate due to heart disease for states that have not expanded coverage. 
       
       
       ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,hd != Mean_not_expanded,hd

       T-Statistic: -1.3163328545331339, P-Value: 0.1961643312117037, P < alpha: False
     
       Reject the null hypothesis, there is no difference in rates of heart disease deaths in states.
     
 
 2. Death rates due to cancer:
  
       Mean_expanded,c: 150 deaths per 100,0000
       
       Mean_not_expanded,c: 155 deaths per 100,000
  
      ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean death rate due to cancer for states that expanded coverage = Mean death rate for states that have not expanded coverage. 
       
      ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,c != Mean_not_expanded,c
      
       T-Statistic: -1.1487430227472555, P-Value: 0.2577782787860322, P < alpha: False
      
       Reject the null hypothesis, there is no difference in rates deaths due to cancer in states with.
  
  
  3. Reported Poor Health:
  
       Mean_expanded,ph: 17.6% of adults report poor health
  
       Mean_not_expanded,ph: 18.5% of adults report poor health
  
      ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of people who report poor health in states that expanded coverage = Mean percentage of people who report poor health in states that did not expand coverage. 
       
      ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,ph != Mean_not_expanded,ph
     
       T-Statistic: -1.0040284567079194, P-Value: 0.32097665837535233, P < alpha: False
     
       Reject the null hypothesis, there is no difference in self reported poor health in states.
    
  
  4. Reported Poor Mental Health:
  
        Mean_expanded,pmh:  23.1% of adults report poor mental health
        
        Mean_not_expanded,pmh: 22.8% of adults report poor mental health
 
        ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of people who report poor mental health in states that expanded coverage = Mean percentage of people who report poor mental health in states that did not expand coverage. 
       
        ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,pmh != Mean_not_expanded,pmh
     
        T-Statistic: -6.613280558230961, P-Value: 2.9035039542281128e-08, P < alpha: True
     
        Do not reject the null hypothesis, there is a difference in self reported poor mental health in states.


Question: Do states that have expanded Medicaid Coverage differ in access to healthcare?

NOTE: A Bonferroni correction is used again to compensates for testing each individual hypothesis simultaneously. Therefore for the following 3 tests will use a significance level of ![formula](https://render.githubusercontent.com/render/math?math=\alpha/3).
 ![formula](https://render.githubusercontent.com/render/math?math=\alpha=0.0167)
  
  1. Percentage of Uninsured Adults:
  
        Mean_expanded,uninisured: 6.7% of adults are uninsured
         
        Mean_not_expanded,uninsured: 10.6% of adults are unisured 
         
        ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of uninsured adults in states that expanded coverage = Mean percentage of uninsured adults in states that have not expanded coverage. 
       
        ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,uninisured != Mean_not_expanded,uninsured
     
        T-Statistic: -5.301286919330062, P-Value: 8.036374628111582e-06, P < alpha: True
     
        Do not reject the null hypothesis, there is a difference in percentage of uninsured adults in states.
  
  
  2. Reported inability to get care due to cost:
  
        Mean_expanded,cost: 11.3% of adults do not get medical care due to cost
         
        Mean_not_expanded,cost: 14.2% of adults do not get medical care due to cost
 
       ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of adults that report an inibility to get care due to cost in states that states that expanded coverage = Mean percentage of adults that report an inibility to get care due to cost in states that have not expanded coverage. 
       
       ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,cost != Mean_not_expanded,cost
     
       T-Statistic: -4.33073454830087, P-Value: 0.00011889736816692388, P < alpha: True
  
       Do not reject the null hypothesis, there is a difference in percentage of adults who do not get care due to cost in states.
        
        
  3. Rates of individuals who had trouble paying off medical bills during past twelve month:
  
        Mean_expanded,bills: 27.2% of adults have trouble paying off their medical bills
  
        Mean_not_expanded,bills: 34.4% of adults have trouble paying off their medical bills
  
      ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of adults that have trouble paying off medical bills for states that expanded coverage = Mean percentage of adults that have trouble paying off medical bills for states that have not expanded coverage. 
       
      ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,bills != Mean_not_expanded,bills
      
       T-Statistic: -4.865100870341971, P-Value: 1.3536393772301125e-05, P < alpha: True
      
       Do not reject the null hypothesis, there is a difference in percentage of adults who have trouble paying off medical bills in states.
       

## Conclusion

As expected, there was an increase in access to healthcare for states that expanded coverage, however surprisingly that increase has only helped improve mental health in those states.

## Future Steps

In the future I would like to collect more data on health care cost, spending, quality, and equality to see how they have been effected by the affordable care act, and possibly try to expand the data to compare the United States health and healthcare to other countries. 
