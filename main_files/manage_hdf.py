import h5py


class Hdf:

    def __int__(self, file_path):
        self.file = file_path

    def create_dataset(self, data):
        with h5py.File(self.file, "w") as hdf:
            hdf.create_dataset('dataset_1', data=data)

    def create_group(self, group_name):
        with h5py.File(self.file, "w") as hdf:
            hdf.create_group(group_name)