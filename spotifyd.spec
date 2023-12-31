Name:     spotifyd
Version:  0.3.5
Release:  %{autorelease}
Summary:  An open source Spotify client running as a UNIX daemon.

License:  GPL-3.0
URL:      https://github.com/Spotifyd/spotifyd
Source0:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo openssl-devel pulseaudio-libs-devel systemd-rpm-macros dbus-devel
Requires:       openssl pulseaudio-libs dbus

%description
Spotifyd streams music just like the official client, but is more lightweight and supports more platforms. Spotifyd also supports the Spotify Connect protocol, which makes it show up as a device that can be controlled from the official clients.
Build with pulsaudio and dbus features (alsa disabled)

%prep
%autosetup

%build
cargo build --release --no-default-features --features pulseaudio_backend,dbus_keyring,dbus_mpris

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_userunitdir}
cp target/release/spotifyd %{buildroot}/%{_bindir}/spotifyd
cp contrib/spotifyd.service %{buildroot}/%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%{_bindir}/spotifyd
%{_userunitdir}/%{name}.service
%license LICENSE

%check

%changelog
%{autochangelog}
