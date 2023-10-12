class Review:
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        viewer._reviews.append(self)
        movie.add_review(self)

        self.all.append(self)

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        if not hasattr(self, '_rating'):
            if not isinstance(value, int) or not (1 <= value <= 5):
                raise Exception("Rating must be between 1 and 5")
            self._rating = value
        else:
            raise Exception("Rating is already set")

    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        from classes.Viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Viewer must be instance of Viewer class")
        
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        from classes.Movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("Movie must be instance of Movie class")