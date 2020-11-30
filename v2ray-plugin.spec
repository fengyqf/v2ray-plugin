Name:           v2ray-plugin
Version:        1.3.1
Release:        1%{?dist}
Summary:        Yet another SIP003 plugin for shadowsocks, based on v2ray

Group:          Applications/Internet
License:        MIT License
URL:            https://github.com/shadowsocks/v2ray-plugin/
#Source0:        https://github.com/shadowsocks/v2ray-plugin/archive/v1.3.1.zip
Source0:        v2ray-plugin-1.3.1.zip

BuildRequires:  git,golang
Requires:       shadowsocks-libev

%description
Yet another SIP003 plugin for shadowsocks, based on v2ray


%prep
%setup -q


%build
LDFLAGS="-X main.VERSION=$VERSION -s -w"
GCFLAGS=""
suffix=""

os=linux
arch=amd64

env CGO_ENABLED=0 GOOS=$os GOARCH=$arch go build -v -ldflags "$LDFLAGS" -gcflags "$GCFLAGS" -o v2ray-plugin




%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
cp v2ray-plugin %{buildroot}%{_bindir}/


%files
%{_bindir}/*

%doc



%changelog

