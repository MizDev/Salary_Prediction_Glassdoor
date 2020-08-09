from glassdoor_scrap import get_jobs

#This line will open a new chrome window and start the scraping.
df = get_jobs("data scientist", 5, False)
print(df)