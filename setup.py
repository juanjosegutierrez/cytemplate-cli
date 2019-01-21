import cytemplate
import sys
from distutils.core import setup
from distutils.extension import Extension

MOD_NAMES = [
    'cytemplate.cython_add',
]


def cythonize_extensions(extensions):
    from Cython.Build import cythonize
    return cythonize(extensions)


def setup_package():
    use_cython = False
    if 'develop' in sys.argv:
        use_cython = True

    extensions = []
    for name in MOD_NAMES:
        path = name.replace('.', '/')
        if use_cython:
            ext = '.pyx'
        else:
            ext = '.c'      
        extensions.append(Extension(name, [path + ext]))
    
    if use_cython:
        extensions = cythonize_extensions(extensions)

    setup(
        name='cytemplate-cli',
        author=cytemplate.__author__,
        author_email=cytemplate.__email__,
        description=cytemplate.__summary__,
        license=cytemplate.__license__,
        url=cytemplate.__url__,
        version=cytemplate.__version__,
        zip_safe=False,
        packages=['cytemplate'],
        ext_modules=extensions,
        entry_points={
            'console_scripts': [
                'cytemplate = cytemplate.__main__:main'
            ]
        }
    )

if __name__ == '__main__':
    setup_package()
