Name:           mkosi
Version:        4
Release:        1%{?dist}
Summary:        Create legacy-free OS images

License:        LGPLv2+
URL:            https://github.com/systemd/mkosi
Source0:        https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python3 >= 3.5
# for subprocess.run

Recommends:     dnf
Recommends:     debootstrap
Recommends:     arch-install-scripts
Recommends:     edk2-ovmf
Recommends:     gnupg
Recommends:     xz
Recommends:     tar
Recommends:     btrfs-progs
Recommends:     dosfstools
Recommends:     squashfs-tools
Recommends:     veritysetup

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
* Sat Feb 10 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4-1
- Update to latest version (#1544123)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2-1
- Update to latest version (#1464285)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1-2
- Rebuild for Python 3.6

* Thu Nov  3 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1-1
- Initial version
