%global __os_install_post %{nil}

Name:		wix-toolset-binaries
Version:	3.11.1
Release:	%{?dist}
Summary:	RPM wrapper for %{name}
License:	Platform SDK Redistributable EULA
Source0:	https://github.com/wixtoolset/wix3/releases/download/wix3111rtm/wix311-binaries.zip
URL:		https://github.com/wixtoolset/wix3/releases/tag/wix3111rtm
BuildArch:	noarch

%description
A package wrapping %{name} to provide dependency features.

%prep
%setup -q -c %{name} -n %{name}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r %{_builddir}/%{name}/* %{buildroot}%{_datadir}/%{name}

%files
%{_datadir}/%{name}

%changelog
* Tue Aug 01 2019 Gal Zaidman <gzaidman@redhat.com>
- package wix-toolset-binaries 3.11.1

