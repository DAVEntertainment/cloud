# description
build for googletest

# how-to

### 1. clone from github
clone from github
```
git clone https://github.com/google/googletest.git gtest
```

checkout to interested version, here, we use `release-1.12.1`
```
cd gtest
git checkout release-1.12.1
```

### 2. build
run the following command
```
cd gtest
mkdir .build
cd .build
cmake -G"Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=gtest-1.12.1 -DCMAKE_DEBUG_POSTFIX=d -Dgtest_force_shared_crt=ON ..
cmake --install .
```

`build.cmd` is used for cloud package gtest-1.12.1 and gtest-1.12.1-shared

### 3. track library
pack `gtest-<version>` with 7z to `gtest-<version>.7z`,
move to `cloud/gtest-<version>.7z`,
track and commit, push with git.
