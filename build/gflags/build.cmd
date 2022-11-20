@REM need to clone https://github.com/gflags/gflags.git into gflags

@set STARTUP_DIR=%cd%
@set SCRIPT_DIR=%~dp0
@set VERSION=2.2.2
@set SOURCE_DIR=%SCRIPT_DIR%\gflags
@set BUILD_DIR=%SOURCE_DIR%\.build
@set INSTALL_DIR=%SCRIPT_DIR%\..\..\gflags-%VERSION%

@echo ##########################################################################################################
@echo building gflags
@echo   SOURCE_DIR   : %SOURCE_DIR%
@echo   VERSION      : %VERSION%
@echo   BUILD_DIR    : %BUILD_DIR%
@echo   INSTALL_DIR  : %INSTALL_DIR%
@echo ##########################################################################################################

@REM step 1. checkout version
@pushd %SOURCE_DIR%
@if not "%errorlevel%" == "0" (
    @echo source dir not exists !!!
    @goto end
)

git checkout release-%VERSION%
git reset --hard

@REM step 2. build library
cmake -S %SOURCE_DIR% -B %BUILD_DIR% -G"Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR% -DGFLAGS_BUILD_SHARED_LIBS=ON -DGFLAGS_BUILD_STATIC_LIBS=ON
cmake --build %BUILD_DIR% --config Debug -j10
cmake --build %BUILD_DIR% --config Release -j10
cmake --install %BUILD_DIR% --config Debug
cmake --install %BUILD_DIR% --config Release

:end
@popd
