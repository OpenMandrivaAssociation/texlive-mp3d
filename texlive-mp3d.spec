# revision 21771
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/mp3d
# catalog-date 2011-03-19 23:48:16 +0100
# catalog-license noinfo
# catalog-version 1.34
Name:		texlive-mp3d
Version:	1.34
Release:	1
Summary:	3D animations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/mp3d
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mp3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mp3d.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Create animations of 3-dimensional objects (such as polyhedra)
in MetaPost.

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
%{_texmfdistdir}/metapost/mp3d/3d.mp
%{_texmfdistdir}/metapost/mp3d/3danim.mp
%{_texmfdistdir}/metapost/mp3d/3dgeom.mp
%{_texmfdistdir}/metapost/mp3d/3dpoly.mp
%{_texmfdistdir}/metapost/mp3d/3dutil.mp
%{_texmfdistdir}/metapost/mp3d/animpoly.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/README
%doc %{_texmfdistdir}/doc/metapost/mp3d/README.doc
%doc %{_texmfdistdir}/doc/metapost/mp3d/create_animation.sh
%doc %{_texmfdistdir}/doc/metapost/mp3d/cube10.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/cube4-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/cube5.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/cube6.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/cube7.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/cube8.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/cube9.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gut2001.pdf
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp1-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp1.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp2-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp2.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp3-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp3.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp4-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp4.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp5-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp5.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp6-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp6.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp7-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp7.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp8-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp8.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/gutmp9.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/monge-eng.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/monge.mp
%doc %{_texmfdistdir}/doc/metapost/mp3d/paper1997corrected.pdf
%doc %{_texmfdistdir}/doc/metapost/mp3d/tb57roeg.pdf
%doc %{_texmfdistdir}/doc/metapost/mp3d/tb57roegel.ltx
%doc %{_texmfdistdir}/doc/metapost/mp3d/tugboat-geometry-space.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
