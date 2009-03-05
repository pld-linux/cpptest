Summary:	Framework for handling automated tests in C++
Summary(pl.UTF-8):	Framework do obslugi zautomatyzowanych testów w C++
Name:		cpptest
Version:	1.1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/cpptest/%{name}-%{version}.tar.gz
# Source0-md5:	818401e4698c2cfe8395e0ed61fbd097
URL:		http://cpptest.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++Test is a portable and powerful framework for handling automated
tests in C++. The focus lies on usability and extendability. Several
output formats are supported and new ones are easily added.

%description -l pl.UTF-8
C++Test jest przenośnym i potężnym frameworkiem do obsługi
zautomatyzowanych testów w C++. Duży nacisk kładzie on na
użyteczność oraz rozszerzalność. Wspieranych jest kilka formatów
wyjściowych a nowe dodaje się z dużą łatwością.

%package devel
Summary:	Header files for cpptest library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cpptest
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cpptest library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cpptest.

%package static
Summary:	Static cpptest library
Summary(pl.UTF-8):	Statyczna biblioteka cpptest
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cpptest library.

%description static -l pl.UTF-8
Statyczna biblioteka cpptest.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libcpptest.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcpptest.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcpptest.so
%{_libdir}/libcpptest.la
%{_includedir}/cpptest*.h
%{_pkgconfigdir}/libcpptest.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcpptest.a
