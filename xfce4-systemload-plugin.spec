%define url_ver %(echo %{version} | cut -c 1-3 )
%define _disable_rebuild_configure 1

Summary:	System load plugin for the Xfce panel
Name:		xfce4-systemload-plugin
Version:	1.2.2
Release:	1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-systemload-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-systemload-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.7
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2) >= 4.7.0
Obsoletes:	xfce-systemload-plugin

%description
A system load panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std
chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so
%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/*
