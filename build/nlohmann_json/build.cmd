@REM need to clone https://github.com/nlohmann/json.git into nlohmann_json

@set STARTUP_DIR=%cd%
@set SCRIPT_DIR=%~dp0
@set VERSION=3.11.2
@set SOURCE_DIR=%SCRIPT_DIR%\nlohmann_json
@set BUILD_DIR=%SOURCE_DIR%\.build
@set INSTALL_DIR=%SCRIPT_DIR%\..\..\nlohmann_json-%VERSION%
@set TEST_PACKAGE_DIR=%SCRIPT_DIR%\test_package
@set TEST_PACKAGE_BUILD_DIR=%TEST_PACKAGE_DIR%\.build

@echo ##########################################################################################################
@echo building nlohmann_json
@echo   SOURCE_DIR              : %SOURCE_DIR%
@echo   VERSION                 : %VERSION%
@echo   BUILD_DIR               : %BUILD_DIR%
@echo   INSTALL_DIR             : %INSTALL_DIR%
@echo   TEST_PACKAGE_DIR        : %TEST_PACKAGE_DIR%
@echo   TEST_PACKAGE_BUILD_DIR  : %TEST_PACKAGE_BUILD_DIR%
@echo ##########################################################################################################

@pushd %SOURCE_DIR%
@if not "%errorlevel%" == "0" (
    @echo source dir not exists !!!
    @echo need to run "git clone https://github.com/nlohmann/json.git nlohmann_json --branch v%VERSION%" first
    @goto error
)

git checkout v%VERSION%
@if not "%errorlevel%" == "0" (
    @echo "checkout to branch v%VERSION% failed !!! (%cd%)"
    @goto error
)
git reset --hard

cmake -S %SOURCE_DIR% -B %BUILD_DIR% -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR%
cmake --install %BUILD_DIR%

cmake -S %TEST_PACKAGE_DIR% -B %TEST_PACKAGE_BUILD_DIR% -DCMAKE_PREFIX_PATH=%INSTALL_DIR%
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
