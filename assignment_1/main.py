def add_book_to_purchase(purchase_dict, title, author, price=0.99):
    book = {
        'title': title,
        'author': author,
        'price': price
    }
    
    purchase_dict['books'].append(book)