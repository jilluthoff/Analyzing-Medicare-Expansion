# Is there really a difference? How Medicare expansion helped increase specific characteristics of health in a state.  
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
The data used for analysis in this project include was pulled from the CDC WONDER and United States Census Bureau.

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
The data was pulled from and loaded into Excel files:
  - All states, all data
  - States that had adpoted expanded Medicare coverage as of 2018, significance test data
  - States that had not adpoted expended Medicare coverage as of 2018, signficance test data

## Exploratory Data Analysis

Pairwise correlations show a range of correlations from negative to positive. 

![alt text](https://github.com/jilluthoff.png)

A Correlations Heatmap Matrix better shows positive correlations values in red and zero correlations in shades of blue.


![alt text](https://github.com/jilluthoff.png)

A scatter matrix plot of the data in states that have expanded medicare coverage shows positive correlations with the data and that most the data is normally distributed.


A scatter matrix plot of the data in states that have not expanded medicare coverage shows a few positive correlations with the data and that most the data is normally distributed.


## Hypothesis Testing
I used Welch's t-test to answer if the means of the two samples (states with expanded medicare coverage vs states without expanded medicare coverage) were equal, since the populations differ in size, therefore the variance is unequal. I also assumped the two sample distributions were normally distributed, which can be inferred from the analysis above. 


![formula](https://render.githubusercontent.com/render/math?math=\alpha=0.05)


Question: Do states that have expanded Medicaid Coverage differ in public health characteristics?
  
  NOTE: A Bonferroni correction is used to compensates for testing each individual hypothesis simultaneously. Therefore, the following 4 tests will use a significance level of ![formula](https://render.githubusercontent.com/render/math?math=\alpha/4).
  ![formula](https://render.githubusercontent.com/render/math?math=\alpha=0.0125)
  
  1. Death rates due to heart disease
  
       ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean death rate due to heart disease for states that expanded coverage = Mean death rate due to heart disease for states that have not expanded coverage. 
       
       ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,hd != Mean_not_expanded,hd

 
  
  
  2. Death rates due to cancer
  
      ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean death rate due to cancer for states that expanded coverage = Mean death rate for states that have not expanded coverage. 
       
      ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,c != Mean_not_expanded,c
  
  
  3. Reported Poor Health
  
     ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of people who report poor health in states that expanded coverage = Mean percentage of people who report poor health in states that did not expand coverage. 
       
     ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,ph != Mean_not_expanded,ph
    
  
  4. Reported Poor Mental Health
 
     ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of people who report poor mental health in states that expanded coverage = Mean percentage of people who report poor mental health in states that did not expand coverage. 
       
     ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,pmh != Mean_not_expanded,pmh


Question: Do states that have expanded Medicaid Coverage differ in access to healthcare?

NOTE: A Bonferroni correction is used again to compensates for testing each individual hypothesis simultaneously. Therefore for the following 3 tests will use a significance level of ![formula](https://render.githubusercontent.com/render/math?math=\alpha/3).
 ![formula](https://render.githubusercontent.com/render/math?math=\alpha=0.0167)
  
  1. Percentage of Uninsured Adults
  
     ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of uninsured adults in states that expanded coverage = Mean percentage of uninsured adults in states that have not expanded coverage. 
       
     ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,uninisured != Mean_not_expanded,uninsured
  
  
  2. Reported inability to get care due to cost
 
     ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of adults that report an inibility to get care due to cost in states that states that expanded coverage = Mean percentage of adults that report an inibility to get care due to cost in states that have not expanded coverage. 
       
     ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,cost != Mean_not_expanded,cost
  
  
  3. Rates of individuals who had trouble paying off medical bills during past twelve month
  
      ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean percentage of adults that have trouble paying off medical bills for states that expanded coverage = Mean percentage of adults that have trouble paying off medical bills for states that have not expanded coverage. 
       
      ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,bills != Mean_not_expanded,bills

## Conclusion


## Future Steps
In the future I would like to collect more data on health care cost, spending, and quality to see how they have been effected by the affordable care act, and possibly try to expand the data to compare the United States health and healthcare to other countries. 
