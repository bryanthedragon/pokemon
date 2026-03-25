from setuptools import setup

setup(
    name='pokemon',
    version='0.1.0',
    description='Generation 1-9 Pokemon lookup and battle simulation',
    forked_url='https://github.com/pcattori/pokemon',

    # OG author
    author='Pedro Cattori',
    author_email='pcattori@gmail.com',

    # forker (me)
    coAuthor= "Brayanthedragon",
    coAuthor_email="brayanthedragon@gmail.com",
    
    packages=
    [
        'pokemon', 'fetch'
    ],
    package_dir=
    {
        'pokemon': 'pokemon'
    },

    package_data=
    {
        'pokemon': 
        [
            'data/*.json'
        ]
    },

    extras_require={
        'fetch': 
        [
            'beautifulsoup4==4.5.1',
            'requests==2.12.4'
        ]
    }
)
