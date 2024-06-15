import shutil
import os
import glob
import mkdn_htmlProcessor as htmlProcessor
import mkdn_reactProcessor_RGallery as reactProcessor_RGallery

def copy_files(origin, destination, file_type):
    '''
    destination: ~/working/1.DB_Processes/RMarkDownProcessor/input
    '''
    # first remove any html files existing in the destination folder
    assert destination == '/home/fagabby/working/1.DB_Processes/RMarkDownProcessor/input'
    input_files = glob.glob(os.path.join(destination, f'*.{file_type}'))
    for file in input_files:
        # print(file)
        os.remove(file)
    other_folders = ['/home/fagabby/working/1.DB_Processes/RMarkDownProcessor/mid', 
                     '/home/fagabby/working/1.DB_Processes/RMarkDownProcessor/output', 
                     '/home/fagabby/working/1.DB_Processes/RMarkDownProcessor/outputReact']
    for folder in other_folders:
        folder_path = glob.glob(os.path.join(folder, '*'))
        for file in folder_path:
            print(file)
            os.remove(file)
    
    if os.path.exists(origin) and os.path.exists(destination):
        if file_type:
            file_paths = glob.glob(os.path.join(origin, f'*.{file_type}'))
            # print(file_paths)
        for file in file_paths:
            shutil.copy(file, destination)
    return True
def run_processing():
    pass

def main():
    origin_folder = input('What the origin folder, like gallery or dplyr: ')
    origin = '/home/fagabby/working/0.DataBrewer/' + origin_folder
    print(origin)
    destination = '/home/fagabby/working/1.DB_Processes/RMarkDownProcessor/input'
    status = False
    status = copy_files(origin=origin, destination=destination, file_type='html')
    print(status)
    if status: 
        htmlProcessor.main()
        if origin_folder == 'gallery':
            reactProcessor_RGallery.main()


if __name__ == '__main__':
    main()