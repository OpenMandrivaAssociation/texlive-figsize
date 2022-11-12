Name:		texlive-figsize
Version:	18784
Release:	1
Summary:	Auto-size graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/figsize
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figsize.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figsize.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The FigSize package enables automatic sizing of graphics,
especially when including graphics with the graphicx package.
The user only has to specify the number of graphics that should
fit to a page or fraction there of and the package will
dynamically calculate the correct graphics sizes relative to
the page size. Thus, graphics can be auto-sized to fill a whole
page or fraction and manual changes of graphic sizes are never
needed when changing document layouts. Finally, the package's
dynamic lengths can be used to allow other document element
sizes to be dynamic.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/figsize/figsize.sty
%doc %{_texmfdistdir}/doc/latex/figsize/README
%doc %{_texmfdistdir}/doc/latex/figsize/epsfig.eps
%doc %{_texmfdistdir}/doc/latex/figsize/figsize.pdf
%doc %{_texmfdistdir}/doc/latex/figsize/figsize.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
