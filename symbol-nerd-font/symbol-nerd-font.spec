%global fontconf 10-nerd-font-symbols.conf

Name:           symbol-nerd-font
Version:        3.4.0
Release:        1%{?dist}
Summary:        Nerd Fonts (icons only, for font fallback configurations)

License:        MIT
URL:            https://github.com/ryanoasis/nerd-fonts
Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/NerdFontsSymbolsOnly.tar.xz

BuildArch:      noarch
Requires:       fontpackages-filesystem

%description
Nerd Fonts is a project that patches developer targeted fonts with a high number of glyphs (icons). 
Specifically to add a high number of extra glyphs from popular 'iconic fonts' such as Font Awesome, Devicons, Octicons, and others.
(This package only contains the icons)

%prep

%build
tar -xvf %{SOURCE0}

%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontbasedir}/%{name} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p SymbolsNerdFont*.ttf %{buildroot}%{_fontbasedir}/%{name}

install -m 0644 -p %{fontconf} %{buildroot}%{_fontconfig_templatedir}

ln -s %{_fontconfig_templatedir}/%{fontconf} %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%files
%license LICENSE
%doc README.md

/%{_fontbasedir}/%{name}/SymbolsNerdFont*.ttf
/%{_fontconfig_templatedir}/%{fontconf}
/%{_fontconfig_confdir}/%{fontconf}

%changelog
* Tue Jun 11 2024 Eric Leung <contact@ericleung.dev> - 3.4.0-1
- Initial package