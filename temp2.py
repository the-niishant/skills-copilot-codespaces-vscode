def extract_initials_from_list(input_list):
    """
    This function extracts the initials from each name in the input list.
    for example
    input_list = ["Alice Smith", "Bob Johnson", "Charlie Brown"]
    output_list = ['AS', 'BJ', 'CB']
    
    """
    return ["".join([x[0] for x in name.split()]) for name in input_list]

print(extract_initials_from_list(["Nishant", "  Nishant Kumar"]))