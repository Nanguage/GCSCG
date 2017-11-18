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
        self.__copy_static()
        self.tem_env = Environment(
            loader=PackageLoader('app', 'template'),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def __copy_static(self):
        """ copy static sources to site dir """
        shutil.copytree(static_dir, join(self.site_path, "static"))

    def gen_index(self):
        """ generate index page """
        tmp = self.tem_env.get_template('index.j2')
        with open(join(self.site_path, 'index.html') ,'w') as f:
            f.write(tmp.render())