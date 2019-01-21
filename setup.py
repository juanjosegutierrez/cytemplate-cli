from setuptools import setup
import blackjack

setup(
    name='blackjack',
    version=blackjack.__version__,
    packages=['blackjack'],
    entry_points={
        'console_scripts': [
            'blackjack = blackjack.__main__:main'
        ]
    }
)
