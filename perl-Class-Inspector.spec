#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Inspector
Version  : 1.36
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Class-Inspector-1.36.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Class-Inspector-1.36.tar.gz
Summary  : 'Get information about a class and its structure'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-Inspector-license = %{version}-%{release}
Requires: perl-Class-Inspector-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Class::Inspector - Get information about a class and its structure
VERSION
version 1.36

%package dev
Summary: dev components for the perl-Class-Inspector package.
Group: Development
Provides: perl-Class-Inspector-devel = %{version}-%{release}
Requires: perl-Class-Inspector = %{version}-%{release}

%description dev
dev components for the perl-Class-Inspector package.


%package license
Summary: license components for the perl-Class-Inspector package.
Group: Default

%description license
license components for the perl-Class-Inspector package.


%package perl
Summary: perl components for the perl-Class-Inspector package.
Group: Default
Requires: perl-Class-Inspector = %{version}-%{release}

%description perl
perl components for the perl-Class-Inspector package.


%prep
%setup -q -n Class-Inspector-1.36
cd %{_builddir}/Class-Inspector-1.36

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Inspector
cp %{_builddir}/Class-Inspector-1.36/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Inspector/8f0de673d49fa9dcad1645c38a9bf9762e87f315
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Inspector.3
/usr/share/man/man3/Class::Inspector::Functions.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Inspector/8f0de673d49fa9dcad1645c38a9bf9762e87f315

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Class/Inspector.pm
/usr/lib/perl5/vendor_perl/5.34.0/Class/Inspector/Functions.pm
