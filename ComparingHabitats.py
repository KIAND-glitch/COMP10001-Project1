from hidden import get_species_richness, get_species_evenness

def compare_diversity(observed_list, diversity_measure):
    '''accepts a list of observed bird species and a string describing the 
    diversity measure to be used to rank the habitats and returns a sorted list  
    of tuples with each tuples consisting of the habitat name and the diversity 
    of the habitat according to the specified diversity measure'''
    
    # TODO implement this function.
    
    # creating a dictionary for the different types of habitats accepted as 
    # input and assigns an empty list to each 
    habitat_species = {}
    for elements in observed_list:
        if elements[1] not in habitat_species:
            habitat_species[elements[1]] = []
            
    habitat_name=habitat_species.keys()
    
    # adds the species observed in each habitat to the habitat_species 
    # dictionary to its respective habitat
    for element in observed_list:
        if element[1] in habitat_name:
            habitat_species[element[1]].append(element[0])
            
    habitat_species_items = habitat_species.items() 
    
    # creating a list to store tuples containing the habitat and the its
    # specified diversity measure 
    lst=[]
    
    if diversity_measure == 'richness':
        for key, value in habitat_species_items:
            lst.append((key, get_species_richness(value)[0]))
    else:
        for key, value in habitat_species_items:
            lst.append((key, get_species_evenness(value)[0]))
            
    def take_second(tpl):
        '''accepts a tuple tpl and returns its second element'''
        return tpl[1]
    
    # sorts list in descending order of diversity measure
    lst.sort(key=take_second, reverse=True)
    
    # sorting alphabetically if the habitats have the same diversity measure
    
    # creates a dictionary which stores habitat names with same and different
    # diversity measure
    
    diversity_ranking = {}
    
    # creates an empty list for each diversity measure
    for elements in lst:
        if elements[1] not in diversity_ranking:
            diversity_ranking[elements[1]] = []
    
    # adds the habitat names to each diversity measure 
    for elements in lst:
        if elements[1] in diversity_ranking.keys():
            diversity_ranking[elements[1]].append(elements[0])
    
    # sorts each list in the dictionary alphabetically
    for key, values in diversity_ranking.items():
        if len(values) > 1:
            values.sort()
    
    # creates the final sorted list to be returned by the function
    sorted_lst = []
    
    for key, values in diversity_ranking.items():
        
        if len(values) > 1:
            for elements in values:
                sorted_lst.append((elements, key))
        else:
            sorted_lst.append((values[0], key))
            
    return sorted_lst


