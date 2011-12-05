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
Version:	5.502
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6a87adda74867e3f8868a0599137bde0
URL:		http://search.cpan.org/dist/MIME-tools/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(File::Path) >= 1
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl(IO::File) >= 1.13
BuildRequires:	perl-File-Temp >= 0.18
BuildRequires:	perl-IO-stringy >= 2.110
BuildRequires:	perl-MIME-Base64 >= 2.20
BuildRequires:	perl-MailTools >= 1.05
BuildRequires:	perl-Test-Deep
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-MailTools >= 1.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq	'perl(Convert::BinHex)'

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
%{perl_vendorlib}/MIME/*.pm
%{perl_vendorlib}/MIME/Parser
%{perl_vendorlib}/MIME/Decoder
%{perl_vendorlib}/MIME/Field
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
