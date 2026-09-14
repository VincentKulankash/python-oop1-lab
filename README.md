# Bookstore OOP Lab

## Overview
This project models a Book and a Coffee sold at a bookstore using Python classes.

## Classes

### Book
- **Attributes:** `title`, `page_count`
- **Validation:** `page_count` must be an integer
- **Methods:** `turn_page()`

### Coffee
- **Attributes:** `size`, `price`
- **Validation:** `size` must be "Small", "Medium", or "Large"
- **Methods:** `tip()` — increases `price` by 1

## Usage
```python
from book import Book
from coffee import Coffee

book = Book("1984", 328)
book.turn_page()

coffee = Coffee("Large", 3.75)
coffee.tip()