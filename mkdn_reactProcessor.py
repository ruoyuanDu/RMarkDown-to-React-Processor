import os
import json
import argparse

def reactProcessor(input):
    inputName = str(input)
    folder_path = './output/'
    words = inputName.split('_')[0].split('-')
    # Capitalize the first letter of each word and join them without hyphens
    functionName = ''.join([word.capitalize() for word in words])
    with open(folder_path+input, 'r') as input:
        beginning = [
            "import React from 'react'; \n",
            "import {useRCustomEffect} from '../../useCustomEffect'; \n",
            "import AddTabset from '../../js/addCodeFoldingTab'; \n",
            # capitalize the first letter of the filename for the function component
            # "export default function " +"R"+inputName.split('_')[0].capitalize()+"(){\n", 
            "export default function " + functionName + "(){\n",
            "useRCustomEffect()\n",
            "AddTabset()\n",
            "return ( <div>\n"  
        ]
        htmlLines = input.readlines()
        ending = [
            "</div>\n)}"
        ]
        lines = beginning + htmlLines+ending
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
            dataList = []
            files = os.listdir(args.input_folder_path)
            for filename in files:
                if os.path.isfile(os.path.join(args.input_folder_path, filename)):
                    print(filename)
                    reactProcessor(filename)
                    words = filename.split('_')[0].split('-')
                    # Capitalize the first letter of each word and join them without hyphens
                    functionName = ''.join([word.capitalize() for word in words])
                    dataList.append(
                        {'component': "<"+functionName+" />", 'path':filename.split('_')[0], 'title':' '.join(filename.split('_')[0].split('-'))}
                    )
            # json_data = json.dumps(dataList, indent=2)
            file_path = "data.js"

            with open(file_path, 'w') as json_file:
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