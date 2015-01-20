Name:           ros-indigo-object-recognition-core
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS object_recognition_core package

Group:          Development/Libraries
License:        BSD
URL:            http://wg-perception.github.io/object_recognition_core/
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       couchdb
Requires:       libcurl-devel
Requires:       ros-indigo-ecto
Requires:       ros-indigo-ecto-image-pipeline
Requires:       ros-indigo-sensor-msgs
BuildRequires:  boost-devel
BuildRequires:  libcurl-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-ecto
BuildRequires:  ros-indigo-ecto-image-pipeline
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
object_recognition_core contains tools to launch several recognition pipelines,
train objects, store models ...

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jan 20 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.6.4-0
- Autogenerated by Bloom

