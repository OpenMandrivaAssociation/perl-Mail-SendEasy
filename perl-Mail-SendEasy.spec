
%define module	Mail-SendEasy
%define name	perl-%{module}
%define version	1.2
%define rel	2

Summary:	Send plain/html e-mails through SMTP servers
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	dos2unix
BuildArch:	noarch
Provides:	perl(Mail::SendEasy::AUTH)
Provides:	perl(Mail::SendEasy::SMTP)

%description
This modules will send in a easy way e-mails.
It supports SMTP authentication and attachments.

%prep
%setup -q -n %{module}-%{version}
dos2unix README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Mail
%{_mandir}/man3/*

