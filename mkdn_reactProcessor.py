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
        # print(soup.body)
        img_tag = soup.find('img')
        if img_tag: 
            src = img_tag['src']
            new_src = f"{{img{functionName}}}"
            img_tag['src'] = ""
            # Replace the src attribute with the desired value
            img_tag['src'] = new_src
            print(img_tag['src'])

        # if soup.find('li', id='stepwise-instructions'):
        if soup.find('ul', attrs={'role': 'tablist'}):
            beginning = [
                "import React from 'react'; \n",
                "import {Link} from 'react-router-dom'; \n",
                "import {useRCustomEffect} from '../../useCustomEffect'; \n",
                # "import AddTabset from '../../js/addCodeFoldingTab'; \n",
                 "import AddTabsetQuarto from '../../js/addCodeFoldingTabforQuarto'; \n",
                "import img"+functionName+" from '../" + src + "'; \n", 
                # capitalize the first letter of the filename for the function component
                # "export default function " +"R"+inputName.split('_')[0].capitalize()+"(){\n", 
                "export default function " + functionName + "(){\n",
                "useRCustomEffect()\n",
                "AddTabsetQuarto()\n",
                "return ( <div>\n"  
            ]
        else:
            beginning = [
                "import React from 'react'; \n",
                "import {Link} from 'react-router-dom'; \n",
                "import {useRCustomEffect} from '../../useCustomEffect'; \n",
                "import img"+functionName+" from '../" + src + "';\n", 
                # capitalize the first letter of the filename for the function component
                # "export default function " +"R"+inputName.split('_')[0].capitalize()+"(){\n", 
                "export default function " + functionName + "(){\n",
                "useRCustomEffect()\n",            
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

        # Replace all <a> tag with <Link>
        pattern = r'<a\s+href="(.*?)">(.*?)<\/a>'
        replacement = r'<Link to="\1">\2</Link>'
        replaced_html = re.sub(pattern, replacement, replaced_html)

        # change all classname to class
        final_html = replaced_html.replace('classname', 'class')
        # then change all class to className
        final_html = final_html.replace('class', 'className')
        

        lines = beginning + [final_html] + ending
        # lines = beginning + htmlLines + ending
        text = ''.join(lines)
    with open('./outputReact/'+inputName+'_react.js', 'w') as output:
        output.write(text)
        
def main():
    parser = argparse.ArgumentParser(description="Process an HTML file.")
    parser.add_argument("--input_folder_path", default='')
    parser.add_argument("--input_file", default='', help="Input HTML file")
    args = parser.parse_args()
    if args.input_file:
        reactProcessor(args.input_file)
    else:
        if args.input_folder_path:
            importList = []
            dataList = []
            files = os.listdir(args.input_folder_path)
            for filename in files:
                if os.path.isfile(os.path.join(args.input_folder_path, filename)):
                    print(filename)
                    reactProcessor(filename)
                    words = filename.split('_')[0].split('-')
                    # remove numbers from the function name if any
                    words = [word for word in words if not word.isdigit()]
                    # Capitalize the first letter of each word and join them without hyphens
                    functionName = ''.join([word.capitalize() for word in words])
                    dataList.append(
                        {'component': '<'+functionName+' />', 'path':filename.split('_')[0], 'title':' '.join(filename.split('_')[0].split('-'))}
                    )
                    # parent folder name of contents
                    parentFolder = "RVisualization"
                    importList.append("import "+functionName+" from" + " '../" + parentFolder+"/contents/"+ filename+"_react'")
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
    # folder_path = './output'
    # dataList = []
    # files = os.listdir(folder_path)
    # for filename in files:
    #     if os.path.isfile(os.path.join(folder_path, filename)):
    #         print(filename)
    #         reactProcessor(filename)
    #         dataList.append(
    #             {'component': "<Spark"+filename.split('_')[0].capitalize()+" />", 'path':'', 'title':filename.split('_')[0]}
    #         )
    # json_data = json.dumps(dataList, indent=2)
    # file_path = "data.js"
    

    # with open(file_path, 'w') as json_file:
    #     json_file.write('const data=[')
    #     for item in dataList:
    #         json_file.write(str(item)+',' + '\n')
    #     json_file.write(']')
    main()