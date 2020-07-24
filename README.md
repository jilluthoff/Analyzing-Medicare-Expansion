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
* [Future Work](#future-work)

## Technologies
Project created with:
* Python
* Pandas
* Matplotlib/Seaborn
* Excel
* Pingouin
* Scipy

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

Question: Do states that have expanded Medicaid Coverage differ in public health characteristics?
  1. Death rates due to heart disease
        $$ H_0: \ \mu_E \leq \mu_N $$
  
  
  2. Death rates due to cancer
  
  
  3. Reported Poor Health
  
  
  4. Reported Poor Mental Health

Question: Do states that have expanded Medicaid Coverage differ in access to healthcare?
  1. Percentage of Uninsured Adults
  
  2. Reported inability to get care due to cost
  
  3. Rates of individuals who had trouble paying off medical bills during past twelve month

## Conclusion
