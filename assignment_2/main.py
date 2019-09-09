def calculate_purchase_price(purchase, set_to_dict=False):
    price_of_books = 0.00
    for book in purchase['books']:
        price_of_books += book['price']
        
    if set_to_dict:
        purchase['total'] = price_of_books
        
    return price_of_books
    
