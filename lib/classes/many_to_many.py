class Author:
    all = []

    def __init__(self, name):
        self._name = name  # store internally in private variable
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # ignore any attempt to change the name
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})



class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = str(name)
        self._category = str(category)
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # ignore invalid assignments
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # ignore invalid assignments
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(dict.fromkeys(authors)) if authors else []

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [
            author for author in self.contributors()
            if sum(1 for a in self.articles() if a.author == author) > 2
        ]
        return authors if authors else None

    # Optional: uncomment if top_publisher is needed
    # @classmethod
    # def top_publisher(cls):
    #     if not cls.all or not Article.all:
    #         return None
    #     return max(cls.all, key=lambda mag: len(mag.articles()))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
