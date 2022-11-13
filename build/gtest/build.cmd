@REM need to clone https://github.com/google/googletest.git into gtest

@set STARTUP_DIR=%cd%
@set SCRIPT_DIR=%~dp0
@set VERSION=1.12.1
@set SOURCE_DIR=%SCRIPT_DIR%\gtest
@set BUILD_DIR=%SOURCE_DIR%\.build

@echo ##########################################################################################################
@echo gtest info
@echo   SOURCE_DIR   : %SOURCE_DIR%
@echo   VERSION      : %VERSION%
@echo ##########################################################################################################

@REM step 1. checkout version
@pushd %SOURCE_DIR%
@if not "%errorlevel%" == "0" (
    @echo source dir not exists !!!
    @goto end
)

git checkout release-%VERSION%
git reset --hard

@REM step 2. build static library
@set INSTALL_DIR=%SCRIPT_DIR%\..\..\gtest-%VERSION%
@set GTEST_CONFIG=-DCMAKE_DEBUG_POSTFIX=d -Dgtest_force_shared_crt=ON -DBUILD_SHARED_LIBS=OFF
@echo ##########################################################################################################
@echo building gtest
@echo   SOURCE_DIR   : %SOURCE_DIR%
@echo   VERSION      : %VERSION%
@echo   BUILD_DIR    : %BUILD_DIR%
@echo   INSTALL_DIR  : %INSTALL_DIR%
@echo   GTEST_CONFIG : %GTEST_CONFIG%
@echo ##########################################################################################################

cmake -S %SOURCE_DIR% -B %BUILD_DIR% -G"Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR% %GTEST_CONFIG%
cmake --build %BUILD_DIR% --config Debug -j10
cmake --build %BUILD_DIR% --config Release -j10
cmake --install %BUILD_DIR% --config Debug
cmake --install %BUILD_DIR% --config Release

@REM step 3. build shared library
@set INSTALL_DIR=%SCRIPT_DIR%\..\..\gtest-%VERSION%-shared
@set GTEST_CONFIG=-DCMAKE_DEBUG_POSTFIX=d -Dgtest_force_shared_crt=ON -DBUILD_SHARED_LIBS=ON
@echo ##########################################################################################################
@echo building gtest
@echo   SOURCE_DIR   : %SOURCE_DIR%
@echo   VERSION      : %VERSION%
@echo   BUILD_DIR    : %BUILD_DIR%
@echo   INSTALL_DIR  : %INSTALL_DIR%
@echo   GTEST_CONFIG : %GTEST_CONFIG%
@echo ##########################################################################################################

cmake -S %SOURCE_DIR% -B %BUILD_DIR% -G"Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR% %GTEST_CONFIG%
cmake --build %BUILD_DIR% --config Debug -j10
cmake --build %BUILD_DIR% --config Release -j10
cmake --install %BUILD_DIR% --config Debug
cmake --install %BUILD_DIR% --config Release

:end
@popd
