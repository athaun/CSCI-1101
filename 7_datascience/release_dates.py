import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
df = pd.read_csv("data/game-ratings-by-release-dates.csv")

df["first_release_date"] = pd.to_datetime(df["first_release_date"])

plt.scatter(df["first_release_date"], df["critic_rating_value"], color = "blue", label = "Critic Ratings", alpha = 0.2)
plt.scatter(df["first_release_date"], df["user_rating_value"], color = "red", label = "User Ratings", alpha = 0.2)
plt.show()