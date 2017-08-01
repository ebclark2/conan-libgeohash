#include <iostream>
extern "C" {
#include "geohash.h"
}

int main() {
  char * geohash = geohash_encode(1.0, 2.0, 0);
}
