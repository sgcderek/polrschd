# polrschd
Python script for predicting NOAA POES GAC transmissions.  
The script will access the public NOAA schedule file at https://noaasis.noaa.gov/cemscs/polrschd.txt and parse event related to POES GAC (NOAA-15, NOAA-18, NOAA-19). It will then display the time at which a satellite begins and ends its GAC transmission, as well as the frequency, polarization, and elevation of the satellite

## Requirements
The script uses urllib, datetime and pyorbital. Only pyorbital is a non-default library and can be installed with pip

## Usage
Very basic usage for now; open polrschd.py3 and change the four parameters at the beginning of the file (input your latitude, longitude, altitude ASL and minimum satellite elevation).  
Once configured, you can run the script.
