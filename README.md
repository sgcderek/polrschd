# polrschd
Python script for predicting NOAA POES GAC transmissions.  
The script will access the public NOAA schedule file at https://noaasis.noaa.gov/cemscs/polrschd.txt and parse event related to POES GAC (NOAA-15, NOAA-18, NOAA-19). It will then display the UTC time and date at which a satellite begins and ends its GAC transmission, as well as the frequency, polarization, and elevation of the satellite.  

GAC transmissions can be subsequently demodulated and decoded by [LeanHRPT-Demod](https://github.com/Xerbo/LeanHRPT-Demod/) and [LeanHRPT-Decode](https://github.com/Xerbo/LeanHRPT-Decode/tree/gac) respectively.

![thumbnail](https://github.com/sgcderek/polrschd/blob/main/thumbnail.jpeg?raw=true)

## Requirements
The script uses urllib, datetime and pyorbital. Only pyorbital is a non-default library and can be installed with pip

## Usage
Very basic usage for now; open polrschd.py3 and change the four parameters at the beginning of the file (input your latitude, longitude, altitude ASL and minimum satellite elevation).  
Once configured, you can run the script and get a list of GAC transmissions available for your area. Make sure to then check the full pass with your normal prediction app (such as gpredict, Look4sat, etc.)
