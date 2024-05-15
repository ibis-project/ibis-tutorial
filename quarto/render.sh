#!/bin/bash


for file in *.qmd; do
    filename=$(basename -- "$file" .qmd)
    quarto convert "$file" --output "../$filename.ipynb"
done

