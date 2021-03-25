#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), remove when upstream will support it
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%if %{without ocaml_opt}
%define		_enable_debug_packages	0
%endif

%define		pkgname	extlib
%define		ocaml_ver	1:3.09.2
Summary:	ExtLib for OCaml
Summary(pl.UTF-8):	ExtLib dla OCamla
Name:		ocaml-%{pkgname}
Version:	1.7.8
Release:	1
License:	LGPL + OCaml linking exception
Group:		Libraries
Source0:	https://github.com/ygrek/ocaml-extlib/releases/download/%{version}/extlib-%{version}.tar.gz
# Source0-md5:	7e0df072af4e2daa094e5936a661cb11
Patch0:		no-git.patch
URL:		https://github.com/ygrek/ocaml-extlib
BuildRequires:	cppo
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
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%build
%{__make} -C src all %{?with_ocaml_opt:opt cmxs} \
       CC="%{__cc} %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/extlib

OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml %{__make} install

echo 'directory = "+extlib"' \
	>> $RPM_BUILD_ROOT%{_libdir}/ocaml/extlib/META
ln -sr $RPM_BUILD_ROOT%{_libdir}/ocaml/extlib/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/extlib

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/extlib/*.mli

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE src/*.mli README.md
%dir %{_libdir}/ocaml/extlib
%{_libdir}/ocaml/extlib/META
%{_libdir}/ocaml/extlib/*.cm[ix]
%{_libdir}/ocaml/extlib/*.cma
%{_libdir}/ocaml/extlib/*.cmt
%{_libdir}/ocaml/extlib/*.cmti
%if %{with ocaml_opt}
%{_libdir}/ocaml/extlib/*.a
%{_libdir}/ocaml/extlib/*.cmxa
%{_libdir}/ocaml/extlib/*.cmxs
%endif
%{_libdir}/ocaml/site-lib/extlib
