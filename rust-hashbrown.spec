# check disabled to prevent circular dependencies
%bcond_with check
%global debug_package %{nil}

%global crate hashbrown

Name:           rust-%{crate}
Version:        0.12.3
Release:        1%{?dist}
Summary:        Rust port of Google's SwissTable hash map

# Upstream license specification: Apache-2.0/MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/hashbrown
Source:         %{crates_source}
Patch0:		hashbrown-0.12.3-build.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(ahash) >= 0.7.0 with crate(ahash) < 0.8.0)
%if %{with check}
BuildRequires:  (crate(doc-comment/default) >= 0.3.1 with crate(doc-comment/default) < 0.4.0)
BuildRequires:  (crate(fnv/default) >= 1.0.7 with crate(fnv/default) < 2.0.0)
BuildRequires:  (crate(lazy_static/default) >= 1.4.0 with crate(lazy_static/default) < 2.0.0)
BuildRequires:  (crate(rand/default) >= 0.7.3 with crate(rand/default) < 0.8.0)
BuildRequires:  (crate(rand/small_rng) >= 0.7.3 with crate(rand/small_rng) < 0.8.0)
BuildRequires:  (crate(rayon/default) >= 1.0.0 with crate(rayon/default) < 2.0.0)
BuildRequires:  (crate(serde_test/default) >= 1.0.0 with crate(serde_test/default) < 2.0.0)
%endif
%endif

%global _description %{expand:
Rust port of Google's SwissTable hash map.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown) = 0.11.2
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/default) = 0.11.2
Requires:       cargo
Requires:       (crate(ahash) >= 0.7.0 with crate(ahash) < 0.8.0)
Requires:       crate(hashbrown) = 0.11.2
Requires:       crate(hashbrown/inline-more) = 0.11.2

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ahash-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/ahash) = 0.11.2
Requires:       cargo
Requires:       (crate(ahash) >= 0.7.0 with crate(ahash) < 0.8.0)
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+ahash-devel %{_description}

This package contains library source intended for building other packages
which use "ahash" feature of "%{crate}" crate.

%files       -n %{name}+ahash-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ahash-compile-time-rng-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/ahash-compile-time-rng) = 0.11.2
Requires:       cargo
Requires:       (crate(ahash/compile-time-rng) >= 0.7.0 with crate(ahash/compile-time-rng) < 0.8.0)
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+ahash-compile-time-rng-devel %{_description}

This package contains library source intended for building other packages
which use "ahash-compile-time-rng" feature of "%{crate}" crate.

%files       -n %{name}+ahash-compile-time-rng-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/alloc) = 0.11.2
Requires:       cargo
Requires:       (crate(rustc-std-workspace-alloc/default) >= 1.0.0 with crate(rustc-std-workspace-alloc/default) < 2.0.0)
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bumpalo-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/bumpalo) = 0.11.2
Requires:       cargo
Requires:       (crate(bumpalo/default) >= 3.5.0 with crate(bumpalo/default) < 4.0.0)
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+bumpalo-devel %{_description}

This package contains library source intended for building other packages
which use "bumpalo" feature of "%{crate}" crate.

%files       -n %{name}+bumpalo-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+compiler_builtins-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/compiler_builtins) = 0.11.2
Requires:       cargo
Requires:       (crate(compiler_builtins/default) >= 0.1.2 with crate(compiler_builtins/default) < 0.2.0)
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+compiler_builtins-devel %{_description}

This package contains library source intended for building other packages
which use "compiler_builtins" feature of "%{crate}" crate.

%files       -n %{name}+compiler_builtins-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+core-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/core) = 0.11.2
Requires:       cargo
Requires:       (crate(rustc-std-workspace-core/default) >= 1.0.0 with crate(rustc-std-workspace-core/default) < 2.0.0)
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+core-devel %{_description}

This package contains library source intended for building other packages
which use "core" feature of "%{crate}" crate.

%files       -n %{name}+core-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+inline-more-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/inline-more) = 0.11.2
Requires:       cargo
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+inline-more-devel %{_description}

This package contains library source intended for building other packages
which use "inline-more" feature of "%{crate}" crate.

%files       -n %{name}+inline-more-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/nightly) = 0.11.2
Requires:       cargo
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+raw-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/raw) = 0.11.2
Requires:       cargo
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+raw-devel %{_description}

This package contains library source intended for building other packages
which use "raw" feature of "%{crate}" crate.

%files       -n %{name}+raw-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/rayon) = 0.11.2
Requires:       cargo
Requires:       (crate(rayon/default) >= 1.0.0 with crate(rayon/default) < 2.0.0)
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages
which use "rayon" feature of "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/rustc-dep-of-std) = 0.11.2
Requires:       cargo
Requires:       (crate(compiler_builtins/default) >= 0.1.2 with crate(compiler_builtins/default) < 0.2.0)
Requires:       crate(hashbrown) = 0.11.2
Requires:       crate(hashbrown/alloc) = 0.11.2
Requires:       crate(hashbrown/core) = 0.11.2
Requires:       crate(hashbrown/nightly) = 0.11.2
Requires:       crate(hashbrown/rustc-internal-api) = 0.11.2

%description -n %{name}+rustc-dep-of-std-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-dep-of-std" feature of "%{crate}" crate.

%files       -n %{name}+rustc-dep-of-std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc-internal-api-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/rustc-internal-api) = 0.11.2
Requires:       cargo
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+rustc-internal-api-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-internal-api" feature of "%{crate}" crate.

%files       -n %{name}+rustc-internal-api-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(hashbrown/serde) = 0.11.2
Requires:       cargo
Requires:       (crate(serde) >= 1.0.25 with crate(serde) < 2.0.0)
Requires:       crate(hashbrown) = 0.11.2

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Sun Mar 28 2021 Bernhard Rosenkränzer <bero@lindev.ch> - 0.11.2-1
- Initial package
