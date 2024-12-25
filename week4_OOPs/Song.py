class Song:
    def __init__(self , title , artist,length):
        self.title= title
        self.artist= artist
        self.length= length 

        def get_title(self):
            return self.title
        def get_artist(self):
            return self.artist
        def get_length(self):
            return self.length
        
        def set_title(self, title):
            self.title = title
        def set_artist(self, artist):
            self.artist = artist
        def set_length(self, length):
            self.length = length
        def __str__(self):
            return f" {self.title} by {self.artist} ({self.length}')"
    
song1 = Song("A bird with Feather","Billie esh"," 4:42")
print(song1)

print(song1.get_title())
song1.set_title("Fav Song")
print(song1.get_title())