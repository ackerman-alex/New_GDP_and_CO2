import pandas as pd
import matplotlib.pyplot as plt
import seaborn.objects as so
import seaborn as sns
from matplotlib import style

print("Alex")

url = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"

c = pd.read_csv(url)

# print(c)

columns = [
    "Mortality rate, infant (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
    "Country Name",
]

df = c[columns]

my_chart = (
    so.Plot(
        df,
        x="GDP per capita (constant 2010 US$)",
        y="Mortality rate, infant (per 1,000 live births)",
    )
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Log GDP and Under-5 Mortality")
    .theme({**style.library["seaborn-v0_8-whitegrid"]})
)

my_chart
