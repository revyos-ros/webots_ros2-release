// Copyright 1996-2024 Cyberbotics Ltd.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef TOUCHSENSOR_HPP
#define TOUCHSENSOR_HPP

#include <webots/Device.hpp>

namespace webots {
  class TouchSensor : public Device {
  public:
    typedef enum { BUMPER = 0, FORCE, FORCE3D } Type;

    explicit TouchSensor(const std::string &name) : Device(name) {}  // Use Robot::getTouchSensor() instead
    explicit TouchSensor(WbDeviceTag tag) : Device(tag) {}
    virtual ~TouchSensor() {}

    virtual void enable(int samplingPeriod);
    virtual void disable();
    int getSamplingPeriod() const;

    double getValue() const;
    const double *getValues() const;

    int getLookupTableSize() const;
    const double *getLookupTable() const;

    Type getType() const;
  };
}  // namespace webots

#endif  // TOUCHSENSOR_HPP
