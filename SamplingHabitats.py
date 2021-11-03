def optimise_study(sample_data, unseen_species, consecutive_visits):
    '''accepts three variables that are sample_data( which is a list of data
    collected over multiple sampling visits ),unseen_species(an int which 
    stores the minimum number of previously unseen species that must be 
    observed before a visit is deemed unproductive) and consecutive_visits
    (an int which store the number of consequtive unproductive visits that can 
    occur before stopping) and then returns a tuple with the number of visits 
    that occur before the survey is stopped and the proportion of species that 
    were observed in comparison to the total number of species from all surveys
    '''
    # TODO implement this function
    
    # creates a dictionary that contains all the different species and the
    # number of times they are observed 
    total_species = {}
    for each_list in sample_data:
        for species_observed in each_list:
            if species_observed in total_species:
                total_species[species_observed] += 1
            else:
                total_species[species_observed] = 1
                
    species = {}  # a dictionary which stores and counts the number of new 
    # species already existing species in each visit
    
    survey_number = 0  # stores the number of visits before the survey stops
    
    unproductive_visits = 0
    
    # iterates through each list in the sample_data to form the species 
    # dictionary and return the desired output
    for each_list in sample_data:

        survey_number += 1 
        
        new_species = 0  # counts the number of new species seen in each list   
        # of the of the sample_data
        
        productive_survey = False  # used later in the if statements to decide 
        # whether a visit is productive or not
        
        # checks whether or not a species has been seen before and if not, it
        # adds it to the species dictionary and increments the number by one
        for each_species in each_list:
            if each_species in species:
                species[each_species] += 1
                
            else:
                species[each_species] = 1
                new_species += 1
            
            # checks if a survey is productive as it iterates through the 
            # different species in the survey
            if new_species >= unseen_species:
                productive_survey = True
            
        if productive_survey is False:
            unproductive_visits += 1
        else:
            unproductive_visits = 0  # resets the number of unproductive visits
            # to zero for the next  iteration
        
        # stops the survey if the unproductive visits exceeds the 
        # consecutive visits and returns the values
        if unproductive_visits >= consecutive_visits:
            return survey_number, len(species) / len(total_species)
    
    # terminates the loop and returns the values if the number of unproductive 
    # vistits does not exceed number of consecutive vists
    return survey_number, len(species) / len(total_species)

