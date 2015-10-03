from distutils.core import setup

setup(
    name='copusher',
    packages=['copusher', 'copusher.storages'],
    version='0.0.1',
    description='A robust Comand Output PUSHER',
    author='Yura Lukashik',
    author_email='YuraLukashik@gmail.com',
    url='https://github.com/YuraLukashik/copusher',
    download_url='https://github.com/YuraLukashik/copusher/tarball/0.0.1',
    keywords=['command', 'output', 'push'],
    classifiers=[],
    install_requires=['pyperclip',],
    scripts=['bin/copusher']
)
