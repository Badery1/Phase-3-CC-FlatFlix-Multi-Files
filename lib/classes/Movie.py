class Movie:
    def __init__(self, title):
        self.title = title
        self._reviews = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception("Title cannot be an empty string")

    def reviews(self):
        return self._reviews
    
    def add_review(self, review):
        self._reviews.append(review)

    def reviewers(self):
        return list(set([review.viewer for review in self._reviews]))

    def average_rating(self):
        if not self._reviews:
            return None

        total_rating = sum([review.rating for review in self._reviews])
        avg_rating = total_rating / len(self._reviews)
        return round(avg_rating, 1)
