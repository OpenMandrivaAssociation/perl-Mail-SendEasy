
%define module	Mail-SendEasy
%define name	perl-%{module}
%define version	1.2
%define rel	3

Summary:	Send plain/html e-mails through SMTP servers
Name:		%{name}
Version:	%perl_convert_version 1.2
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Mail/Mail-SendEasy-1.2.tar.gz
BuildRequires:	perl-devel
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}
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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2-3mdv2010.0
+ Revision: 430487
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2-2mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jun 03 2007 Anssi Hannula <anssi@mandriva.org> 1.2-2mdv2008.0
+ Revision: 34869
- annual rebuild


* Sun May 28 2006 Anssi Hannula <anssi@mandriva.org> 1.2-1mdv2007.0
- initial Mandriva package


