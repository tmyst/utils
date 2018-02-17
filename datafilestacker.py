# -*- coding: utf-8 -*-
import glob
class datafilestacker:
    root = None
    filelist = None
    filtered = None
    numheader = 1

    def __init__(self, root):
        self.root = root
        self.filelist = glob.glob(root + "/*")
        self.filtered = self.filelist

    def filter(self, string, inplace=False):
        if inplace:
            self.filtered = [f for f in self.filelist if f.count(string)]
        else:
            return [f for f in self.filelist if f.count(string)]

    def resetfilter(self):
        self.filtered = self.filelist

    def setnumheader(self, num):
        self.numheader = num

    def stack_to_file(self, path):
        with open(path, 'w') as fw:
            with open(self.filtered[0], 'r') as first:
                for i in range(self.numheader):
                    fw.write(first.readline())

            for file in self.filtered:
                with open(file, 'r') as fr:
                    for i in range(self.numheader):
                        line = fr.readline()
                    while True:
                        line = fr.readline()
                        if not line:
                            break
                        fw.writelines(line)