import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load dataset
data = pd.read_csv('IMDB-Movie-Data.csv')

# Preview dataset
print(data[['Title', 'Genre', 'Director', 'Rating', 'Revenue (Millions)']].head())

# Top 10 Rated Movies in Comedy Genre
top_10_comedy = (
    data[data['Genre'].str.contains('Comedy', case=False, na=False)]
    .nlargest(10, 'Rating')[['Title', 'Rating', 'Director', 'Year']]
)
print("\n--- Top 10 Rated Movies in Comedy Genre ---")
print(top_10_comedy)

plt.figure(figsize=(10, 5))
sns.barplot(
    x='Rating',
    y='Title',
    hue='Title',
    data=top_10_comedy,
    palette='magma',
    legend=False,
)
plt.title('Top 10 Rated Movies in Comedy Genre')
plt.xlabel('IMDb Rating')
plt.ylabel('Movie Title')
plt.tight_layout()
plt.show()
plt.close()

# Top 5 Rated Movies Overall
top_5_overall = data.nlargest(5, 'Rating')[
    ['Title', 'Rating', 'Director', 'Year']
]
print("\n--- Top 5 Rated Movies Overall ---")
print(top_5_overall)

plt.figure(figsize=(10, 5))
sns.barplot(
    x='Rating',
    y='Title',
    hue='Title',
    data=top_5_overall,
    palette='crest',
    legend=False,
)
plt.title('Top 5 Rated Movies Overall', fontsize=14)
plt.xlabel('IMDb Rating', fontsize=12)
plt.ylabel('Movie Title', fontsize=12)
plt.tight_layout()
plt.show()
plt.close()

# Top 5 Directors by Movie Count
top_directors = data['Director'].value_counts().head(5)
print("\n--- Top 5 Directors by Movie Count ---")
print(top_directors)
print("-" * 40)

plt.figure(figsize=(10, 6), dpi=100)
sns.barplot(
    x=top_directors.index,
    y=top_directors.values,
    hue=top_directors.index,
    palette='Blues_r',
    legend=False,
)
plt.title('Top 5 Directors by Movie Count', fontsize=14, fontweight='bold')
plt.xlabel('Director', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)
plt.xticks(rotation=25, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
plt.close()