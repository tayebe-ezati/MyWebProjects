import pandas as pd
import matplotlib.pyplot as plt

# مرحله ۱: فایل CSV رو بخون
df = pd.read_csv("day4_sales.csv")
print("فایل با موفقیت خونده شد ✅")
print(df)

# مرحله ۲: جمع فروش ماهانه
monthly = df.groupby("month")["sales"].sum()
print("\nجمع فروش ماهانه:")
print(monthly)

# مرحله ۳: رسم نمودار ستونی
monthly.plot(kind="bar", title="Monthly Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_bar.png")
print("\n📊 نمودار monthly_bar.png ساخته شد!")

# مرحله ۴: نمودار دسته‌بندی شده
pivoted = df.pivot(index="month", columns="category", values="sales")
pivoted.plot(kind="bar", title="Sales by Category per Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("grouped_bar.png")
print("📊 نمودار grouped_bar.png ساخته شد!")
