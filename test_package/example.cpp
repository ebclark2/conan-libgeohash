#include <iostream>
#include <iomanip>
#include <stdexcept>
extern "C" {
#include "geohash.h"
}

#include <cmath>

bool AreSame(double a, double b, double epsilon=0.000001) {
    return std::fabs(a - b) < epsilon;
}

int main() {
  double lat = 1.0;
  double lng = 2.0;
  char * geohash = geohash_encode(lat, lng, 11);
  GeoCoord g = geohash_decode(geohash);

  std::cout<<std::fixed<<"Latitude="<<std::setprecision(10)<<lat<<" Longitude="<<lng<<std::endl;
  std::cout<<"Encoded geohash: \'"<<geohash<<"\'"<<std::endl;
  std::cout<<std::fixed<<"Decoded geohash.Latitude="<<std::setprecision(10)
           <<g.latitude<<" Longitude="<<g.longitude<<std::endl;

  if (!AreSame(g.latitude, lat) || !AreSame(g.longitude,lng)) {
    throw std::runtime_error("Decoded latitude and longitude doesn't match");
  }
  return 0;
}
