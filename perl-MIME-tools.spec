#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	tools
Summary:	MIME::tools - modules for parsing (and creating!) MIME entities
Summary(pl.UTF-8):	MIME::tools - zestaw modułów do operacji na danych w formacie MIME
Name:		perl-MIME-tools
Version:	5.509
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2f0e07da2ff4b0478908544cc4b40fa
URL:		http://search.cpan.org/dist/MIME-tools/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(File::Path) >= 1
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl(IO::File) >= 1.13
BuildRequires:	perl-File-Temp >= 0.18
BuildRequires:	perl-MIME-Base64 >= 2.20
BuildRequires:	perl-MailTools >= 1.05
BuildRequires:	perl-Test-Deep
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.663
Requires:	perl-MailTools >= 1.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq_perl	Convert::BinHex

%description
MIME-tools is a collection of Perl5 MIME:: modules for parsing,
decoding and generating single- or multipart (even nested multipart)
MIME messages. (Yes, kids, that means you can send messages with
attached GIF files).

%description -l pl.UTF-8
MIME::tools to zestaw modułów MIME:: dla Perla 5 do analizy,
dekodowania oraz tworzenia jedno- i wieloczęściowych (a nawet
zagnieżdżonych wieloczęściowych) wiadomości MIME (tak, to znaczy, że
można wysyłać wiadomości z dołączonymi plikami GIF).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/MIME-tools/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{perl_vendorlib}/MIME/Body.pm
%{perl_vendorlib}/MIME/Decoder.pm
%{perl_vendorlib}/MIME/Entity.pm
%{perl_vendorlib}/MIME/Head.pm
%{perl_vendorlib}/MIME/Parser.pm
%{perl_vendorlib}/MIME/Tools.pm
%{perl_vendorlib}/MIME/WordDecoder.pm
%{perl_vendorlib}/MIME/Words.pm
%{perl_vendorlib}/MIME/Decoder
%{perl_vendorlib}/MIME/Field
%{perl_vendorlib}/MIME/Parser
%{_mandir}/man3/MIME::Body.3pm*
%{_mandir}/man3/MIME::Decoder*.3pm*
%{_mandir}/man3/MIME::Entity.3pm*
%{_mandir}/man3/MIME::Field::*.3pm*
%{_mandir}/man3/MIME::Head.3pm*
%{_mandir}/man3/MIME::Parser*.3pm*
%{_mandir}/man3/MIME::Tools.3pm*
%{_mandir}/man3/MIME::WordDecoder.3pm*
%{_mandir}/man3/MIME::Words.3pm*
%{_examplesdir}/%{name}-%{version}
