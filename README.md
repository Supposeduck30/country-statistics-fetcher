# Country Statistics Fetcher
## A fully functional program written in python that can return any one of 8 statistics of a country
This program incorporates the use of the REST Countries API, which allows the program to fetch real time statistics of a country. This program:
- Asks you what country you want to research
- Give you a list of statistics you can search 
- Uses the API to access real time statistics and outputs it

## Version History 

### 1.0.0
- Terminal based
- Asks which country to focus on
- Lists 8 different statistics that can be fetched 
 - Population
 - Regon
 - Subregion
 - Capital
 - Area
 - Timezones 
 - Currency
 - Languages 

## How to run 
1. Clone the repository

2. (OPTIONAL) Create and activate a virtual environment
```
python3 -m venv venv        # create venv
# Activate the venv
source venv/bin/activate    # Linux/macOS
.\venv\Scripts\activate     # Windows PowerShell
```

3. Install the required package
```
pip install requests
```

4. Run the script
```
python country_statistics.py
```

## How it works 
1. It asks for a country name input
   
2. It then sends a request to the REST Countries API to fetch data from that country
   
3. It lists the available statistics
   
4. User chooses a statistic 

5. The program fetches the statistic from the API and prints it 

## Output 
```
Which country? india

Available statistics:
  • population
  • region
  • subregion
  • capital
  • area
  • timezones
  • currencies
  • languages

Which statistic? population

Population for India: 1380004385
```
## Upcoming Features
- More statistics will be coming 

## Known Issues 
- May not be completely up to date (depends on how often the API gets updated)
- Doesn’t list all the languages of a certain country
- Needs internet connection to access the API 
