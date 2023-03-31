Name:		texlive-jlabels
Version:	24858
Release:	2
Summary:	Make letter-sized pages of labels
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jlabels
License:	NOSOURCE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlabels.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlabels.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides controls for the numbers of rows and
columns.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/jlabels/jlabels.sty
%doc %{_texmfdistdir}/doc/latex/jlabels/README
%doc %{_texmfdistdir}/doc/latex/jlabels/jlabels.pdf
%doc %{_texmfdistdir}/doc/latex/jlabels/jlabels.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
