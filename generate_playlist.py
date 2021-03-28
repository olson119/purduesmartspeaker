from csv import reader
import csv

def create_playlist(emotion):
    if (emotion == "angry" or emotion == "anger"):
        emotion = ["angry", "anger"]

    playlist = []
    with open('songs.csv', 'r', encoding='utf-8') as file:
        header = 0
        csv_reader = reader(file)
        for row in csv_reader:
            if (header != 0):
                if (row[3].lower() in emotion or row[4].lower() in emotion):
                    playlist.append(row[2])
            else:
                header += 1
    return playlist

if __name__ == "__main__":
    emotion = input("Please enter emotion: ")
    emotion = emotion.lower()
    playlist = create_playlist(emotion)
    print(len(playlist))
    print(playlist)

