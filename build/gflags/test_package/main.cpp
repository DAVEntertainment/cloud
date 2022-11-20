#include <iostream>
#include <string>
#include <vector>

#define STRIP_FLAG_HELP 1
#include <gflags/gflags.h>

DEFINE_bool(joke, false, "tell a joke?");
DEFINE_int32(age, 18, "your age");

int main(int argc, char* argv[]) {
    // doc http://gflags.github.io/gflags/

    // show command lines
    google::SetArgv(argc, (const char**)argv);
    std::cout << "args: " << std::endl;
    for(auto& arg: google::GetArgvs()) {
        std::cout << "   " << arg << std::endl;
    }

    // parse
    gflags::ParseCommandLineFlags(&argc, &argv, false);
    std::cout << "configs:" << std::endl;
    std::cout << "   joke: " << (FLAGS_joke? "true": "false") << std::endl;
    std::cout << "   age : " << FLAGS_age << std::endl;
    return 0;
}
