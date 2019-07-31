"""
第三方库自动安装脚本
ps:不推荐使用这种方式，因为os.system能执行的不仅仅是pip命令，这种方式存在安全隐患
假如被人os.system("rm -rf")一下那就可怕了
推荐使用pip install requirement.txt方式
requirement.txt中可以指定lib的版本
例如pandas=0.23.0
"""
import os
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", "jieba", "beautifulsoup4", "wheel", "networkx",
        "sympy", "pyinstaller", "django", "flask", "werobot", "pyqt5", "pandas", "pyopengl", "pypdf2", "docopt", "pygame"}
try:
    for lib in libs:
        os.system("pip install "+lib)
    print("Successful")
except:
    print("Falied somehow")
