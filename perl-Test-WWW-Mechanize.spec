#
#Conditional build:
%bcond_without	tests	# perform "make test"
#
%define		pdir	Test
%define		pnam	WWW-Mechanize
Summary:	Test::WWW::Mechanize - Testing-specific WWW::Mechanize subclass
Summary(pl.UTF-8):	Test::WWW::Mechanize - podklasa WWW::Mechanize służąca do testów
Name:		perl-Test-WWW-Mechanize
Version:	1.60
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f14a2b64c39ec2536456b85a295f9074
URL:		https://search.cpan.org/dist/Test-WWW-Mechanize/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Carp-Assert-More
BuildRequires:	perl-Test-LongString
BuildRequires:	perl(Test::Builder::Tester) >= 1.09
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::WWW::Mechanize is a subclass of WWW::Mechanize that incorporates
features for web application testing.

%description -l pl.UTF-8
Test::WWW::Mechanize to podlasa WWW::Mechanize zawierająca
funkcjonalność przeznaczoną do testowania aplikacji WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Test/WWW/Mechanize

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/WWW/*.pm
%dir %{perl_vendorlib}/Test/WWW/Mechanize
%{_mandir}/man3/*
