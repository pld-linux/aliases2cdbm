Summary:	Convert mail aliases into input suitable for cdbmake
Name:		aliases2cdbm 
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
URL:		http://www.pobox.com/~jmknoble/software/
Source0:	http://www.pobox.com/~jmknoble/software/aliases2cdbm/%{name}-%{version}.tar.gz
Patch0:		%{name}-tolower.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
`Aliases2cdbm' is a utility for converting mail aliases from a text
file (e.g., /etc/aliases) into input suitable for the `cdbmake'
utility. Cdbmake can then create a constant database (CDB) suitable
for reliable, high-speed mail alias lookups (see
<ftp://koobera.math.uic.edu/www/cdb.html> for more information about
D.J. Bernstein's cdb package, which includes cdbmake).


%prep
%setup -q
%patch0 -p1 

%build

%{__make} OPTFLAGS="${RPM_OPT_FLAGS}" PREFIX="%{prefix}"
%{__make} OPTFLAGS="${RPM_OPT_FLAGS}" PREFIX="%{prefix}" extra

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man1}

install aliases2cdbm 		$RPM_BUILD_ROOT%{_bindir}
#install	exim.newaliases.cdb	$RPM_BUILD_ROOT%{_sbindir}
install aliases2cdbm.1		$RPM_BUILD_ROOT%{_mandir}/man1
                                                                                   
gzip -9nf README aliases.sample aliases.warnings 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(0755,root,root) %{_bindir}/aliases2cdbm
%attr(0444,root,root) %{_mandir}/man1/*
#%attr(0644,root,root) %{_sysconfdir}/aliases.conf
#%attr(0755,root,root) %{_bindir}/exim.newaliases.cdb
