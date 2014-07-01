关于如何打包并安装Python函数包

win：
进入到CMD，并移动到python函数包目录（前提是有函数文件.py以及setup.py文件）
输入python setup.py sdist 进行打包

接着输入python setup.py install
进行函数安装