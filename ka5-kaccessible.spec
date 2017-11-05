%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		kaccessible
Summary:	Kaccessible
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9cb6df5d4a6c6fdcddf568513e09a7b3
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kaccessible implements a QAccessibleBridgePlugin to provide
accessibility services like focus tracking and a screenreader.

Components;
- kaccessibleapp is a dbus activation service that acts as proxy.
- kaccessiblebridge will be loaded by the QAccessible framework into
  each Qt-/KDE-application.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/libexec/kaccessibleapp
%dir %{_libdir}/kde4/plugins/accessiblebridge
%attr(755,root,root) %{_libdir}/kde4/plugins/accessiblebridge/kaccessiblebridge.so
%{_datadir}/dbus-1/services/org.kde.kaccessible.service
