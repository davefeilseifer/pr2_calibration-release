Name:           ros-hydro-pr2-se-calibration-launch
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS pr2_se_calibration_launch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_se_calibration_launch
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-pr2-calibration-launch
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-pr2-calibration-launch

%description
pr2_se_calibration_launch

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Oct 14 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.5-0
- Autogenerated by Bloom

* Wed Sep 17 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.4-0
- Autogenerated by Bloom

* Thu Sep 11 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.3-0
- Autogenerated by Bloom

* Mon Sep 08 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.2-0
- Autogenerated by Bloom

