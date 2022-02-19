import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv")



# Pandas

# Head limits things shown(can be chained with other things)
#print(df.head(5))

#Shows columns
#print(df.columns)

#Filters Director name out of df
#print(df['director_name'])

#Limis search to 3 columns
#print(df[["director_name", "imdb_score", "movie_imdb_link"]].head(5))

#*Might not work* limits score to be above 7.5
#print(df[df["imdb_score"] > 7.5].head(5))

#Counts all values in search
#print(df["director_name"].value_counts().head(5))

#Sums toghether all thing in search
#gross = print(df.groupby("director_name")["gross"].sum())

#Sorts vals in ascendng order
#df_movies_year = df.groupby("director_name")["movie_title"].count().sort_values(ascending = False)
#print(df_movies_year)

x = ["Chocalates", "Candies", "Sweets"]
y = [10, 20, 30]
fig = plt.figure()
plt.plot(x,y)

fig.savefig("graph.png")









