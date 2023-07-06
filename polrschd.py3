
########################################################################
########################### PREDICT SETTINGS ###########################
########################### (change  these!) ###########################
########################################################################

yourLat = 78.22   # Your latitude
yourLon = 15.39   # Your longitude
yourAlt = 400     # Your altitude (meters above sea level)
minElevation = -2 # Minimum elevation of the GAC event (can be negative)

########################################################################
########################################################################


import urllib.request, os, time
from datetime import datetime
from pyorbital.orbital import Orbital

# https://code.it4i.cz/blender/blender-embree3/-/blob/sculpt25/tools/bcolors.py
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

polrschdURL = "https://noaasis.noaa.gov/cemscs/polrschd.txt" # polrschd.txt URL
polrschdLocal = "polrschd.txt"
polrschdExpire = 260000

print(f"{bcolors.OKCYAN}{bcolors.BOLD}Calculating GAC events for following conditions;{bcolors.ENDC}")
print(f"{bcolors.OKCYAN}Receiver latitude:  ",yourLat,"˚")
print("Receiver longitude: ",yourLon,"˚")
print("Receiver altitude:  ",yourAlt,"m")
print("Min. sat. elevation:", minElevation,f"˚{bcolors.ENDC}")

orbitalNOAA15 = Orbital("NOAA-15")
orbitalNOAA18 = Orbital("NOAA-18")
orbitalNOAA19 = Orbital("NOAA-19")

# Use local file if recent enough (to reduce number of requests)
if (os.path.isfile(polrschdLocal)):
	if (time.time() - os.path.getmtime(polrschdLocal)) > polrschdExpire:
		print("Local file expired, will download")
		urllib.request.urlretrieve(polrschdURL, polrschdLocal)
	else:
		print("Using local file")
else:
	print("Local file not found, will download")
	urllib.request.urlretrieve(polrschdURL, polrschdLocal)

for line in open(polrschdLocal, 'r'): # open txt, read each line
	text = line[:-1] # strip newline
	date = text[0:17] # get date from line
	dateParsed = datetime.strptime(date, '%Y/%j/%H:%M:%S') # parse date from weird format YYYY/DDD/HH:MM:SS
	satID = text[23:25] # get satellite number from line
	
	# parse satellite number ID into name
	if (satID == "01"):
		satIDParsed = "MetOp-B"
	elif (satID == "02"):
		satIDParsed = "MetOp-A"
	elif (satID == "03"):
		satIDParsed = "MetOp-C"
	elif (satID == "15"):
		satIDParsed = "NOAA-15"
		satellite = orbitalNOAA15
	elif (satID == "18"):
		satIDParsed = "NOAA-18"
		satellite = orbitalNOAA18
	elif (satID == "19"):
		satIDParsed = "NOAA-19"
		satellite = orbitalNOAA19
	else:
		satIDParsed = satID
	
	# Determine frequency from transmitter ID	
	if "LSB" in text:
		txFreq = "1698.0 MHz RHCP"
	elif "MSB" in text:
		txFreq = "1702.5 MHz LHCP"
	elif "HSB" in text:
		txFreq = "1707.0 MHz RHCP"
	elif "ESB" in text:
		txFreq = "2247.5 MHz RHCP"
	else:
		txFreq = "Unknown Frequency"
			
	# Determine type of event	
	if "PBK,START,GAC" in text:
		eventType = "Start of GAC transmission"
	elif "PBK,END,GAC" in text:
		eventType = "End of GAC transmission  "
	else:
		eventType = "other"
		
	if ((eventType == "Start of GAC transmission") | (eventType == "End of GAC transmission  ")):

		# Compute observed elevation of satellite during event
		elevation = (round(satellite.get_observer_look(dateParsed, yourLon, yourLat, yourAlt/1000)[1]))
		elStr = str(elevation)+"°"
		
		# Set print color
		if ((elevation > 5) & (eventType == "Start of GAC transmission")):
			printCol = f"{bcolors.BOLD}{bcolors.OKGREEN}"
		elif ((elevation >= 0) & (eventType == "Start of GAC transmission")):
			printCol = f"{bcolors.OKGREEN}"
		elif ((elevation >= 0) & (eventType == "End of GAC transmission  ")):
			printCol = f"{bcolors.WARNING}"
		else:
			printCol = f"{bcolors.FAIL}"
			
		if (elevation >= minElevation):
			print(printCol, dateParsed, satIDParsed, eventType, txFreq, elStr, f"{bcolors.ENDC}")
