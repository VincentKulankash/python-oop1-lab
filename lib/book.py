#!/usr/bin/env python3

class Book:
    """
    Represents a book in the bookstore.
    Attributes:
        title (str): The title of the book.
        page_count (int): The number of pages in the book.
    """

    def __init__(self, title, page_count):
        # Initialize the book with a title and page count
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """Getter for page_count."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Setter validates that page_count is an integer."""
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        """Simulates turning a page in the book."""
        print("Flipping the page...wow, you read fast!")


if __name__ == "__main__":
    b1 = Book("The Great Gatsby", 180)
    b1.turn_page()
    print(b1.page_count)

    b2 = Book("Bad Book", "many")