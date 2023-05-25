from os import listdir, rename, stat
from os.path import isfile, join, isdir
from shutil import copyfile
import os


class FileUtil:
    @staticmethod
    def get_files(path, validate=True):
        file_names = listdir(path)
        files = [join(path, file_name) for file_name in file_names]
        if not validate:
            return files
        return [f for f in files if isfile(f)]

    @staticmethod
    def get_all_file_names(path):
        files = [f for f in listdir(path) if isfile(join(path, f))]
        return files

    @staticmethod
    def get_directories(path):
        directories = [f for f in listdir(path) if isdir(join(path, f))]
        return [join(path, d) for d in directories]

    @staticmethod
    def get_directory_names(path):
        directories = [f for f in listdir(path) if isdir(join(path, f))]
        return directories

    @staticmethod
    def get_files_and_directories(path):
        return [join(path, f) for f in listdir(path)]

    @staticmethod
    def get_all_files(path):
        files = FileUtil.get_files_recursively(path)
        return [f for f in files if isfile(f) and not f.endswith('Thumbs.db')]

    @staticmethod
    def get_files_recursively(path):
        all_files = list()
        files = FileUtil.get_files_and_directories(path)
        all_files.extend(files)
        for file in files:
            if isdir(file):
                files_in_sub_dir = FileUtil.get_files_recursively(file)
                all_files.extend(files_in_sub_dir)
        return all_files

    @staticmethod
    def rename_file(from_file, to_file):
        rename(from_file, to_file)

    @staticmethod
    def copy_file(from_file, to_file, create_path_if_not_exist=False):
        if create_path_if_not_exist:
            dir_path = '\\'.join(to_file.split('\\')[:-1])
            if not os.path.exists(dir_path):
                FileUtil.create_directory_recursively(dir_path)
        copyfile(from_file,  to_file)

    @staticmethod
    def get_file_size(path):
        return stat(path).st_size

    @staticmethod
    def create_directory_recursively(path):
        folders = path.split('\\')
        # skip creating root directory
        if len(folders) < 2:
            return
        for i in range(2, len(folders) + 1):
            current_path = '\\'.join(folders[:i])
            if not os.path.exists(current_path):
                print('Create folder: {0}'.format(current_path))
                os.mkdir(current_path)

    @staticmethod
    def create_directory_if_not_exist(path):
        if not os.path.exists(path):
            print('Create folder: {0}'.format(path))
            os.mkdir(path)

    @staticmethod
    def file_exists(path):
        return os.path.exists(path)

    @staticmethod
    def get_all_files_in_parallel(file_paths):
        pass

    @staticmethod
    def read_files_in_parallel(file_paths):
        pass

    @staticmethod
    def delete_file(file_path):
        os.remove(file_path)

    @staticmethod
    def get_file_name(file_path):
        if not file_path:
            return None
        return os.path.basename(file_path)


if __name__ == '__main__':
    pass
