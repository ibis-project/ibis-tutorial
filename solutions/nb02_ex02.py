names_df = pd.read_json("data/penguins/species.jsonl", lines=True)
names = ibis.memtable(names_df)
penguins.join(names, "species")
