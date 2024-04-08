%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-webots-ros2-epuck
Version:        2023.1.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS webots_ros2_epuck package

License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-builtin-interfaces
Requires:       ros-iron-controller-manager
Requires:       ros-iron-diff-drive-controller
Requires:       ros-iron-geometry-msgs
Requires:       ros-iron-joint-state-broadcaster
Requires:       ros-iron-nav-msgs
Requires:       ros-iron-rclpy
Requires:       ros-iron-robot-state-publisher
Requires:       ros-iron-rviz2
Requires:       ros-iron-sensor-msgs
Requires:       ros-iron-std-msgs
Requires:       ros-iron-tf2-ros
Requires:       ros-iron-webots-ros2-control
Requires:       ros-iron-webots-ros2-driver
Requires:       ros-iron-webots-ros2-msgs
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-iron-ament-copyright
%endif

%description
E-puck2 driver for Webots simulated robot

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Mon Apr 08 2024 Cyberbotics <support@cyberbotics.com> - 2023.1.2-1
- Autogenerated by Bloom

* Tue Jul 18 2023 Cyberbotics <support@cyberbotics.com> - 2023.1.1-2
- Autogenerated by Bloom

* Tue Jul 11 2023 Cyberbotics <support@cyberbotics.com> - 2023.1.1-1
- Autogenerated by Bloom

* Thu Jun 29 2023 Cyberbotics <support@cyberbotics.com> - 2023.1.0-1
- Autogenerated by Bloom

* Tue May 23 2023 Cyberbotics <support@cyberbotics.com> - 2023.0.4-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Cyberbotics <support@cyberbotics.com> - 2023.0.3-3
- Autogenerated by Bloom

* Wed Apr 12 2023 Cyberbotics <support@cyberbotics.com> - 2023.0.3-1
- Autogenerated by Bloom

* Wed Mar 22 2023 Cyberbotics <support@cyberbotics.com> - 2023.0.2-2
- Autogenerated by Bloom

