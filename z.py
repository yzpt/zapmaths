# Python code to generate and print INSERT statements for demo01 to demo99

# Start and end values for the range
start_value = 1
end_value = 99

# List to store the INSERT statements
insert_statements = []

# Loop through the range and generate INSERT statements
for i in range(start_value, end_value + 1):
    nom = 'Nom'
    prenom = 'Prénom'
    identifiant = 'demo' + str(i).zfill(2)  # zfill adds leading zeros if necessary
    classe = 'DEMO'
    mdp = identifiant  # Assuming the password is the same as the identifier
    
    # Generate the INSERT statement and add it to the list
    insert_query = f"INSERT INTO `table_eleves` (`NOM`, `PRENOM`, `IDENTIFIANT`, `CLASSE`, `id`, `mdp`) VALUES ('{nom}', '{prenom}', '{identifiant}', '{classe}', NULL, '{mdp}');"
    insert_statements.append(insert_query)

# Print the generated INSERT statements
for query in insert_statements:
    print(query)
