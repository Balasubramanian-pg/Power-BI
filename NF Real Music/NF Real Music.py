import json
import pandas as pd

# Load JSON data
file_paths = [
    r"C:\Users\GANESH\Downloads\raw_response.json",
    r"C:\Users\GANESH\Downloads\raw_response(1).json",
    r"C:\Users\GANESH\Downloads\raw_response(2).json",
    r"C:\Users\GANESH\Downloads\raw_response(3).json",
    r"C:\Users\GANESH\Downloads\raw_response(4).json",
    r"C:\Users\GANESH\Downloads\raw_response(5).json"
]

rows = []
for file_path in file_paths:
    with open(file_path) as file:
        data = json.load(file)
        tracks = data['data']['albumUnion']['tracks']['items']
        for track in tracks:
            track_name = track['track']['name']
            playcount = int(track['track']['playcount'])
            disc_number = track['track']['discNumber']
            track_number = track['track']['trackNumber']
            duration_ms = track['track']['duration']['totalMilliseconds']
            duration_min = duration_ms / 60000  # Convert milliseconds to minutes
            artist_name = track['track']['artists']['items'][0]['profile']['name']
            rows.append((track_name, playcount, disc_number, track_number, duration_min, artist_name))

# Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=['Track Name', 'Playcount', 'Disc Number', 'Track Number', 'Duration (min)', 'Artist Name'])

# Sort the DataFrame by playcount in descending order
sorted_df = df.sort_values(by='Playcount', ascending=False)

# Print the sorted DataFrame
print(sorted_df)

# Save the sorted DataFrame to a CSV file
sorted_df.to_csv('NF Real Music.csv', index=False)
