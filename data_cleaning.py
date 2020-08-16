# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:12:55 2020

@author: Miz
"""
import pandas as pd
import datetime

jobs = pd.read_csv("jobs.csv")

#Remove competitors & Headquarters
jobs = jobs.drop('Headquarters', 1)
jobs = jobs.drop('Competitors', 1)
jobs = jobs.drop('Id', 1)

#Remove -1 values (Not found)
jobs = jobs[jobs['Salary Estimate']  != '-1']

#Remove '(GlassDoor est.)' text from Salary Estimate
salary = jobs['Salary Estimate'].apply(lambda x:x.split('(')[0])

#Remove K & $
salary = salary.apply(lambda x: x.replace('K','').replace('$',''))

#Add column 'per hour' if salary provided is per hour
jobs['Hourly'] = jobs['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

#Add column employer provided salary
jobs['Employer_Provided'] = jobs['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

#Remove 'per hour' & 'employer provided salary' text
salary = salary.apply(lambda x:x.lower().replace('per hour','').replace('employer provided salary:',''))

#Add 3 columns
jobs['Min_Salary'] = salary.apply(lambda x: int(x.split('-')[0]))
jobs['Max_Salary'] = salary.apply(lambda x: int(x.split('-')[1]))
jobs['Avg_Salary'] = jobs.Min_Salary  + jobs.Max_Salary / 2

#Parse rating
jobs['Company'] = jobs.apply(lambda x: x['Company Name'] if x['Rating'] == -1 else x['Company Name'][:-3] , axis=1)
#Parse State
jobs['Job_State'] = jobs['Location'].apply(lambda x: x.split(',')[1])
#jobs['Job_State'].value_counts()
#Age column
now = datetime.datetime.now()
jobs['Company_Age'] = jobs['Founded'].apply(lambda x: x if x < 0 else now.year - x)

#jobs['Type of ownership'].value_counts()
#jobs['Industry'].value_counts()
jobs['Size'].value_counts()







