Summary:	Convert mail aliases into input suitable for cdbmake
Summary(pl):	Konwerter aliasów pocztowych na wej¶cie dla cdbmake
Name:		aliases2cdbm
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.pobox.com/~jmknoble/software/aliases2cdbm/%{name}-%{version}.tar.gz
# Source0-md5:	1408c1f17db44045b9b37e2c6ec6a4a7
Patch0:		%{name}-tolower.patch
URL:		http://www.pobox.com/~jmknoble/software/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
`Aliases2cdbm' is a utility for converting mail aliases from a text
file (e.g., /etc/mail/aliases) into input suitable for the `cdbmake'
utility. Cdbmake can then create a constant database (CDB) suitable
for reliable, high-speed mail alias lookups (see
<ftp://koobera.math.uic.edu/www/cdb.html> for more information about
D.J. Bernstein's cdb package, which includes cdbmake).

%description -l pl
Aliases2cdbm to narzêdzie do konwersji aliasów pocztowych z pliku
tekstowego (np. /etc/mail/aliases) na postaæ odpowiedni± jako wej¶cie
narzêdzia cdbmake. cdbmake mo¿e tworzyæ sta³± bazê danych (CDB)
odpowiedni± do pewnego i szybkiego wyszukiwania aliasów (pod adresem
ftp://koobera.math.uic.edu/www/cdb.html znajeduje siê wiêcej
informacji o pakiecie cdb D. J. Bernsteina, w tym o cdbmake).

%prep
%setup -q
%patch0 -p1

%build
%{__make} OPTFLAGS="%{rpmcflags}" PREFIX="%{_prefix}"
%{__make} OPTFLAGS="%{rpmcflags}" PREFIX="%{_prefix}" extra

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man1}

install aliases2cdbm 		$RPM_BUILD_ROOT%{_bindir}
#install	exim.newaliases.cdb	$RPM_BUILD_ROOT%{_sbindir}
install aliases2cdbm.1		$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README aliases.sample aliases.warnings
%attr(0755,root,root) %{_bindir}/aliases2cdbm
%attr(0444,root,root) %{_mandir}/man1/*
#%attr(0644,root,root) %{_sysconfdir}/aliases.conf
#%attr(0755,root,root) %{_bindir}/exim.newaliases.cdb
