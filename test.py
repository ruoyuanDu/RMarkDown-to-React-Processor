import re
pattern = r'<a\s+href="(?!.*?id="downloadData")(?!.*?#)(.*?)">(.*?)<\/a>'
pattern = r'<a\s+href="(?!.*?id="downloadData")(?!#)([^"]*)">(.*?)<\/a>'
# pattern = r'<a\s+href="((?!#)[^"]+)">(.*?)<\/a>'





replacement = r'<Link to="\1">\2</Link>'

string = '<a href="/R/gallery/ggplot2-map-airline"><strong>earlier article</strong></a>' 
string1 = '<p><img className="cover-img" src={imgGgplot2MapAirlineAnimation} /></p><p>In this <a href="/R/gallery/ggplot2-map-airline"><strong>earlier article</strong></a>, we visualized the global flights and airports as a static graphic. This current work tweaks the static graphic into an animation to make the visualization much more dynamic and engaging. <span id="highlightBackground">The early part of data wrangling is identical to the static graphic. If you’re already familiar with the data cleanup, you can <a href="#skip"><strong>skip</strong></a> directly to the edits designed for animation.</span> 🌻</p>'
string2 = '''
<p><span id="highlightBackground" style="color:#009999;background-color:#fffac7;">The data wrangling above is identical to the creation of the <a href="../ggplot2-map-airline">static graphic</a>. <span id="skip"><strong>Edits 1-6 below the line are particularly catered for animation.</strong><a href="https//'www.aws.com" id=downloadData><strong>skip</strong></a></span></span></p>
'''

replaced_html = re.sub(pattern, replacement, string1)
print(replaced_html)
