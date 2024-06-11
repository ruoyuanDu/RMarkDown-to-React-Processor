0. Add these folders first in the current path: input, mid, output, outputReact  
1. Put all original html file in input folder    
2. In terminal run: python3 mkdn_htmlProcessor.py   
    this will process all html files under the input folder and save processed files to the output folder 
    To process a single file in the input folder, use htmlProcessor.py input_fiel <file_name(no path needed as long as it's in the input folder)>. The file should be in the input folder too.  
3. In terminal run: python3 mkdn_reactProcessor_RGallery.py --input_folder_path './output'
or
    In terminal run: python3 mkdn_reactProcessor_dplyr.py --input_folder_path './output'
or 
    In terminal run: python3 mkdn_reactProcessor_RVisualization.py --input_folder_path './output'
or 
    In terminal run: python3 mkdn_reactProcessor_regular-expression.py --input_folder_path './output'
or 
    In terminal run: python3 mkdn_reactProcessor_stringr.py --input_folder_path './output'
or 
    In terminal run: python3 mkdn_reactProcessor_tidyr.py --input_folder_path './output'
or 
    In terminal run: python3 mkdn_reactProcessor_tibble.py --input_folder_path './output'
or 
    In terminal run: python3 mkdn_reactProcessor_purrr.py --input_folder_path './output'
or 
    In terminal run: python3 mkdn_reactProcessor_blog.py --input_folder_path './output'

    this will take files from the output folder and create new react.js files in the outputReact folder.  
    To process a single file in the input folder, use reactProcessor.py input_fiel <file_name(no path needed as long as it's in the output folder)>. The file should be in the output folder too.

4. (No longer need this sep for processing small logoes as those images have been added through the Index page, not through individual pges)If there are logo images need to be preprocessed(like dplyr, stringr, regex), then add all original html file first to the initialInput_for_extra folder, and run:
    python3 extra_reactProcessor.py
    Then output files will be saved in the extraIput folder. To continue further processing, copy and paste files from the extraInput folder to the input folder for step 2 and 3 above.

UPDATE
