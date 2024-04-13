import os
import argparse
from bs4 import BeautifulSoup
import re

def extraProcessor(file):
    folder_path = './initialInput_for_extra/'
    output_path = './extraInput/'
    
    with open(folder_path+file, 'r') as input:
        soup = BeautifulSoup(input, 'html.parser')
        first_h1 = soup.find('h1', class_='title')
        new_div = soup.new_tag('div')
        new_div['class'] = 'small-logo'
        # logo_img = first_h1.find('img', class_='logo-diff')
        logo_img = soup.find('img', class_='logo-diff')
        if logo_img:    
            if 'class' in logo_img.attrs:
                logo_img['class'].append('cover-img')
            else:
                logo_img['class']= 'cover-img'
            new_div.append(logo_img)
            first_h1.insert_before(new_div)
            

    with open(output_path+file, 'w') as output:
        output.write(str(soup))


def main():
    folder_path = './initialInput_for_extra'
    files = os.listdir(folder_path)
    for file in files:
        if os.path.isfile(os.path.join(folder_path, file)):
            extraProcessor(file)

if __name__ == "__main__":
    main()