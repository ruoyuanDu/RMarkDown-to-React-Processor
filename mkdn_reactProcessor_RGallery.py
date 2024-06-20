import os
# import json
import argparse
from bs4 import BeautifulSoup
import re

def reactProcessor(input):
    inputName = str(input)
    folder_path = '/home/fagabby/working/1.DB_Processes/RMarkDownProcessor/output/' 
    words = inputName.split('_')[0].split('-')
    # remove numbers from the function name if any
    words = [word for word in words if not word.isdigit()]
    # Capitalize the first letter of each word and join them without hyphens
    functionName = ''.join([word.capitalize() for word in words])
    with open(folder_path+input, 'r') as input:
        soup = BeautifulSoup(input, 'html.parser')
        img_tag = None
        if soup.find('img'):
            img_tag = soup.find('img')
        # logo_imgs = []
        # for img in soup.find_all('img'):
        #     # exclude the first a few logo <img> tags with class logo-diff 
        #     if 'logo-diff' not in img.get('class', []):
        #         img_tag = img
        #         break
        #     elif 'logo-diff' in img.get('class', []):
        #         logo_imgs.append(img)
            
        # img_tag = soup.find('img') 
        # change the format of the first cover page <img> tag
        importing = []
        if img_tag: 
            src = img_tag['src']
            # for webp import path
            src_webp = src.split('.')[0] + '.webp'
 
            new_src = f"{{img{functionName}}}"
            # for webp 
            new_src_webp = "{" + f"img{functionName}" + "Webp" + "}"

            img_tag['src'] = ""
            # Replace the src attribute with the desired value
            img_tag['src'] = new_src
            img_tag['class'] = 'cover-img'
   
        # exclude case where img_tag is not found, so does src
        if img_tag:  
            beginning = importing + [
                "import React from 'react'; \n",
                "import {Link} from 'react-router-dom'; \n",
                "import {useRCustomEffect} from '../../useCustomEffect'; \n",
                "import AddTabsetQuarto from '../../js/addCodeFoldingTabforQuarto'; \n",
                "import img"+functionName+" from '../" + src + "'; \n", 
                "import img"+functionName+ "Webp"+ " from '../" + src_webp + "'; \n", 
                # "import" + new_src_webp + " from '../" + src + "'; \n", 
                # capitalize the first letter of the filename for the function component
                # "export default function " +"R"+inputName.split('_')[0].capitalize()+"(){\n", 
                "export default function " + functionName + "(){\n",
                "useRCustomEffect()\n",
                "AddTabsetQuarto()\n",
                "return ( <div>\n"  
            ]

        else:
            beginning = importing + [
                "import React from 'react'; \n",
                "import {Link} from 'react-router-dom'; \n",
                "import {useRCustomEffect} from '../../useCustomEffect'; \n",
                "import AddTabsetQuarto from '../../js/addCodeFoldingTabforQuarto'; \n\n",
                # capitalize the first letter of the filename for the function component
                # "export default function " +"R"+inputName.split('_')[0].capitalize()+"(){\n", 
                "export default function " + functionName + "(){\n",
                "useRCustomEffect()\n",
                "AddTabsetQuarto()\n",
                "return ( <div>\n"  
            ]
        # htmlLines = input.readlines()
        ending = [
            "</div>\n)}"
        ]

        # Change the src of the first <img> tag
        html_txt = str(soup)
        # First Replace { and } with '&#123;' and '&#125;'
        html_txt = html_txt.replace('{', '&#123;').replace('}', '&#125;')
        
        # Then find the first <img > tag and change the src to the right format of {}
        img_src_pattern = r'<img\s+([^>]*?)src="&#123;([^"]*)&#125;"(?:[^>]*)\s*\/>'
        replacement = r'<img \1src={\2} />'
        replaced_html = re.sub(img_src_pattern, replacement, html_txt)


        # Replace all <a> tag with <Link>, exclude ones with <a href="#"> as <Link> can't be used to point to sections under same page
        # exclude <a id="downloadData"
        # pattern = r'<a\s+href="([^#].*?)">(.*?)<\/a>'
        # pattern = r'<a\s+href="(?!.*?id="downloadData")(.*?)">(.*?)<\/a>'
        # pattern = r'<a\s+href="(?!.*?id="downloadData")(?!.*?#)(.*?)">(.*?)<\/a>' # this pattern can't handle where <a> tags' href with and without # appearing in the same paragraph, liek this: string1 = '<p><img className="cover-img" src={imgGgplot2MapAirlineAnimation} /></p><p>In this <a href="/R/gallery/ggplot2-map-airline"><strong>earlier article</strong></a>, we visualized the global flights and airports as a static graphic. This current work tweaks the static graphic into an animation to make the visualization much more dynamic and engaging. <span id="highlightBackground">The early part of data wrangling is identical to the static graphic. If you’re already familiar with the data cleanup, you can <a href="#skip"><strong>skip</strong></a> directly to the edits designed for animation.</span> 🌻</p>'
        pattern = r'<a\s+href="(?!.*?id="downloadData")(?!#)([^"]*)">(.*?)<\/a>'
        replacement = r'<Link to="\1">\2</Link>'
        replaced_html = re.sub(pattern, replacement, replaced_html)
        if img_tag:
            # add webp to the first image
            pattern = r'<p><img class="([^"]+)" src={([^"]+)} /></p>'
            replacement = (
                r'  <picture>\n'
                f'    <source type="image/webp" srcset={new_src_webp} />\n'
                f'    <img className="cover-img" src={new_src} />\n'
                r'  </picture>\n'
            )
            replaced_html = re.sub(pattern, replacement, replaced_html)

            # add webp format for gallery only, change path accordingly for other pacakges
            img_pattern = re.compile(
                r'<figure class="figure">\s*<p>\s*<img class="(img-fluid quarto-figure quarto-figure-center figure-img)" src="([^"]+).png"\s*/>\s*</p>\s*</figure>',
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
            replaced_html = re.sub(img_pattern, replacement, replaced_html)
            
            # add webp format to images in the continue reading section
            pattern = re.compile(
                r'<p><Link to="([^"]+)"><img class="[^"]*" src="([^"]+)\.png"/></Link></p>',
                re.DOTALL
            )
            replacement = (
                r'<p><Link to="\1">\n'
                # r'<figure className="figure">\n'
                r'  <picture>\n'
                r'    <source type="image/webp" srcset="https://s3.amazonaws.com/databrewer/media/\2.webp" />\n'
                r'    <img className="img-fluid" src="https://s3.amazonaws.com/databrewer/media/\2.png" />\n'
                r'  </picture>\n'
                # r'</figure>\n'
                r'</Link></p>'
            )
            replaced_html = re.sub(pattern, replacement, replaced_html)

            # This is another pattern inside the continue read section
            pattern = re.compile(
                r'<p><img class="[^"]*" src="([^"]+)\.png"/></p>',
                re.DOTALL
            )
            replacement = (
                r'<p>\n'
                r'  <picture>\n'
                r'    <source type="image/webp" srcset="https://s3.amazonaws.com/databrewer/media/\1.webp" />\n'
                r'    <img className="img-fluid" src="https://s3.amazonaws.com/databrewer/media/\1.png" />\n'
                r'  </picture>\n'
                r'</p>'
            )
            replaced_html = re.sub(pattern, replacement, replaced_html)

        # change all classname to class
        # adding = to exclude replacing classname and class outside tags
        final_html = replaced_html.replace('classname=', 'class=')
        # then change all class to className
        final_html = final_html.replace('class=', 'className=')
        
        

        lines = beginning + [final_html] + ending
        # lines = beginning + htmlLines + ending
        text = ''.join(lines)
    with open('./outputReact/'+inputName+'_react.js', 'w') as output:
        output.write(text)

    if img_tag:
        return {'src': src, 'src_webp': src_webp}
        
def main():
    # parser = argparse.ArgumentParser(description="Process an HTML file.")
    # parser.add_argument("--input_folder_path", default='')
    # parser.add_argument("--input_file", default='', help="Input HTML file")
    # args = parser.parse_args()
    input_folder_path = "/home/fagabby/working/1.DB_Processes/RMarkDownProcessor/output"
    # if args.input_file:
    #     reactProcessor(args.input_file)
    # else:
    #     if args.input_folder_path:
    importList = []
    importImageList = []
    importImageWebpList = []
    dataList = []
    # files = os.listdir(args.input_folder_path)
    files = os.listdir(input_folder_path)
    for filename in files:
        if os.path.isfile(os.path.join(args.input_folder_path, filename)):
            img_path_dict = reactProcessor(filename)
            words = filename.split('_')[0].split('-')
            # remove numbers from the function name if any
            words = [word for word in words if not word.isdigit()]
            # Capitalize the first letter of each word and join them without hyphens
            functionName = ''.join([word.capitalize() for word in words])
            dataList.append(
                {'component': '<'+functionName+' />', 'path':filename.split('_')[0], 'title':' '.join(filename.split('_')[0].split('-')), 'cover':f"img{functionName}" ,'cover_webp': f"img{functionName}Webp"}
            )
            # for gallery

            importList.append("import "+functionName+" from" + " '../RgalleryPages" + "/contents/"+ filename+"_react'")
            if img_path_dict is not None:
                importImageList.append("import img"+functionName+" from" + " '../RgalleryPages/" + img_path_dict['src'] + "'")
                importImageWebpList.append("import img"+functionName+"Webp from" + " '../RgalleryPages/" + img_path_dict['src_webp'] + "'")
            # in order to remove the single quote '' in the data list, use vscode regular expression
            # pattern: '<img([^']+)/>'
            # replacement: <img$1 />

        importList = importList + importImageList + importImageWebpList
        # json_data = json.dumps(dataList, indent=2)
        file_path = "data.js"

        with open(file_path, 'w') as json_file:
            json_file.write("import React from 'react';\n")
            for item in importList:
                json_file.write(str(item)+'\n')
            json_file.write('const data=[')              
            for item in dataList:
                json_file.write(str(item)+',' + '\n')
                print(item)
            json_file.write(']')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an HTML file.")
    parser.add_argument("--input_folder_path", default='')
    parser.add_argument("--input_file", default='', help="Input HTML file")
    args = parser.parse_args()
    if args.input_file:
        reactProcessor(args.input_file)
    else:
        if args.input_folder_path:
            importList = []
            importImageList = []
            importImageWebpList = []
            dataList = []
            files = os.listdir(args.input_folder_path)
            for filename in files:
                if os.path.isfile(os.path.join(args.input_folder_path, filename)):
                    img_path_dict = reactProcessor(filename)
                    words = filename.split('_')[0].split('-')
                    # remove numbers from the function name if any
                    words = [word for word in words if not word.isdigit()]
                    # Capitalize the first letter of each word and join them without hyphens
                    functionName = ''.join([word.capitalize() for word in words])
                    dataList.append(
                        {'component': '<'+functionName+' />', 'path':filename.split('_')[0], 'title':' '.join(filename.split('_')[0].split('-')), 'cover':f"img{functionName}" ,'cover_webp': f"img{functionName}Webp"}
                    )
                    # for gallery

                    importList.append("import "+functionName+" from" + " '../RgalleryPages" + "/contents/"+ filename+"_react'")
                    importImageList.append("import img"+functionName+" from" + " '../RgalleryPages/" + img_path_dict['src'] + "'")
                    importImageWebpList.append("import img"+functionName+"Webp from" + " '../RgalleryPages/" + img_path_dict['src_webp'] + "'")
                    # in order to remove the single quote '' in the data list, use vscode regular expression
                    # pattern: '<img([^']+)/>'
                    # replacement: <img$1 />

            importList = importList + importImageList + importImageWebpList
            # json_data = json.dumps(dataList, indent=2)
            file_path = "data.js"

            with open(file_path, 'w') as json_file:
                json_file.write("import React from 'react';\n")
                for item in importList:
                    json_file.write(str(item)+'\n')
                json_file.write('const data=[')              
                for item in dataList:
                    json_file.write(str(item)+',' + '\n')
                    print(item)
                json_file.write(']')