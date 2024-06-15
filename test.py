import re
html_txt = '''
<figure class="figure">
<p><img class="img-fluid quarto-figure quarto-figure-center figure-img" src="graphics/heatmap_vaccine_function_completed_polio.png"/></p>
</figure>
'''

html_txt = '''
<p><a href="../ggplot2-heatmap-sunspot-activities"><img class="img-fluid" src="graphics/heatmap_sunspot_completed.png"/></a></p>
'''
html_txt = '''
<p><img className="cover-img" src={imgGgplot2HeatmapVaccineForDiseases} /></p>
'''
pattern = re.compile(
    r'<p><a href="([^"]+)"><img class="[^"]*" src="([^"]+)\.png"/></a></p>',
    re.DOTALL
)
pattern = r'<p><img className="([^"]+)" src={([^"]+)} /></p>'

# <picture>
#     <source className="logo-diff img-fluid cover-img" type="image/webp" srcset={`${imgdplyrWebp}, ${imgdplyr}`} />                 
#     <img className="logo-diff img-fluid cover-img" src={imgdplyr} ></img>
# </picture>
new_src_webp = r"{imgFunctionWebp}"
new_src = r"{imgFunction}"
replacement = (
    r'  <picture>\n'
    f'    <source type="image/webp" srcset={new_src_webp} />\n'
    f'    <img className="cover-img" src={new_src} />\n'
    r'  </picture>\n'
)
replaced_html = re.sub(pattern, replacement, html_txt)
print(replaced_html)

