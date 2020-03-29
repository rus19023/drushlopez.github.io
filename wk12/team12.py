import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("weather_year.csv")
print(data)

print()
print()
print(len(data))

print()
print()
print(data.columns)

print()
print()
print(data["EDT"])

print()
print()
print(data[["EDT", "Mean TemperatureF"]])

print()
print()
print(data.EDT)

print()
print()
print(data.EDT.head())

print()
print()
print(data.EDT.tail())

print()
print()
print(data["Mean TemperatureF"].head())

print()
print()
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

print()
print()
print(data)

print()
print()
print(data.mean_temp.head())

print()
print()
print(data.mean_temp.std())

print()
print()
print(data.mean_temp.hist())
# plt.show()

print()
print()
print(data.std())

print()
print("data.date.head()")
print(data.date.head())

print()
print()
first_date = data.date.values[0]
print(first_date)

print()
print()
from datetime import datetime
d = datetime.strptime(first_date, "%Y-%m-%d")
print(d)

print()
print("data.date.head()")
data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
print(data.date.head())

print()
print()


print()
print()

print()
print()

print()
print()

print()
print()

