#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asciinema
Version  : 2.1.0
Release  : 22
URL      : https://github.com/asciinema/asciinema/archive/v2.1.0/asciinema-2.1.0.tar.gz
Source0  : https://github.com/asciinema/asciinema/archive/v2.1.0/asciinema-2.1.0.tar.gz
Summary  : Terminal session recorder
Group    : Development/Tools
License  : GPL-3.0
Requires: asciinema-bin = %{version}-%{release}
Requires: asciinema-license = %{version}-%{release}
Requires: asciinema-man = %{version}-%{release}
Requires: asciinema-python = %{version}-%{release}
Requires: asciinema-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# asciinema
[![Build Status](https://github.com/asciinema/asciinema/actions/workflows/asciinema.yml/badge.svg)](https://github.com/asciinema/asciinema/actions/workflows/asciinema.yml)
[![PyPI](https://img.shields.io/pypi/v/asciinema.svg)](https://pypi.org/project/asciinema/)
[![license](http://img.shields.io/badge/license-GNU-blue.svg)](https://raw.githubusercontent.com/asciinema/asciinema/master/LICENSE)

%package bin
Summary: bin components for the asciinema package.
Group: Binaries
Requires: asciinema-license = %{version}-%{release}

%description bin
bin components for the asciinema package.


%package doc
Summary: doc components for the asciinema package.
Group: Documentation
Requires: asciinema-man = %{version}-%{release}

%description doc
doc components for the asciinema package.


%package license
Summary: license components for the asciinema package.
Group: Default

%description license
license components for the asciinema package.


%package man
Summary: man components for the asciinema package.
Group: Default

%description man
man components for the asciinema package.


%package python
Summary: python components for the asciinema package.
Group: Default
Requires: asciinema-python3 = %{version}-%{release}

%description python
python components for the asciinema package.


%package python3
Summary: python3 components for the asciinema package.
Group: Default
Requires: python3-core
Provides: pypi(asciinema)

%description python3
python3 components for the asciinema package.


%prep
%setup -q -n asciinema-2.1.0
cd %{_builddir}/asciinema-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633448220
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/asciinema
cp %{_builddir}/asciinema-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/asciinema/8624bcdae55baeef00cd11d5dfcfa60f68710a02
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/asciinema

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/asciinema/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/asciinema/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/asciinema.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
