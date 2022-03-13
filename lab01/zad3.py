import pandas
import matplotlib.pyplot as plt
miasta = pandas.read_csv("miasta.csv")
print(miasta)
print(miasta.values)
row={"Rok":2010 ,"Gdansk":260, "Poznan":555  ,"Szczecin":405}
miasta = miasta.append(row, ignore_index = True)
print(miasta)

plt.plot(miasta["Rok"].values,miasta["Gdansk"].values,marker = 'o',color='red')
plt.xlabel("Rok")
plt.ylabel("Populacja")
plt.title("Populacja miasta Gdansk na przestrzeni lat")
plt.show()