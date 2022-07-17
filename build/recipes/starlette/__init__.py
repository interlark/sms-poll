from pythonforandroid.recipe import PythonRecipe


class StarletteRecipe(PythonRecipe):
    name = 'starlette'
    version = '0.19.1'
    url = 'https://files.pythonhosted.org/packages/2b/18/405f4fb59119b8efa203c10a04a32a927976b5450cf649c8b4c9d079d21e/starlette-0.19.1.tar.gz'

    call_hostpython_via_targetpython = False
    install_in_hostpython = False
    depends = ['anyio', 'typing_extensions']


recipe = StarletteRecipe()
