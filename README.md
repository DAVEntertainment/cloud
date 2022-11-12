# thirdparties
thirdparties' binary for win32 x86_64 msvc2019 md

# structure
```
cloud
|-- build   // thirdparty library build materials
|   |-- pyutils // python scripts
|   |-- pylint  // python lint related
|   |-- boost   // boost library build materials
|   |   |-- build.py
|   |   `-- README.md   // instruction for building this library, we MUST add one for each library
|   |-- ...     // other libraries
|   `-- nlohmann_json   // nlohmann_json library
|       |-- build.py
|       `-- README.md
`-- packages    // thirdparty libraries packages, to use them, simply distract them
    `-- boost-1.80.0.7z // boost library
```

# how to add a new thirdparty
1. add a folder for the library, e.g. `cloud/build/boost`
2. add build scripts, e.g. `cloud/build/boost/build.py`
3. add `README.md` with instructions to build the library, e.g. `cloud/build/boost/README.md`
4. add `.repo` file(empty) for the library, e.g. `cloud/build/boost/.repo`(so that lint will ignore the folder)
5. build the library with you build script, and install it to cloud root, e.g. `cloud/boost-1.80.0` (name rule: <library>-<full-version>)
6. pack the library with 7z and track them in `cloud/packages`, e.g. `cloud/packages/boost-1.80.0.7z`
