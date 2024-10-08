import cdsapi
import sys

dataset = "reanalysis-era5-single-levels-monthly-means"
variables = ['sea_surface_temperature',
              '2m_temperature',
                'total_precipitation',
                'total_cloud_cover',
                'total_column_water_vapour',
                'mean_sea_level_pressure',
                'vertical_integral_of_eastward_water_vapour_flux',
                'vertical_integral_of_northward_water_vapour_flux']  # Add the list of variables you want to download

# Initialize the client
client = cdsapi.Client()

# Loop through each variable
for variable in variables:
    # Create a filename dynamically using the variable name
    filename = f"reanalysis-era5-single-levels-monthly-means-{variable}.nc"
    print(f"Downloading data for {variable} to {filename}")
    
    # Update the request for the current variable
    request = {
        'product_type': ['monthly_averaged_reanalysis'],
        'variable': [variable],
        'year': ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        'month': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        'time': ['00:00'],
        'data_format': 'netcdf',
        'download_format': 'unarchived'
    }
    
    # Retrieve and download the dataset for the current variable
    client.retrieve(dataset, request).download(filename)
    print(f"Download complete for {variable}")


