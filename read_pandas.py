import pandas as pd
import plotly.express as px

def read_csv(data,colnames):
    df = pd.read_csv(data, sep=',', usecols = colnames,header =0)    
    df.columns = ["Duration","HR","Power"]
    return df

def make_plot(df):
    fig = px.line(df.head(2000), x = "Zeit in ms", y = "Messwerte in mV")
    return fig

def set_zones(df,MaxHR):
    HR = df.iloc[:,1]
    z1 = []
    z2 = []
    z3 = []
    z4 = []
    z5 = []
    for i in HR:
        if MaxHR * 0.5 <= i and MaxHR * 0.6 >= i:
            z1.append(True)
        else:
            z1.append(False)
        if MaxHR * 0.6 < i and MaxHR * 0.7 >= i:
            z2.append(True)
        else:
            z2.append(False)
        if MaxHR * 0.7 < i and MaxHR * 0.8 >= i:
            z3.append(True)
        else:
            z3.append(False)
        if MaxHR * 0.8 < i and MaxHR * 0.9 >= i:
            z4.append(True)
        else:
            z4.append(False)
        if MaxHR * 0.9 < i and MaxHR * 1 >= i:
            z5.append(True)
        else:
            z5.append(False)
    df["Z1"] = z1
    df["Z2"] = z2
    df["Z3"] = z3
    df["Z4"] = z4
    df["Z5"] = z5

    return df
