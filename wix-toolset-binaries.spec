%global __os_install_post %{nil}

Name:		wix-toolset-binaries
Version:	3.11.1
Release:	1%{?dist}
Summary:	RPM wrapper for %{name}
License:	MS-RL
Source0:	https://github.com/wixtoolset/wix3/releases/download/wix3111rtm/wix311-binaries.zip
Source1:	https://raw.githubusercontent.com/wixtoolset/wix3/wix3111rtm/LICENSE.TXT
URL:		https://github.com/wixtoolset/wix3/releases/tag/wix3111rtm
BuildArch:	noarch

%description
A package wrapping %{name} to provide dependency features.

%prep
%setup -q -c %{name} -n %{name}

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r %{_builddir}/%{name}/* %{buildroot}%{_datadir}/%{name}

%files
# Note:
# /usr/share/wix-toolset-binaries/sdk/inc should go into -devel
# /usr/share/wix-toolset-binaries/sdk/*/x86/ should go into i686 arch packages
# /usr/share/wix-toolset-binaries/sdk/*/lib/x64/ should go into x86_64 arch packages
# we are not doing it now here since we plan to use the whole package with wine on x86_64 only.

%{_datadir}/%{name}
%license LICENSE.TXT

%changelog
* Thu Aug 01 2019 Gal Zaidman <gzaidman@redhat.com> - 3.11.1-1
- package wix-toolset-binaries 3.11.1

