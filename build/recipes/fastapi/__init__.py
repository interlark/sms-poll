import os

from pythonforandroid.recipe import PythonRecipe


SETUP_PY = """
from setuptools import setup, find_packages

setup(
    name='{{NAME}}',
    packages=find_packages(exclude=["tests.*", "tests"]),
    version='{{VERSION}}',
)
"""


class FastapiRecipe(PythonRecipe):
    name = 'fastapi'
    version = '0.78.0'
    url = 'https://files.pythonhosted.org/packages/b7/2a/4676736c3b1864ca483265db43cad9710b83a95c2530aa6bfe671b83fd46/fastapi-0.78.0.tar.gz'

    call_hostpython_via_targetpython = False
    install_in_hostpython = False
    depends = ['starlette', 'pydantic']


    def install_python_package(self, arch, name=None, env=None, is_dir=True):
        target_dir = self.get_build_dir(arch.arch)
        with open(os.path.join(target_dir, 'setup.py'), 'w', encoding='utf8') as f_setup:
            setup_content = (SETUP_PY
                             .replace('{{VERSION}}', self.version)
                             .replace('{{NAME}}', self.name))
            f_setup.write(setup_content)

        super().install_python_package(arch, name, env, is_dir)

recipe = FastapiRecipe()
