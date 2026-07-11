%global tl_name mp3d
%global tl_revision 29349

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.34
Release:	%{tl_revision}.1
Summary:	3D animations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/mp3d
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mp3d.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mp3d.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Create animations of 3-dimensional objects (such as polyhedra) in
MetaPost.

