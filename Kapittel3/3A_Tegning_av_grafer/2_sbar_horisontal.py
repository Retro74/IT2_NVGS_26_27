import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

platform = ["TikTok", "Instagram", "Snapchat", "YouTube", "FaceBook"]
timer_per_uke =[15,12,10,8,3]
df = pd.DataFrame(zip(platform, timer_per_uke), columns=["Platform", "Timer pr uke"])
some_colors = ["#69c9d0", "#c13584", "#fffc00", "#ff0000", "#1877f2"]

sns.set_theme()
sns.barplot(df, x="Timer pr uke", y="Platform", palette=some_colors)
plt.title("Ukentlig tidsbruk på SoMe")
plt.xlabel("Timer")
plt.ylabel("SoMe platform")

plt.show()