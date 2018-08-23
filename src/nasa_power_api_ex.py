import requests
import pandas as pd

"""
Some Useful Parameters:
- ALLSKY_SFC_SW_DWN: All Sky Insolation Incident on a Horizontal Surface (kwh/m2/day)
- T2M: temperature at 2 meters from gound (C)
- PRECTOT: precipitation (mm/day)
- PS: Surface Pressure (kPa)
- WS2M: Wind Speed at 2 Meters (m/s)
- KT: Insolation Clearness Index (dimensionless)
- DNR: Direct Normal Radiation (kWh/m^2/day)
- DIFF: Diffuse Radiation On A Horizontal Surface (kWh/m^2/day)

for more documentation: https://power.larc.nasa.gov/docs/v1/
"""

parameters = 'ALLSKY_SFC_SW_DWN', 'KT', 'T2M', 'PRECTOT', 'PS', 'WS2M'
parameters = ','.join(parameters)

api_kwds = \
    {
        'user': 'anonymous',
        'parameters': parameters,
        'start_date': 2016,
        'end_date': 2016,
        'temp_average': 'INTERANNUAL',
        'lat': 36,
        'lon': 45
    }

base = ('https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&identifier=SinglePoint&'
        'parameters={parameters}&'
        'startDate={start_date}&'
        'endDate={end_date}&'
        'userCommunity=SSE&'
        'tempAverage={temp_average}&'
        'outputList=JSON,ASCII&'
        'lat={lat}&'
        'lon={lon}&'
        'user={user}')

url = base.format(**api_kwds)
response = requests.get(url)
json = response.json()
data = json['features'][0]['properties']['parameter']
df = pd.DataFrame(data)
df.index = pd.to_datetime(df.index)
