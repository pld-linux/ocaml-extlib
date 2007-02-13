%define		_vendor_name	extlib
%define		ocaml_ver	1:3.09.2
Summary:	ExtLib for OCaml
Summary(pl.UTF-8):	ExtLib dla OCamla
Name:		ocaml-%{_vendor_name}
Version:	1.4
Release:	5
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

%description -l pl.UTF-8
ExtLib to projekt, którego celem jest dostarczenie kompletnej lecz
małej biblioteki standardowej dla języka programowania OCaml. Celem
tej biblioteki jest dodanie nowych funkcji do modułów biblioteki
standardowej OCamla, zmodyfikowanie niektórych funkcji w celu
uzyskania lepszej wydajności lub bezpieczeństwa, a także dodanie
nowych modułów, które powinny być przydatne dla przeciętnego
programisty OCamla.

ExtLib nie jest bezpośrednio związany z autorami OCamla (INRIA), ale
tę bibliotekę można traktować jako propozycję do włączenia do
oficjalnej dystrybucji.

%package devel
Summary:	ExtLib for OCaml - development part
Summary(pl.UTF-8):	ExtLib dla OCamla - część programistyczna
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

%description devel -l pl.UTF-8
ExtLib to projekt, którego celem jest dostarczenie kompletnej lecz
małej biblioteki standardowej dla języka programowania OCaml. Celem
tej biblioteki jest dodanie nowych funkcji do modułów biblioteki
standardowej OCamla, zmodyfikowanie niektórych funkcji w celu
uzyskania lepszej wydajności lub bezpieczeństwa, a także dodanie
nowych modułów, które powinny być przydatne dla przeciętnego
programisty OCamla.

ExtLib nie jest bezpośrednio związany z autorami OCamla (INRIA), ale
tę bibliotekę można traktować jako propozycję do włączenia do
oficjalnej dystrybucji.

Ten pakiet zawiera pliki potrzebne do tworzenia programów w OCamlu z
użyciem tej biblioteki.

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
