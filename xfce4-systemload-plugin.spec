%define url_ver %(echo %{version} | cut -c 1-3 )

Summary:	System load plugin for the Xfce panel
Name:		xfce4-systemload-plugin
Version:	1.0.0
Release:	%mkrel 1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-systemload-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-systemload-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.7
BuildRequires:	xfce4-panel-devel >= 4.7
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfcegui4-devel
Obsoletes:	xfce-systemload-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A system load panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
