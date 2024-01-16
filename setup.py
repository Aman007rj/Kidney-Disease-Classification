import setuptools

with open('README.MD', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
__version__ ='0.0.0'

REPO_NAME = 'Kidney-Disease-Classifier'
AUTHOR_NAME = 'Aman007rj'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'aman007tj@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='CNN app',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    
)