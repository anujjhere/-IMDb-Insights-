#1.Analyze Movie Ratings Trends Over Time
#Objective: Understand how movie ratings have changed across decades.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\ravic\Downloads\results_with_crew.csv", encoding='ISO-8859-1')

ratings_by_year = df.groupby('startYear')['averageRating'].mean()

plt.figure(figsize=(12, 6))
plt.plot(ratings_by_year.index, ratings_by_year.values, marker='o')
plt.title("Average IMDb Rating by Release Year")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.grid(True)
plt.tight_layout()
plt.show()







#2. Identify Top Directors by Average Rating
#Objective: Rank directors based on the average rating of their movies.

top_directors = df.groupby('directors')['averageRating'].mean().sort_values(ascending=False).head(10)
print("Top 10 Directors by Average Rating:")
print(top_directors)









#3. Explore Genre Popularity and Impact
#Objective: Determine which genres are most frequent and highest rated.
# Split and explode genres
genre_df = df.copy()
genre_df['genres'] = genre_df['genres'].str.split(', ')
genre_df = genre_df.explode('genres')
# Most frequent genres
genre_counts = genre_df['genres'].value_counts()
print("Top 5 Most Common Genres:")
print(genre_counts.head())
# Average rating by genre
genre_ratings = genre_df.groupby('genres')['averageRating'].mean().sort_values(ascending=False)
print("\nTop 5 Genres by Average Rating:")
print(genre_ratings.head())








#4. Relationship Between Runtime and Rating
#Objective: Check if longer movies tend to receive better ratings.


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='runtimeMinutes', y='averageRating', alpha=0.5)
plt.title("Runtime vs IMDb Rating")
plt.xlabel("Runtime (minutes)")
plt.ylabel("IMDb Rating")
plt.tight_layout()
plt.show()








#5. Identify Prolific Writers or Writer-Director Combos
#Objective: Discover creators with multiple high-rated movies.
df['creator_combo'] = df['writers'] + ' / ' + df['directors']
combo_ratings = df.groupby('creator_combo')['averageRating'].mean()
top_combos = combo_ratings.sort_values(ascending=False).head(10)

print("Top 10 Writer/Director Combos by Average Rating:")
print(top_combos)







#6. Top 10 Genres by Count
#Prepare genre counts
genre_counts = genre_df['genres'].value_counts().head(10)

# Bar plot
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar', color='skyblue')
plt.title("Top 10 Most Common Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()







#7.Box Plot – Distribution of Ratings by Top 5 Genres
top_5_genres = genre_df['genres'].value_counts().head(5).index
filtered_genres = genre_df[genre_df['genres'].isin(top_5_genres)]

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=filtered_genres, x='genres', y='averageRating', palette='Set2')
plt.title("Distribution of Ratings by Top 5 Genres")
plt.xlabel("Genre")
plt.ylabel("IMDb Rating")
plt.tight_layout()
plt.show()





#8.Heatmap – Correlation Between Numeric Variables
# Select numeric columns for correlation
numeric_df = df[['averageRating', 'numVotes', 'runtimeMinutes', 'rank']]

# Compute correlation matrix
correlation = numeric_df.corr()

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix of Numeric Features")
plt.tight_layout()
plt.show()




#9.Line Plot – IMDb Rating Trends Over Time
# Load the dataset
# Group by release year and calculate the average rating
ratings_by_year = df.groupby('startYear')['averageRating'].mean().sort_index()

# Plot the line chart
plt.figure(figsize=(12, 6))
plt.plot(ratings_by_year.index, ratings_by_year.values, marker='o', linestyle='-', color='teal')
plt.title("Average IMDb Rating by Release Year", fontsize=16)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Average IMDb Rating", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()



#10.Scatter Plot – Runtime vs IMDb Rating
# Plot the scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='runtimeMinutes', y='averageRating', alpha=0.5, color='purple')

plt.title("Runtime vs IMDb Rating", fontsize=16)
plt.xlabel("Runtime (minutes)", fontsize=12)
plt.ylabel("Average IMDb Rating", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()




