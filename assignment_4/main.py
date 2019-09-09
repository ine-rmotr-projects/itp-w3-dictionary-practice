def eldest_customer_per_state(customers_dict):
    results = {}

    
    for state, customers_list in customers_dict.items():
        if not customers_list:
            results.setdefault(state, None)
            
        else:
            oldest = None
            for customer in customers_list:
                if oldest == None or customer['age'] > oldest['age']:
                    oldest = customer
                    
            results[state] = oldest
    
    return results