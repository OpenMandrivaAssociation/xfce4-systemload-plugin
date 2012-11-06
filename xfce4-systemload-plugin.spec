%define url_ver %(echo %{version} | cut -c 1-3 )

Summary:	System load plugin for the Xfce panel
Name:		xfce4-systemload-plugin
Version:	1.1.1
Release:	1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-systemload-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-systemload-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.9
BuildRequires:	xfce4-panel-devel >= 4.9
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig(upower-glib)
Obsoletes:	xfce-systemload-plugin

%description
A system load panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/libsystemload.so
%{_datadir}/xfce4/panel/plugins/systemload.desktop
