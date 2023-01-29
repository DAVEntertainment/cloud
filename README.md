# cloud thirdparties
cloud thirdparties' build scripts

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
4. build the library with you build script, and install it to cloud root, e.g. `cloud/boost-1.80.0` (name rule: <library>-<full-version>)
5. pack the library with 7z and track them in `cloud/packages`, e.g. `cloud/packages/boost-1.80.0.7z`

# additional information
1. if not specified, we build both static and shared library for default
2. a library is a static library if it has a `-static` postfix
3. a library is a shared library if it has a `-shared` postfix
4. a library contains both static and shared libraries if no `-shared` nor `-static` specified
5. `-release` and `-debug` are in a similar situation (just like `-shared` and `-static`)
