%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-webots-ros2-control
Version:        2023.1.3
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS webots_ros2_control package

License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-controller-manager
Requires:       ros-jazzy-hardware-interface
Requires:       ros-jazzy-pluginlib
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-lifecycle
Requires:       ros-jazzy-webots-ros2-driver
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-controller-manager
BuildRequires:  ros-jazzy-hardware-interface
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-lifecycle
BuildRequires:  ros-jazzy-ros-environment
BuildRequires:  ros-jazzy-webots-ros2-driver
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-lint-auto
BuildRequires:  ros-jazzy-ament-lint-common
%endif

%description
ros2_control plugin for Webots

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
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

