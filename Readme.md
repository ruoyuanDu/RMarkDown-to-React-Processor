0. Add these folders first in the current path: input, mid, output, outputReact  
1. Put all original html file in input folder    
2. In terminal run: python3 mkdn_htmlProcessor.py   
    this will process all html files under the input folder and save processed files to the output folder 
    To process a single file in the input folder, use htmlProcessor.py input_fiel <file_name(no path needed as long as it's in the input folder)>. The file should be in the input folder too.  
3. In terminal run: python3 mkdn_reactProcessor.py --input_folder_path './output'
    this will take files from the output folder and create new react.js files in the outputReact folder.  
    To process a single file in the input folder, use reactProcessor.py input_fiel <file_name(no path needed as long as it's in the output folder)>. The file should be in the output folder too.