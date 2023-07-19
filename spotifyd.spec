Name:     spotifyd
Version:  0.3.5
Release:  %{autorelease}
Summary:  An open source Spotify client running as a UNIX daemon.

License:  GPL-3.0
URL:      https://github.com/Spotifyd/spotifyd
Source0:  https://github.com/Spotifyd/spotifyd/releases/download/v%{version}/spotifyd-linux-full.tar.gz
Source1:  https://github.com/Spotifyd/spotifyd/releases/download/v%{version}/spotifyd-linux-full.sha512

BuildRequires:  cargo openssl-devel alsa-lib-devel pulseaudio-libs-devel systemd-rpm-macros dbus-devel
Requires:       openssl pulseaudio-libs alsa-lib dbus

%description
Spotifyd streams music just like the official client, but is more lightweight and supports more platforms. Spotifyd also supports the Spotify Connect protocol, which makes it show up as a device that can be controlled from the official clients.

%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%check


%files
%license
%doc


%changelog
%{autochangelog}

