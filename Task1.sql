SELECT name, artists, duration_ms, release_date, year, accousticness, danceability, energy, instrumentalness, liveness, loudness, speechines, tempo, valence, mode, key, popularity, explicit
COUNT(*) AS duplicate_count
FROM spotify_data GOUP BY name, artists, duration_ms, release_date, year, accousticness, danceability, energy, instrumentalness, liveness, loudness, speechines, tempo, valence, mode, key, popularity, explicit
HAVING COUNT > 1;