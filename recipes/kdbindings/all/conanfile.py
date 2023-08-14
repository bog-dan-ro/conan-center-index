from conan import ConanFile
from conan.tools.files import get, copy
import os

class KDBindingsConan(ConanFile):
    name = "kdbindings"
    version = "1.0.3"
    license = "MIT"
    topics = ("reactive", "c++", "kdab")
    description = "Reactive programming & data binding in C++"
    url = "https://github.com/KDAB/KDBindings"
    author = "KDAB <info@kdab.com>"
    no_copy_source = True

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True, destination=self.source_folder)

    def package(self):
        copy(self, "*.h", os.path.join(self.source_folder, "src","kdbindings"), os.path.join(self.package_folder, "include", "kdbindings"))

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.set_property("cmake_file_name", "KDBindings")
        self.cpp_info.set_property("cmake_target_name", "KDAB::KDBindings")
        self.cpp_info.set_property("cmake_target_aliases", ["KDBindings"])
