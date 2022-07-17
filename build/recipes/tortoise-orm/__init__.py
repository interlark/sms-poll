from pythonforandroid.recipe import PythonRecipe


class TortoiseOrmRecipe(PythonRecipe):
    name = 'tortoise-orm'
    version = '0.19.2'
    url = 'https://files.pythonhosted.org/packages/ef/fa/18ca86cafc210358b99ab227980647d6c7c12aaef70d9126b83958012a97/tortoise-orm-0.19.2.tar.gz'

    call_hostpython_via_targetpython = False
    install_in_hostpython = False
    depends = ['aiosqlite', 'iso8601', 'pypika-tortoise', 'pytz']


recipe = TortoiseOrmRecipe()
