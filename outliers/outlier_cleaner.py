#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors=[]
    print (zip(ages, predictions, net_worths))
    for prediction, net_worth in zip(predictions, net_worths):
        errors.append(prediction - net_worth)
    
    cleaned_data=zip(ages, net_worths, errors)
    samples = int(len(cleaned_data)*0.9)
    cleaned_data.sort(key=lambda tup: (tup[2]))

    
    return cleaned_data[:samples]
