# IMPORT PACKAGES
from matplotlib import pyplot as plt
import pandas as pd

# IMPORT DATAFRAME & PRINT INFO OF DATAFRAME
df = pd.read_csv("the_office_series.csv", parse_dates=["Date"])
print(df.info())

# CHANGE PARAMETERES OF PLT DIMENSIONS & CHANGE STYLE
plt.rcParams["figure.figsize"] = [16, 9]
plt.style.use("fivethirtyeight")

# CREATE LIST OF RATING VALUES (COLORS)
ratings = []
for ind, row in df.iterrows():
    if row["Ratings"] >= 9:
        ratings.append("green")
    elif row["Ratings"] >= 8:
        ratings.append("yellow")
    elif row["Ratings"] < 8:
        ratings.append("red")
print(ratings)

# CREATE LIST OF LENGTH VALUES
durations = []
for ind, row in df.iterrows():
    if row["Duration"] >= 40:
        durations.append(250)
    elif row["Duration"] < 40:
        durations.append(25)

# CREATE VARIABLES FOR PLT
x1 = df["Date"]
y1 = df["Viewership"]
z1 = ratings
a1 = durations

# CREATE, LABEL, TITLE, CHANGE TICKS, & SHOW SCATTER PLT
plt.scatter(x1, y1, c=z1, s=a1)
plt.yticks(
    [2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5],
    ["2.5m", "5.0m", "7.5m", "10.0m", "12.5m", "15.0m", "17.5m", "20.0m", "22.5m"],
)
plt.xlabel("Date (Year)")
plt.ylabel("Viewership (Million)")
plt.title("Popularity, Duration, and Guest Appearances")
plt.show()

# DETERMINE & PRINT ONE GUEST STAR FROM THE MOST VIEWED EPISODE OF DF
print(df[df["Viewership"] == df["Viewership"].max()]["GuestStars"])
top_star = " Cloris Leachman, Jack Black, and Jessica Alba."
w = "The guest stars for in the most viewed episode of The Office are,"
print(w + top_star)
