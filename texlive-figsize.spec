# revision 18784
# category Package
# catalog-ctan /macros/latex/contrib/figsize
# catalog-date 2006-12-13 12:28:27 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-figsize
Version:	0.1
Release:	1
Summary:	Auto-size graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/figsize
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figsize.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figsize.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/figsize/figsize.sty
%doc %{_texmfdistdir}/doc/latex/figsize/README
%doc %{_texmfdistdir}/doc/latex/figsize/epsfig.eps
%doc %{_texmfdistdir}/doc/latex/figsize/figsize.pdf
%doc %{_texmfdistdir}/doc/latex/figsize/figsize.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
