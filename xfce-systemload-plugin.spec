Summary:	System load plugin for the Xfce panel
Name:		xfce-systemload-plugin
Version:	0.4.2
Release:	%mkrel 2
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-systemload-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-systemload-plugin/xfce4-systemload-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	perl-XML-Parser
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A system load panel plugin for the Xfce Desktop Environment.

%prep
%setup -qn xfce4-systemload-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang xfce4-systemload-plugin

%clean
rm -rf %{buildroot}

%files -f xfce4-systemload-plugin.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
