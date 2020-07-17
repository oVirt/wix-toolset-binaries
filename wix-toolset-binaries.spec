%global __os_install_post %{nil}
%global releasetag wix3112rtm

Name:		wix-toolset-binaries
Version:	3.11.2
Release:	1%{?dist}
Summary:	RPM wrapper for %{name}
License:	MS-RL
Source0:	https://github.com/wixtoolset/wix3/releases/download/%{releasetag}/wix311-binaries.zip
Source1:	https://raw.githubusercontent.com/wixtoolset/wix3/%{releasetag}/LICENSE.TXT
Source2:	https://raw.githubusercontent.com/oVirt/wix-toolset-binaries/master/README.md
URL:		https://github.com/wixtoolset/wix3/releases/tag/%{releasetag}
BuildArch:	noarch

%description
A package wrapping %{name} to provide dependency features.

%prep
%setup -q -c %{name} -n %{name}
cp %{SOURCE2} .

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
%doc README.md

%changelog
* Fri Jul 17 2020 Sandro Bonazzola <sbonazzo@redhat.com> - 3.11.2-1
- Rebase on upstream 3.11.2

* Thu Aug 01 2019 Gal Zaidman <gzaidman@redhat.com> - 3.11.1-2
- package wix-toolset-binaries 3.11.1-2

* Thu Aug 01 2019 Gal Zaidman <gzaidman@redhat.com> - 3.11.1-1
- package wix-toolset-binaries 3.11.1

