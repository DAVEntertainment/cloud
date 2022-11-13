# description
build for nlohmann json

nlohmann json is a header-only library and supports cmake,
so running cmake basic flow is enough

# how-to

### 1. clone from github
clone from github
```
git clone https://github.com/nlohmann/json.git nlohmann_json
```

checkout to interested version, here, we use `v3.11.2`
```
cd nlohmann_json
git checkout v3.11.2
```

### 2. build
run the following command
```
cd nlohmann_json
mkdir .build
cd .build
cmake -DCMAKE_INSTALL_PREFIX=nlohmann_json-3.11.2 ..
cmake --install .
```

### 3. track library
pack `nlohmann_json-<version>` with 7z to `nlohmann_json-<version>.7z`,
move to `cloud/nlohmann_json-<version>.7z`,
track and commit, push with git.
