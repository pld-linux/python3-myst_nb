%define 	module	myst_nb
Summary:	A Jupyter Notebook Sphinx reader
Summary(pl.UTF-8):	Biblioteka do czytania formatu Jupyter Notebook dla Sphinksa
Name:		python3-%{module}
Version:	1.3.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/myst_nb/
Source0:	https://files.pythonhosted.org/packages/source/m/myst_nb/%{module}-%{version}.tar.gz
# Source0-md5:	95273355f33700fcf162fd9caaef6da1
URL:		https://github.com/executablebooks/myst-nb
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.4
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Jupyter Notebook Sphinx reader built on top of the MyST markdown
parser.

%description -l pl.UTF-8
Biblioteka do czytania formatu Jupyter Notebook dla Sphinksa,
zbudowana w oparciu o parser markdown MyST.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%attr(755,root,root) %{_bindir}/mystnb-docutils-html
%attr(755,root,root) %{_bindir}/mystnb-docutils-html5
%attr(755,root,root) %{_bindir}/mystnb-docutils-latex
%attr(755,root,root) %{_bindir}/mystnb-docutils-pseudoxml
%attr(755,root,root) %{_bindir}/mystnb-docutils-xml
%attr(755,root,root) %{_bindir}/mystnb-quickstart
%attr(755,root,root) %{_bindir}/mystnb-to-jupyter
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
