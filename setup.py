import pypandoc
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='easy_server_indexing',  # How you named your package folder (MyLib)
    packages=['easy_server_indexing'],  # Chose the same as "name"
    version='0.1.1',  # Start with a small number and increase it with every change you make
    license='mit  ',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='The following package can be integrated into a server indexing softwares which will skip the already traversed files and resume the traversing from the stated error file path.',
    # Give a short description about your library
    long_description = long_description,
        #
    author='Pankaj Sonar, Piyush Rumao',  # Type in your name
    author_email='pankaj.sonar@ucdconnect.ie, piyushrumao@gmail.com',  # Type in your E-Mail
    url='https://github.com/pankajsonar19/easy_server_indexing',
    # Provide either the link to your github or to your website
    download_url='https://github.com/pankajsonar19/easy_server_indexing.git',  # I explain this later on
    keywords=['indexing', 'resume_code', 'resume', 'resumecode','resume_crawl','oswalk','traverse','server_indexing','pause','pause indexing','crawl','listdir'],  # Keywords that define your package best
    install_requires=['pypandoc'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
