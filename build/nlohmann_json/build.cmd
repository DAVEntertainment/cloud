@REM need to clone https://github.com/nlohmann/json.git into nlohmann_json

@set STARTUP_DIR=%cd%
@set SCRIPT_DIR=%~dp0
@set VERSION=3.11.2
@set SOURCE_DIR=%SCRIPT_DIR%\nlohmann_json
@set BUILD_DIR=%SOURCE_DIR%\.build
@set INSTALL_DIR=%SCRIPT_DIR%\..\..\nlohmann_json-%VERSION%

@echo ##########################################################################################################
@echo building nlohmann_json
@echo   SOURCE_DIR  : %SOURCE_DIR%
@echo   VERSION     : %VERSION%
@echo   BUILD_DIR   : %BUILD_DIR%
@echo   INSTALL_DIR : %INSTALL_DIR%
@echo ##########################################################################################################

@pushd %SOURCE_DIR%
@if not "%errorlevel%" == "0" (
    @echo source dir not exists !!!
    @goto end
)

git checkout v%VERSION%
git reset --hard

cmake -S %SOURCE_DIR% -B %BUILD_DIR% -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR%
cmake --install %BUILD_DIR%

:end
@popd
