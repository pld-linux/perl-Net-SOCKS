#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Net
%define		pnam	SOCKS
Summary:	Net::SOCKS perl module
Summary(pl.UTF-8):	Moduł perla Net::SOCKS
Name:		perl-Net-SOCKS
Version:	0.03
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/SOCKS-%{version}.tar.gz
# Source0-md5:	81f63a1fb252d211a083909fbdc1611b
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Net-SOCKS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SOCKS - a SOCKS client.

%description -l pl.UTF-8
Net::SOCKS - klient SOCKS.

%prep
%setup -q -n SOCKS-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO example
%{perl_vendorlib}/Net/SOCKS.pm
%{perl_vendorlib}/auto/Net/SOCKS
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
