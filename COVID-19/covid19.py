###start date: 23/04/2020
###finish date: 


##libraries
import operator
import requests
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv




#other functions





##graphs
def TD(x, y):
	# with open("totDeaths.csv", "w", newline="") as f:
	# 	fn = ["Day number", "Deaths"]
	# 	write = csv.DictWriter(f, fieldnames = fn)
	# 	write.writeheader()
	# 	write.writerow({"Day number": x, "Deaths": y})
	plt.title("Total Deaths")
	plt.xlabel("Days")
	plt.ylabel("Deaths")
	plt.scatter(x, y)
	plt.grid()
	plt.show()

def DD(a, b):
	#with open("dailyDeaths.csv", "w", newline="") as f:
	#	fn = ["Day number", "Deaths"]
	#	write = csv.DictWriter(f, fieldnames = fn)
	#	write.writeheader()
	#	write.writerow({"Day number": a, "Deaths": b})

	plt.xlabel("Days")
	plt.ylabel("Deaths")
	plt.scatter(a, b)
	plt.plot(a, b)
	plt.title("Daily Deaths")

	plt.grid()
	plt.show()

##machine Learn


##main
URL = requests.get("https://www.worldometers.info/coronavirus/worldwide-graphs/") #gets the page

page = soup(URL.content, "html.parser") #parses the page

containers = page.findAll("strong")
i = []
n = 0

#getting deaths
for container in containers:
	container = container.get_text()
	if "," in container:
		container = container.replace(",", "")
	try:
		i.append(int(container))
		n += 1
	except ValueError:
		continue

n = int(n/2)
days = n 

#getting dates
dates = []
D = page.findAll("div", {"align":"left"})
for d in D:
	d = d.get_text()
	d = d.strip("\xa0")
	
numberOfDays = []

#total deaths
totDeaths = i
totDeaths = totDeaths[:len(totDeaths) - days] #removes the first part of the list aka dailyDeaths
totDeaths = totDeaths[::-1] #reverses the list
# totDeathsArr = np.array(totDeaths)
# totDeathsLog = np.log(totDeathsArr)

#dailyDeaths
dailyDeaths = i
dailyDeaths = dailyDeaths[::-1] #reverses the list because it has dailyDeaths + totDeaths
dailyDeaths = dailyDeaths[:len(dailyDeaths) - days] #removes the second part of the list aka totDeaths, just leaving the dailyDeaths
dailyDeathsArr = np.array(dailyDeaths) #turns the list into an array
for a in range(len(dailyDeaths)):
        numberOfDays.append(a+1)

# numberOfDaysArr = np.array(numberOfDays)
# numberOfDaysLog = np.log(numberOfDaysArr)

TD(numberOfDays, totDeaths)
DD(numberOfDays, dailyDeaths)

# print(numberOfDaysArr)
