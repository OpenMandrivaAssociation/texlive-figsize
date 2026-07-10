%global tl_name figsize
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Auto-size graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/figsize
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figsize.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figsize.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The FigSize package enables automatic sizing of graphics, especially
when including graphics with the graphicx package. The user only has to
specify the number of graphics that should fit to a page or fraction
there of and the package will dynamically calculate the correct graphics
sizes relative to the page size. Thus, graphics can be auto-sized to
fill a whole page or fraction and manual changes of graphic sizes are
never needed when changing document layouts. Finally, the package's
dynamic lengths can be used to allow other document element sizes to be
dynamic.

