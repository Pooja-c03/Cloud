import threading
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target
data['species'] = data['target'].apply(lambda x: iris.target_names[x])

data_sort = data.sort_values(by='petal length (cm)', ascending=False)

def large():
    with open('output_file1.txt', 'w') as f:
        for species in iris.target_names:
            species_data = data_sort[data_sort ['species'] == species].head(3)
            f.write(f"Largest 3 flowers for {'species'}: \n")
            f.write(species_data.to_string(index=False) + "\n\n")
    print("Largest flowers written")

def small():
    with open('output_file2.txt', 'w') as f:
        for species in iris.target_names:
            species_data = data_sort[data_sort ['species'] == species].tail(3)
            f.write(f"Smallest 3 flowers for {'species'}: \n")
            f.write(species_data.to_string(index=False) + "\n\n")
    print("Smallest flowers written")

t1 = threading.Thread(target=large)
t2 = threading.Thread(target=small)

t1.start()
t2.start()

t1.join()
t2.join()
