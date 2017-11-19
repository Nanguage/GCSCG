import os
import shutil
from os.path import dirname, abspath, join

from jinja2 import Environment, PackageLoader, select_autoescape

file_path = dirname(abspath(__file__))
template_dir = join(file_path, "app/template")
static_dir = join(file_path, "app/static")

class G(object):
    """ page generater """
    def __init__(self, site_path):
        """
        :path: page output dir.
        """
        self.site_path = site_path
        self.__clear_site_path()
        self.__copy_static()
        self.tem_env = Environment(
            loader=PackageLoader('app', 'template'),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def __clear_site_path(self):
        for root, dirs, files in os.walk(self.site_path):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))

    def __copy_static(self):
        """ copy static sources to site dir """
        source = static_dir
        targrt = join(self.site_path, 'static')
        shutil.copytree(source, targrt)

    def gen_index(self):
        """ generate index page """
        tmp = self.tem_env.get_template('index.j2')
        with open(join(self.site_path, 'index.html') ,'w') as f:
            f.write(tmp.render())