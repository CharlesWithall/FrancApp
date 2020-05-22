from cx_Freeze import setup, Executable

setup(
    name="FrancApp",
    version="0.1",
    description="French language learning app",
    executables=[Executable("FA_Window.py")])
