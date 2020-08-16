from glassdoor_scrap import get_jobs
import pandas as pd

#This line will open a new chrome window and start the scraping.
#df = get_jobs("data scientist", 2000, False)
#df.to_csv("jobs.csv", sep=',')

jobs = pd.read_csv("jobs.csv")
print(jobs.describe())
