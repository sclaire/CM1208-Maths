import math
import numpy as np

def open_history():

    history = open("history.txt", "r")
    all_rows = []
    
    for rows in history:
        all_rows.append(rows.split())
    
    return all_rows

def open_queries():
    
    queries = open("queries.txt", "r")
    all_rows = []
    
    for rows in queries:
        all_rows.append(rows.split())
    
    return all_rows

def main():
    
    history_vec = history_vectors()
    query_entries = open_queries()
    
    avg_angle = average_angle()
    positive_entries = 0
    
    for customer_key, if_bought in history_vec.items():
        for value in if_bought:
            if value == 1:
                positive_entries = positive_entries + 1
                
    history_vec = convert_history_to_np_dtype()        
    query_vec = convert_queries_to_np_dtype()    
    query_vec_ind = convert_queries_to_np_dtype_individual()
    
    #print(query_vec, history_vec)
    
    all_angles = []
    
    for all_query_vec in query_vec_ind:
        
        angles_for_query = []
        
        for all_history_vec in history_vec:
            
            if np.any(np.not_equal(all_query_vec, all_history_vec)):
                
                print(all_query_vec, all_history_vec)
                
                angles_for_query.append(calculate_angle(all_query_vec, all_history_vec))
                
                #print(all_query_vec, all_history_vec)
                #print(calculate_angle(all_query_vec, all_history_vec))
     
        all_angles.append(angles_for_query)
               
    #print(all_angles)
   
    print(all_angles)
    
        
    #print(query_vec_ind)
    #    
    #for each_query in query_entries: 
    #    print("Shopping Cart: ", *each_query)
    #    
    #    for individual_item in each_query:
    #        
    #        item_angle = []
    #        
    #        print("Item: ", individual_item)
    #    
    #        print(query_vec_ind[(int(individual_item) - 1)])
    #    
    #        for all_history_vec in history_vec:
    #                
    #            if np.any(np.not_equal((query_vec_ind[(int(individual_item) - 1)]), all_history_vec)):
    #                
    #                item_angle.append(calculate_angle((query_vec_ind[(int(individual_item) - 1)]), all_history_vec))
    #
    #                print(min(item_angle))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
    print("Positive Entries: ", positive_entries)
    print("Average Angle: ", avg_angle)
    
    query_no = 0
    
    for each_query in query_entries: 
        print("Shopping Cart: ", *each_query)
        
        for individual_item in each_query:
            no_in_list = (int(individual_item) - 1)
            
            print("Item: ", individual_item, "Angle: ", min(all_angles[no_in_list]), 
                  "Match: ", np.argmin(all_angles[no_in_list]))
            
            
            
            #print("Angle: ", str(round(angle, 2)))
            
            
        query_no = query_no + 1
        
    
    
    
    
		
def history_vectors():
    
    history_data = open_history()
    
    header_row = history_data[0]
    total_customers = header_row[0]
    total_items = header_row[1]
    
    result_dictionary = {}   
    customer_item_array = []

    customer_no = 1
    
    for customers in range(int(total_customers)):
        array_of_items = []
        
        for items in range(int(total_items)):
            array_of_items.append(0)
            
        result_dictionary.update({customer_no : array_of_items})
        customer_no = customer_no + 1
        
    for data in history_data[1:]:
        customer_item_array.append((data[0], data[1]))
            
    for customer, item in customer_item_array:
        for customer_key, if_bought in result_dictionary.items():
            
            if int(customer) == int(customer_key):
                item_no = int(item) - 1
                (result_dictionary[customer_key][item_no]) = 1
                    
    return result_dictionary     
                
def calculate_angle(x, y):

    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    rounded_theta = round(theta, 2)

    return rounded_theta       

def convert_history_to_np_dtype():
    
    all_vectors = history_vectors()
    
    all_arrays = np.array(list(all_vectors.values()))
    
    return all_arrays

def convert_queries_to_np_dtype():
    
    all_vectors = query_vectors()
    
    all_arrays = np.array(list(all_vectors.values()))
    
    return all_arrays

def convert_queries_to_np_dtype_individual():
    
    all_vectors = query_vectors_individual()
    
    all_arrays = np.array(list(all_vectors.values()))
    
    return all_arrays

def average_angle():
    
    all_vectors = convert_history_to_np_dtype()
    
    all_angles = []
    
    for x_vector in all_vectors:
        for y_vector in all_vectors:
            
            if np.any(np.not_equal(x_vector, y_vector)):
                all_angles.append(calculate_angle(x_vector, y_vector))
                
    return (np.average(all_angles))


def query_vectors_individual():
    
    history_data = open_history()
    header_row = history_data[0]
    total_items = header_row[1]
    #print(total_items)
    
    query_number = 0
    result_dictionary = {}  
    
    for queries in range(int(total_items)):
        array_of_items = []
        
        for items in range(int(total_items)):
            array_of_items.append(0)
            
        result_dictionary.update({query_number : array_of_items})
        query_number = query_number + 1  
    
    for key, value in result_dictionary.items():
        
        result_dictionary[key][key] = 1
                          
    return result_dictionary
    
    
    

            
def query_vectors():
    
    all_queries = open_queries()
    history_data = open_history()
    
    total_queries = 0
    query_number = 0
    
    for each_query in all_queries:
        total_queries = total_queries + 1
    
    header_row = history_data[0]
    total_items = header_row[1]
    
    result_dictionary = {}   
    
    for queries in range((total_queries)):
        array_of_items = []
        
        for items in range(int(total_items)):
            array_of_items.append(0)
            
        result_dictionary.update({query_number : array_of_items})
        query_number = query_number + 1    
    
    for query_no in range(int(total_queries)): 
        for query_no_entries in all_queries[query_no]:
            
            list_number = (int(query_no_entries) - 1)
            result_dictionary[query_no][list_number] = 1
            
    return result_dictionary
    
    

            
        
    
    
    
    
	








	
