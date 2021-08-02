import glob
import json

FOLDER_NAME = "CommitmentPlanRP"


def format_to_cs(file):
    with open(file, 'r') as f:
        mapping = json.load(f)

    cs_file_name = file[:-5] + '.txt'
    with open(cs_file_name, 'w') as f:
        kv_info = mapping[0].get('destUrl')
        kv = kv_info.split('.')[0][len('https://'):]
        f.write('        public override string KeyVaultName => "{0}";\n\n'.format(kv))
        for map in mapping:
            cs_format = '        public override string {} => "CommitmentplansMamlProd--{}";\n\n'.format(
                map.get('name')[0].upper() + map.get('name')[1:],
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
