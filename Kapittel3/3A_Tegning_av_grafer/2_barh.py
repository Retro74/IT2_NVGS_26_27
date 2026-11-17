import matplotlib.pyplot as plt

platform = ["TikTok", "Instagram", "Snapchat", "YouTube", "FaceBook"]
timer_per_uke =[15,12,10,8,3]
some_colors = ["#69c9d0", "#c13584", "#fffc00", "#ff0000", "#1877f2"]

plt.barh(platform, timer_per_uke, color=some_colors)
plt.title("Ukentlig tidsbruk på SoMe")
plt.xlabel("Timer")
plt.ylabel("SoMe platform")

plt.show()