%define         _vendor_name extlib
Summary:	extlib for ocaml
Name:		ocaml-%{_vendor_name}
Version:        1.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/ocaml-lib/%{_vendor_name}-%{version}.tgz
BuildRequires:	ocaml >= 3.04-7
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtLib is a project aiming at providing a complete - yet small - standard library for the OCaml programming langage. The purpose of this library is to add new functions to OCaml Standard Library modules, to modify some functions in order to get better performances or more safety (tail-recursive) but also to provide new modules which should be useful for the average OCaml programmer.

ExtLib is not directly related to OCaml authors (INRIA) although this library can be seen as a proposal for inclusion in the official distribution.

%package devel
Summary:	extlib for ocaml - development part
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
ExtLib is a project aiming at providing a complete - yet small - standard library for the OCaml programming langage. The purpose of this library is to add new functions to OCaml Standard Library modules, to modify some functions in order to get better performances or more safety (tail-recursive) but also to provide new modules which should be useful for the average OCaml programmer.

ExtLib is not directly related to OCaml authors (INRIA) although this library can be seen as a proposal for inclusion in the official distribution.

This package contains files needed to develop OCaml programs using
this library.


%prep
%setup -q -n %{_vendor_name}-%{version}

%build
%{__make} CC="%{__cc} %{rpmcflags} -fPIC" all opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/extlib
install *.cm[ixa]* *.a $RPM_BUILD_ROOT%{_libdir}/ocaml/extlib

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/extlib
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/extlib/META <<EOF
requires = ""
version = "%{version}"
directory = "+extlib"
archive(byte) = "extlib.cma"
archive(native) = "extlib.cmxa"
linkopts = ""
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE *.mli README.txt
%dir %{_libdir}/ocaml/extlib
%{_libdir}/ocaml/extlib/*.cm[ixa]*
%{_libdir}/ocaml/extlib/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/extlib
