import pandas as pd


def main():
    data = pd.read_csv('data.csv')
    print(data.head())
    return data



if __name__ == '__main__':
    main()