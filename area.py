import pandas as pd

df = pd.read_csv('area.csv')

ch = int(input("Enter the no of rows: "))

while ch != 0:
    lenght = float(input("Enter lenght: "))
    breadth = float(input("Enter breadth: "))
    area = lenght*breadth

    df.loc[len(df)] = [lenght, breadth, area]
    ch = ch - 1

df.to_csv('area.csv', index=False)
print(df) 