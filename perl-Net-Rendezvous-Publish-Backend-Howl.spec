%define upstream_name Net-Rendezvous-Publish-Backend-Howl
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Backend module using howl for Net::Rendezvous
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org//CPAN/authors/id/R/RC/RCLAMP/%{upstream_name}-%{upstream_version}.tar.bz2
Source1:	%{name}.rpmlintrc

BuildRequires:	howl-devel
BuildRequires:	perl(Net::Rendezvous)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(ExtUtils::ParseXS)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Class::Accessor::Lvalue)
BuildRequires:	perl-devel 

%description
This module interfaces to the Porchdog's Howl library in order to allow 
service publishing.
It is used by Net::Rendezvous::Publish, in order to adapt to
different mDns implementation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL INSTALLDIRS=vendor

%check
# requires mdns running
#./Build test

%install
./Build install destdir=%{buildroot} installdirs=vendor

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sun Feb 12 2012 Per √òyvind Karlsen <peroyvind@mandriva.org> 0.30.0-2
+ Revision: 773661
- use virtual perl() dependencies only
- clean out spec
- add exception filter on description-line-too-long for debug package
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat Aug 01 2009 J√©r√¥me Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 406176
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.03-11mdv2009.0
+ Revision: 258103
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.03-10mdv2009.0
+ Revision: 246167
- rebuild

* Thu Jan 24 2008 Nicolas L√©cureuil <nlecureuil@mandriva.com> 0.03-8mdv2008.1
+ Revision: 157722
- Fix BuildRequires

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.03-6mdv2008.1
+ Revision: 123184
- kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Pascal Terjan <pterjan@mandriva.org> 0.03-6mdv2007.0
+ Revision: 81361
- Also BuildRequires perl-ExtUtils-CBuilder for Module::Build to work on XS
- BuildRequires perl-ExtUtils-ParseXS for Module::Build to work on XS

  + Michael Scherer <misc@mandriva.org>
    - Import perl-Net-Rendezvous-Publish-Backend-Howl

* Fri Jan 06 2006 Michael Scherer <misc@mandriva.org> 0.03-6mdk
- remove test ( require a running mdns server )

* Wed Oct 05 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.03-5mdk
- Fix BuildRequires

* Wed Oct 05 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.03-4mdk
- Fix BuildRequires

* Tue Oct 04 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.03-3mdk
- Fix BuildRequires

* Sat Oct 01 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.03-2mdk
- Buildrequires fix

* Sat Sep 24 2005 Michael Scherer <misc@mandriva.org> 0.03-1mdk
- First mandriva package

