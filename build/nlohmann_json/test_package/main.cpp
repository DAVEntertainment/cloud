#include <iostream>
#include <string>
#include <nlohmann/json.hpp>

int main() {
    std::string content = R"(
        {
            "pi": 3.141,
            "happy": true
        }
    )";
    auto json0 = nlohmann::json::parse(content);
    std::cout << "content: " << content << std::endl;
    std::cout << "json0: " << json0 << std::endl;

    nlohmann::json json1 = {
        {"pi", 3.141},
        {"happy", true},
    };
    std::cout << "json1: " << json1 << std::endl;
    return 0;
}
