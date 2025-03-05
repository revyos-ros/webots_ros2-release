%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-webots-ros2-tests
Version:        2025.0.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS webots_ros2_tests package

License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-jazzy-rclpy
BuildRequires:  ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ros2bag
BuildRequires:  ros-jazzy-rosbag2-storage-default-plugins
BuildRequires:  ros-jazzy-webots-ros2-driver
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-jazzy-ament-copyright
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-launch
BuildRequires:  ros-jazzy-launch-testing
BuildRequires:  ros-jazzy-launch-testing-ament-cmake
BuildRequires:  ros-jazzy-launch-testing-ros
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-std-srvs
BuildRequires:  ros-jazzy-tf2-ros
BuildRequires:  ros-jazzy-webots-ros2-epuck
BuildRequires:  ros-jazzy-webots-ros2-husarion
BuildRequires:  ros-jazzy-webots-ros2-mavic
BuildRequires:  ros-jazzy-webots-ros2-tesla
BuildRequires:  ros-jazzy-webots-ros2-tiago
BuildRequires:  ros-jazzy-webots-ros2-turtlebot
BuildRequires:  ros-jazzy-webots-ros2-universal-robot
%endif

%description
System tests for `webots_ros2` packages.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/jazzy"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Wed Mar 05 2025 Cyberbotics <support@cyberbotics.com> - 2025.0.0-1
- Autogenerated by Bloom

* Thu Nov 21 2024 Cyberbotics <support@cyberbotics.com> - 2023.1.3-3
- Autogenerated by Bloom

* Tue Nov 12 2024 Cyberbotics <support@cyberbotics.com> - 2023.1.3-2
- Autogenerated by Bloom

* Thu Sep 26 2024 Cyberbotics <support@cyberbotics.com> - 2023.1.3-1
- Autogenerated by Bloom

* Tue Jun 25 2024 Cyberbotics <support@cyberbotics.com> - 2023.1.2-6
- Autogenerated by Bloom

* Tue Jun 18 2024 Cyberbotics <support@cyberbotics.com> - 2023.1.2-5
- Autogenerated by Bloom

* Fri Apr 19 2024 Cyberbotics <support@cyberbotics.com> - 2023.1.2-4
- Autogenerated by Bloom

* Mon Apr 08 2024 Cyberbotics <support@cyberbotics.com> - 2023.1.2-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Cyberbotics <support@cyberbotics.com> - 2023.1.1-3
- Autogenerated by Bloom

