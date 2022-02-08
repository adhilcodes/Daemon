import pickle

# The function network will return a numpy.ndarray
def decide(dict_values, verbose):
    
    # unpacking values from dictionary
    data_ = []
    data = [dict_values['ram_free'], dict_values['swap_free'], dict_values['disk_free'], dict_values['cpu_idle'], dict_values['loadavg1'], dict_values['loadavg2'], dict_values['loadavg3']]
    data_.append(data)
    
    # passing the values to the machine learning model
    filename = "./netdaemon/model/networkmodel"
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(data_)
    if verbose:
        print(f"[.] Output from Regression Model: {result}")
    return result

