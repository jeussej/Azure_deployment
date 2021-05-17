import pandas as pd
from joblib import dump
import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    # load data
    df = pd.read_csv("./data/Lol_Games.csv")
    X= df[["kills", "deaths" , "goldDiff" , "expDiff"]].copy()
    Y=df["hasWon"]
    
    x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.4, shuffle=True)


    assert x_train.shape[0] == y_train.shape[0]

    # make model
    forest=RandomForestClassifier()

    forest.fit(x_train,y_train)

    score = forest.score(x_test, y_test)
    
    print("Score:", score)
    
    # we could now retrain best_clf on all data, or do some model averaging
    # we will simply store it however
    dump(forest, "./models/clf.bin")
    
    with open('./models/clf.pkl', 'wb') as model_pkl:
        pickle.dump(forest, model_pkl)
    
    

       
    
    
    