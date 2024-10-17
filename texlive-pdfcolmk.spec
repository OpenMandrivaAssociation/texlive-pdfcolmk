Name:		texlive-pdfcolmk
Version:	52912
Release:	2
Summary:	Improved colour support under pdfTeX (legacy stub)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfcolmk
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcolmk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcolmk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package used to provide macros that emulated the 'colour
stack' functionality of dvips. The colour stack deals with
colour manipulations when asynchronous events (like
page-breaking) occur. At the time the package was written,
pdfTeX did not (yet) have such a stack, though dvips had had
one for a long time. This package was an experimental solution
to the problem, and worked best with pdfeTeX. For current
releases of pdfTeX (later than version 1.40.0, released in
2007), this package is not needed, since "real" colour stacks
are available. The present pdfcolmk is therefore just an empty
stub that does nothing at all, just in case there are still
documents that reference it. The documented source of the
original package is still available at the github repository.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pdfcolmk
%doc %{_texmfdistdir}/doc/latex/pdfcolmk

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
