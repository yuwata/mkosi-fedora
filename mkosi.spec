Name:           mkosi
Version:        2
Release:        1%{?dist}
Summary:        Create legacy-free OS images

License:        LGPLv2+
URL:            https://github.com/systemd/mkosi
Source0:        https://github.com/systemd/mkosi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python3 >= 3.5
# for subprocess.run

Recommends:     debootstrap
Recommends:     arch-install-scripts
Recommends:     xz
Recommends:     btrfs-progs
Recommends:     dosfstools
Recommends:     edk2-ovmf

%description
A fancy wrapper around "dnf --installroot", "debootstrap" and
"pacstrap", that may generate disk images with a number of bells and
whistles.

Generated images are "legacy-free". This means only GPT disk labels
(and no MBR disk labels) are supported, and only systemd based images
may be generated. Moreover, for bootable images only EFI systems are
supported (not plain MBR/BIOS).

%prep
%autosetup

%build
# no build required

%install
# It's just one file, and setup.py install would copy useless .egg-info
install -Dpt %{buildroot}%{_bindir}/ mkosi

%files
%license LICENSE
%doc README.md
%_bindir/mkosi

%changelog
* Fri Jun 23 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2-1
- Update to latest version (#1464285)

* Thu Nov  3 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1-1
- Initial version
