rem the nx installation dir. if there are spaces in the path, it needs to be quoted like here - quotes around the whole equation
SET "UGII_BASE_DIR=C:\Program Files\Siemens\NX 12.0"
rem these two are not used by nx, just for setting the path
SET UGII_ROOT_DIR=%UGII_BASE_DIR%\UGII
SET UGII_NXBIN_DIR=%UGII_BASE_DIR%\NXBIN
rem the installed python interpreter, version 3.6 for nx12
SET PYTHON=C:\Users\kowuki\.conda\envs\nx12
SET INTERPRETER=%PYTHON%;%PYTHON%\DLLs;%PYTHON%\Lib;%PYTHON%\Lib\site-packages
SET PYTHONPATH=%INTERPRETER%;%UGII_BASE_DIR%\nxbin\python
SET PATH=%PATH%;%UGII_NXBIN_DIR%;%UGII_ROOT_DIR%
start "" "C:\Program Files\JetBrains\PyCharm 2023.1.1\bin\pycharm64.exe"