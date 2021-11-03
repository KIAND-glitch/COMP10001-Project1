def get_species_evenness(observed_list):
    '''accepts an observed list of species present in a habitat and returns a 
    tuple of the species eveness calculated as an inverse of simpson's index
    and list of alphabetically sorted tuples consisting of a bird species and 
    the number of times it was observed'''
    # TODO implement this function
    
    # creating a dictionary to store the different species and the number of
    # times they are obeserved in the habitat
    species_dictionary = {}
    
    for species_observed in observed_list:
        if species_observed in species_dictionary:
            species_dictionary[species_observed] += 1
        else:
            species_dictionary[species_observed] = 1
            
    species_count = sorted(species_dictionary.values())
    
    sorted_lst = sorted(species_dictionary.items())  # stores the  
    # alphabetically sorted list of tuples
    
    # calculates the sum of the species count
    sum_of_species_count = 0
    
    for each_species in species_count:
        sum_of_species_count += each_species
    
    # creates a list which stored the proportion of the observations
    lst = []
    
    for each_species in species_count:
        proportion = each_species / sum_of_species_count
        lst.append(proportion)
        
    # calculating the simpsons index which is the sum of squares of the
    # proportion of observations
    simpsons_index = 0
    
    for proportions in lst:
        simpsons_index = simpsons_index + proportions**2
        
    if simpsons_index != 0:
        inverse_simpson_index = 1.0 / simpsons_index
    else:
        inverse_simpson_index = 0
   
    return inverse_simpson_index, sorted_lst
    