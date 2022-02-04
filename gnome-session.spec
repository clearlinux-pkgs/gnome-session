#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-session
Version  : 41.3
Release  : 40
URL      : https://download.gnome.org/sources/gnome-session/41/gnome-session-41.3.tar.xz
Source0  : https://download.gnome.org/sources/gnome-session/41/gnome-session-41.3.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-session-bin = %{version}-%{release}
Requires: gnome-session-data = %{version}-%{release}
Requires: gnome-session-libexec = %{version}-%{release}
Requires: gnome-session-license = %{version}-%{release}
Requires: gnome-session-locales = %{version}-%{release}
Requires: gnome-session-man = %{version}-%{release}
Requires: gnome-session-services = %{version}-%{release}
Requires: dconf
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(xtrans)
BuildRequires : systemd-dev
BuildRequires : upower-dev
BuildRequires : xmlto
BuildRequires : xtrans-dev
Patch1: gles_env.patch

%description
gnome-session
=============
gnome-session contains the GNOME session manager, as well as a
configuration program to choose applications starting on login.

%package bin
Summary: bin components for the gnome-session package.
Group: Binaries
Requires: gnome-session-data = %{version}-%{release}
Requires: gnome-session-libexec = %{version}-%{release}
Requires: gnome-session-license = %{version}-%{release}
Requires: gnome-session-services = %{version}-%{release}

%description bin
bin components for the gnome-session package.


%package data
Summary: data components for the gnome-session package.
Group: Data

%description data
data components for the gnome-session package.


%package doc
Summary: doc components for the gnome-session package.
Group: Documentation
Requires: gnome-session-man = %{version}-%{release}

%description doc
doc components for the gnome-session package.


%package libexec
Summary: libexec components for the gnome-session package.
Group: Default
Requires: gnome-session-license = %{version}-%{release}

%description libexec
libexec components for the gnome-session package.


%package license
Summary: license components for the gnome-session package.
Group: Default

%description license
license components for the gnome-session package.


%package locales
Summary: locales components for the gnome-session package.
Group: Default

%description locales
locales components for the gnome-session package.


%package man
Summary: man components for the gnome-session package.
Group: Default

%description man
man components for the gnome-session package.


%package services
Summary: services components for the gnome-session package.
Group: Systemd services

%description services
services components for the gnome-session package.


%prep
%setup -q -n gnome-session-41.3
cd %{_builddir}/gnome-session-41.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644002775
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-session
cp %{_builddir}/gnome-session-41.3/COPYING %{buildroot}/usr/share/package-licenses/gnome-session/4cc77b90af91e615a64ae04893fdffa7939db84c
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-session-41
## install_append content
# specify this is a wayland session
sed -i s/Name=GNOME/Name=GNOME\ on\ Wayland/ %{buildroot}/usr/share/wayland-sessions/gnome.desktop
# rename gnome.desktop -> gnome-wayland.session so xorg session is default
mv %{buildroot}/usr/share/wayland-sessions/{gnome,gnome-wayland}.desktop
# rename gnome-xorg.desktop -> gnome.desktop to avoid 2 xorg session entries ('GNOME' & 'Gnome on Xorg')
mv %{buildroot}/usr/share/xsessions/gnome{-xorg,}.desktop
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-session
/usr/bin/gnome-session-custom-session
/usr/bin/gnome-session-inhibit
/usr/bin/gnome-session-quit

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/gnome-session.convert
/usr/share/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
/usr/share/gnome-session/hardware-compatibility
/usr/share/gnome-session/sessions/gnome-dummy.session
/usr/share/gnome-session/sessions/gnome.session
/usr/share/wayland-sessions/gnome-wayland.desktop
/usr/share/xsessions/gnome.desktop

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gnome\-session/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-session-binary
/usr/libexec/gnome-session-check-accelerated
/usr/libexec/gnome-session-check-accelerated-gl-helper
/usr/libexec/gnome-session-check-accelerated-gles-helper
/usr/libexec/gnome-session-ctl
/usr/libexec/gnome-session-failed

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-session/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-session-inhibit.1
/usr/share/man/man1/gnome-session-quit.1
/usr/share/man/man1/gnome-session.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/gnome-launched-.scope.d/override.conf
/usr/lib/systemd/user/gnome-session-failed.service
/usr/lib/systemd/user/gnome-session-failed.target
/usr/lib/systemd/user/gnome-session-initialized.target
/usr/lib/systemd/user/gnome-session-manager.target
/usr/lib/systemd/user/gnome-session-manager@.service
/usr/lib/systemd/user/gnome-session-monitor.service
/usr/lib/systemd/user/gnome-session-pre.target
/usr/lib/systemd/user/gnome-session-restart-dbus.service
/usr/lib/systemd/user/gnome-session-shutdown.target
/usr/lib/systemd/user/gnome-session-signal-init.service
/usr/lib/systemd/user/gnome-session-wayland.target
/usr/lib/systemd/user/gnome-session-wayland@.target
/usr/lib/systemd/user/gnome-session-x11-services-ready.target
/usr/lib/systemd/user/gnome-session-x11-services.target
/usr/lib/systemd/user/gnome-session-x11.target
/usr/lib/systemd/user/gnome-session-x11@.target
/usr/lib/systemd/user/gnome-session.target
/usr/lib/systemd/user/gnome-session@.target
/usr/lib/systemd/user/gnome-session@gnome.target.d/gnome.session.conf

%files locales -f gnome-session-41.lang
%defattr(-,root,root,-)

