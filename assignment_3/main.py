def number_of_customers_per_state(customers_dict):
    results = {}
    
    for state in customers_dict:
        if customers_dict[state] == None:
            results.setdefault(state, 0)
        else:
            results.setdefault(state, len(customers_dict[state]))
        
    return results