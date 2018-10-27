#Reading data from https://github.com/fivethirtyeight/guns-data
import csv
f=open("guns.csv","r")
data=list(csv.reader(f))
#Previewing the dataset in order to figure an approach
print(data[:5])

#Removing header for easier data manipulation
headers=data[:1]
data=data[1:]
print(headers)
#Previewing data without header row
print(data[:5])

#Determing the gun deaths per year
year_counts={}
years=[row[1] for row in data]
for year in years:
    if year in year_counts:
        year_counts[year]+=1
    else:
        year_counts[year]=1

#Checking the extracted data
print(year_counts)

#Determine the number of fatalities per date
import datetime

date=[datetime.datetime(year=int(row[1]),month=int(row[2]),day=1) for row in data]
print(date[:5])

date_counts={}
for row in date:
    if row in date_counts:
        date_counts[row]+=1
    else:
        date_counts[row]=1

#Checking the extracted data
print(date_counts)

#Insight regarding gun fatalities due to variance by gender and race
sex_column=[sex_rows[5] for sex_rows in data]
sex_counts={}
for rows in sex_column:
    if rows in sex_counts:
        sex_counts[rows]+=1
    else:
        sex_counts[rows]=1
        
race_column=[race_rows[7] for race_rows in data]
race_counts={}
for rows in race_column:
    if rows in race_counts:
        race_counts[rows]+=1
    else:
        race_counts[rows]=1

#Checking the extracted data
print(sex_counts)
print(race_counts)

#Obtaining data for percentage per racial category in the US
import csv

f=open("census.csv","r")
census=list(csv.reader(f))

#Preview of census data
print(census)

#Counts of firearm fatality by race per 100,000 people
sex_column=[sex_rows[5] for sex_rows in data]
sex_counts={}
for rows in sex_column:
    if rows in sex_counts:
        sex_counts[rows]+=1
    else:
        sex_counts[rows]=1
        
race_column=[race_rows[7] for race_rows in data]
race_counts={}
for rows in race_column:
    if rows in race_counts:
        race_counts[rows]+=1
    else:
        race_counts[rows]=1
        
mapping = {"Asian/Pacific Islander": 15159516 + 674625,
           "Native American/Native Alaskan": 3739506,
           "Black": 40250635,
           "Hispanic": 44618105,
           "White": 197318956}

race_per_hundredk={}
for k,v in race_counts.items():
    race_per_hundredk[k]=v*100000/mapping[k]
    
#Checking the extracted data
print(race_per_hundredk)

#Gain insight into the intent of the incidents and see which are Homicide

intents=[rows[3] for rows in data]
races=[rows[7] for rows in data]

homicide_race_counts={}

for i,race in enumerate(races):
    if intents[i]=='Homicide':
        if race in homicide_race_counts:
            homicide_race_counts[race]+=1
        else:
            homicide_race_counts[race]=1

mapping = {"Asian/Pacific Islander": 15159516 + 674625,
           "Native American/Native Alaskan": 3739506,
           "Black": 40250635,
           "Hispanic": 44618105,
           "White": 197318956}

for k,v in race_counts.items():
    race_per_hundredk[k]=v*100000/mapping[k]

#Let's see if there is any link between month and homicide rate.
month_homicide={}
total_homicide=0
for row in data:
    month=row[2]
    total_homicide+=1
    if month in month_homicide:
        month_homicide[month]+=1
    else:
        month_homicide[month]=1

for each in month_homicide.keys():
    month_homicide[each]=month_homicide[each]/total_homicide
    
month_homicide
#Judging by the homicide rates of each month, we can conclude there is
#no link between the months and the homicide rates. Each month looks about
#the same with the exception for February. Maybe people are less likely to be
#in a murdering mood with the presence of Valentine's?...
#Taking a second look, there seems to be a higher homicide rate during the warmer
#months of summer.

#Let's see if there are any links between homicide rate and gender.
gender_homicide={}
for row in data:
    gender=row[5]
    if gender in gender_homicide:
        gender_homicide[gender]+=1
    else:
        gender_homicide[gender]=1

for each in gender_homicide.keys():
    gender_homicide[each]=gender_homicide[each]/total_homicide
    
gender_homicide

'''
There is a definite link between gender and homicide. Males are more likely to commit
homicide than females. This is a fair sanity check with reality...
'''

#Let's see if there any links between education and the probability of
#committing homicides. Hypothesis is that if perpetrator has lower education
#level, he or she is more likely to commit a homicide.
education_homicide={}
for row in data:
    education=row[10]
    if education=='1':
        education='1 Less than High School'
    if education=='2':
        education='2 Graduated from High School or equivalent'
    if education=='3':
        education='3 Some College'
    if education=='4':
        education='4 At least graduated from College'
    if education=='5':
        education='5 N/A'
    if education=='NA':
        education='5 N/A'
    if education in education_homicide:
        education_homicide[education]+=1
    else:
        education_homicide[education]=1
        
for each in education_homicide.keys():
    education_homicide[each]=education_homicide[each]/total_homicide
    
education_homicide
'''
Interestingly, people who graduated high school but did not pursue high education
are more likely to commit homicides. This definitely goes against my hypothesis because
the percentage rate for people with less than high school is not higher than that of those
that did graduated from high school
'''