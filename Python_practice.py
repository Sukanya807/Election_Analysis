print ("Hello World")
print ("hello world")
counties=["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties:
    print("True")
else:
    print("False")    

if "El Paso" not in counties:
    print("True")
else:
    print("False")

if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")     



counties_tuple=["Arapahoe","Denver","Jefferson"]
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for county,voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for county in counties_dict.values():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
for county,voters in counties_dict.items():
    print(str(county)+" county"+" has"+" "+str(voters)+" "+"registered voters.")

voting_data=[{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]
for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]["county"])

for i in range(len(voting_data)):
    print(voting_data[i]["registered_voters"])

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict.values())

for county_dict in voting_data:
    for value in counties_dict:
        print(value)

for county_dict in voting_data:
    print(county_dict["registered_voters"])

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for county,voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

voting_data=[{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]
for county_dict in voting_data:
    print(county_dict)

for counties_dict in voting_data:
    
            print(f"{counties_dict['county']} county has {counties_dict['registered_voters']:,} registered voters.")
name="Sukanya"
country="United States"
age=25
hourly_wage=15
satisfied=True
daily_wage=hourly_wage*8
print(f"Your name is {name}")
print(f"You live in {country}")
print(f"You are {age} years old")
print(f"You make ${daily_wage} per day")
print(f"Are you satisfied with your current wage?{satisfied}")