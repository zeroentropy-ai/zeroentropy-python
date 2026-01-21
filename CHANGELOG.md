# Changelog

## 0.1.0-alpha.8 (2026-01-21)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/zeroentropy-ai/zeroentropy-python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** manual updates ([dbd1650](https://github.com/zeroentropy-ai/zeroentropy-python/commit/dbd1650daad7af66a53f12fc7b10db1814893483))
* **client:** add support for binary request streaming ([b06f1c2](https://github.com/zeroentropy-ai/zeroentropy-python/commit/b06f1c2a4e00ed0a0ab9b3584c61fc487824ae63))


### Bug Fixes

* ensure streams are always closed ([c253ead](https://github.com/zeroentropy-ai/zeroentropy-python/commit/c253ead4750b611c5c650bbbcb3f26d7b9c68905))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([75191f8](https://github.com/zeroentropy-ai/zeroentropy-python/commit/75191f8c6094f4a4560eb7ce3c156fc1b742df73))
* use async_to_httpx_files in patch method ([80e7b4e](https://github.com/zeroentropy-ai/zeroentropy-python/commit/80e7b4e3f5456134a521d24056f47d8f501d8e5b))


### Chores

* add missing docstrings ([ae8ed92](https://github.com/zeroentropy-ai/zeroentropy-python/commit/ae8ed924d17668c0452d957d50722e09866606e4))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([2b44852](https://github.com/zeroentropy-ai/zeroentropy-python/commit/2b44852cac52b0b51c0159582ec4f185e666e012))
* **docs:** use environment variables for authentication in code snippets ([b328198](https://github.com/zeroentropy-ai/zeroentropy-python/commit/b3281987cab77990b3d83155308872f848c930d0))
* **internal:** add `--fix` argument to lint script ([cc848fe](https://github.com/zeroentropy-ai/zeroentropy-python/commit/cc848fe86aa35af50041babacb33920adf3dd90b))
* **internal:** add missing files argument to base client ([4848858](https://github.com/zeroentropy-ai/zeroentropy-python/commit/48488580f4d52661a9facbad07ffa2ae5a82cc31))
* **internal:** codegen related update ([63df3e7](https://github.com/zeroentropy-ai/zeroentropy-python/commit/63df3e7b3af67b1dc7cd1d9a91ef9b109e209e75))
* **internal:** codegen related update ([3084586](https://github.com/zeroentropy-ai/zeroentropy-python/commit/3084586d9d839b9d56172a9c020d5d8adb6f02de))
* **internal:** update `actions/checkout` version ([2448d28](https://github.com/zeroentropy-ai/zeroentropy-python/commit/2448d28a581c998a24ada6a39180cdc894a3a1c2))
* speedup initial import ([5e2b1ce](https://github.com/zeroentropy-ai/zeroentropy-python/commit/5e2b1ce9622fd4b32b237041b6e16b2bdcafe44e))
* update lockfile ([0178c61](https://github.com/zeroentropy-ai/zeroentropy-python/commit/0178c61d65f910bb134becf71fbb9c500c9b2009))

## 0.1.0-alpha.7 (2025-11-24)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/zeroentropy-ai/zeroentropy-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** manual updates ([7b6f1c5](https://github.com/zeroentropy-ai/zeroentropy-python/commit/7b6f1c52caff5579b0f42534ae393bf2bd634e2b))
* clean up environment call outs ([de35b9d](https://github.com/zeroentropy-ai/zeroentropy-python/commit/de35b9dc8c136eeaa0909076488f152a5f885398))
* **client:** support file upload requests ([4e03611](https://github.com/zeroentropy-ai/zeroentropy-python/commit/4e036110dec2d075f4de4cf44691c131dfa545b7))
* improve future compat with pydantic v3 ([372675f](https://github.com/zeroentropy-ai/zeroentropy-python/commit/372675f01b9fd520b0f49749b85314a3333dfa2a))
* **types:** replace List[str] with SequenceNotStr in params ([37625fd](https://github.com/zeroentropy-ai/zeroentropy-python/commit/37625fd6bb4efb5a4926e565eaa7b25852d75f51))


### Bug Fixes

* avoid newer type syntax ([8f77952](https://github.com/zeroentropy-ai/zeroentropy-python/commit/8f7795235684015a6cd419e2bab68b99ecf63b23))
* **client:** don't send Content-Type header on GET requests ([dfd4e86](https://github.com/zeroentropy-ai/zeroentropy-python/commit/dfd4e866616c9c7e9fa6ffa3b757abf6d8cd9ebc))
* **parsing:** correctly handle nested discriminated unions ([79004f8](https://github.com/zeroentropy-ai/zeroentropy-python/commit/79004f855735cc872d0050f781bf8b84d04fd592))
* **parsing:** ignore empty metadata ([a8b35a8](https://github.com/zeroentropy-ai/zeroentropy-python/commit/a8b35a89d5b113eb662bd3113c9433dc5f1382f9))
* **parsing:** parse extra field types ([5530ece](https://github.com/zeroentropy-ai/zeroentropy-python/commit/5530ece04b51a3300c4202b66d4e50101c374a60))


### Chores

* **internal:** add Sequence related utils ([856feb3](https://github.com/zeroentropy-ai/zeroentropy-python/commit/856feb326411abd1fc736eee5a64401f526285ca))
* **internal:** bump pinned h11 dep ([b9e057f](https://github.com/zeroentropy-ai/zeroentropy-python/commit/b9e057f0827b8ed5851ec7e7a8b9ed622019f065))
* **internal:** change ci workflow machines ([bb0ac37](https://github.com/zeroentropy-ai/zeroentropy-python/commit/bb0ac37c96cf27acdcc4e578e9419cbe4a457e18))
* **internal:** fix ruff target version ([80e5aae](https://github.com/zeroentropy-ai/zeroentropy-python/commit/80e5aae0af40e80b5962b0dbf2d5351d9df4432e))
* **internal:** move mypy configurations to `pyproject.toml` file ([97977db](https://github.com/zeroentropy-ai/zeroentropy-python/commit/97977db20f3f27cb1b01f4be6e3538796c0a5414))
* **internal:** update comment in script ([e5a7e0f](https://github.com/zeroentropy-ai/zeroentropy-python/commit/e5a7e0f1592dcfe868064dcdea1446b358662461))
* **internal:** update pyright exclude list ([0c89992](https://github.com/zeroentropy-ai/zeroentropy-python/commit/0c89992ab3ef88427c150b72fe510e26a202db43))
* **package:** mark python 3.13 as supported ([144f8ca](https://github.com/zeroentropy-ai/zeroentropy-python/commit/144f8ca076c92c7e68403d6a0a49ce1caeee69b9))
* **project:** add settings file for vscode ([c4f8607](https://github.com/zeroentropy-ai/zeroentropy-python/commit/c4f86076c0b09422a445ffa91e6880a085fabacd))
* **readme:** fix version rendering on pypi ([3ccc314](https://github.com/zeroentropy-ai/zeroentropy-python/commit/3ccc314b021100775fe854d7225405c63b299599))
* **tests:** simplify `get_platform` test ([ae111a6](https://github.com/zeroentropy-ai/zeroentropy-python/commit/ae111a642a1da930f319ce62f1a28f203881cfe5))
* update @stainless-api/prism-cli to v5.15.0 ([0deb0ff](https://github.com/zeroentropy-ai/zeroentropy-python/commit/0deb0ff394e034254520520675869023912cecc1))
* update github action ([7e76e08](https://github.com/zeroentropy-ai/zeroentropy-python/commit/7e76e087f68489a4a24ac990d48dd665d81f7181))

## 0.1.0-alpha.6 (2025-07-08)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/zeroentropy-ai/zeroentropy-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** manual updates ([b6616f5](https://github.com/zeroentropy-ai/zeroentropy-python/commit/b6616f523b9dd5a4a3f9142bf2a561b560767492))
* **api:** manual updates ([8752560](https://github.com/zeroentropy-ai/zeroentropy-python/commit/875256098555c768cd90d459df84e7cdcb4244ce))
* **api:** manual updates ([11c83ad](https://github.com/zeroentropy-ai/zeroentropy-python/commit/11c83ad2bc4942f703bd255301816eb3a99682b7))
* **api:** manual updates ([801513a](https://github.com/zeroentropy-ai/zeroentropy-python/commit/801513aefc80ac3345bb8d9995d558e576d3c58e))
* **client:** add support for aiohttp ([3aa7ee2](https://github.com/zeroentropy-ai/zeroentropy-python/commit/3aa7ee28445efc3285b1ce79d6b7959d18bf7425))


### Bug Fixes

* **ci:** correct conditional ([6ab3ba2](https://github.com/zeroentropy-ai/zeroentropy-python/commit/6ab3ba21090ea2c54dfd7b9aea8c1d86963cd046))
* **ci:** release-doctor — report correct token name ([c9a55cb](https://github.com/zeroentropy-ai/zeroentropy-python/commit/c9a55cb8318c27c3acd8a84395cd295e348a05f9))
* **client:** correctly parse binary response | stream ([f7b7ef9](https://github.com/zeroentropy-ai/zeroentropy-python/commit/f7b7ef9f45ff779734d1b6ee48349943bf14fce2))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([027e535](https://github.com/zeroentropy-ai/zeroentropy-python/commit/027e535f70651ff5f6b0df8eb3a9786e31241896))


### Chores

* **ci:** change upload type ([cb76da7](https://github.com/zeroentropy-ai/zeroentropy-python/commit/cb76da7ab4ab322268bd7663f5371893ff851a05))
* **ci:** enable for pull requests ([fb3b81d](https://github.com/zeroentropy-ai/zeroentropy-python/commit/fb3b81d7b36b9242b56ed8e5e928272857a82aac))
* **ci:** only run for pushes and fork pull requests ([ff5c91d](https://github.com/zeroentropy-ai/zeroentropy-python/commit/ff5c91d9ebca88bad06e0b9b1c62cd013dcf1b9b))
* **internal:** update conftest.py ([0ddbc5a](https://github.com/zeroentropy-ai/zeroentropy-python/commit/0ddbc5ac04d55067056a50b6ad38b9afc9be15c1))
* **readme:** update badges ([e790eb4](https://github.com/zeroentropy-ai/zeroentropy-python/commit/e790eb48bfd89d6b384cd9382480574a83cee175))
* **tests:** add tests for httpx client instantiation & proxies ([64a0a4c](https://github.com/zeroentropy-ai/zeroentropy-python/commit/64a0a4cb1b1c4f71b37174e748e91e0df7bcc2cc))
* **tests:** run tests in parallel ([0261b3c](https://github.com/zeroentropy-ai/zeroentropy-python/commit/0261b3c5bb54b02fe84b42c2d0e41a5e43519adc))
* **tests:** skip some failing tests on the latest python versions ([2cbe097](https://github.com/zeroentropy-ai/zeroentropy-python/commit/2cbe097a9ac15c6f87e7137788a44058bd966524))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([3cd4296](https://github.com/zeroentropy-ai/zeroentropy-python/commit/3cd4296f8fe24f373dba2100dc1bc389f8e3b496))

## 0.1.0-alpha.5 (2025-06-04)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/zeroentropy-ai/zeroentropy-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** manual updates ([50807fe](https://github.com/zeroentropy-ai/zeroentropy-python/commit/50807fe3454c36376e479e0533fba94bbc47aa8a))

## 0.1.0-alpha.4 (2025-06-03)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/zeroentropy-ai/zeroentropy-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** manual updates ([4185d7a](https://github.com/zeroentropy-ai/zeroentropy-python/commit/4185d7aecfe3cca9e31679b2c6ef37776b98b91f))
* **api:** manual updates ([da3806c](https://github.com/zeroentropy-ai/zeroentropy-python/commit/da3806c9866a91252236ff7ff10b5a2eaf9d336a))
* **api:** manual updates ([2872301](https://github.com/zeroentropy-ai/zeroentropy-python/commit/28723016250ec0bba2196d157efd920b79a524b5))
* **api:** manual updates ([1444264](https://github.com/zeroentropy-ai/zeroentropy-python/commit/1444264df4b3d12c6df32621622e9b4ae2d35645))
* **client:** allow passing `NotGiven` for body ([#33](https://github.com/zeroentropy-ai/zeroentropy-python/issues/33)) ([fc2b31c](https://github.com/zeroentropy-ai/zeroentropy-python/commit/fc2b31c7c6f11f046ae4aa7415fb9d58b450a0b5))
* **client:** send `X-Stainless-Read-Timeout` header ([#27](https://github.com/zeroentropy-ai/zeroentropy-python/issues/27)) ([2b1bf5a](https://github.com/zeroentropy-ai/zeroentropy-python/commit/2b1bf5a3ede3b9184f95924a33152a12f7237fb0))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#31](https://github.com/zeroentropy-ai/zeroentropy-python/issues/31)) ([fd3d006](https://github.com/zeroentropy-ai/zeroentropy-python/commit/fd3d006d7d08b6904fb9b56a9c1bd9b2b5c408f4))
* **ci:** ensure pip is always available ([#45](https://github.com/zeroentropy-ai/zeroentropy-python/issues/45)) ([544dcae](https://github.com/zeroentropy-ai/zeroentropy-python/commit/544dcaee18e2bfa523642f59e9e1175488b6fde8))
* **ci:** remove publishing patch ([#46](https://github.com/zeroentropy-ai/zeroentropy-python/issues/46)) ([a2b0950](https://github.com/zeroentropy-ai/zeroentropy-python/commit/a2b09502670c7142eb0ad2947f1b8d610632a532))
* **client:** mark some request bodies as optional ([fc2b31c](https://github.com/zeroentropy-ai/zeroentropy-python/commit/fc2b31c7c6f11f046ae4aa7415fb9d58b450a0b5))
* **types:** handle more discriminated union shapes ([#44](https://github.com/zeroentropy-ai/zeroentropy-python/issues/44)) ([c2760e1](https://github.com/zeroentropy-ai/zeroentropy-python/commit/c2760e1fc8ec87deda30efd5f35cb812d9c27623))


### Chores

* **docs:** update client docstring ([#38](https://github.com/zeroentropy-ai/zeroentropy-python/issues/38)) ([c642337](https://github.com/zeroentropy-ai/zeroentropy-python/commit/c64233754816e51e25fbd988110d6d677bae971f))
* fix typos ([#47](https://github.com/zeroentropy-ai/zeroentropy-python/issues/47)) ([8fe5be4](https://github.com/zeroentropy-ai/zeroentropy-python/commit/8fe5be4670c414102d31ca5501bcec49c3142dba))
* **internal:** bummp ruff dependency ([#26](https://github.com/zeroentropy-ai/zeroentropy-python/issues/26)) ([02a42b4](https://github.com/zeroentropy-ai/zeroentropy-python/commit/02a42b40a585d70fbaec2a28e3534ffa0f86968b))
* **internal:** bump rye to 0.44.0 ([#43](https://github.com/zeroentropy-ai/zeroentropy-python/issues/43)) ([027f69f](https://github.com/zeroentropy-ai/zeroentropy-python/commit/027f69f2275239cfcbaa8658df2f1d5d5d9e6595))
* **internal:** change default timeout to an int ([#25](https://github.com/zeroentropy-ai/zeroentropy-python/issues/25)) ([9a3559f](https://github.com/zeroentropy-ai/zeroentropy-python/commit/9a3559f3f98f1699fe89a03239a9426860c097ef))
* **internal:** codegen related update ([#42](https://github.com/zeroentropy-ai/zeroentropy-python/issues/42)) ([8cb037b](https://github.com/zeroentropy-ai/zeroentropy-python/commit/8cb037b4bf93d1ae9879ab7b456b563b0da38e4d))
* **internal:** codegen related update ([#48](https://github.com/zeroentropy-ai/zeroentropy-python/issues/48)) ([7cfedb5](https://github.com/zeroentropy-ai/zeroentropy-python/commit/7cfedb53ac5ed2c2e7b57ec3fa94c10cdfa5d770))
* **internal:** fix devcontainers setup ([#34](https://github.com/zeroentropy-ai/zeroentropy-python/issues/34)) ([aebe3f6](https://github.com/zeroentropy-ai/zeroentropy-python/commit/aebe3f69ddf00105381945d6c02858bcb3a42837))
* **internal:** fix type traversing dictionary params ([#28](https://github.com/zeroentropy-ai/zeroentropy-python/issues/28)) ([298eed2](https://github.com/zeroentropy-ai/zeroentropy-python/commit/298eed24ae48668d7eea7d35a97917e8920656b9))
* **internal:** minor type handling changes ([#29](https://github.com/zeroentropy-ai/zeroentropy-python/issues/29)) ([9921817](https://github.com/zeroentropy-ai/zeroentropy-python/commit/9921817d4c6c9cdb5487499cedff14a23542440c))
* **internal:** properly set __pydantic_private__ ([#35](https://github.com/zeroentropy-ai/zeroentropy-python/issues/35)) ([406c052](https://github.com/zeroentropy-ai/zeroentropy-python/commit/406c052ee2860e8af31e6c5d656bedfbde2f79a5))
* **internal:** remove extra empty newlines ([#41](https://github.com/zeroentropy-ai/zeroentropy-python/issues/41)) ([fd60612](https://github.com/zeroentropy-ai/zeroentropy-python/commit/fd60612d55b1423e96f5aca7e3297bc732c94005))
* **internal:** remove unused http client options forwarding ([#39](https://github.com/zeroentropy-ai/zeroentropy-python/issues/39)) ([2cabf49](https://github.com/zeroentropy-ai/zeroentropy-python/commit/2cabf492018133ba9870fcc568366e822d3df628))
* **internal:** update client tests ([#30](https://github.com/zeroentropy-ai/zeroentropy-python/issues/30)) ([329cd1e](https://github.com/zeroentropy-ai/zeroentropy-python/commit/329cd1ee7b7fbd41f4563b829e5c276f42aa8e34))
* **internal:** update client tests ([#32](https://github.com/zeroentropy-ai/zeroentropy-python/issues/32)) ([d8618e8](https://github.com/zeroentropy-ai/zeroentropy-python/commit/d8618e8fed41ffb439ccce21ef0cb7e0ee3ee6db))
* **internal:** version bump ([#22](https://github.com/zeroentropy-ai/zeroentropy-python/issues/22)) ([c4fbbe6](https://github.com/zeroentropy-ai/zeroentropy-python/commit/c4fbbe6af970317989f0f6d3d2d40a96f04976e4))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#36](https://github.com/zeroentropy-ai/zeroentropy-python/issues/36)) ([97b55c0](https://github.com/zeroentropy-ai/zeroentropy-python/commit/97b55c0c6482507e6d34f64d418d7a6bf3b68931))

## 0.1.0-alpha.3 (2025-01-28)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/zeroentropy-ai/zeroentropy-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Chores

* go live ([#15](https://github.com/zeroentropy-ai/zeroentropy-python/issues/15)) ([94648e3](https://github.com/zeroentropy-ai/zeroentropy-python/commit/94648e31f00197387695a5b5d0f832f179f6bd99))

## 0.1.0-alpha.2 (2025-01-18)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/zeroentropy-ai/zeroentropy-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#10](https://github.com/zeroentropy-ai/zeroentropy-python/issues/10)) ([d61d43b](https://github.com/zeroentropy-ai/zeroentropy-python/commit/d61d43bc52d19325ef066fef6ceb461a253f4139))
* **api:** update via SDK Studio ([#11](https://github.com/zeroentropy-ai/zeroentropy-python/issues/11)) ([0a8a11a](https://github.com/zeroentropy-ai/zeroentropy-python/commit/0a8a11a7e24b8dfbd64fdde2cb5a11edc0ce9791))
* **api:** update via SDK Studio ([#12](https://github.com/zeroentropy-ai/zeroentropy-python/issues/12)) ([723864e](https://github.com/zeroentropy-ai/zeroentropy-python/commit/723864e726f857267c0c44705485ba9b7d165731))
* **api:** update via SDK Studio ([#13](https://github.com/zeroentropy-ai/zeroentropy-python/issues/13)) ([5799893](https://github.com/zeroentropy-ai/zeroentropy-python/commit/57998931b1c6a68648a5bd124bd0649219237e8d))
* **api:** update via SDK Studio ([#14](https://github.com/zeroentropy-ai/zeroentropy-python/issues/14)) ([03d17bb](https://github.com/zeroentropy-ai/zeroentropy-python/commit/03d17bb0694165401e27f1e7e7d4cd85155b25f2))
* **api:** update via SDK Studio ([#5](https://github.com/zeroentropy-ai/zeroentropy-python/issues/5)) ([62aa3ad](https://github.com/zeroentropy-ai/zeroentropy-python/commit/62aa3ad1383b814d855947effdede5c6d1c90fd6))
* **api:** update via SDK Studio ([#7](https://github.com/zeroentropy-ai/zeroentropy-python/issues/7)) ([0d38bcf](https://github.com/zeroentropy-ai/zeroentropy-python/commit/0d38bcf30e218fd7b4b6043a82b54a9aabff0f3e))
* **api:** update via SDK Studio ([#8](https://github.com/zeroentropy-ai/zeroentropy-python/issues/8)) ([c10e665](https://github.com/zeroentropy-ai/zeroentropy-python/commit/c10e665d5c73669ddbf6a40fd76da2f91bb8c699))
* **api:** update via SDK Studio ([#9](https://github.com/zeroentropy-ai/zeroentropy-python/issues/9)) ([3d9aa30](https://github.com/zeroentropy-ai/zeroentropy-python/commit/3d9aa30f732fbdda5f30c32f2f9c95163a556120))


### Documentation

* remove stainless citation ([2230305](https://github.com/zeroentropy-ai/zeroentropy-python/commit/22303055e83e1ee4cbaf9c148c627aaf198e38b8))

## 0.1.0-alpha.1 (2025-01-18)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/ZeroEntropy-AI/zeroentropy-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([44c5f4c](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/44c5f4c293198fb1712f08931b2012853d217339))
* **api:** update via SDK Studio ([d4732f5](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/d4732f5969ee6bb7f46b9538764935990e93a9b2))
* **api:** update via SDK Studio ([7beca06](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/7beca06664b3e777443ea2cfb4e64edfc14a2039))
* **api:** update via SDK Studio ([cd52c38](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/cd52c38c5f88113a49e17480403903e946b2afbd))
* **api:** update via SDK Studio ([8618e3d](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/8618e3d44a19cae736e3644d2ebba44e0bc7b296))
* **api:** update via SDK Studio ([b55e3d0](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/b55e3d0766ba025c45d59bb81b0122096075a4ce))
* **api:** update via SDK Studio ([ae43ac2](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/ae43ac219efea486ec9fa0bd31dbb97e6b72252d))
* **api:** update via SDK Studio ([3718a26](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/3718a265afa4f8229c9f12745ba908e257f6f24d))
* **api:** update via SDK Studio ([9695627](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/9695627c43c6db83d3b16139a7d02514f55a4d00))
* **api:** update via SDK Studio ([f5f67b8](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/f5f67b8a4dc4a7fc7f3c8ee2f89c7ad836f6ca15))
* **api:** update via SDK Studio ([40c2d91](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/40c2d9132ee91f88357d24eb600507837faa30c6))


### Chores

* go live ([#1](https://github.com/ZeroEntropy-AI/zeroentropy-python/issues/1)) ([f82efbb](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/f82efbbb2f5b25fe7a95074135abccb1e6347edf))
* update SDK settings ([#3](https://github.com/ZeroEntropy-AI/zeroentropy-python/issues/3)) ([afd234a](https://github.com/ZeroEntropy-AI/zeroentropy-python/commit/afd234a9afcd12e98b70551263bd51f55b0bf588))
