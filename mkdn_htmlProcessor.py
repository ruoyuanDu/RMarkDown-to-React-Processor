import re
import argparse
from bs4 import BeautifulSoup
import os

def processor(input_file):
        folder_path = './input/'
        with open(folder_path+input_file, 'r', encoding='utf-8') as file, open('./mid/' + input_file.split('.')[0]+'_mid', 'w', encoding='utf-8') as midOutput:
            soup = BeautifulSoup(file, 'html.parser')
            # remove any <style></style> tag in the html
            for style_tag in soup.body.find_all('style'):
                style_tag.decompose()

            # remove any <script></script>
            script_tags = soup.body.find_all('script')
            if script_tags:
                for script in script_tags:
                    script.decompose()
            # Find and remove inline style attributes from all tags within the <body> tag
            for tag in soup.body.find_all(True):
                if tag.has_attr('style'):
                    del tag['style']

            # change <h1> tag to <h3> tag
            h1_tags = soup.find_all('h1', {'class':'title'})
            for h1 in h1_tags:
                h1.name = 'h3'


            # # remveoe all \n from <p> tag contents to avoid incorrect non-space between words
            # p_tags = soup.find_all('p')
            # for p_tag in p_tags:
            #     p_text = ' '.join(p_tag.stripped_strings).replace('\n', ' ')
            #     print(p_text)
            #     # Replace the content of the <p> tag while preserving its structure
            #     for child in p_tag.children:
            #         if isinstance(child, str):
            #             child.replace_with(child.replace('\n', ' '))

            # h_tags = soup.find_all(re.compile('^h\d'))

            # # Loop through each <h> tag
            # for h_tag in h_tags:
            #     # Loop through the children of the tag
            #     for child in h_tag.children:
            #         # If the child is a string and the parent tag is not <pre> or <code>, remove newline characters from it
            #         if isinstance(child, str):
            #             child.replace_with(child.replace('\n', ' '))


            body_content = soup.body.extract()
            midOutput.write(str(body_content)) 
        
        with open('./mid/' + input_file.split('.')[0]+'_mid', 'r') as midInput,  open('./output/'+input_file.split('.')[0]+'_output', 'w', encoding='utf-8') as output:
            lines = midInput.readlines()[1:-1]
            # text = ''.join(lines)

            for i, line in enumerate(lines):
                if line.startswith(' ') and '</code></pre>' not in line:
                    modified_line = '<span>' + line + '</span>'
                    # last_index = modified_line.rindex('>')
                    # modified_line_final = modified_line[:last_index + 1] + '</span>' + modified_line[last_index + 8:] + '\n'
                    # text = text.replace(line, modified_line_final)
                    lines[i] = modified_line
                elif line.startswith(' ') and '</code></pre>'in line:
                    modified_line = '<span>' + line
                    last_index = modified_line.find("</code>")
                    if last_index != -1:
                        modified_line_final = modified_line[:last_index] + '</span>' + modified_line[last_index:]
                    else:
                        modified_line_final = modified_line     
                    # modified_line_final = modified_line[0:last_index] + '</span>' + modified_line[last_index + 8:] + '\n'
                    lines[i] = modified_line_final
                if line.startswith('<!--'):
                    lines[i] = ''
                
                # add <br /> for tabluar table data at the beginning of each line
                     # Add <br /> to patterns:
                    '''
                        <br />SepalWidthCm     2.0
                        <br />PetalLengthCm    1.0
                        <br />PetalWidthCm     0.1
                    '''
                pattern = r"^[0-9a-zA-Z#&{[(-].*(?<!</p>)$"
                if re.match(pattern, line.strip()):
                    lines[i] = "<br />"+line
            text = ''.join(lines)
            # Add <pre> and <code> 
            pattern = r'<pre><code>(.*?)</code></pre>'
            pattern2 = r'<pre class="sourceCode r"><code class="sourceCode r">(.*?)</code></pre>'
            replacement = r"<pre className='demo-highlight sourceCode r'><code className='sourceCode r'>\1</code></pre>"
            text = re.sub(pattern, replacement, text, flags=re.DOTALL)
            text = re.sub(pattern2, replacement, text, flags=re.DOTALL)

            # Replace { and } with '&#123;' and '&#125;'
            text = text.replace('{', '&#123;').replace('}', '&#125;')

            pattern = re.compile(r'</a></span>', re.IGNORECASE)
            # Define a replacement pattern
            replacement = r'</a></span><br />'
            text = re.sub(pattern, replacement, text)


            # Remove <!-- /content --> before </div>
            text = re.sub(r'</div>\s*<!--\s*/content\s*-->', '</div>', text)



            output.write(text)

def main():
    parser = argparse.ArgumentParser(description="Process an HTML file.")
    parser.add_argument("input_file", help="Input HTML file")
    args = parser.parse_args()
    processor(args.input_file)

if __name__ == "__main__":
    # main()
    folder_path = './input'
    files = os.listdir(folder_path)
    for filename in files:
        if os.path.isfile(os.path.join(folder_path, filename)):
            print(filename)
            processor(filename)    