import re
html_txt = '''
<figure className="figure">
<p><img className="img-fluid quarto-figure quarto-figure-center figure-img" src="graphics/heatmap_vaccine_function_completed_polio.png"/></p>
</figure>
'''
pattern = re.compile(
    r'<figure className="figure">\s*<p>\s*<img className="(img-fluid quarto-figure quarto-figure-center figure-img)" src="([^"]+).png"\s*/>\s*</p>\s*</figure>',
    re.DOTALL
)

replacement = (
    r'<figure className="figure">\n'
    r'  <picture>\n'
    r'    <source type="image/webp" srcset="https://s3.amazonaws.com/databrewer/media/\2.webp" />\n'
    r'    <img className="\1" src="\2"/>\n'
    r'  </picture>\n'
    r'</figure>'
)
replaced_html = re.sub(pattern, replacement, html_txt)
print(replaced_html)