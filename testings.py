# Example: Counting unique artists
import pandas as pd

# Sample DataFrame
data = {'artist': ['Taylor Swift, Ed Sheeran', 
                   'Ed Sheeran', 
                   'Ariana Grande, Justin Bieber, Ed Sheeran', 
                   'Taylor Swift, Justin Bieber']}
df = pd.DataFrame(data)

# Split artist names, flatten the list, and find unique artists
all_artists = df['artist'].str.split(',').explode().str.strip()
unique_artists = all_artists.unique()

# Count unique artists
unique_count = len(unique_artists)

# Print the unique artists and their count
print("Unique Artists:", unique_artists)
print("Number of Unique Artists:", unique_count)
