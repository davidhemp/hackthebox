apt-get update
apt-get -y install ca-certificates gnupg
# We add the OpenVPN repo to get the latest version.
echo "deb http://build.openvpn.net/debian/openvpn/stable noble main" >/etc/apt/sources.list.d/openvpn.list
wget -O - https://swupdate.openvpn.net/repos/repo-public.gpg | apt-key add -
apt-get update
i
# Ubuntu > 16.04 and Debian > 8 have OpenVPN >= 2.4 without the need of a third party repository.
apt-get install -y openvpn iptables openssl wget ca-certificates curl