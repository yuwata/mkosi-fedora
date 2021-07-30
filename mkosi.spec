Name:           mkosi
Version:        10
Release:        %autorelease
Summary:        Create bespoke OS images

License:        LGPLv2+
URL:            https://github.com/systemd/mkosi
Source0:        https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global recoreq %{?el7:Requires}%{!?el7:Recommends}

%{recoreq}:     dnf
%{recoreq}:     gnupg
%{recoreq}:     xz
%{recoreq}:     tar
%{recoreq}:     e2fsprogs
%{recoreq}:     squashfs-tools
%{recoreq}:     veritysetup
%if 0%{?el7} == 0
Recommends:     debootstrap
Recommends:     arch-install-scripts
Recommends:     edk2-ovmf
Recommends:     btrfs-progs
Recommends:     dosfstools
Recommends:     python3dist(argcomplete)
%endif

%description
A fancy wrapper around "dnf --installroot", "debootstrap" and
"pacstrap", that may generate disk images with a number of bells and
whistles.

Generated images are "legacy-free". This means only GPT disk labels
(and no MBR disk labels) are supported, and only systemd based images
may be generated. Moreover, for bootable images only EFI systems are
supported (not plain MBR/BIOS).

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%_bindir/mkosi
%{python3_sitelib}/mkosi/
%{python3_sitelib}/mkosi-%{version}-py*.egg-info/
%_mandir/man1/mkosi.1*

%check
# just a smoke test for syntax or import errors
%buildroot/usr/bin/mkosi --help >/dev/null

%changelog
%autochangelog
