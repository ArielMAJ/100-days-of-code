import pandas as pd

data_dict = {
    "students": ['Ruth', 'Ringo', "barney"],
    "scores": [100,69,77]
}

data = pd.DataFrame(data_dict)

data.to_csv("pets_data.csv")