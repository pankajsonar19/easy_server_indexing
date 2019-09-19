from easy_server_indexing.resume import resume_code
from pathlib import Path


if __name__ == '__main__':

    root = 'C:/Users/pnkjs/OneDrive/Desktop/ALTADA/Server_192_168_10_8_Data_and_Docs'
    root_path = Path(root)

    error = 'C:/Users/pnkjs/OneDrive/Desktop/ALTADA/Server_192_168_10_8_Data_and_Docs/File_Check/bdc.xls'
    error_path = Path(error)

    if (root_path != None and error_path != None):

        path_list = resume_code(root_path,error_path)

        #print(path_list)

    else:
        print('Please enter a valid root path or error path')
