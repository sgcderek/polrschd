# polrschd
Python script for predicting NOAA POES GAC transmissions.  
The script will access the public NOAA schedule file at https://noaasis.noaa.gov/cemscs/polrschd.txt and parse events related to POES GAC (NOAA-15, NOAA-18, NOAA-19). It will then display the UTC/local time and date at which a satellite begins and ends its GAC transmission, as well as the frequency, polarization, and elevation of the satellite.  

GAC transmissions can be subsequently demodulated and decoded by [LeanHRPT-Demod](https://github.com/Xerbo/LeanHRPT-Demod/) and [LeanHRPT-Decode](https://github.com/Xerbo/LeanHRPT-Decode/tree/gac) respectively.

![thumbnail](https://github.com/sgcderek/polrschd/blob/main/thumbnail.jpeg?raw=true)

## Installation

Clone repository
```bash
git clone https://github.com/horsaen/polrschd.git && cd polrschd
```

Install dependencies
```bash
pip3 install -r requirements.txt
```

## Usage

Edit [main.py](main.py) to set required parameters, then simply run the script
```bash
python3 main.py
```
