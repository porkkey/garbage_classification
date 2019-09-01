import src.data.parse_Json as pj
import numpy as np
import os
import zipfile

class data_loader:
    def __init__(self, parent_path):
        self._parent_path = parent_path

    def load_label_json(self):
        path = self._parent_path + "garbage_classify_rule.json"
        self._json_dict = pj.load_json(path)
        return self._json_dict

    def load_train_data(self):
        self._init_unzip_path()
        return self._load_data_and_label()

    def _init_unzip_path(self):
        #init environment
        print("===========init environment=============")
        suffix = ".zip"
        prefix = "train_data"
        folder_path = os.path.join(self._parent_path, prefix)
        zip_path = self._parent_path + "/" + prefix + suffix

        if os.path.isfile(zip_path):
            if os.path.exists(folder_path):
                for files in os.listdir(folder_path):
                    os.remove(os.path.join(folder_path, files))
            else:
                os.mkdir(folder_path)
            self._unzip_train_data(zip_path, self._parent_path)
        else:
            print("train_data.zip is not exist")

    def _unzip_train_data(self, zip_src, dest_path):
        #extract training data
        r = zipfile.is_zipfile(zip_src)
        if r:
            fz = zipfile.ZipFile(zip_src, "r")
            for file in fz.namelist():
                fz.extract(file, dest_path)
            print("===========extract training data success============")
        else:
            print("this is not .zip file")

    def _load_data_and_label(self):
        print("==============start loading training data=============")
        _folder_path = self._parent_path + "/train_data"
        # self._label_dict = {}
        class_train = []
        label_train = []
        for sub_file in os.listdir(_folder_path):
            if sub_file.endswith(".txt"):
                with open(_folder_path + '/' + sub_file, "r", encoding="UTF-8") as read_txt:
                    while True:
                        lines = read_txt.readline()
                        if not lines:
                            break
                        # self._label_dict[_folder_path + lines.split(",")[0]] = lines.split(",")[1]
                        class_train.append(_folder_path + lines.split(",")[0])
                        label_train.append(lines.split(",")[1])
        temp = np.array([class_train, label_train])
        # temp.transpose()
        # shuffle the samples
        np.random.shuffle(temp)
        # after trainspose, images is in dimesion 0 and label in dimension 1
        image_list = list(temp[0, :])
        label_list = list(temp[1, :])
        label_list = [int(i) for i in label_list]
        return image_list, label_list


if __name__=="__main__":
    path = "G:/MyGit/garbage_classification/src/garbage_classify"
    dl = data_loader(path)
    image_list, label_list = dl.load_train_data()



