def Detail2(person):
    # related_obj_list will be the list I will iterate through
<<<<<<< HEAD
<<<<<<< HEAD
    related_obj_list={}
    # List of related sets
    model_Names=['PersonToSchool', 'PersonToCourse', 'PersonToProfessionalDevelopment', 'PersonToSide',
                  'PersonToSkills', 'PersonToLanguage' , 'PersonToClearance', 'PersonToCompany', 'PersonToAwards',
                  'PersonToClubs_Hobbies', 'PersonToVolunteering']
    for model in model_Names:
        # Adjusting the model_Names to appriorate syntax for related_name reference
        # Related_names are a way to reverse foreign key
        related_name=model.lower().replace('_','')+'_set'
        related_obj=eval('person.'+related_name)
        related_obj=related_obj.all()
        # I want to first check if related_obj has any objects if not I want to print empty. If it's not empty
        # I loop through the related_obj
        temp_list = []
        for item in related_obj:
		# Adds each intermediary table object to list
        	temp_list.append(item)
        related_obj_list[model] = temp_list
        print(related_obj_list)
    return related_obj_list
=======
	related_obj_list={}
=======
    related_obj_list={}
>>>>>>> 903f24b60272e7eaa88f16e6d4c4b0817793b9ab
    # List of related sets
    model_Names=['PersonToSchool', 'PersonToCourse', 'PersonToProfessionalDevelopment', 'PersonToSide',
                  'PersonToSkills', 'PersonToLanguage' , 'PersonToClearance', 'PersonToCompany', 'PersonToAwards',
                  'PersonToClubs_Hobbies', 'PersonToVolunteering']
    for model in model_Names:
        # Adjusting the model_Names to appriorate syntax for related_name reference
        # Related_names are a way to reverse foreign key
        related_name=model.lower().replace('_','')+'_set'
        related_obj=eval('person.'+related_name)
        related_obj=related_obj.all()
        # I want to first check if related_obj has any objects if not I want to print empty. If it's not empty
        # I loop through the related_obj
        temp_list = []
        for item in related_obj:
		# Adds each intermediary table object to list
<<<<<<< HEAD
			temp_list.append(item)
		related_obj_list[model] = temp_list
	return related_obj_list
>>>>>>> ded216f852c651889e7872ae31f367c57d02966f
=======
        	temp_list.append(item)
        related_obj_list[model] = temp_list
        print(related_obj_list)
    return related_obj_list
>>>>>>> 903f24b60272e7eaa88f16e6d4c4b0817793b9ab
