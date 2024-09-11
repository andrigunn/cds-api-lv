import cdsapi

dataset = "seasonal-postprocessed-pressure-levels"

variables = ['geopotential_anomaly']  

year = '2024'
month = '09'

# Initialize the client
client = cdsapi.Client()

# Loop through each variable
for variable in variables:
    # Create a filename dynamically using the variable name
    filename = f"seasonal-postprocessed-pressure-levels-{year}-{month}-{variable}.nc"
    print(f"Downloading data for {variable} to {filename}")
    
    # Update the request for the current variable
    request = {   
    'originating_centre': 'ecmwf',
    'system': '51',
     'variable': [variable],
    'pressure_level': ['500'],
    'product_type': ['ensemble_mean'],
    'year': ['2024'],
    'month': ['09'],
    'leadtime_month': ['1', '2', '3', '4', '5', '6'],
    'data_format': 'netcdf'
    }
    
    # Retrieve and download the dataset for the current variable
    client.retrieve(dataset, request).download(filename)
    print(f"Download complete for {variable}")