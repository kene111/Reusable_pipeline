# import Library
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import  f1_score
    

def model_testing(x_test, y_test, model):

    x_test_ = np.load(x_test)
    y_test_ = np.load(y_test)

    model = joblib.load(model)


    y_pred = model.predict(x_test_)

    

    # accuracy of test set f1-score
    f1_score_ = f1_score(y_test_, y_pred,average='micro')
    
    # write predictions to results.txt
    with open('results.txt','w') as result:
        result.write(f'F1 score: {f1_score_}  \n\n Prediciton: {RFC_pred} | Actual {y_test}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_test')
    parser.add_argument('--y_test')
    parser.add_argument('--model')
    args = parser.parse_args()
    model_testing(args.x_test, args.y_test, args.model)
    
