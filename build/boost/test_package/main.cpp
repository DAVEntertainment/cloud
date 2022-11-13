#include <iostream>
#include <boost/version.hpp>
#include <boost/date_time.hpp>

int main() {
    auto now = boost::posix_time::second_clock::local_time();
    std::cout << "Starting at: " << now << std::endl;
    std::cout << "Boost version: " << BOOST_VERSION << std::endl;
    return 0;
}
