import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
df = pd.read_csv("data/game-ratings-by-top-10-platforms.csv")

# Group my metrics
df_follow = df.groupby("platform_name")["follow_count"].sum().reset_index()
df_follow = df_follow.rename(columns = {"follow_count": "total_follows"})

df_hype = df.groupby("platform_name")["hype_count"].sum().reset_index()
df_hype = df_hype.rename(columns = {"hype_count": "total_hypes"})

# Analyze the data
BAR_WIDTH = 0.4
plt.bar(df_follow.index - BAR_WIDTH / 2, df_follow["total_follows"], color = "blue", label = "Follows", width = BAR_WIDTH)
plt.bar(df_hype.index + BAR_WIDTH / 2, df_hype["total_hypes"], color = "red", label = "Hypes", width = BAR_WIDTH)

plt.xticks(df_follow.index, df_follow["platform_name"], rotation = 45)
plt.legend(loc = "upper left")

plt.show()