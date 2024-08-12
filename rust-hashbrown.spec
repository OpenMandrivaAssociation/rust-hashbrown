# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_with check
%global debug_package %{nil}

%global crate hashbrown

Name:           rust-hashbrown
Version:        0.14.5
Release:        1
Summary:        Rust port of Google's SwissTable hash map
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hashbrown
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(ahash) >= 0.8.7 with crate(ahash) < 0.9.0~)
BuildRequires:  (crate(allocator-api2) >= 0.2.9 with crate(allocator-api2) < 0.3.0~)
BuildRequires:  (crate(allocator-api2/alloc) >= 0.2.9 with crate(allocator-api2/alloc) < 0.3.0~)
BuildRequires:  rust >= 1.63.0
%if %{with check}
BuildRequires:  (crate(bumpalo/allocator-api2) >= 3.13.0 with crate(bumpalo/allocator-api2) < 4.0.0~)
BuildRequires:  (crate(bumpalo/default) >= 3.13.0 with crate(bumpalo/default) < 4.0.0~)
BuildRequires:  (crate(doc-comment/default) >= 0.3.1 with crate(doc-comment/default) < 0.4.0~)
BuildRequires:  (crate(fnv/default) >= 1.0.7 with crate(fnv/default) < 2.0.0~)
BuildRequires:  (crate(lazy_static/default) >= 1.4.0 with crate(lazy_static/default) < 2.0.0~)
BuildRequires:  (crate(rand/default) >= 0.8.3 with crate(rand/default) < 0.9.0~)
BuildRequires:  (crate(rand/small_rng) >= 0.8.3 with crate(rand/small_rng) < 0.9.0~)
BuildRequires:  (crate(rayon/default) >= 1.0.0 with crate(rayon/default) < 2.0.0~)
BuildRequires:  (crate(rkyv/default) >= 0.7.42 with crate(rkyv/default) < 0.8.0~)
BuildRequires:  (crate(rkyv/validation) >= 0.7.42 with crate(rkyv/validation) < 0.8.0~)
BuildRequires:  (crate(serde_test/default) >= 1.0.0 with crate(serde_test/default) < 2.0.0~)
%endif

%global _description %{expand:
A Rust port of Google's SwissTable hash map.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown) = 0.14.5
Requires:       cargo
Requires:       rust >= 1.63.0

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/default) = 0.14.5
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5
Requires:       crate(hashbrown/ahash) = 0.14.5
Requires:       crate(hashbrown/allocator-api2) = 0.14.5
Requires:       crate(hashbrown/inline-more) = 0.14.5

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ahash-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/ahash) = 0.14.5
Requires:       (crate(ahash) >= 0.8.7 with crate(ahash) < 0.9.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+ahash-devel %{_description}

This package contains library source intended for building other packages which
use the "ahash" feature of the "%{crate}" crate.

%files       -n %{name}+ahash-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/alloc) = 0.14.5
Requires:       (crate(rustc-std-workspace-alloc/default) >= 1.0.0 with crate(rustc-std-workspace-alloc/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+allocator-api2-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/allocator-api2) = 0.14.5
Requires:       (crate(allocator-api2) >= 0.2.9 with crate(allocator-api2) < 0.3.0~)
Requires:       (crate(allocator-api2/alloc) >= 0.2.9 with crate(allocator-api2/alloc) < 0.3.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+allocator-api2-devel %{_description}

This package contains library source intended for building other packages which
use the "allocator-api2" feature of the "%{crate}" crate.

%files       -n %{name}+allocator-api2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compiler_builtins-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/compiler_builtins) = 0.14.5
Requires:       (crate(compiler_builtins/default) >= 0.1.2 with crate(compiler_builtins/default) < 0.2.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+compiler_builtins-devel %{_description}

This package contains library source intended for building other packages which
use the "compiler_builtins" feature of the "%{crate}" crate.

%files       -n %{name}+compiler_builtins-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+core-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/core) = 0.14.5
Requires:       (crate(rustc-std-workspace-core/default) >= 1.0.0 with crate(rustc-std-workspace-core/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+core-devel %{_description}

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%files       -n %{name}+core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+equivalent-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/equivalent) = 0.14.5
Requires:       (crate(equivalent) >= 1.0.0 with crate(equivalent) < 2.0.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+equivalent-devel %{_description}

This package contains library source intended for building other packages which
use the "equivalent" feature of the "%{crate}" crate.

%files       -n %{name}+equivalent-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+inline-more-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/inline-more) = 0.14.5
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+inline-more-devel %{_description}

This package contains library source intended for building other packages which
use the "inline-more" feature of the "%{crate}" crate.

%files       -n %{name}+inline-more-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/nightly) = 0.14.5
Requires:       (crate(allocator-api2) >= 0.2.9 with crate(allocator-api2) < 0.3.0~)
Requires:       (crate(allocator-api2/alloc) >= 0.2.9 with crate(allocator-api2/alloc) < 0.3.0~)
Requires:       (crate(allocator-api2/nightly) >= 0.2.9 with crate(allocator-api2/nightly) < 0.3.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+raw-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/raw) = 0.14.5
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+raw-devel %{_description}

This package contains library source intended for building other packages which
use the "raw" feature of the "%{crate}" crate.

%files       -n %{name}+raw-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/rayon) = 0.14.5
Requires:       (crate(rayon/default) >= 1.0.0 with crate(rayon/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rkyv-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/rkyv) = 0.14.5
Requires:       (crate(rkyv) >= 0.7.42 with crate(rkyv) < 0.8.0~)
Requires:       (crate(rkyv/alloc) >= 0.7.42 with crate(rkyv/alloc) < 0.8.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+rkyv-devel %{_description}

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%files       -n %{name}+rkyv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/rustc-dep-of-std) = 0.14.5
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5
Requires:       crate(hashbrown/alloc) = 0.14.5
Requires:       crate(hashbrown/compiler_builtins) = 0.14.5
Requires:       crate(hashbrown/core) = 0.14.5
Requires:       crate(hashbrown/nightly) = 0.14.5
Requires:       crate(hashbrown/rustc-internal-api) = 0.14.5

%description -n %{name}+rustc-dep-of-std-devel %{_description}

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%files       -n %{name}+rustc-dep-of-std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustc-internal-api-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/rustc-internal-api) = 0.14.5
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+rustc-internal-api-devel %{_description}

This package contains library source intended for building other packages which
use the "rustc-internal-api" feature of the "%{crate}" crate.

%files       -n %{name}+rustc-internal-api-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hashbrown/serde) = 0.14.5
Requires:       (crate(serde) >= 1.0.25 with crate(serde) < 2.0.0~)
Requires:       cargo
Requires:       crate(hashbrown) = 0.14.5

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
