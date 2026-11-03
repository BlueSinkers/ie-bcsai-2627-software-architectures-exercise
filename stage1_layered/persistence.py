# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


def save_book(title, price_cents, stock):
    book_id = len(books) + 1
    book = {
        "id": book_id,
        "title": title,
        "price_cents": price_cents,
        "stock": stock,
    }
    books[book_id] = book
    return book


def find_book(book_id):
    if book_id in book:
        return books[book_id]
    else:
        return None


def all_books():
    return list(books.values())


def update_stock(book_id, new_stock):
    books[book_id]["stock"] = new_stock


def save_order(order):
    # TODO step 1: give the order the next id, store it in `orders` and return it
    orders[len(orders) + 1] = order


def find_order(order_id):
    # TODO step 1: return the order, or None if it does not exist
    if order_id in orders:
        return orders[order_id]
    else:
        return None
