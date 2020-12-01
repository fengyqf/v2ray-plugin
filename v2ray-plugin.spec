Name:           v2ray-plugin
Version:        1.3.1
Release:        1%{?dist}
Summary:        Yet another SIP003 plugin for shadowsocks, based on v2ray

Group:          Applications/Internet
License:        MIT License
URL:            https://github.com/shadowsocks/v2ray-plugin/
Source0:        https://github.com/shadowsocks/v2ray-plugin/releases/download/v1.3.1/v2ray-plugin-linux-amd64-v1.3.1.tar.gz
#Source0:        v2ray-plugin-1.3.1.zip

BuildRequires:  git,golang
#Requires:       shadowsocks-libev

%description
Yet another SIP003 plugin for shadowsocks, based on v2ray


%prep
%setup -q


%build



%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
cp v2ray-plugin_* %{buildroot}%{_bindir}/v2ray-plugin


%files
%{_bindir}/*

%doc



%changelog

