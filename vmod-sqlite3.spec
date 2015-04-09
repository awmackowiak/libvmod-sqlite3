Name: vmod-sqlite3
Version: 0.1.0
Release: 1%{?dist}
Summary: SQLite3 VMOD for Varnish

Group: System Environment/Daemons
License: BSD
URL: https://github.com/fgsch/libvmod-sqlite3
Source0: libvmod-sqlite3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: pkgconfig(varnishapi)
BuildRequires: python-docutils
BuildRequires: varnish >= 3.0
BuildRequires: varnish < 4.0
Requires: varnish >= 3.0
Requires: varnish < 4.0

%description
SQLite3 VMOD for Varnish

%prep
%setup -q -n libvmod-sqlite3-%{version}

%build
%configure VARNISHSRC=%{VARNISHSRC} \
    VMODDIR="$(PKG_CONFIG_PATH=%{VARNISHSRC} \
    pkg-config --variable=vmoddir varnishapi)" \
    --docdir='%_docdir/%{name}-%{version}'
make

%check
make check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnish*/vmods/*
%doc LICENSE

%changelog
* Thu Apr  9 2015 Federico G. Schwindt <fgsch@lodoss.net> - 0.1.0-1
- Initial release.
