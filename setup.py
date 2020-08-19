from distutils.core import setup

package_dir = {
    # 注意这个要写全，所有文件夹都要！
    "Cat_Library.information":"./Cat_Library/information",
    "Cat_Library.cat_shape":"./Cat_Library/information",
    }

packages = list(package_dir.keys())

setup(name='Cat_Library',
    version='1.0',
    author='TrainHeartnetCat',
    description='Cat_Library is a training project for oldcat.',
    url="https://github.com/TrainHeartnetCat/Cat_Library",
    package_dir=package_dir,
    packages=packages,
)