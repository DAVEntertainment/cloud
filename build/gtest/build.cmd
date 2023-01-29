@REM need to clone https://github.com/google/googletest.git into gtest

@set STARTUP_DIR=%cd%
@set SCRIPT_DIR=%~dp0
@set VERSION=1.12.1
@set SOURCE_DIR=%SCRIPT_DIR%\gtest
@set BUILD_DIR=%SOURCE_DIR%\.build
@set TEST_PACKAGE_DIR=%SCRIPT_DIR%\test_package
@set TEST_PACKAGE_BUILD_DIR=%TEST_PACKAGE_DIR%\.build

@echo ##########################################################################################################
@echo gtest info
@echo   SOURCE_DIR   : %SOURCE_DIR%
@echo   VERSION      : %VERSION%
@echo ##########################################################################################################

@REM step 1. checkout version
@pushd %SOURCE_DIR%
@if not "%errorlevel%" == "0" (
    @echo source dir not exists !!!
    @echo need to run "git clone https://github.com/google/googletest.git gtest --branch release-%VERSION%" first
    @goto error
)

git checkout release-%VERSION%
@if not "%errorlevel%" == "0" (
    @echo "checkout to branch release-%VERSION% failed !!! (%cd%)"
    @goto error
)
git reset --hard

@REM step 2. build static library
@set INSTALL_DIR=%SCRIPT_DIR%\..\..\gtest-%VERSION%-static
@set GTEST_CONFIG=-DCMAKE_DEBUG_POSTFIX=d -Dgtest_force_shared_crt=ON -DBUILD_SHARED_LIBS=OFF
@echo ##########################################################################################################
@echo building gtest
@echo   SOURCE_DIR              : %SOURCE_DIR%
@echo   VERSION                 : %VERSION%
@echo   BUILD_DIR               : %BUILD_DIR%
@echo   INSTALL_DIR             : %INSTALL_DIR%
@echo   GTEST_CONFIG            : %GTEST_CONFIG%
@echo   TEST_PACKAGE_DIR        : %TEST_PACKAGE_DIR%
@echo   TEST_PACKAGE_BUILD_DIR  : %TEST_PACKAGE_BUILD_DIR%
@echo ##########################################################################################################

cmake -S %SOURCE_DIR% -B %BUILD_DIR% -G"Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR% %GTEST_CONFIG%
cmake --build %BUILD_DIR% --config Debug -j10
cmake --install %BUILD_DIR% --config Debug
cmake --build %BUILD_DIR% --config Release -j10
cmake --install %BUILD_DIR% --config Release

cmake -S %TEST_PACKAGE_DIR% -B %TEST_PACKAGE_BUILD_DIR% -G"Visual Studio 16 2019" -DCMAKE_PREFIX_PATH=%INSTALL_DIR%
cmake --build %TEST_PACKAGE_BUILD_DIR% --config Debug -j10
cmake --build %TEST_PACKAGE_BUILD_DIR% --config Release -j10

%TEST_PACKAGE_BUILD_DIR%\Debug\test_package.exe
@if not "%errorlevel%" == "0" (
    @echo run test package with config Debug failed, abort!!!
    @goto error
)
%TEST_PACKAGE_BUILD_DIR%\Release\test_package.exe
@if not "%errorlevel%" == "0" (
    @echo run test package with config Release failed, abort!!!
    @goto error
)

@REM step 3. build shared library
@set INSTALL_DIR=%SCRIPT_DIR%\..\..\gtest-%VERSION%-shared
@set GTEST_CONFIG=-DCMAKE_DEBUG_POSTFIX=d -Dgtest_force_shared_crt=ON -DBUILD_SHARED_LIBS=ON
@echo ##########################################################################################################
@echo building gtest
@echo   SOURCE_DIR              : %SOURCE_DIR%
@echo   VERSION                 : %VERSION%
@echo   BUILD_DIR               : %BUILD_DIR%
@echo   INSTALL_DIR             : %INSTALL_DIR%
@echo   GTEST_CONFIG            : %GTEST_CONFIG%
@echo   TEST_PACKAGE_DIR        : %TEST_PACKAGE_DIR%
@echo   TEST_PACKAGE_BUILD_DIR  : %TEST_PACKAGE_BUILD_DIR%
@echo ##########################################################################################################

cmake -S %SOURCE_DIR% -B %BUILD_DIR% -G"Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR% %GTEST_CONFIG%
cmake --build %BUILD_DIR% --config Debug -j10
cmake --install %BUILD_DIR% --config Debug
cmake --build %BUILD_DIR% --config Release -j10
cmake --install %BUILD_DIR% --config Release

cmake -S %TEST_PACKAGE_DIR% -B %TEST_PACKAGE_BUILD_DIR% -G"Visual Studio 16 2019" -DCMAKE_PREFIX_PATH=%INSTALL_DIR%
cmake --build %TEST_PACKAGE_BUILD_DIR% --config Debug -j10
cmake --build %TEST_PACKAGE_BUILD_DIR% --config Release -j10

%TEST_PACKAGE_BUILD_DIR%\Debug\test_package.exe
@if not "%errorlevel%" == "0" (
    @echo run test package with config Debug failed, abort!!!
    @goto error
)
%TEST_PACKAGE_BUILD_DIR%\Release\test_package.exe
@if not "%errorlevel%" == "0" (
    @echo run test package with config Release failed, abort!!!
    @goto error
)

@goto end

:error
@set errorlevel=1

:end
@popd
