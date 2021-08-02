import glob
global location


def location_func():
    print('location:', location)

def get_all_parameter_json_files():
    FOLDER_NAME = "StorageService"

    file_name = "{}/*prod-*-001-*.Parameters.json".format(FOLDER_NAME, FOLDER_NAME)
    files = glob.glob(file_name)
    print("files:", files)
    return files


if __name__ == '__main__':
    files = get_all_parameter_json_files()
    for file in files:
        location = file.split("_")[0].split('-')[-1].replace(' ', '').lower()
        location_func()
