from pythonforandroid.recipe import PythonRecipe


class UvicornRecipe(PythonRecipe):
    name = 'uvicorn'
    version = '0.18.2'
    url = 'https://files.pythonhosted.org/packages/c1/ec/23abd850aa173e35b0436f46a3385585b131ee0e70a55c408d89cade30a1/uvicorn-0.18.2.tar.gz'

    call_hostpython_via_targetpython = False
    install_in_hostpython = False
    depends = ['click', 'h11']


recipe = UvicornRecipe()
