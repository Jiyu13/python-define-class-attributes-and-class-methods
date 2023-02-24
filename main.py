class Album:

    # define a class constant - will not change
    GENRES = ["Hip-Hop", "Pop", "Jazz"]

    #  define a class attribute - can be changed
    album_count = 0

    def __init__(self, date, genre):
        #  manipulate class attributes from instance methods
        # album_count increases by 1 every time an instance album is created/initialised
        # Album.album_count += 1

        if self.check_genre(genre):
            # call classmethod
            self.increase_album_count()
            self.genre = genre
            self.release_date = date

    # define class methods - related to class itself
    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES


joshua_tree = Album(1987, "Jazz")
# access class attribute through instance
print(joshua_tree.album_count)  # 1

Album(2021, "Jazz")
Album(2022, "Jazz")
Album(2023, "Jazz")
# access class attribute through Album class
print(Album.album_count)    # 4

print(Album.GENRES)         # ['Hip-Hop', 'Pop', 'Jazz']

# set class constant GENRES to update it
Album.GENRES = "not a list anymore"
print(Album.GENRES)         # not a list anymore


