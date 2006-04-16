%define		_vendor_name	extlib
%define		ocaml_ver	1:3.09.1
Summary:	ExtLib for OCaml
Summary(pl):	ExtLib dla OCamla
Name:		ocaml-%{_vendor_name}
Version:	1.4
Release:	4
License:	LGPL + OCaml linking exception
Group:		Libraries
Source0:	http://dl.sourceforge.net/ocaml-lib/%{_vendor_name}-%{version}.tgz
# Source0-md5:	d53cf08e13e5b9487035bcc8af1165f2
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtLib is a project aiming at providing a complete - yet small -
standard library for the OCaml programming language. The purpose of
this library is to add new functions to OCaml Standard Library
modules, to modify some functions in order to get better performances
or more safety (tail-recursive) but also to provide new modules which
should be useful for the average OCaml programmer.

ExtLib is not directly related to OCaml authors (INRIA) although this
library can be seen as a proposal for inclusion in the official
distribution.

%description -l pl
ExtLib to projekt, którego celem jest dostarczenie kompletnej lecz
ma³ej biblioteki standardowej dla jêzyka programowania OCaml. Celem
tej biblioteki jest dodanie nowych funkcji do modu³ów biblioteki
standardowej OCamla, zmodyfikowanie niektórych funkcji w celu
uzyskania lepszej wydajno¶ci lub bezpieczeñstwa, a tak¿e dodanie
nowych modu³ów, które powinny byæ przydatne dla przeciêtnego
programisty OCamla.

ExtLib nie jest bezpo¶rednio zwi±zany z autorami OCamla (INRIA), ale
tê bibliotekê mo¿na traktowaæ jako propozycjê do w³±czenia do
oficjalnej dystrybucji.

%package devel
Summary:	ExtLib for OCaml - development part
Summary(pl):	ExtLib dla OCamla - czê¶æ programistyczna
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
ExtLib is a project aiming at providing a complete - yet small -
standard library for the OCaml programming language. The purpose of
this library is to add new functions to OCaml Standard Library
modules, to modify some functions in order to get better performances
or more safety (tail-recursive) but also to provide new modules which
should be useful for the average OCaml programmer.

ExtLib is not directly related to OCaml authors (INRIA) although this
library can be seen as a proposal for inclusion in the official
distribution.

This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl
ExtLib to projekt, którego celem jest dostarczenie kompletnej lecz
ma³ej biblioteki standardowej dla jêzyka programowania OCaml. Celem
tej biblioteki jest dodanie nowych funkcji do modu³ów biblioteki
standardowej OCamla, zmodyfikowanie niektórych funkcji w celu
uzyskania lepszej wydajno¶ci lub bezpieczeñstwa, a tak¿e dodanie
nowych modu³ów, które powinny byæ przydatne dla przeciêtnego
programisty OCamla.

ExtLib nie jest bezpo¶rednio zwi±zany z autorami OCamla (INRIA), ale
tê bibliotekê mo¿na traktowaæ jako propozycjê do w³±czenia do
oficjalnej dystrybucji.

Ten pakiet zawiera pliki potrzebne do tworzenia programów w OCamlu z
u¿yciem tej biblioteki.

%prep
%setup -q -n %{_vendor_name}-%{version}

%build
%{__make} all opt \
	CC="%{__cc} %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/extlib

OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml %{__make} install

mv $RPM_BUILD_ROOT%{_libdir}/ocaml/extlib/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/extlib
echo 'directory = "+extlib"' \
	>> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/extlib/META
rm -f $RPM_BUILD_ROOT%{_libdir}/ocaml/extlib/*.mli

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE *.mli README.txt
%dir %{_libdir}/ocaml/extlib
%{_libdir}/ocaml/extlib/*.cm[ixa]*
%{_libdir}/ocaml/extlib/*.a
%{_libdir}/ocaml/site-lib/extlib
