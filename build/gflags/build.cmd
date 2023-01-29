@REM need to clone https://github.com/gflags/gflags.git into gflags

@set STARTUP_DIR=%cd%
@set SCRIPT_DIR=%~dp0
@set VERSION=2.2.2
@set SOURCE_DIR=%SCRIPT_DIR%\gflags
@set BUILD_DIR=%SOURCE_DIR%\.build
@set INSTALL_DIR=%SCRIPT_DIR%\..\..\gflags-%VERSION%
@set TEST_PACKAGE_DIR=%SCRIPT_DIR%\test_package
@set TEST_PACKAGE_BUILD_DIR=%TEST_PACKAGE_DIR%\.build

@echo ##########################################################################################################
@echo building gflags
@echo   SOURCE_DIR              : %SOURCE_DIR%
@echo   VERSION                 : %VERSION%
@echo   BUILD_DIR               : %BUILD_DIR%
@echo   INSTALL_DIR             : %INSTALL_DIR%
@echo   TEST_PACKAGE_DIR        : %TEST_PACKAGE_DIR%
@echo   TEST_PACKAGE_BUILD_DIR  : %TEST_PACKAGE_BUILD_DIR%
@echo ##########################################################################################################

@REM step 1. checkout version
@pushd %SOURCE_DIR%
@if not "%errorlevel%" == "0" (
    @echo source dir not exists !!!
    @echo need to run "git clone https://github.com/gflags/gflags.git gflags --branch v%VERSION%" first
    @goto error
)

git checkout v%VERSION%
@if not "%errorlevel%" == "0" (
    echo "checkout to branch v%VERSION% failed !!! (%cd%)"
    goto end
)
git reset --hard

@REM step 2. build library
cmake -S %SOURCE_DIR% -B %BUILD_DIR% -G"Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR% -DGFLAGS_BUILD_SHARED_LIBS=ON -DGFLAGS_BUILD_STATIC_LIBS=ON
cmake --build %BUILD_DIR% --config Debug -j10
cmake --install %BUILD_DIR% --config Debug
cmake --build %BUILD_DIR% --config Release -j10
cmake --install %BUILD_DIR% --config Release

@REM step 3. test with test_package
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
