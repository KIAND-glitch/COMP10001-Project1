def get_species_richness(observed_list):
    '''accepts a list of bird species observed in a habitat and then calculates
    and returns the number of different species obeserved and also returns a 
    alphabetically sorted list of the different species as a tuple''' 
    
    # creating a dictionary to store the different species and the number of
    # times they are obeserved in the habitat
    species_dictionary = {} 
    
    for species_observed in observed_list:
        if species_observed in species_dictionary:
            species_dictionary[species_observed] += 1
        else:
            species_dictionary[species_observed] = 1
            
    # sorts it alphabetically
    species = sorted(species_dictionary.keys())
    
    species_count = len(species)
    
    return species_count, species