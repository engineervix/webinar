# Changelog

All notable changes to this project will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project attempts to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.1.0](https://github.com/engineervix/webinar/compare/v0.0.0...v0.1.0) (2024-05-07)


### ♻️ Code Refactoring

* cleanup base template ([5d13fd5](https://github.com/engineervix/webinar/commit/5d13fd53114368b7472d867551023292f168cf29))
* configure django-rq, hcaptcha, apprise & other settings ([16b22ac](https://github.com/engineervix/webinar/commit/16b22ac9bb5b385aa342376556ad33d69040cc75))
* consolidate all core logic and make ready to ship ([4eae752](https://github.com/engineervix/webinar/commit/4eae7527ad34621fbb62e3103a689254ad698a2a))
* crispy forms ain't gonna work here ([53c03c9](https://github.com/engineervix/webinar/commit/53c03c9d574cb5845c19094329f1a64f11acbd82))
* finalise templates & make ready for initial deployment ([cd56535](https://github.com/engineervix/webinar/commit/cd5653583d9dbf2d9b5db29d668a9475bd096914))
* make use of django-rq ([ff12d42](https://github.com/engineervix/webinar/commit/ff12d42faaaecf08b89155194b57f265e4ee1dde))


### 🐛 Bug Fixes

* ensure alert styles are working ([aec3dc6](https://github.com/engineervix/webinar/commit/aec3dc64f87a44b3fe71d8d90a2be651159db3a4))
* ensure tailwind detects the utility classes ([ba0af02](https://github.com/engineervix/webinar/commit/ba0af02562855f7bba2aee9171db1827bdbe7f13))


### ⚙️ Build System

* add add-to-calendar-button ([cb90209](https://github.com/engineervix/webinar/commit/cb90209c80455e52874e068ec94e32548a3131d3))
* add missing frontend configs 🙈 ([ac603b8](https://github.com/engineervix/webinar/commit/ac603b8b00a2d6ea8f8a0c51cb9accaabe498040))
* change add-to-calendar-button config ([c5f4e8e](https://github.com/engineervix/webinar/commit/c5f4e8e52486e1a0ce69df76b558c9990433e95d))
* configure tailwind and remove extraneous templates & stylesheets ([a0836f6](https://github.com/engineervix/webinar/commit/a0836f6c50bac73972ca777a39738d5ce1f442ef))
* ensure pytz is available ([0a80a4a](https://github.com/engineervix/webinar/commit/0a80a4a34475a5433b82da52ab617f39b8856438))
* install apprise premailer and pycmarkgfm ([48a6f7a](https://github.com/engineervix/webinar/commit/48a6f7a86381fc12c257a376930e5c588b2b1e7a))
* remove bourbon and update cz-conventional-changelog setup ([592ed30](https://github.com/engineervix/webinar/commit/592ed30628d8819aedced857e606438296736798))
* update tailwind setup as per docs ([e316bc3](https://github.com/engineervix/webinar/commit/e316bc322eaa5fbcd3e49933763d23a754c0d895))
* we don't want the entire kitchen sink ([3c3ad42](https://github.com/engineervix/webinar/commit/3c3ad4259965180b25eddcc28a61733411df83bb))


### 👷 CI/CD

* add missing env variables ([2386adf](https://github.com/engineervix/webinar/commit/2386adfc0e94d020c7579dfa68b409ee0aa349bf))
* bump actions/setup-node to v4 ([f453064](https://github.com/engineervix/webinar/commit/f453064e059f7cc05ca55df0035d4f88e64d37fb))
* do not specify djlint version ([49b0c81](https://github.com/engineervix/webinar/commit/49b0c81edc7fd709d94873148c03ac0a86e1418c))


### 🚀 Features

* add analytics in production ([51d8aeb](https://github.com/engineervix/webinar/commit/51d8aebd1b21bbf7365258787a95bbac73a4ef22))
* add email template in markdown ([ab5ddcd](https://github.com/engineervix/webinar/commit/ab5ddcd7d56eff47fb3fcb1f4846d3a21bb53c26))
* add footer component ([d28dea3](https://github.com/engineervix/webinar/commit/d28dea36d4755bc8509037d475dc628f529fc15d))
* add notification function powered by apprise and ntfy.sh ([21dcb82](https://github.com/engineervix/webinar/commit/21dcb82348cdba3ec85929324963baf411c1efb5))
* basic hero layout ([01f542b](https://github.com/engineervix/webinar/commit/01f542bbddd00c144e8e8f651c88ffdf402c991a))
* configure mail ([479c6f9](https://github.com/engineervix/webinar/commit/479c6f9a86d52a33e8d47573b7142c545e20bd6f))
* update meta on home page template ([a06bf56](https://github.com/engineervix/webinar/commit/a06bf56213d25a2489332ce504c0892783476abf))


### 💄 Styling

* add banner and remove unused image assets ([0a7bae9](https://github.com/engineervix/webinar/commit/0a7bae91f3ec6f8e9ca4154aa0f2b369cfa94799))
* add daisyUI component library ([e71fdf8](https://github.com/engineervix/webinar/commit/e71fdf8af0a96333367d8c10a08dd65d32d6cfbd))
* additional frontend enhancements ([2512c53](https://github.com/engineervix/webinar/commit/2512c537a911ee736358b4a468d4f0e28ea7ac6e))
* change favicon ([29b0866](https://github.com/engineervix/webinar/commit/29b0866865b35a0cd4d90959eedfb9487b63f0de))
* fix linting ([b81ca7a](https://github.com/engineervix/webinar/commit/b81ca7a4de2a9f2ae83f3e93587e53fb5bf6ed4d))
* fix linting ([dc1ba61](https://github.com/engineervix/webinar/commit/dc1ba61d0397436e19bd7e1693c037bfcabd11f0))
* put together initial layout ([6eb7326](https://github.com/engineervix/webinar/commit/6eb73265883a419ab1058d0a39319c041e1f879e))
* update hero image ([2bb109a](https://github.com/engineervix/webinar/commit/2bb109a50fe8c4e247edad463efb01f8b0c22b9d))


### 📝 Docs

* add description ([a931f97](https://github.com/engineervix/webinar/commit/a931f97bd79223d1cc6aa7e119b76bdda1b32f97))
* add one-sentence intro ([b5e30c9](https://github.com/engineervix/webinar/commit/b5e30c9030174229cc9903998c67a0da9582c5bf))
* quick cleanup of the documentation ([11ebc20](https://github.com/engineervix/webinar/commit/11ebc20a248a397a7884a4a5d905210bfc495e3f))
* update docs ([d750fc3](https://github.com/engineervix/webinar/commit/d750fc3038a583c7efd6799976aeb6c57a07799d))
* update the docs ([207eded](https://github.com/engineervix/webinar/commit/207edede45a3c3ad44fdbde759bc29c4e4e23f81))
