# Is there a difference? Analyzing whether the Affordable Care Act helped increase health in states that adpoted and implemented the expansion.  

![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/STATES_MEDICARE.png)

With the 2020 election on the horizon and healthcare reform as a major discussion point, this project intended to better understand if the Affordable Care Act (aka Obamacare), which gave states the option to expand their Medicaid programs, actually made a difference in the health of adults between the ages of 19-64. 


## Table of contents
* [Background](#background)
* [Technologies](#technologies)
* [Data Acquisition](#data-acquisition)
* [Data Processing](#data-processing)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Hypothesis Testing](#hypothesis-testing)
* [Conclusion](#conclusion)
* [Future Steps](#future-steps)

## Background 

Health is a strong indicator of quality of life, and provides insight into access to nutrition, economic challenges and other barriers to health that may persist within a state's population. Medicaid is the nation's public health insurance program for people with low incomes, who would otherwise lack access to affordable health insurance. It limits out-of-pocker costs and covers a broad array of health services. 

The Affordable Care Act (ACA) was passed in 2010 and implented in many states in 2014. It had 3 main goals:
1. Make health insurance more afforadable and available to more people by providing subsities to households with incomes between 100 and 400% of the federal poverty level.
2. Expand the Medicaid program to cover all adults with income below 138% of the federal poverty level ($17,236 for an individual in 2019. *Not all states have expanded their programs
3. Support innovative medical care delivery methods designed to lower the cost of health care generally. 

Coverage for Medicaid expansion adults (people between the ages 19 - 64 who are low income) contains the ACA’s ten “essential health benefits” which include preventive services and expanded mental health and substance use treatment services. Medicaid plays an important role in addressing the opioid epidemic and more broadly in connecting Medicaid beneficiaries to behavioral health (addiction - drinking, smoking, eating) services. 

## Technologies
Project created with:
 - Python
 - Pandas
 - Matplotlib/Seaborn
 - Excel
 - Pingouin
 - Scipy

## Data Acquisition 

Health is best measured by looking at the state's public health (rate of disease), access to healthcare, and quality of care. 

The data used for analysis in this project was pulled from CDC WONDER and the United States Census Bureau and included the following datasets:

  - State Public Health Datasets:
    - Heart Disease Death Rate per 100,000 
    - Cancer Death Rate per 100,000
    - Stroke Death Rate per 100,000
    - Adults Self Reported Mental Health Status in the Last 30 Days
    - Adults Self Reported Health Status
    - Adults that Smoke
    - Adults that are Overweight or Obese
    - Suicide Rate
    - Mortality Rate
    - Life Expectancy
      
  - State Access to Healthcare Datasets:
    - State Uninsured Rates
    - Rates of individuals who had trouble paying off medical bills during past twelve month
    - Percent of adults who could not get medical care when needed due to cost


## Data Processing
The data was pulled from each website and loaded into a single excel file:
   - All states All Data Collected.xlsx contains all data collected for every state  
  
Then the data was read into pandas and split into two subgroup:
   - states that had adopted and expanded Medicare coverage
   - states that had either not adpoted and/or expanded Medicare coverage as of 2018. 

## Exploratory Data Analysis

The histograms of all the data sets collected show that the majority of the data is normally distributed. 

![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/All_States_All_Data_Histograms.png)

The heatmap matrix shows general correlations between the different dataset, and I am hoping to find differing correlations with the split datasets. 

![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Heatmap_all_States.png)

Now separating the data and looking at histograms of the datasets for states that did expand coverage, you can see that most the data appears to be normally distributed.

![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Expanded_Histograms.png)

The Heatmap matrix shows correlations decreasing between poor health characteristics (obesity, death rates, etc) and categories associated with low access to health care (uninsured rates etc), and correlations seem to be increase between good health characteristics (good mental health, etc.) and categories associated with low access to care. 

![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Heatmap_states_expanded.png)

The histograms for states that did not increase coverage show the data seems to be relatively normally distributed. 

![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Not_Histograms.png)

Looking at the correlation between categories for states that  did not expand coverage has some interesting trends as well. 

![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Heatmap_States_NOT.png)


## Hypothesis Testing

Welch's t-test was used to answer if the means of the two samples (states with expanded medicare coverage vs states without expanded medicare coverage) were equal because the samples differ in size and therefore the variance is unequal. It was also assumed the two sample distributions of each category were normally distributed, which can be inferred from the histograms above. 

Question: Do states that have expanded Medicaid Coverage differ access and public health characteristics than states that do not?

![formula](https://render.githubusercontent.com/render/math?math=\alpha=0.05)

A Bonferroni correction is used to compensates for testing each individual hypothesis simultaneously, therefore the following tests will use a significance level of ![formula](https://render.githubusercontent.com/render/math?math=\alpha/20).

So, ![formula](https://render.githubusercontent.com/render/math?math=\alpha=0.0025)

 To answer the question, the follow test have the hypothesis: 
  
   ![formula](https://render.githubusercontent.com/render/math?math=H_0:) Mean expanded coverage = Mean not expanded coverage. 
   
   ![formula](https://render.githubusercontent.com/render/math?math=H_A:) Mean_expanded,hd != Mean_not_expanded,hd    
  

1. Death rates due to heart disease:
  
  ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_HD.png)

       Mean_expanded,hd: 160.2 deaths per 100,000
       
       Mean_not_expanded,hd: 170.9 deaths per 100,000

       T-Statistic: -1.31633, P-Value: 0.19616, P < alpha: False
     
       Reject the null hypothesis, there is no difference in rates of heart disease deaths.
     
 
2. Death rates due to cancer:
 
  ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_Cancer.png)
  
       Mean_expanded,cancer: 149.7 deaths per 100,0000
       
       Mean_not_expanded,cancer: 154.5 deaths per 100,000
  
       T-Statistic: -1.1487, P-Value: 0.2578, P < alpha: False
      
       Reject the null hypothesis, there is no difference in rates deaths due to cancer.
  
  
3. Death rates due to stroke:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_Stroke.png)
  
       Mean_expanded,stroke: 149.7 deaths per 100,0000
       
       Mean_not_expanded,stroke: 154.5 deaths per 100,000
     
       T-Statistic: -2.3968, P-Value: 0.0216, P < alpha: False
     
       Reject the null hypothesis, there is no difference in rates deaths due to stroke.
    
  
4. Death rates due to suicide:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_suicide.png)
  
       Mean_expanded,suicide:  15.9 deaths per 100,0000
        
       Mean_not_expanded,suicide: 17.3 deaths per 100,0000
     
       T-Statistic: -1.1916, P-Value: 0.2395, P < alpha: False
     
       Reject the null hypothesis, there is no difference in deaths due to suicide.
       
  
 5. Mortality rates:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_Mortality.png)
  
       Mean_expanded,mortality:  728.5 per 100,0000
        
       Mean_not_expanded,mortality: 778.4 per 100,0000
     
       T-Statistic: -2.0245, P-Value: 0.0494, P < alpha: False
     
       Reject the null hypothesis, there is no difference in mortality rates.
       
 
 6. Life Expectancy:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_LE.png)
  
       Mean_expanded,suicide:  79.04
        
       Mean_not_expanded,suicide: 78.13
     
       T-Statistic: 1.8499, P-Value: 0.0713, P < alpha: False
     
       Reject the null hypothesis, there is no difference in life expectancy.

 
 7. Percent adults that are overweight or obese:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_Overweight.png)
  
       Mean_expanded,obesity:  65.6% adults are overweight or obese
        
       Mean_not_expanded,obesity: 67.6% adults are overweight or obese
     
       T-Statistic: -2.4229, P-Value: 0.0194, P < alpha: False
     
       Reject the null hypothesis, there is no difference in rates of obesity.
  
 
 8. Percent adults that smoke:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_Smoke.png)
 
       Mean_expanded,smoke: 16.4% of adults that smoke
        
       Mean_not_expanded,smoke: 17.0% of adults that smoke
     
       T-Statistic: -0.6858, P-Value: 0.4964, P < alpha: False
      
       Reject the null hypothesis, there is no difference in rates of adults that smoke
       
  
 9. Percent of adults that report excellent health
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_ExcH.png)
  
       Mean_expanded,excellent_health:  17.8% of adults report excellent health
        
       Mean_not_expanded,excellent_health: 17.1% of adults report excellent health
     
       T-Statistic: 1.2078, P-Value: 0.2337, P < alpha: False
     
       Reject the null hypothesis, there is no difference in percent of adults that report excellent health. 
       

 10. Percent of adults that report very good health
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_VGHealth.png)
  
       Mean_expanded,very_good_health:  32.6% of adults report very good health
        
       Mean_not_expanded,very_good_health: 32.4% of adults report very good health
     
       T-Statistic: 0.2440, P-Value: 0.8085, P < alpha: False
     
       Reject the null hypothesis, there is no difference in percent of adults that report very good health.
       
   
 11. Percent of adults that report good health
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_suicide.png)
  
       Mean_expanded,good_health:  31.9% of adults report good health
        
       Mean_not_expanded,good_health: 31.9 of adults report good health
     
       T-Statistic: -0.0725, P-Value: 0.9425, P < alpha: False
     
       Reject the null hypothesis, there is no difference in percent of adults that report very good health.
       
       
  12. Percent of adults that report fair health:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_Fair_Health.png)
  
       Mean_expanded,fair_health:  13.0% of adults report fair health
        
       Mean_not_expanded,fair_health: 13.3% of adults report fair health
     
       T-Statistic: -0.5396, P-Value: 0.5922, P < alpha: False
     
       Reject the null hypothesis, there is no difference in percent of adults that report fair health     
       
 
  13. Percent of adults that report poor health:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_Poor_Health.png)
  
       Mean_expanded,poor_health: 4.6% of adults report poor health
        
       Mean_not_expanded,poor_health: 5.2% of adults report poor health
     
       T-Statistic: -1.4605, P-Value: 0.1522, P < alpha: False
     
       Reject the null hypothesis, there is no difference in percent of adults that report poor health
       
  
  14. Report Excellent Mental Health (0 Poor days):
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_EXCMH.png)
  
       Mean_expanded,excellent_mental:  63.3% of adults report excellent mental health
        
       Mean_not_expanded,excellent_mental: 64.1% of adults report excellent mental health
     
       T-Statistic: -1.1081, P-Value: 0.2751, P < alpha: False
     
       Reject the null hypothesis, there is no difference the percentage of adults who reported excellent mental health.
 
  
  15. Report Good Mental Health (1-4 Poor Days):
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_GoodMH.png)
  
       Mean_expanded,good_mental:  13.7% of adults report good mental health
        
       Mean_not_expanded,good_mental: 13.0% of adults report good mental health
     
       T-Statistic: 1.5651, P-Value: 0.1259, P < alpha: False
     
       Reject the null hypothesis, there is no difference in the percentage of adults who reported good mental health.
 
 
  16. Reported Fair Mental Health (5-13 Days Poor):
 
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_FairMH.png)
  
       Mean_expanded,fair_mental:  10.2 of adults report fair mental health
        
       Mean_not_expanded,fair_mental: 9.7% of adults report fair mental health
     
       T-Statistic: 1.6392, P-Value: 0.1107, P < alpha: False
     
       Reject the null hypothesis, there is no difference in the percentage of adults who reported fair mental health. 
   
   
  17. Reported Bad Mental Health (14+ Days Poor):
 
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_BADMH.png)
  
       Mean_expanded,bad_mental:  12.8% of adults report poor mental health
        
       Mean_not_expanded,bad_mental: 13.1% of adults report poor mental health
     
       T-Statistic: -0.5301, P-Value: 0.5987, P < alpha: False
     
       Reject the null hypothesis, there is no difference in the percentage of adults who report bad mental health.
       

  18. Percentage of Uninsured Adults:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_Uninsured.png)
  
        Mean_expanded,uninisured: 9.51% of adults are uninsured
         
        Mean_not_expanded,uninsured: 15.3% of adults are unisured 
     
        T-Statistic: -5.2923, P-Value: 0.0000, P < alpha: True
     
        Do not reject the null hypothesis, there is a difference in percentage of uninsured adults in states with expanded coverage vs states without expanded coverage.
  
  
  19. Reported inability to get care due to cost:
       
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_No_care.png)
     
        Mean_expanded,cost: 11.3% of adults do not get medical care due to cost
         
        Mean_not_expanded,cost: 14.2% of adults do not get medical care due to cost
     
       T-Statistic: -4.3307, P-Value: 0.0001, P < alpha: True
  
        Do not reject the null hypothesis, there is a difference in percentage of adults who do not get care due to cost in states.
        
        
  20. Rates of individuals who had trouble paying off medical bills during past twelve month:
  
   ![alt text](https://github.com/jilluthoff/Analyzing-Medicare-Expansion/blob/master/images/Box_Trouble.png)
       
       Mean_expanded,bills: 27.1% of adults have trouble paying off their medical bills
  
       Mean_not_expanded,bills: 34.4% of adults have trouble paying off their medical bills
      
       T-Statistic: -4.8651, P-Value: 0.0000, P < alpha: True
      
       Do not reject the null hypothesis, there is a difference in percentage of adults who have trouble paying off medical bills in states the have expanded medicare versus states that have not expanded medicare.
       

## Conclusion

As expected we can say that there is a difference in access to health care, but there does not seem to be a difference in health of adults between the ages of 19-64.

## Future Steps

In the future I would like to collect more data on health care cost, spending, quality, and equality to see how they have been effected by the affordable care act, and possibly try to expand the data to compare the United States health and healthcare to other countries. 
