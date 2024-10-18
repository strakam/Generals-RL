# Changelog

## [1.0.1](https://github.com/strakam/generals-bots/compare/v1.0.0...v1.0.1) (2024-10-18)


### 🐛 Bug Fixes

* Fix deterministicity.. seeds now work properly ([d56c63c](https://github.com/strakam/generals-bots/commit/d56c63c1b17590882246210ce270cc6443c68671))
* Generals are now generated sufficiently apart, with free path between them ([ccbb1dc](https://github.com/strakam/generals-bots/commit/ccbb1dc3a01e9fd28e1a28cc890324977babdb17))
* Make truncation as a parameter to the env ([8af020e](https://github.com/strakam/generals-bots/commit/8af020e362acf016c7079ce3bc96d6459e2b470e))
* Update complete example ([e588cfa](https://github.com/strakam/generals-bots/commit/e588cfaff1056bbbbfb62b76846195936dc11b52))

## [1.0.0](https://github.com/strakam/generals-bots/compare/v0.5.1...v1.0.0) (2024-10-14)


### ⚠ BREAKING CHANGES

* Rename repository ([#89](https://github.com/strakam/generals-bots/issues/89))

### 🚀 Features

* Add new registry system ([faeffe9](https://github.com/strakam/generals-bots/commit/faeffe95b69eb37964ce00777e0be15c59b16559))
* Add normalization wrapper ([74e447a](https://github.com/strakam/generals-bots/commit/74e447addb4802e235a45286357edeb9d0e559be))
* Add observation as image wrapper ([34666c3](https://github.com/strakam/generals-bots/commit/34666c30b144fb6cea480333ac8200cbc55a1a33))
* Add RemoveActionMaskWrapper ([3f590fe](https://github.com/strakam/generals-bots/commit/3f590fe2181d9b21bbd9df4cab5cb02d69defdf1))
* Finish registry system ([977dec5](https://github.com/strakam/generals-bots/commit/977dec5d8f4df3fe671a8aa0e46dfc49935debd1))
* Rename repository ([#89](https://github.com/strakam/generals-bots/issues/89)) ([c85364e](https://github.com/strakam/generals-bots/commit/c85364eb84d0b21cb4c3932002a2375d07b01c43))


### 🐛 Bug Fixes

* Add ABC baseclass to abstrat classes so that they cannot be instantiated ([f1991fb](https://github.com/strakam/generals-bots/commit/f1991fbce30fb62550c0b37a8174129f49dc32c4))
* Add missing requirements ([8c63062](https://github.com/strakam/generals-bots/commit/8c63062b1ca60591e35f36d368eb28da4339aec3))
* Apply precommit ([8ae653f](https://github.com/strakam/generals-bots/commit/8ae653f9db185bc004bd2459c6a0125ed27d4742))
* Apply precommit ([5798a74](https://github.com/strakam/generals-bots/commit/5798a74f929adbff6b8bcad65d548377576729bd))
* Fix seeding for gym v1.0.0 ([c283488](https://github.com/strakam/generals-bots/commit/c283488e780e0416821f57957ff62fa443f58a49))
* Import types from gymnasium.core ([5fbdc17](https://github.com/strakam/generals-bots/commit/5fbdc173872d858a6c61b04c6e3dde6b2524ae80))
* New seed handling since gym v1.0.0 ([7ff6ed8](https://github.com/strakam/generals-bots/commit/7ff6ed82d7fec4cc04a27dd32fb5b8119d8dfe61))
* New seed handling since gym v1.0.0 ([1e79af3](https://github.com/strakam/generals-bots/commit/1e79af38ad8d8ec992d0d262d12118c561f37038))


### 🛠️ Refactor

* Add abstract command property to event handlers ([cde3f45](https://github.com/strakam/generals-bots/commit/cde3f45a8e2106ef544258371e881450ddbad36a))
* Add Channels class ([40f70bc](https://github.com/strakam/generals-bots/commit/40f70bcbb83a98fbc50f0de6c5187ef3a9c040a4))
* Add Enums for keybindings ([0e98e1f](https://github.com/strakam/generals-bots/commit/0e98e1f866392b7629ae398de271fae5f45c5cb0))
* Add EventHandler static constroctor ([252020d](https://github.com/strakam/generals-bots/commit/252020d9efe7a50a0fb09e51a5209a1c3f711b92))
* Add FoV toggle to all modes ([a2afa3b](https://github.com/strakam/generals-bots/commit/a2afa3b0b999de930a16a6d624bd2290342e4a04))
* Add GuiMode enum ([6b2e295](https://github.com/strakam/generals-bots/commit/6b2e295d60494558ed3e6f3a13366ddcbc9ef881))
* Add strategy pattern for event handlers ([7a9c526](https://github.com/strakam/generals-bots/commit/7a9c526a1380be3646b01bb4bf610b870a3f6585))
* Add types in renderer ([bc3f7b0](https://github.com/strakam/generals-bots/commit/bc3f7b0df8cd1f67cd2e39f730e30b57b26b0690))
* additional fix ([7a9c526](https://github.com/strakam/generals-bots/commit/7a9c526a1380be3646b01bb4bf610b870a3f6585))
* Additional include to fix crashing ([1dc144a](https://github.com/strakam/generals-bots/commit/1dc144af6479508331df4534de6943a0d3a20a73))
* Better check for replay commands handling ([557e97a](https://github.com/strakam/generals-bots/commit/557e97af6c6e1eb98a3326cc4dec6c039540489b))
* Create CommonEnvironment that is subclassed ([5899908](https://github.com/strakam/generals-bots/commit/5899908746ec7245b5bef94a89fb1ca406656bfe))
* Fix direction types ([a4713b0](https://github.com/strakam/generals-bots/commit/a4713b0d8f31be3b0e366a62f3458645ec31d00f))
* Fix referencing wrong variables ([566b586](https://github.com/strakam/generals-bots/commit/566b58612fde07d19143e6510e432bb430cbcc1c))
* Fix some naming stuff ([acf8fd5](https://github.com/strakam/generals-bots/commit/acf8fd5f2729f71a2af07ba3f912e6dd77550432))
* Fix some observation space mismatches ([d67dbbf](https://github.com/strakam/generals-bots/commit/d67dbbf2d5015241b265ac729e5ddfd44a907ce5))
* Fix wrong class initialization in handlers ([7a9c526](https://github.com/strakam/generals-bots/commit/7a9c526a1380be3646b01bb4bf610b870a3f6585))
* handle quit better ([7a9c526](https://github.com/strakam/generals-bots/commit/7a9c526a1380be3646b01bb4bf610b870a3f6585))
* Improve code style ([38b0266](https://github.com/strakam/generals-bots/commit/38b0266f60eb830f1bf32913dfec77c1481b0aba))
* Improve handle events ([4258b79](https://github.com/strakam/generals-bots/commit/4258b79a607e8baa76c25279df9bd15202ebbbe6))
* Include enums, remove unused things ([3aafe7f](https://github.com/strakam/generals-bots/commit/3aafe7fb84d1f8f587b9aea2aef9ed6f524bf2f3))
* Instantiate event handler only once on GUI creation ([4921188](https://github.com/strakam/generals-bots/commit/49211883b640c05ceb47b711e4c7a0f7f4a8d42e))
* little fix ([7a9c526](https://github.com/strakam/generals-bots/commit/7a9c526a1380be3646b01bb4bf610b870a3f6585))
* Make default default reward methods static ([32e8cf7](https://github.com/strakam/generals-bots/commit/32e8cf7daf73199027f2d802d1a580b85c31fee2))
* Make env more aligned from RL practitioner perspective ([df3e36e](https://github.com/strakam/generals-bots/commit/df3e36e1d3ef03aa90af5710de55611a11622bd7))
* Remake folder structure ([722b1e9](https://github.com/strakam/generals-bots/commit/722b1e9d2d2309cb8fa18e75dc3509e57c889bd8))
* Remove unused imports ([61f276c](https://github.com/strakam/generals-bots/commit/61f276cd36d07dc4cfcd0cd28b8ea1466b011dd3))
* Remove unused mode attribute ([aaa68eb](https://github.com/strakam/generals-bots/commit/aaa68eba2343a0dbfcc5bf4f6f82923c9515e2ab))
* Rename Observation item visibile_cells to visible_cells ([aa196ac](https://github.com/strakam/generals-bots/commit/aa196acf14a99c2648b46d590c4dbed114534f91))
* Restructure files ([03465b8](https://github.com/strakam/generals-bots/commit/03465b801743e0c38aed5d7067f70e86acf809a4))
* Use match clause in grid setter ([c6efed0](https://github.com/strakam/generals-bots/commit/c6efed02076bac7a7db93b49f285db4e19a96af7))

## [0.5.1](https://github.com/strakam/Generals-RL/compare/v0.5.0...v0.5.1) (2024-10-01)


### 🐛 Bug Fixes

* fix broken imports after merge ([aa7147f](https://github.com/strakam/Generals-RL/commit/aa7147fe99a588afa40eb586b492a36c61718727))
* fix broken variables and methods ([5b3533c](https://github.com/strakam/Generals-RL/commit/5b3533cc9bd2dfcf34c9196b29e5ff296bec88ce))


### 🛠️ Refactor

* abstract GUI handling ([f3552fc](https://github.com/strakam/Generals-RL/commit/f3552fc8d93e2c729cefae554586c0baf553f489))
* add more typing ([71e72ab](https://github.com/strakam/Generals-RL/commit/71e72ab3699deff36f08944c4259a9766d6aded2))
* fix RewardFn type alias ([0c30cb7](https://github.com/strakam/Generals-RL/commit/0c30cb7c14692bb97765ef114bdfd0986789be9a))
* From Map to GridFactory ([075eb0f](https://github.com/strakam/Generals-RL/commit/075eb0f1a49355617b30a5f8958aacfe0388aea1))
* Improve Grid class ([aa8438e](https://github.com/strakam/Generals-RL/commit/aa8438e5d56c9e0527df842a4f70350fc416e6f9))
* improve GUI handling ([7020813](https://github.com/strakam/Generals-RL/commit/7020813ab5a634c79ccc781235beca235b7897b9))
* move all GUI properties to Properties class ([669b8a3](https://github.com/strakam/Generals-RL/commit/669b8a3f628c2d48fdc71f484e82c9743a3e44a3))

## [0.5.0](https://github.com/strakam/Generals-RL/compare/v0.4.0...v0.5.0) (2024-10-01)


### 🚀 Features

* Reset replay if 'r' is pressed ([0c2357f](https://github.com/strakam/Generals-RL/commit/0c2357f2f49493d7b17804dc1144ae1b1c1fba80))


### 🐛 Bug Fixes

* Accept map passed from options ([baf2021](https://github.com/strakam/Generals-RL/commit/baf202193686b9cd97e4dcca9a611b4e4af2fb08))
* Create proper types for spaces ([f543663](https://github.com/strakam/Generals-RL/commit/f543663c0a8f332043fd8ec4ea86c11ab84893cf))


### 🛠️ Refactor

* add missing types ([960afae](https://github.com/strakam/Generals-RL/commit/960afae4080382fceffa06a66e882108a38f716a))
* move common attributes to Agent class ([e48a39b](https://github.com/strakam/Generals-RL/commit/e48a39bd91fcd60c9053e925822d820e349ab94e))
* New action space and observation space ([4979342](https://github.com/strakam/Generals-RL/commit/49793423e9039bae463d21f80c0d4923a7f44d4b))
* Unify reward_fn design ([3039ace](https://github.com/strakam/Generals-RL/commit/3039aceb27d63cdbbfe8f8f8fee8d71451e6915e))

## [0.4.0](https://github.com/strakam/Generals-RL/compare/v0.3.2...v0.4.0) (2024-09-29)


### 🚀 Features

* Support rectangular grid shapes ([bb3c5e1](https://github.com/strakam/Generals-RL/commit/bb3c5e1ef7cd53c8d92c3a901010ef6f263e73d8))


### 🐛 Bug Fixes

* Delete replay class on reset ([3ee9a68](https://github.com/strakam/Generals-RL/commit/3ee9a688a73eacdd5a780baeb4186edeaf4ddf06))
* Fix possibility that two generals are generated in the same location ([d63978b](https://github.com/strakam/Generals-RL/commit/d63978b2b09acda1b22d86d80386117e508e7ff2))

## [0.3.2](https://github.com/strakam/Generals-RL/compare/v0.3.1...v0.3.2) (2024-09-27)


### 🐛 Bug Fixes

* **mapper:** properly regenerate invalid map ([63ff837](https://github.com/strakam/Generals-RL/commit/63ff837c86d57f6b92d7445b5f1aaff0aed43673))


### 🛠️ Refactor

* Change agent passing, minimize examples ([11a38b7](https://github.com/strakam/Generals-RL/commit/11a38b711816e33300f25c4f024653f813b1be49))
* **render:** simplify code ([58e8b01](https://github.com/strakam/Generals-RL/commit/58e8b0142c2e4e775488db00e2e8205d618b9952))

## [0.3.1](https://github.com/strakam/Generals-RL/compare/v0.3.0...v0.3.1) (2024-09-26)


### 🛠️ Refactor

* gigantic refactor ([d67e887](https://github.com/strakam/Generals-RL/commit/d67e8877523850df0c017fea0b5d7b7dd1dd92ae))
* Rethink maps ([bbfb777](https://github.com/strakam/Generals-RL/commit/bbfb777cd4d02ba2f415171fdd94e74680fa80d8))
* rethink replay ([ebc2587](https://github.com/strakam/Generals-RL/commit/ebc2587ade5e2d3ecab11177a0c428406fc053af))

## [0.3.0](https://github.com/strakam/Generals-RL/compare/v0.2.1...v0.3.0) (2024-09-25)


### 🚀 Features

* add custom colors and names ([8fcc858](https://github.com/strakam/Generals-RL/commit/8fcc8584702fc975548cbb2b6894db41272a8fee))


### 🐛 Bug Fixes

* **game:** check validity of moves in game step ([e6fc5f0](https://github.com/strakam/Generals-RL/commit/e6fc5f0a2cb07ddf630812ae965c3b932edbbdde))
* only non-trivial actions are valid ([e3119cd](https://github.com/strakam/Generals-RL/commit/e3119cd5f7182d50619859f5ebdf867bc1257f82))
* raise warning when invalid moves are made by agents ([6cd5257](https://github.com/strakam/Generals-RL/commit/6cd52572c2aeff50d567034021a33983acd00153))


### 🛠️ Refactor

* **agent:** cleaner code, better naming ([a4b3b64](https://github.com/strakam/Generals-RL/commit/a4b3b6426582d668068cbfa13978939e76674679))
* **game:** change move format ([f14d716](https://github.com/strakam/Generals-RL/commit/f14d7165e6f859604858d2dd046b10b3c702b702))
* Simplify Expander code ([4cedc9f](https://github.com/strakam/Generals-RL/commit/4cedc9fddbc4ecb67516399046786d849645e00d))

## [0.2.1](https://github.com/strakam/Generals-RL/compare/v0.1.0...v0.2.1) (2024-09-24)


### Features

* add parameters to random agent ([d3451b7](https://github.com/strakam/Generals-RL/commit/d3451b7b64f9377301b65286cc40d7f3f758591c))
* extend action space (idle action allowed) ([9d4e1fa](https://github.com/strakam/Generals-RL/commit/9d4e1fae508f5c419a77d77c17dd7409e0e5bfc2))
* user can choose gymnasium opponent NPC ([6ff2120](https://github.com/strakam/Generals-RL/commit/6ff212064a2aa613812bcbec021d6947c9b04cc9))


### Bug Fixes

* allow change of game speed during pause ([99606c8](https://github.com/strakam/Generals-RL/commit/99606c8b477368e0d617556ccd226ddd6f7e168a))
* make info dictionaries empty ([7c1e0c0](https://github.com/strakam/Generals-RL/commit/7c1e0c0688a5c181b670bfdc52f5ce34d7b54924))
