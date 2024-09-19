#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v4
# autospec commit: f4bef72
#
Name     : gnome-session
Version  : 46.0
Release  : 63
URL      : https://download.gnome.org/sources/gnome-session/46/gnome-session-46.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-session/46/gnome-session-46.0.tar.xz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
Requires: systemd

%description services
services components for the gnome-session package.


%prep
%setup -q -n gnome-session-46.0
cd %{_builddir}/gnome-session-46.0
%patch -P 1 -p1
pushd ..
cp -a gnome-session-46.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710894398
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-session
cp %{_builddir}/gnome-session-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-session/4cc77b90af91e615a64ae04893fdffa7939db84c || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-session-46
## install_append content
# specify this is a wayland session
sed -i s/Name=GNOME/Name=GNOME\ on\ Wayland/ %{buildroot}/usr/share/wayland-sessions/gnome.desktop
# rename gnome.desktop -> gnome-wayland.session so xorg session is default
mv %{buildroot}/usr/share/wayland-sessions/{gnome,gnome-wayland}.desktop
# rename gnome-xorg.desktop -> gnome.desktop to avoid 2 xorg session entries ('GNOME' & 'Gnome on Xorg')
mv %{buildroot}/usr/share/xsessions/gnome{-xorg,}.desktop
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gnome-session-inhibit
/V3/usr/bin/gnome-session-quit
/usr/bin/gnome-session
/usr/bin/gnome-session-inhibit
/usr/bin/gnome-session-quit

%files data
%defattr(-,root,root,-)
/usr/share/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
/usr/share/gnome-session/hardware-compatibility
/usr/share/gnome-session/sessions/gnome-dummy.session
/usr/share/gnome-session/sessions/gnome.session
/usr/share/wayland-sessions/gnome-wayland.desktop
/usr/share/xdg-desktop-portal/gnome-portals.conf
/usr/share/xsessions/gnome.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/gnome\-session/*

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gnome-session-binary
/V3/usr/libexec/gnome-session-check-accelerated
/V3/usr/libexec/gnome-session-check-accelerated-gl-helper
/V3/usr/libexec/gnome-session-check-accelerated-gles-helper
/V3/usr/libexec/gnome-session-ctl
/V3/usr/libexec/gnome-session-failed
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

%files locales -f gnome-session-46.lang
%defattr(-,root,root,-)

