wget -O - https://data.riksdagen.se/dataset/katalog/dataset.Xml \
| xmlstarlet sel -t -v "datasetlista/dataset[format='json' and typ='anforande']/url" \
| sed -e 's/^/https:\/\/data.riksdagen.se/' > sources.txt
