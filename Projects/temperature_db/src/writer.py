import os


class Writer:
    PATH_TO_STORAGE_DIR = '../db'

    def ToFile(self, data, file_name):
        file_path = f'{Writer.PATH_TO_STORAGE_DIR}{file_name}.dat'
        with open(file_name, 'w+') as writer:
            for data_element in data:
                writer.write(str(data_element))
                writer.write('\n')
        # print(f'Finished writing the data to the file...')
