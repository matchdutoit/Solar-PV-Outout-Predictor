import requests
import pandas as pd
import numpy as np
import time
import sys

# c = {'lat': [36, 36, 37, 37], 'lon': [45, 46, 47, 48]}
# coords = pd.DataFrame(c)


def get_nasa(latlondf):
    json_list = []
    for i in latlondf.index:
        time.sleep(4)
        lat = latlondf.at[i,'lat']
        lon = latlondf.at[i,'lon']
        year = latlondf.at[i,'year']
        
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
                'start_date': int(year),
                'end_date': int(year),
                'temp_average': 'INTERANNUAL',
                'lat': lat,
                'lon': lon
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
        json_list.append(json)
        
    return json_list



def join_coords(json_list):
    """
    This function takes the list of jsons, extracts the annual averages for each parameter, and returns a new
    dataframe with the params for each lat/lon pair.
    """
    serieslist = []
    for i, el in enumerate(json_list):
        data = el['features'][0]['properties']['parameter']
        df = pd.DataFrame(data)
        series = df.iloc[-1,:]
        serieslist.append(series)

    attributes = pd.concat(serieslist, axis=1).T
    attributes.reset_index(drop=True, inplace=True)
    df = coords.join(attributes)
    return df


if __name__ == "__main__":
    # Import lat/lon csv to df
    coords = pd.read_csv('data/df_lly_test.csv')
    # Run api request to get nasa power data
    json_list = get_nasa(coords)
    # Join data onto existin lat/lon dataframe
    df = join_coords(json_list)
    df.to_csv('data/weather_test',index=False)





