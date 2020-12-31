import joblib
import pandas as pd
from datetime import datetime



def preprocess_data():

    # import data
    accident_data = pd.read_csv('https://raw.githubusercontent.com/Uthmanic/07-road-safety/master/data/dftRoadSafety_Accidents_2016.csv')
    vehicle_data = pd.read_csv('https://raw.githubusercontent.com/Uthmanic/07-road-safety/master/data/Veh.csv')

    all_data = pd.merge(vehicle_data, accident_data, how = 'inner', on = 'Accident_Index')

    # function for obtaining month in date column

    def month(date):
        fulldate = datetime.strptime(date, '%d/%m/%Y')
        return int(datetime.strftime(fulldate, '%m'))

    # create a coloumn for month
    all_data['Month'] = all_data['Date'].apply(month)


    # function for obtaining year in date column
    def year(date):
        fulldate = datetime.strptime(date, '%d/%m/%Y')
        return int(datetime.strftime(fulldate, '%Y'))

    # create a coloumn for year
    all_data['Year'] = all_data['Date'].apply(year)

     
    # function for obtaining hour in time column
    def hour(time):
        try:
            fulltime = datetime.strptime(time, '%H:%M')
            return int(datetime.strftime(fulltime, '%H'))
        except Exception:
            # for missing values 
            return 0
        
    # create a coloumn for hour of the day    
    all_data['Hour_of_the_day'] = all_data['Time'].apply(hour)

    # drop irrelevant columns

    all_data.drop(['LSOA_of_Accident_Location', 'Local_Authority_(Highway)', 'Time', 'Date'], axis=1, inplace=True)

    # drop rows with nan values 
    all_data.dropna(inplace=True)

    # serialize clean data
    joblib.dump(all_data , 'clean_data')
        
         
if __name__ == '__main__':
    print('Preprocessing data...')
    preprocess_data()