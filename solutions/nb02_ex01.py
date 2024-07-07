names = con.read_csv("data/penguins/species.csv")
penguins.join(names, "species")
