#5. Length, Indexing, and Iteration
# __len__, __getitem__, __setitem__, __iter__, __next__

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __setitem__(self, index, value):
        self.songs[index] = value

# Using magic methods
pl = Playlist(["Song A", "Song B", "Song C"])

print(len(pl))        # Calls __len__
print(pl[0])          # Calls __getitem__
pl[1] = "Song X"      # Calls __setitem__
print(pl[1])
