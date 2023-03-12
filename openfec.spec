Name:		openfec
Version:	1.4.2.9
Release:	1
Summary:	Application-Level Forward Erasure Correction codes
License:	CeCILL-C and GPLv2+ and BSD
URL:		  https://github.com/roc-streaming/openfec
Source0:	https://github.com/roc-streaming/openfec/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	coreutils
BuildRequires:	findutils
# https://github.com/roc-streaming/openfec/pull/6
# https://github.com/OpenFEC/OpenFEC/pull/2
#Patch0:		openfec-1.4.2-distro-cmake.patch
# https://github.com/roc-streaming/openfec/pull/2
#Patch1:		openfec-1.4.2.4-big-endian-fix.patch

%description
Application-Level Forward Erasure Correction codes, or AL-FEC (also called
UL-FEC, for Upper-Layers FEC). The idea, in one line, is to add redundancy
in order to be able to recover from erasures. Because of their position in
the communication stack, these codes are implemented as software codecs,
and they find many applications in robust transmission and distrituted
storage systems.

%package devel
Summary: Development libraries for openfec
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The openfec-devel package contains header files necessary for
developing programs using openfec.

%package utils
Summary: Utilities for openfec
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for openfec.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

# Install headers
mkdir -p %{buildroot}%{_includedir}/%{name}
pushd src
find -name '*.h' -type f -exec install -pDm 0644 '{}' %{buildroot}%{_includedir}/%{name}/'{}' \;
popd


%files
%license LICENCE_CeCILL-C_V1-en.txt Licence_CeCILL_V2-en.txt
%doc README CHANGELOG
%{_libdir}/libopenfec.so.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/libopenfec.so

%files utils
%{_bindir}/descr_stats
%{_bindir}/eperftool
%{_bindir}/simple_client
%{_bindir}/simple_server
