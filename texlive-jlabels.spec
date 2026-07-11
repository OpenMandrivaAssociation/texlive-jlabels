%global tl_name jlabels
%global tl_revision 24858

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Make letter-sized pages of labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jlabels
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jlabels.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jlabels.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides controls for the numbers of rows and columns.

