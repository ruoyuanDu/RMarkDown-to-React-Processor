data=[{'component': '<Ggplot2HeatmapVaccineForPolio />', 'path': 'ggplot2-heatmap-vaccine-for-polio', 'title': 'ggplot2 heatmap vaccine for polio', 'cover': 'imgGgplot2HeatmapVaccineForPolio', 'cover_webp': 'imgGgplot2HeatmapVaccineForPolioWebp'},
{'component': '<Ggplot2LineSlopeplot />', 'path': 'ggplot2-line-slopeplot', 'title': 'ggplot2 line slopeplot', 'cover': 'imgGgplot2LineSlopeplot', 'cover_webp': 'imgGgplot2LineSlopeplotWebp'},]

for item in data:
    item['component'] = item['component'].replace("'", '')
print(data)