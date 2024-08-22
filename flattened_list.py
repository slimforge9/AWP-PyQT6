from forms_database import dict_of_fields as db


def get_list(chosen_forms):

    # Create holder
    flattened_list = []

    # Get fields
    for chosen_form in chosen_forms.keys():
        for page in db[chosen_form]:
            if page == 'description':
                continue
            else:
                for field in db[chosen_form][page].keys():
                    flattened_list.append(field)

    # Create dict for ordered distinct fields list
    flat_fields = dict.fromkeys(flattened_list)

    # Return flattened list
    return list(flat_fields.keys())
