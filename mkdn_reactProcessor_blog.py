import os
# import json
import argparse
from bs4 import BeautifulSoup
import re

def reactProcessor(input):
    inputName = str(input)
    folder_path = './output/' 
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
        # importing list for case when there is image 
        if img_tag:         
            beginning = importing + [
                "import React from 'react'; \n",
                "import {Link} from 'react-router-dom'; \n",
                "import {useRCustomEffect} from '../../useCustomEffect'; \n",
                # "import AddTabsetQuarto from '../../js/addCodeFoldingTabforQuarto'; \n",
                "import img"+functionName+" from '../" + src + "'; \n", 
                "import img"+functionName+ "Webp"+ " from '../" + src_webp + "'; \n", 
                # "import" + new_src_webp + " from '../" + src + "'; \n", 
                # capitalize the first letter of the filename for the function component
                # "export default function " +"R"+inputName.split('_')[0].capitalize()+"(){\n", 
                "export default function " + functionName + "(){\n",
                "useRCustomEffect()\n",
                # "AddTabsetQuarto()\n",
                "return ( <div>\n"  
            ]
        # importing list when there is no tablist
        else:
            beginning = importing + [
                "import React from 'react'; \n",
                "import {Link} from 'react-router-dom'; \n",
                "import {useRCustomEffect} from '../../useCustomEffect'; \n",
                # "import AddTabsetQuarto from '../../js/addCodeFoldingTabforQuarto'; \n\n",
                # capitalize the first letter of the filename for the function component
                # "export default function " +"R"+inputName.split('_')[0].capitalize()+"(){\n", 
                "export default function " + functionName + "(){\n",
                "useRCustomEffect()\n",
                # "AddTabsetQuarto()\n",
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
        pattern = r'<a\s+href="(?!.*?id="downloadData")(?!#)([^"]*)">(.*?)<\/a>'
        replacement = r'<Link to="\1">\2</Link>'
        replaced_html = re.sub(pattern, replacement, replaced_html)

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
            r'<p><img class="([^"]+)" src="([^"]+).png"/></p>',
            re.DOTALL
        )

        replacement = (
            r'<figure className="figure">\n'
            r'  <picture>\n'
            r'    <source type="image/webp" srcset="https://s3.amazonaws.com/databrewer/media/\2.webp" />\n'
            r'    <img className="\1" src="\2.png" data-fallback="\2.png" />\n'
            r'  </picture>\n'
            r'</figure>'
        )
        replaced_html = re.sub(img_pattern, replacement, replaced_html)


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
    # return the first image src
    if src and src_webp:
        return {'src': src, 'src_webp': src_webp}
        
def main():
    # parser = argparse.ArgumentParser(description="Process an HTML file.")
    # parser.add_argument("--input_folder_path", default='')
    # parser.add_argument("--input_file", default='', help="Input HTML file")
    # args = parser.parse_args()
    input_folder_path = "/home/fagabby/working/1.DB_Processes/RMarkDownProcessor/output"
    # if args.input_file:
    #     src = reactProcessor(args.input_file)
    # else:
    #     if args.input_folder_path:
    importList = []
    importImageList = []
    importImageWebpList = []
    dataList = []
    # files = os.listdir(args.input_folder_path)
    files = os.listdir(input_folder_path)
    for filename in files:
        if os.path.isfile(os.path.join(input_folder_path, filename)):
            img_path_dict = reactProcessor(filename)
            words = filename.split('_')[0].split('-')
            # remove numbers from the function name if any
            words = [word for word in words if not word.isdigit()]
            # Capitalize the first letter of each word and join them without hyphens
            functionName = ''.join([word.capitalize() for word in words])
            dataList.append(
                {'component': '<'+functionName+' />', 'path':filename.split('_')[0], 'title':' '.join(filename.split('_')[0].split('-')),'subTitle':'Subtitle', 'dscrpt': 'This is description', 'image': 'img'+functionName, 'cover_webp': f"img{functionName}Webp", 'time':'2 min'}
            )
            # parent folder name of contents
            ## for blog
            # parentFolder = "blog"
            importList.append("import "+functionName+" from" + " '../blog" +"/contents/"+ filename+"_react'")
            importImageList.append("import img"+functionName+" from" + " '../blog/" + img_path_dict['src'] + "'")
            importImageWebpList.append("import img"+functionName+"Webp from" + " '../blog/" + img_path_dict['src_webp'] + "'")
    
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
        json_file.write(']')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an HTML file.")
    parser.add_argument("--input_folder_path", default='')
    parser.add_argument("--input_file", default='', help="Input HTML file")
    args = parser.parse_args()
    if args.input_file:
        src = reactProcessor(args.input_file)
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
                        {'component': '<'+functionName+' />', 'path':filename.split('_')[0], 'title':' '.join(filename.split('_')[0].split('-')),'subTitle':'Subtitle', 'dscrpt': 'This is description', 'image': 'img'+functionName, 'time':'2 min'}
                    )
                    # parent folder name of contents
                    ## for blog
                    # parentFolder = "blog"
                    importList.append("import "+functionName+" from" + " '../blog" +"/contents/"+ filename+"_react'")
                    importImageList.append("import img"+functionName+" from" + " '../blog/" + img_path_dict['src'] + "'")
                    importImageWebpList.append("import img"+functionName+"Webp from" + " '../blog/" + img_path_dict['src_webp'] + "'")
            
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
                json_file.write(']')