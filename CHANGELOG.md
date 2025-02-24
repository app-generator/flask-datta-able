# Change Log

## [1.0.25] 2025-02-24
### Changes

- Codebase Refactoring

## [1.0.24] 2025-02-21
### Changes

- Update RM (minor)

## [1.0.23] 2025-02-20
### Changes

- Update Dependencies
- Added Error Pages 

## [1.0.22] 2025-02-20
### Changes

- Added Dynamic DataTables
- Remove the Flask-RestX API

## [1.0.21] 2024-12-07
### Changes

- Added Celery Support
  - a minimal core
- Flask-RestX API

## [1.0.20] 2024-11-30
### Changes

- Update Routes
- Update Demo Link:
  - [Flask Datta Able](https://flask-datta-demo.onrender.com)

## [1.0.19] 2024-11-29
### Changes

- Bump UI Version
- Codebase Improvements
- Update RM Links:
  - 👉 [Flask Datta Able](https://app-generator.dev/product/datta-able/flask/) - `Product Page`
  - 👉 [Flask Datta Able](https://flask-datta-demo.onrender.com) - `LIVE Demo` 
  - 👉 [Flask Datta Able Documentation](https://app-generator.dev/docs/products/flask/datta-able/index.html) - `Complete Information` and Support Links
    - [Getting Started with Flask](https://app-generator.dev/docs/technologies/flask/index.html) - a `comprehensive tutorial`
    - `Configuration`: Install Tailwind/Flowbite, Prepare Environment, Setting up the Database 
    - `Start with Docker`
    - `Manual Build`
    - `Start the project`
    - `Deploy on Render`

## [1.0.18] 2024-05-18
### Changes

- Updated DOCS (readme)
  - [Custom Development](https://appseed.us/custom-development/) Section
  - [CI/CD Assistance for AWS, DO](https://appseed.us/terms/#section-ci-cd)

## [1.0.17] 2024-03-05
### Changes

- Update [Custom Development](https://appseed.us/custom-development/) Section
  - New Pricing: `$3,999`

## [1.0.16] 2023-02-14
### Changes

- Update [Custom Development](https://appseed.us/custom-development/) Section
- Minor Changes (readme)

## [1.0.15] 2023-10-08
### Changes

- Docs Update (readme)
- Added infos for [Flask Datta PRO](https://appseed.us/product/datta-able-pro/flask/)

## [1.0.14] 2023-10-08
### Changes

- Update Dependencies

## [1.0.13] 2023-01-02
### Changes

- `DOCS Update` (readme)
  - [Flask Datta Able - Go LIVE](https://www.youtube.com/watch?v=ZpKy2j9UU84) (`video presentation`)

## [1.0.12] 2022-12-31
### Changes

- Deployment-ready for Render (CI/CD)
  - `render.yaml`
  - `build.sh`
- `DB Management` Improvement
  - `Silent fallback` to **SQLite**

## [1.0.11] 2022-09-07
### Improvements

- Added OAuth via Github
- Improved Auth Pages
- Profile page (minor update) 

## [1.0.10] 2022-06-28
### Improvements

- Bump UI: `v1.0.0-enh1`
  - Added `dark-mode`
  - User profile page 

## [1.0.9] 2022-06-23
### Improvements

- Built with [Datta Able Generator](https://appseed.us/generator/datta-able/)
  - Timestamp: `2022-06-23 18:20`

## [1.0.8] 2022-06-13
### Improvements

- Improved `Auth UX`
- Built with [Datta Able Generator](https://appseed.us/generator/datta-able/)
  - Timestamp: `2022-05-30 21:10`

## [1.0.7] 2022-05-30
### Improvements

- Built with [Datta Able Generator](https://appseed.us/generator/datta-able/)
  - Timestamp: `2022-05-30 21:10`

## [1.0.6] 2022-03-30
### Fixes

- **Patch ImportError**: [cannot import name 'safe_str_cmp' from 'werkzeug.security'](https://docs.appseed.us/content/how-to-fix/importerror-cannot-import-name-safe_str_cmp-from-werkzeug.security)
  - `Werkzeug` deprecation of `safe_str_cmp` starting with version `2.1.0`
    - https://github.com/pallets/werkzeug/issues/2359

## [1.0.5] 2022-01-16
### Improvements

- Bump Flask Codebase to [v2stable.0.1](https://github.com/app-generator/boilerplate-code-flask-dashboard/releases)
- Dependencies update (all packages) 
  - Flask==2.0.2 (latest stable version)
  - flask_wtf==1.0.0
  - jinja2==3.0.3
  - flask-restx==0.5.1
- Forms Update:
  - Replace `TextField` (deprecated) with `StringField`

## Unreleased
### Fixes

- 2021-11-08 - `v1.0.5-rc1`
  - ImportError: cannot import name 'TextField' from 'wtforms'
    - Problem caused by `WTForms-3.0.0`
    - Fix: use **WTForms==2.3.3**

## [1.0.4] 2021-11-06
### Improvements

- Bump Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard) v2.0.0
  - Dependencies update (all packages) 
    - Flask==2.0.1 (latest stable version)
- Better Code formatting
- Improved Files organization
- Optimize imports
- Docker Scripts Update

## [1.0.3] 2021-05-16
### Dependencies Update

- Bump Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard) v1.0.6
- Freeze used versions in `requirements.txt`
    - jinja2 = 2.11.3

## [1.0.2] 2021-03-18
### Improvements

- Bump Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard) v1.0.5
- Freeze used versions in `requirements.txt`
    - flask_sqlalchemy = 2.4.4
    - sqlalchemy = 1.3.23
    
## [1.0.1] 2020-01-17
### Improvements

- Bump UI: [Jinja Datta Able](https://github.com/app-generator/jinja-datta-able/releases) v1.0.1
- UI: [Datta Able](https://github.com/codedthemes/datta-able-bootstrap-dashboard) 2021-01-01 snapshot
- Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard/releases) v1.0.3

## [1.0.0] 2020-02-07
### Initial Release
