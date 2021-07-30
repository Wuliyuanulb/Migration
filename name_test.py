import glob
global location


def location_func():
    print('location:', location)

def get_all_parameter_json_files():
    FOLDER_NAME = "CommitmentPlanRP"

    file_name = "{}/{}-*-001_UpdateService_Parameters.json".format(FOLDER_NAME, FOLDER_NAME)
    files = glob.glob(file_name)
    print("files:", files)
    return files


if __name__ == '__main__':
    files = get_all_parameter_json_files()
    for file in files:
        location = file.split("-")[1]

        location_func()
