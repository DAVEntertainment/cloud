# description
build for gflags

# how-to

### 1. clone from github
clone from github
```
git clone https://github.com/gflags/gflags.git gflags
```

checkout to interested version, here, we use `v2.2.2`
```
cd gflags
git checkout v2.2.2
```

### 2. build
run the following command
```
cd gflags
mkdir .build
cd .build
cmake -G"Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=gflags-2.2.2 -DGFLAGS_BUILD_SHARED_LIBS=ON -DGFLAGS_BUILD_STATIC_LIBS=ON ..
cmake --build . --config Debug -j12
cmake --install . --config Debug
```

`build.cmd` is used for cloud package gflags-2.2.2

### 3. track library
pack `gflags-<version>` with 7z to `gflags-<version>.7z`,
move to `cloud/gflags-<version>.7z`,
track and commit, push with git.
