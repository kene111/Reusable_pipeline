# import Library
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import  f1_score
import pandas
import argparse
    

def model_training(clean_data):
    
    
    # deserialize clean data from output directory
    all_data = joblib.load(clean_data)

    # create features and targets
    X = all_data.drop(columns=['Accident_Index', 'Accident_Severity'])
    y = all_data['Accident_Severity']
    
    # split data based on y categories
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=1)
    
    # import model
    RFC = RandomForestClassifier(random_state=1)

    #fit train set
    RFC.fit(x_train, y_train)

    #saving the x_test and y_test
    np.save('x_test.npy', x_test)
    np.save('y_test.npy', y_test)

    # saving the model

    joblib.dump(RFC , 'model.pkl')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean_data')
    args = parser.parse_args()
    model_training(args.clean_data)