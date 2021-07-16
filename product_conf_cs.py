import glob
import json

FOLDER_NAME = "catalog-ca"


def format_to_cs(file):
    with open(file, 'r') as f:
        mapping = json.load(f)

    cs_file_name = file[:-5] + '.txt'
    with open(cs_file_name, 'w') as f:
        for map in mapping:
            cs_format = 'public override string {} => "{}";\n\n'.format(map.get('name'),
                                                                        map.get('destUrl').split('--')[-1])
            f.write(cs_format)


def _get_files():
    file_name_format = rf'{FOLDER_NAME}\mapping_folder\*.json'
    files = glob.glob(file_name_format)
    print("All files:", files)
    return files


if __name__ == '__main__':
    files = _get_files()
    for file in files:
        format_to_cs(file)
