# revision 23619
# category Package
# catalog-ctan /macros/latex/contrib/jlabels
# catalog-date 2011-06-24 10:20:36 +0200
# catalog-license other-free
# catalog-version 2011-06-05
Name:		texlive-jlabels
Version:	20110605
Release:	1
Summary:	Make letter-sized pages of labels
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jlabels
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlabels.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlabels.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides controls for the numbers of rows and
columns.

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
%{_texmfdistdir}/tex/latex/jlabels/jlabels.sty
%doc %{_texmfdistdir}/doc/latex/jlabels/README
%doc %{_texmfdistdir}/doc/latex/jlabels/README.TEXLIVE
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
