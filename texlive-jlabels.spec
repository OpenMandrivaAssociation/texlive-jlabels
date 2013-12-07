# revision 24858
# category Package
# catalog-ctan /macros/latex/contrib/jlabels
# catalog-date 2011-12-16 16:22:52 +0100
# catalog-license nosource
# catalog-version 2011-06-05
Name:		texlive-jlabels
Version:	20110605
Release:	6
Summary:	Make letter-sized pages of labels
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jlabels
License:	NOSOURCE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlabels.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlabels.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110605-3
+ Revision: 752898
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110605-2
+ Revision: 745258
- texlive-jlabels

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110605-1
+ Revision: 718752
- texlive-jlabels
- texlive-jlabels
- texlive-jlabels

