from pythonforandroid.recipe import PythonRecipe


class AnyioRecipe(PythonRecipe):
    name = 'anyio'
    version = '3.6.1'
    url = 'https://files.pythonhosted.org/packages/67/c4/fd50bbb2fb72532a4b778562e28ba581da15067cfb2537dbd3a2e64689c1/anyio-3.6.1.tar.gz'

    call_hostpython_via_targetpython = False
    install_in_hostpython = False
    depends = ['setuptools', 'idna', 'sniffio']


recipe = AnyioRecipe()
