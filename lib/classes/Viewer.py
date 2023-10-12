class Viewer:
    def __init__(self, username):
        self.username = username
        self._reviews = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 6 <= len(username) < 16:
            self._username = username
        else:
            raise Exception("Username must be between 6 and 16 characters")

    def reviews(self):
        return self._reviews

    def reviewed_movies(self):
        return list(set([review.movie for review in self._reviews]))

    def has_reviewed_movie(self, movie):
        return movie in self.reviewed_movies()

    def add_review(self, movie, rating):
        from classes.Review import Review
        review = Review(self, movie, rating)
        self._reviews.append(review)
        movie.reviews().append(review)
        return review
