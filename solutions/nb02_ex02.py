# Coerce the dataframe to an ibis table
coordinates = ibis.memtable(coordinates_df)

# Join with the existing penguins table
penguins.join(coordinates, "island")
