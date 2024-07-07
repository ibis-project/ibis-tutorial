for island in ["Biscoe", "Dream", "Torgersen"]:
    # Filter for only this island
    query = penguins.filter(penguins.island == island)

    # Write the results to csv
    query.to_csv(f"{island.lower()}.csv")
