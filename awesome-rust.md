# Awesome Rust [![build badge](https://github.com/rust-unofficial/awesome-rust/actions/workflows/rust.yml/badge.svg?branch=main)](https://github.com/rust-unofficial/awesome-rust/actions/workflows/rust.yml) [![Track Awesome List](https://www.trackawesomelist.com/badge.svg)](https://www.trackawesomelist.com/rust-unofficial/awesome-rust/)

A curated list of Rust code and resources.

If you want to contribute, please read [this](CONTRIBUTING.md).

## Table of contents

<!-- toc -->

- [Applications](#applications)
  * [Audio and Music](#audio-and-music)
  * [Cryptocurrencies](#cryptocurrencies)
  * [Database](#database)
  * [Emulators](#emulators)
  * [File manager](#file-manager)
  * [Games](#games)
  * [Graphics](#graphics)
  * [Image processing](#image-processing)
  * [Industrial automation](#industrial-automation)
  * [Observability](#observability)
  * [Operating systems](#operating-systems)
  * [Package Managers](#package-managers)
  * [Payments](#payments)
  * [Productivity](#productivity)
  * [Routing protocols](#routing-protocols)
  * [Security tools](#security-tools)
  * [Social networks](#social-networks)
  * [System tools](#system-tools)
  * [Task scheduling](#task-scheduling)
  * [Text editors](#text-editors)
  * [Text processing](#text-processing)
  * [Utilities](#utilities)
  * [Video](#video)
  * [Virtualization](#virtualization)
  * [Web](#web)
  * [Web Servers](#web-servers)
- [Development tools](#development-tools)
  * [Build system](#build-system)
  * [Debugging](#debugging)
  * [Deployment](#deployment)
  * [Embedded](#embedded)
  * [FFI](#ffi)
  * [Formatters](#formatters)
  * [IDEs](#ides)
  * [Profiling](#profiling)
  * [Services](#services)
  * [Static analysis](#static-analysis)
  * [Testing](#testing)
  * [Transpiling](#transpiling)
- [Libraries](#libraries)
  * [Artificial Intelligence](#artificial-intelligence)
    + [Genetic algorithms](#genetic-algorithms)
    + [Machine learning](#machine-learning)
    + [OpenAI](#openai)
  * [Astronomy](#astronomy)
  * [Asynchronous](#asynchronous)
  * [Audio and Music](#audio-and-music-1)
  * [Authentication](#authentication)
  * [Automotive](#automotive)
  * [Bioinformatics](#bioinformatics)
  * [Caching](#caching)
  * [Cloud](#cloud)
  * [Command-line](#command-line)
  * [Compression](#compression)
  * [Computation](#computation)
  * [Concurrency](#concurrency)
  * [Configuration](#configuration)
  * [Cryptography](#cryptography)
  * [Data processing](#data-processing)
  * [Data streaming](#data-streaming)
  * [Data structures](#data-structures)
  * [Data visualization](#data-visualization)
  * [Database](#database-1)
  * [Date and time](#date-and-time)
  * [Distributed systems](#distributed-systems)
  * [Domain driven design](#domain-driven-design)
  * [eBPF](#ebpf)
  * [Email](#email)
  * [Encoding](#encoding)
  * [Filesystem](#filesystem)
  * [Finance](#finance)
  * [Functional Programming](#functional-programming)
  * [Game development](#game-development)
  * [Geospatial](#geospatial)
  * [Graph algorithms](#graph-algorithms)
  * [Graphics](#graphics-1)
  * [GUI](#gui)
  * [Image processing](#image-processing-1)
  * [Language specification](#language-specification)
  * [Logging](#logging)
  * [Macro](#macro)
  * [Markup language](#markup-language)
  * [Mobile](#mobile)
  * [Network programming](#network-programming)
  * [Parsing](#parsing)
  * [Peripherals](#peripherals)
  * [Platform specific](#platform-specific)
  * [Scripting](#scripting)
  * [Simulation](#simulation)
  * [System](#system)
  * [Task scheduling](#task-scheduling-1)
  * [Template engine](#template-engine)
  * [Text processing](#text-processing-1)
  * [Text search](#text-search)
  * [Unsafe](#unsafe)
  * [Video](#video-1)
  * [Virtualization](#virtualization-1)
  * [Web programming](#web-programming)
- [Registries](#registries)
- [Resources](#resources)
- [License](#license)

<!-- tocstop -->

## Applications

See also [Rust — Production](https://www.rust-lang.org/production) organizations running Rust in production.

* [alacritty](https://github.com/alacritty/alacritty) <img src="https://img.shields.io/github/stars/alacritty/alacritty?style=social" alt="Stars" width="80"> — A cross-platform, GPU enhanced terminal emulator
* [Arti](https://gitlab.torproject.org/tpo/core/arti) — An implementation of Tor, in Rust. (So far, it's a not-very-complete client. But watch this space!) [![Crates.io](https://img.shields.io/crates/v/arti.svg)](https://crates.io/crates/arti)
* [asm-cli-rust](https://github.com/cch123/asm-cli-rust) — An interactive assembly shell written in rust.
* [cloudflare/boringtun](https://github.com/cloudflare/boringtun) <img src="https://img.shields.io/github/stars/cloudflare/boringtun?style=social" alt="Stars" width="80"> — A Userspace WireGuard VPN Implementation [![build badge](https://img.shields.io/badge/crates.io-v0.2.0-orange.svg)](https://crates.io/crates/boringtun)
* [datafusion](https://github.com/apache/arrow-datafusion) <img src="https://img.shields.io/github/stars/apache/arrow-datafusion?style=social" alt="Stars" width="80"> — Apache Arrow DataFusion and Ballista query engines
* [denoland/deno](https://github.com/denoland/deno) <img src="https://img.shields.io/github/stars/denoland/deno?style=social" alt="Stars" width="80"> — A secure JavaScript/TypeScript runtime built with V8, Rust, and Tokio [![Build Status](https://github.com/denoland/deno/workflows/ci/badge.svg?branch=master&event=push)](https://github.com/denoland/deno/actions)
* [doprz/dipc](https://github.com/doprz/dipc) <img src="https://img.shields.io/github/stars/doprz/dipc?style=social" alt="Stars" width="80"> — Convert your favorite images and wallpapers with your favorite color palettes/themes [![crates.io](https://img.shields.io/crates/v/dipc)](https://crates.io/crates/dipc)
* [Factotum](https://github.com/snowplow/factotum) <img src="https://img.shields.io/github/stars/snowplow/factotum?style=social" alt="Stars" width="80"> — A system to programmatically run data pipelines
* [fcsonline/drill](https://github.com/fcsonline/drill) <img src="https://img.shields.io/github/stars/fcsonline/drill?style=social" alt="Stars" width="80"> — A HTTP load testing application inspired by Ansible syntax
* [fend](https://github.com/printfn/fend) <img src="https://img.shields.io/github/stars/printfn/fend?style=social" alt="Stars" width="80"> - Arbitrary-precision unit-aware calculator [![build](https://github.com/printfn/fend/workflows/build/badge.svg)](https://github.com/printfn/fend)
* [Fractalide](https://github.com/fractalide/fractalide) <img src="https://img.shields.io/github/stars/fractalide/fractalide?style=social" alt="Stars" width="80"> — Simple Rust Microservices
* [habitat](https://github.com/habitat-sh/habitat) <img src="https://img.shields.io/github/stars/habitat-sh/habitat?style=social" alt="Stars" width="80"> — A tool created by Chef to build, deploy, and manage applications.
* [Herd](https://github.com/imjacobclark/Herd) <img src="https://img.shields.io/github/stars/imjacobclark/Herd?style=social" alt="Stars" width="80"> — an experimental HTTP load testing application
* [hickory-dns](https://crates.io/crates/trust-dns) — A DNS-server [![Build Status](https://github.com/hickory-dns/hickory-dns/workflows/test/badge.svg?branch=main)](https://github.com/hickory-dns/hickory-dns/actions?query=workflow%3Atest)
* [innernet](https://github.com/tonarino/innernet) <img src="https://img.shields.io/github/stars/tonarino/innernet?style=social" alt="Stars" width="80"> - An overlay or private mesh network that uses Wireguard under the hood
* [jedisct1/flowgger](https://github.com/awslabs/flowgger) <img src="https://img.shields.io/github/stars/awslabs/flowgger?style=social" alt="Stars" width="80"> — A fast, simple and lightweight data collector
* [kalker](https://github.com/PaddiM8/kalker) <img src="https://img.shields.io/github/stars/PaddiM8/kalker?style=social" alt="Stars" width="80"> - A scientific calculator that supports math-like syntax with user-defined variables, functions, derivation, integration, and complex numbers. Cross-platform + WASM support [![Build Status](https://github.com/PaddiM8/kalker/workflows/Release/badge.svg)](https://github.com/PaddiM8/kalker/actions)
* [kytan](https://github.com/changlan/kytan) <img src="https://img.shields.io/github/stars/changlan/kytan?style=social" alt="Stars" width="80"> — High Performance Peer-to-Peer VPN
* [linkerd/linkerd2-proxy](https://github.com/linkerd/linkerd2-proxy) — Ultralight service mesh for Kubernetes.
* [MaidSafe](https://github.com/maidsafe) — A decentralized platform.
* [mdBook](https://github.com/rust-lang/mdBook) <img src="https://img.shields.io/github/stars/rust-lang/mdBook?style=social" alt="Stars" width="80"> — A command line utility to create books from markdown files [![Build Status](https://github.com/rust-lang/mdBook/workflows/CI/badge.svg?branch=master)](https://github.com/rust-lang/mdBook/actions)
* [mirrord](https://github.com/metalbear-co/mirrord) <img src="https://img.shields.io/github/stars/metalbear-co/mirrord?style=social" alt="Stars" width="80"> — Connect your local process and your cloud environment, and run local code in cloud conditions
* [nicohman/eidolon](https://github.com/nicohman/eidolon) <img src="https://img.shields.io/github/stars/nicohman/eidolon?style=social" alt="Stars" width="80"> — A steam and drm-free game registry and launcher for linux and macosx
* [notty](https://github.com/withoutboats/notty) <img src="https://img.shields.io/github/stars/withoutboats/notty?style=social" alt="Stars" width="80"> — A new kind of terminal
* [Pijul](https://pijul.org) — A patch-based distributed version control system
* [Rauthy](https://github.com/sebadob/rauthy) <img src="https://img.shields.io/github/stars/sebadob/rauthy?style=social" alt="Stars" width="80"> — OpenID Connect Single Sign-On Identity & Access Management
* [Rio](https://github.com/raphamorim/rio) <img src="https://img.shields.io/github/stars/raphamorim/rio?style=social" alt="Stars" width="80"> - A hardware-accelerated GPU terminal emulator powered by WebGPU, focusing to run in desktops and browsers.
* [rx](https://github.com/cloudhead/rx) <img src="https://img.shields.io/github/stars/cloudhead/rx?style=social" alt="Stars" width="80"> — Vi inspired Modern Pixel Art Editor
* [Servo](https://github.com/servo/servo) <img src="https://img.shields.io/github/stars/servo/servo?style=social" alt="Stars" width="80"> — A prototype web browser engine
* [shoes](https://github.com/cfal/shoes) <img src="https://img.shields.io/github/stars/cfal/shoes?style=social" alt="Stars" width="80"> - A multi-protocol proxy server
* [shuttle](https://github.com/shuttle-hq/shuttle) <img src="https://img.shields.io/github/stars/shuttle-hq/shuttle?style=social" alt="Stars" width="80"> — A serverless platform built for Rust
* [Sniffnet](https://github.com/GyulyVGC/sniffnet) <img src="https://img.shields.io/github/stars/GyulyVGC/sniffnet?style=social" alt="Stars" width="80"> — Cross-platform application to monitor your network traffic with ease [![build badge](https://img.shields.io/github/actions/workflow/status/gyulyvgc/sniffnet/rust.yml?logo=github)](https://github.com/GyulyVGC/sniffnet/blob/main/.github/workflows/rust.yml) [![crate](https://img.shields.io/crates/v/sniffnet?logo=rust)](https://crates.io/crates/sniffnet)
* [SWC](https://github.com/swc-project/swc) <img src="https://img.shields.io/github/stars/swc-project/swc?style=social" alt="Stars" width="80"> — super-fast TypeScript / JavaScript compiler
* [tiny](https://github.com/osa1/tiny) <img src="https://img.shields.io/github/stars/osa1/tiny?style=social" alt="Stars" width="80"> — A terminal IRC client
* [UpVPN](https://github.com/upvpn/upvpn-app) <img src="https://img.shields.io/github/stars/upvpn/upvpn-app?style=social" alt="Stars" width="80">  — WireGuard VPN client for macOS, Linux, and Windows built on Tauri.
* [wasmer](https://github.com/wasmerio/wasmer) <img src="https://img.shields.io/github/stars/wasmerio/wasmer?style=social" alt="Stars" width="80"> — A safe and fast WebAssembly runtime supporting WASI and Emscripten [![Build Status](https://github.com/wasmerio/wasmer/workflows/build/badge.svg?style=flat-square)](https://github.com/wasmerio/wasmer/actions)
* [Weld](https://github.com/serayuzgur/weld) <img src="https://img.shields.io/github/stars/serayuzgur/weld?style=social" alt="Stars" width="80"> — Full fake REST API generator
* [wezterm](https://github.com/wez/wezterm) <img src="https://img.shields.io/github/stars/wez/wezterm?style=social" alt="Stars" width="80"> — A GPU-accelerated cross-platform terminal emulator and multiplexer
* [WinterJS](https://github.com/wasmerio/winterjs) <img src="https://img.shields.io/github/stars/wasmerio/winterjs?style=social" alt="Stars" width="80"> — A secure JavaScript runtime built with SpiderMonkey, Rust and Axum
* [zellij](https://github.com/zellij-org/zellij) <img src="https://img.shields.io/github/stars/zellij-org/zellij?style=social" alt="Stars" width="80"> — A terminal multiplexer (workspace) with batteries included

### Audio and Music

* [enginesound](https://github.com/DasEtwas/enginesound) <img src="https://img.shields.io/github/stars/DasEtwas/enginesound?style=social" alt="Stars" width="80"> — A GUI and command line application used to procedurally generate semi-realistic engine sounds. Featuring in-depth configuration, variable sample rate and a frequency analysis window.
* [Festival](https://github.com/hinto-janai/festival) <img src="https://img.shields.io/github/stars/hinto-janai/festival?style=social" alt="Stars" width="80"> — A local music player/server/client [![build-badge](https://github.com/hinto-janai/festival/actions/workflows/ci.yml/badge.svg)](https://github.com/hinto-janai/festival/actions/workflows/ci.yml)
* [figsoda/mmtc](https://github.com/figsoda/mmtc) <img src="https://img.shields.io/github/stars/figsoda/mmtc?style=social" alt="Stars" width="80"> [[mmtc](https://crates.io/crates/mmtc)] — Minimal mpd terminal client that aims to be simple yet highly configurable [![build-badge](https://github.com/figsoda/mmtc/actions/workflows/ci.yml/badge.svg)](https://github.com/figsoda/mmtc/actions/workflows/ci.yml)
* [Glicol](https://github.com/chaosprint/glicol) <img src="https://img.shields.io/github/stars/chaosprint/glicol?style=social" alt="Stars" width="80"> — Graph-oriented live coding language written in Rust for collaborative musicking in browsers.
* [ncspot](https://github.com/hrkfdn/ncspot) <img src="https://img.shields.io/github/stars/hrkfdn/ncspot?style=social" alt="Stars" width="80"> - Cross-platform ncurses Spotify client, inspired by ncmpc and the likes. [![build badge](https://github.com/hrkfdn/ncspot/workflows/Build/badge.svg)](https://github.com/hrkfdn/ncspot/actions?query=workflow%3ABuild)
* [Polaris](https://github.com/agersant/polaris) <img src="https://img.shields.io/github/stars/agersant/polaris?style=social" alt="Stars" width="80"> — A music streaming application.
* [Spotify Player](https://github.com/aome510/spotify-player) — A Spotify player in the terminal with full feature parity.
* [Spotifyd](https://github.com/Spotifyd/spotifyd) <img src="https://img.shields.io/github/stars/Spotifyd/spotifyd?style=social" alt="Stars" width="80"> — An open source Spotify client running as a UNIX daemon. ![Continuous Integration](https://github.com/Spotifyd/spotifyd/workflows/Continuous%20Integration/badge.svg?branch=master)
* [termusic](https://github.com/tramhao/termusic) <img src="https://img.shields.io/github/stars/tramhao/termusic?style=social" alt="Stars" width="80"> - Music Player TUI written in Rust
* [WhatBPM](https://github.com/sergree/whatbpm) <img src="https://img.shields.io/github/stars/sergree/whatbpm?style=social" alt="Stars" width="80"> — A daily statically generated information resource for electronic dance music producers. Provides daily analytics on the most frequently used values for each EDM genre: tempos, keys, root notes, and so on, using publicly available data such as Beatport and Spotify. ![Continuous Integration](https://github.com/sergree/whatbpm/actions/workflows/website_build_deploy.yml/badge.svg?branch=main)

### Cryptocurrencies

* [artemis](https://github.com/paradigmxyz/artemis) <img src="https://img.shields.io/github/stars/paradigmxyz/artemis?style=social" alt="Stars" width="80"> - A simple, modular, and fast framework for writing MEV bots in Rust.
* [beerus](https://github.com/eigerco/beerus) <img src="https://img.shields.io/github/stars/eigerco/beerus?style=social" alt="Stars" width="80"> - Beerus is a trustless StarkNet Light Client, ⚡blazing fast ⚡ and powered by Rust 🦀 [![GitHub Workflow Status](https://github.com/eigerco/beerus/actions/workflows/test.yml/badge.svg)](https://github.com/eigerco/beerus/actions/workflows/test.yml)
* [Bitcoin Satoshi's Vision](https://github.com/brentongunning/rust-sv) [[sv](https://crates.io/crates/sv)] — A Rust library for working with Bitcoin SV .
* [cairo](https://github.com/starkware-libs/cairo) <img src="https://img.shields.io/github/stars/starkware-libs/cairo?style=social" alt="Stars" width="80"> - Cairo is the first Turing-complete language for creating provable programs for general computation. This is also the native language of [StarkNet](https://www.starknet.io/en), a ZK-Rollup using STARK proofs ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/starkware-libs/cairo/CI?style=flat-square&logo=github)
* [cairo-vm](https://github.com/lambdaclass/cairo-vm) — Rust implementation of the Cairo VM [![rust](https://github.com/lambdaclass/cairo-vm/actions/workflows/rust.yml/badge.svg)](https://github.com/lambdaclass/cairo-vm/actions/workflows/rust.yml)
* [ChainX](https://github.com/chainx-org/ChainX) <img src="https://img.shields.io/github/stars/chainx-org/ChainX?style=social" alt="Stars" width="80"> — Fully Decentralized Interchain Crypto Asset Management on Polkadot.
* [CITA](https://github.com/citahub/cita) <img src="https://img.shields.io/github/stars/citahub/cita?style=social" alt="Stars" width="80"> — A high performance blockchain kernel for enterprise users.
* [coinbase-pro-rs](https://github.com/inv2004/coinbase-pro-rs) — Coinbase pro client in Rust, supports sync/async/websocket
* [Diem](https://github.com/diem/diem) <img src="https://img.shields.io/github/stars/diem/diem?style=social" alt="Stars" width="80"> — Diem’s mission is to enable a simple global currency and financial infrastructure that empowers billions of people.
* [electrumrs](https://github.com/romanz/electrs) <img src="https://img.shields.io/github/stars/romanz/electrs?style=social" alt="Stars" width="80"> — An efficient re-implementation of Electrum Server in Rust.
* [ethabi](https://github.com/rust-ethereum/ethabi) <img src="https://img.shields.io/github/stars/rust-ethereum/ethabi?style=social" alt="Stars" width="80"> - Encode and decode smart contract invocations.
* [ethaddrgen](https://github.com/Limeth/ethaddrgen) <img src="https://img.shields.io/github/stars/Limeth/ethaddrgen?style=social" alt="Stars" width="80"> — Custom Ethereum vanity address generator made in Rust
* [ethers-rs](https://github.com/gakonst/ethers-rs) - Complete Ethereum & Celo library and wallet implementation in Rust. ![Build Status](https://github.com/gakonst/ethers-rs/workflows/Tests/badge.svg)
* [etk](https://github.com/quilt/etk) <img src="https://img.shields.io/github/stars/quilt/etk?style=social" alt="Stars" width="80"> - etk is a collection of tools for writing, reading, and analyzing EVM bytecode.
* [Forest](https://github.com/ChainSafe/forest) <img src="https://img.shields.io/github/stars/ChainSafe/forest?style=social" alt="Stars" width="80"> - Rust Filecoin implementation [![Build Status](https://img.shields.io/circleci/build/gh/ChainSafe/forest/main?branch=master)](https://app.circleci.com/pipelines/github/ChainSafe/forest?branch=main)
* [Foundry](https://github.com/foundry-rs/foundry) <img src="https://img.shields.io/github/stars/foundry-rs/foundry?style=social" alt="Stars" width="80"> - Foundry is a blazing fast, portable and modular toolkit for Ethereum application development written in Rust. ![Build Status](https://img.shields.io/github/workflow/status/foundry-rs/foundry/test?style=flat-square)
* [Grin](https://github.com/mimblewimble/grin/) <img src="https://img.shields.io/github/stars/mimblewimble/grin?style=social" alt="Stars" width="80"> — Evolution of the MimbleWimble protocol
* [hdwallet](https://github.com/jjyr/hdwallet) <img src="https://img.shields.io/github/stars/jjyr/hdwallet?style=social" alt="Stars" width="80"> [[hdwallet](https://crates.io/crates/hdwallet)] — BIP-32 HD wallet related key derivation utilities.
* [Holochain](https://github.com/holochain/holochain) <img src="https://img.shields.io/github/stars/holochain/holochain?style=social" alt="Stars" width="80"> — Scalable P2P alternative to blockchain for all those distributed apps you always wanted to build. [![detect critical check failures](https://github.com/holochain/holochain/actions/workflows/check_run_detect_release_pr_failure.yml/badge.svg)](https://github.com/holochain/holochain/actions/workflows/check_run_detect_release_pr_failure.yml)
* [ibc-rs](https://github.com/informalsystems/hermes) - Rust implementation of the [Interblockchain Communication](https://ibc.cosmos.network/) protocol
* [infincia/bip39-rs](https://github.com/infincia/bip39-rs) [[bip39](https://crates.io/crates/bip39)] — Rust implementation of BIP39.
* [interBTC](https://github.com/interlay/interbtc) <img src="https://img.shields.io/github/stars/interlay/interbtc?style=social" alt="Stars" width="80"> — Trustless and fully decentralized Bitcoin bridge to Polkadot and Kusama.
* [Joystream](https://github.com/Joystream/joystream) <img src="https://img.shields.io/github/stars/Joystream/joystream?style=social" alt="Stars" width="80"> — A user governed video platform
* [Lighthouse](https://github.com/sigp/lighthouse) <img src="https://img.shields.io/github/stars/sigp/lighthouse?style=social" alt="Stars" width="80"> — Rust Ethereum Consensus Layer (CL) Client [![Build Status](https://github.com/sigp/lighthouse/workflows/test-suite/badge.svg?branch=master)](https://github.com/sigp/lighthouse/actions)
* [madara](https://github.com/keep-starknet-strange/madara) <img src="https://img.shields.io/github/stars/keep-starknet-strange/madara?style=social" alt="Stars" width="80"> - Kaioshin is a ⚡ blazing fast ⚡ Starknet sequencer, based on substrate and written in Rust 🦀. [![GitHub Workflow Status](https://github.com/keep-starknet-strange/madara/actions/workflows/test.yml/badge.svg)](https://github.com/keep-starknet-strange/madara/actions/workflows/test.yml)
* [mev-inspect-rs](https://github.com/flashbots/mev-inspect-rs) - Ethereum MEV Inspector in Rust
* [near/nearcore](https://github.com/near/nearcore) <img src="https://img.shields.io/github/stars/near/nearcore?style=social" alt="Stars" width="80"> — decentralized smart-contract platform for low-end mobile devices.
* [Nervos CKB](https://github.com/nervosnetwork/ckb) — Nervos CKB is a public permissionless blockchain, the common knowledge layer of Nervos network.
* [Nimiq](https://github.com/nimiq/core-rs) <img src="https://img.shields.io/github/stars/nimiq/core-rs?style=social" alt="Stars" width="80"> — Rust implementation of Nimiq node
* [opensea-rs](https://github.com/gakonst/opensea-rs) - Rust bindings & CLI to the Opensea API and Contracts.
* [Parity-Bitcoin](https://github.com/paritytech/parity-bitcoin) — The Parity Bitcoin client
* [Phala-Network/phala-blockchain](https://github.com/Phala-Network/phala-blockchain) — Confidential smart contract blockchain based on Intel SGX and Substrate
* [polkadot-sdk](https://github.com/paritytech/polkadot-sdk) — The Parity Polkadot Blockchain SDK
* [revm](https://github.com/bluealloy/revm) <img src="https://img.shields.io/github/stars/bluealloy/revm?style=social" alt="Stars" width="80"> - Revolutionary Machine (revm) is a fast Ethereum virtual machine written in rust.
* [rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin) — Library with support for de/serialization, parsing and executing on data structures and network messages related to Bitcoin.
* [rust-lightning](https://github.com/lightningdevkit/rust-lightning) [![Crate](https://img.shields.io/crates/v/lightning.svg?logo=rust)](https://crates.io/crates/lightning) — Bitcoin Lightning library written in Rust. The main crate,`lightning`, does not handle networking, persistence, or any other I/O. Thus,it is runtime-agnostic, but users must implement basic networking logic, chain interactions, and disk storage.po on linking crate.
* [sigma-rust](https://github.com/ergoplatform/sigma-rust) — Rust implementation of ErgoTree interpreter and wallet-related features.
* [Solana](https://github.com/solana-labs/solana) <img src="https://img.shields.io/github/stars/solana-labs/solana?style=social" alt="Stars" width="80"> — Incredibly fast, highly scalable blockchain using Proof-of-History.
* [Substrate](https://github.com/paritytech/substrate) <img src="https://img.shields.io/github/stars/paritytech/substrate?style=social" alt="Stars" width="80"> — Generic modular blockchain template written in Rust
* [Sui](https://github.com/MystenLabs/sui) <img src="https://img.shields.io/github/stars/MystenLabs/sui?style=social" alt="Stars" width="80"> — A next-generation smart contract platform with high throughput, low latency, and an asset-oriented programming model powered by the Move programming language.
* [svm-rs](https://github.com/alloy-rs/svm-rs) - Solidity-Compiler Version Manager.
* [tendermint-rs](https://github.com/informalsystems/tendermint-rs) - Rust implementation of Tendermint blockchain data structures and clients
* [wagyu](https://github.com/howardwu/wagyu) <img src="https://img.shields.io/github/stars/howardwu/wagyu?style=social" alt="Stars" width="80"> [[wagyu](https://crates.io/crates/wagyu)] — Rust library for generating cryptocurrency wallets
* [zcash](https://github.com/zcash/zcash) <img src="https://img.shields.io/github/stars/zcash/zcash?style=social" alt="Stars" width="80"> — Zcash is an implementation of the "Zerocash" protocol.

### Database

* [Atomic-Server](https://github.com/atomicdata-dev/atomic-server/) [[atomic-server](https://crates.io/crates/atomic_server)] - NoSQL graph database with realtime updates, dynamic indexing and easy-to-use GUI for CMS purposes. [![Release](https://github.com/atomicdata-dev/atomic-server/actions/workflows/docker.yml/badge.svg)](https://github.com/atomicdata-dev/atomic-server/actions/workflows/docker.yml)
* [CozoDB](https://github.com/cozodb/cozo) <img src="https://img.shields.io/github/stars/cozodb/cozo?style=social" alt="Stars" width="80"> - A transactional, relational database that uses Datalog and focuses on graph data and algorithms. Time-travel-capable, and fast! [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/cozodb/cozo/build.yml?branch=main)](https://github.com/cozodb/cozo/actions/workflows/build.yml)
* [darkbird](https://github.com/Rustixir/darkbird) <img src="https://img.shields.io/github/stars/Rustixir/darkbird?style=social" alt="Stars" width="80"> [[darkbird](https://crates.io/crates/darkbird)] - HighConcurrency, RealTime, InMemory storage inspired by erlang mnesia
* [Databend](https://github.com/datafuselabs/databend) <img src="https://img.shields.io/github/stars/datafuselabs/databend?style=social" alt="Stars" width="80"> - A Modern Real-Time Data Processing & Analytics DBMS with Cloud-Native Architecture [![Release](https://github.com/datafuselabs/databend/actions/workflows/databend-release.yml/badge.svg)](https://github.com/datafuselabs/databend/actions/workflows/databend-release.yml)
* [DB3 Network](https://github.com/dbpunk-labs/db3) — DB3 is a community-driven blockchain layer2 decentralized database network ![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/dbpunk-labs/db3/ci.yml?branch=main&style=flat-square)
* [erikgrinaker/toydb](https://github.com/erikgrinaker/toydb) <img src="https://img.shields.io/github/stars/erikgrinaker/toydb?style=social" alt="Stars" width="80"> — Distributed SQL database in Rust, written as a learning project.
* [Garage](https://github.com/deuxfleurs-org/garage) <img src="https://img.shields.io/github/stars/deuxfleurs-org/garage?style=social" alt="Stars" width="80"> [[garage](https://crates.io/crates/garage)] — S3-compatible distributed object storage service designed for self-hosting at a small-to-medium scale. [![Build Status](https://drone.deuxfleurs.fr/api/badges/Deuxfleurs/garage/status.svg?ref=refs/heads/main)](https://drone.deuxfleurs.fr/Deuxfleurs/garage)
* [GreptimeDB](https://github.com/grepTimeTeam/greptimedb/) <img src="https://img.shields.io/github/stars/grepTimeTeam/greptimedb?style=social" alt="Stars" width="80"> - An open-source, cloud-native, distributed time-series database with PromQL/SQL/Python supported.[![CI](https://github.com/greptimeTeam/greptimedb/actions/workflows/develop.yml/badge.svg)](https://github.com/greptimeTeam/greptimedb/actions/workflows/develop.yml)
* [indradb](https://crates.io/crates/indradb) — Rust based graph database
* [Lucid](https://github.com/lucid-kv/lucid) <img src="https://img.shields.io/github/stars/lucid-kv/lucid?style=social" alt="Stars" width="80"> — High performance and distributed KV store accessible through a HTTP API. [![Build Status](https://github.com/lucid-kv/lucid/workflows/Lucid/badge.svg?branch=master)](https://github.com/lucid-kv/lucid/actions?workflow=Lucid)
* [Materialize](https://github.com/MaterializeInc/materialize) <img src="https://img.shields.io/github/stars/MaterializeInc/materialize?style=social" alt="Stars" width="80"> - Streaming SQL database powered by Timely Dataflow :heavy_dollar_sign: [![Build status](https://badge.buildkite.com/97d6604e015bf633d1c2a12d166bb46f3b43a927d3952c999a.svg?branch=main)](https://buildkite.com/materialize/tests)
* [Neon](https://github.com/neondatabase/neon) <img src="https://img.shields.io/github/stars/neondatabase/neon?style=social" alt="Stars" width="80"> Serverless Postgres. We separated storage and compute to offer autoscaling, branching, and bottomless storage.
* [noria](https://github.com/mit-pdos/noria) <img src="https://img.shields.io/github/stars/mit-pdos/noria?style=social" alt="Stars" width="80"> [[noria](https://crates.io/crates/noria)] — Dynamically changing, partially-stateful data-flow for web application backends
* [ParityDB](https://github.com/paritytech/parity-db) <img src="https://img.shields.io/github/stars/paritytech/parity-db?style=social" alt="Stars" width="80"> — Fast and reliable database, optimised for read operation
* [PumpkinDB](https://github.com/PumpkinDB/PumpkinDB) <img src="https://img.shields.io/github/stars/PumpkinDB/PumpkinDB?style=social" alt="Stars" width="80"> — an event sourcing database engine
* [Qdrant](https://github.com/qdrant/qdrant) <img src="https://img.shields.io/github/stars/qdrant/qdrant?style=social" alt="Stars" width="80"> - An open source vector similarity search engine with extended filtering support [![Tests](https://github.com/qdrant/qdrant/workflows/Tests/badge.svg)](https://github.com/qdrant/qdrant/actions)
* [Qrlew/qrlew](https://github.com/Qrlew/qrlew) <img src="https://img.shields.io/github/stars/Qrlew/qrlew?style=social" alt="Stars" width="80"> [[qrlew](https://crates.io/crates/qrlew)] - The SQL-to-SQL Differential Privacy layer [![Qrlew](https://github.com/Qrlew/qrlew/actions/workflows/ci.yml/badge.svg)](https://github.com/Qrlew/qrlew/actions) ![Crates.io Version](https://img.shields.io/crates/v/qrlew?logo=Rust)
* [RisingWaveLabs/RisingWave](https://github.com/RisingWaveLabs/risingwave) <img src="https://img.shields.io/github/stars/RisingWaveLabs/risingwave?style=social" alt="Stars" width="80"> - the next-generation streaming database in the cloud [![CI](https://github.com/RisingWaveLabs/risingwave/actions/workflows/main.yml/badge.svg)](https://github.com/RisingWaveLabs/risingwave/actions/workflows/main.yml/badge.svg?branch=main)
* [seppo0010/rsedis](https://github.com/seppo0010/rsedis) <img src="https://img.shields.io/github/stars/seppo0010/rsedis?style=social" alt="Stars" width="80"> — A Redis reimplementation in Rust
* [Skytable](https://github.com/skytable/skytable) <img src="https://img.shields.io/github/stars/skytable/skytable?style=social" alt="Stars" width="80"> — A multi-model NoSQL database ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/skytable/skytable/Tests?style=flat-square)
* [sled](https://crates.io/crates/sled) — A (beta) modern embedded database [![Build Status](https://github.com/spacejam/sled/workflows/Rust/badge.svg?branch=master)](https://github.com/spacejam/sled/actions?workflow=Rust)
* [SQLSync](https://github.com/orbitinghail/sqlsync) <img src="https://img.shields.io/github/stars/orbitinghail/sqlsync?style=social" alt="Stars" width="80"> — Multiplayer offline-first SQLite [![GitHub Workflow Status](https://github.com/orbitinghail/sqlsync/actions/workflows/actions.yaml/badge.svg?branch=main)](https://github.com/orbitinghail/sqlsync/actions?query=branch%3Amain)
* [SurrealDB](https://github.com/surrealdb/surrealdb) <img src="https://img.shields.io/github/stars/surrealdb/surrealdb?style=social" alt="Stars" width="80"> — A scalable, distributed, document-graph database [![Build Status](https://img.shields.io/github/workflow/status/surrealdb/surrealdb/Continuous%20integration/main)](https://github.com/surrealdb/surrealdb/actions)
* [TerminusDB](https://github.com/terminusdb/terminusdb-store) <img src="https://img.shields.io/github/stars/terminusdb/terminusdb-store?style=social" alt="Stars" width="80"> - open source graph database and document store [![Build Status](https://github.com/terminusdb/terminusdb-store/workflows/Build/badge.svg?branch=master)](https://github.com/terminusdb/terminusdb-store/actions)
* [tikv](https://github.com/tikv/tikv) <img src="https://img.shields.io/github/stars/tikv/tikv?style=social" alt="Stars" width="80"> — A distributed KV database in Rust [![Build Status](https://ci.pingcap.net/job/tikv_ghpr_test/badge/icon)](https://ci.pingcap.net/job/tikv_ghpr_test/)
* [vorot93/libmdbx-rs](https://github.com/vorot93/libmdbx-rs) [[mdbx-sys](https://crates.io/crates/mdbx-sys)] — Rust bindings for MDBX, a "fast, compact, powerful, embedded, transactional key-value database, with permissive license". This is a fork of mozilla/lmdb-rs with patches to make it work with libmdbx.
* [WooriDB](https://github.com/naomijub/wooridb) <img src="https://img.shields.io/github/stars/naomijub/wooridb?style=social" alt="Stars" width="80"> - General purpose time serial database inspired by Crux and Datomic.

### Emulators

See also [crates matching keyword 'emulator'](https://crates.io/keywords/emulator).

* CHIP-8
  * [ColinEberhardt/wasm-rust-chip8](https://github.com/ColinEberhardt/wasm-rust-chip8) — A WebAssembly CHIP-8 emulator written with Rust
  * [starrhorne/chip8-rust](https://github.com/starrhorne/chip8-rust) — Yet another rust chip8 emulator
* Commodore 64
  * [kondrak/rust64](https://github.com/kondrak/rust64) <img src="https://img.shields.io/github/stars/kondrak/rust64?style=social" alt="Stars" width="80"> —
* Flash Player
  * [Ruffle](https://github.com/ruffle-rs/ruffle) <img src="https://img.shields.io/github/stars/ruffle-rs/ruffle?style=social" alt="Stars" width="80"> — Ruffle is an Adobe Flash Player emulator written in the Rust programming language. Ruffle targets both the desktop and the web using WebAssembly. [![CI](https://github.com/ruffle-rs/ruffle/actions/workflows/test_rust.yml/badge.svg)](https://github.com/ruffle-rs/ruffle/actions/workflows/test_rust.yml)[![CI](https://github.com/ruffle-rs/ruffle/actions/workflows/test_web.yml/badge.svg)](https://github.com/ruffle-rs/ruffle/actions/workflows/test_web.yml)
* Gameboy
  * [Gekkio/mooneye-gb](https://github.com/Gekkio/mooneye-gb) —
  * [joamag/boytacean](https://github.com/joamag/boytacean) <img src="https://img.shields.io/github/stars/joamag/boytacean?style=social" alt="Stars" width="80"> — GameBoy Color emulator written in Rust that runs on the Web using WebAssembly.
  * [mohanson/gameboy](https://github.com/mohanson/gameboy) <img src="https://img.shields.io/github/stars/mohanson/gameboy?style=social" alt="Stars" width="80"> — Full featured Cross-platform GameBoy emulator. Forever boys!.
  * [mvdnes/rboy](https://github.com/mvdnes/rboy) <img src="https://img.shields.io/github/stars/mvdnes/rboy?style=social" alt="Stars" width="80"> —
* Gameboy Advance
  * [michelhe/rustboyadvance-ng](https://github.com/michelhe/rustboyadvance-ng) - RustboyAdvance-ng is a Gameboy Advance emulator with desktop, android and [WebAssembly](https://michelhe.github.io/rustboyadvance-ng/) support. [![build badge](https://github.com/michelhe/rustboyadvance-ng/workflows/Deploy/badge.svg?branch=master)](https://github.com/michelhe/rustboyadvance-ng/actions?query=workflow%3ADeploy)
* GameMaker
  * [OpenGMK](https://github.com/OpenGMK/OpenGMK) <img src="https://img.shields.io/github/stars/OpenGMK/OpenGMK?style=social" alt="Stars" width="80"> — OpenGMK is a modern rewrite of the proprietary GameMaker Classic engines, providing a full sourceport of the runner, a decompiler, a TASing framework, and libraries for working with gamedata yourself.
* Intel 8080 CPU
  * [mohanson/i8080](https://github.com/mohanson/i8080) <img src="https://img.shields.io/github/stars/mohanson/i8080?style=social" alt="Stars" width="80"> — Intel 8080 cpu emulator by Rust
* iOS
  * [touchHLE](https://github.com/hikari-no-yume/touchHLE) <img src="https://img.shields.io/github/stars/hikari-no-yume/touchHLE?style=social" alt="Stars" width="80"> — High-level emulator for iPhone OS apps
* iPod
  * [clicky](https://github.com/daniel5151/clicky) <img src="https://img.shields.io/github/stars/daniel5151/clicky?style=social" alt="Stars" width="80"> — A clickwheel iPod emulator (WIP)
* NES
  * [koute/pinky](https://github.com/koute/pinky) <img src="https://img.shields.io/github/stars/koute/pinky?style=social" alt="Stars" width="80"> —
  * [pcwalton/sprocketnes](https://github.com/pcwalton/sprocketnes) <img src="https://img.shields.io/github/stars/pcwalton/sprocketnes?style=social" alt="Stars" width="80">
* Nintendo DS
  * [dust](https://github.com/kelpsyberry/dust) <img src="https://img.shields.io/github/stars/kelpsyberry/dust?style=social" alt="Stars" width="80"> — A Nintendo DS emulator written in Rust
* PlayStation 4
  * [Obliteration](https://github.com/obhq/obliteration) <img src="https://img.shields.io/github/stars/obhq/obliteration?style=social" alt="Stars" width="80"> — Experimental PS4 emulator written in Rust for Windows, macOS and Linux [![CI](https://github.com/obhq/obliteration/actions/workflows/main.yml/badge.svg)](https://github.com/obhq/obliteration/actions/workflows/main.yml)
* ZX Spectrum
  * [rustzx/rustzx](https://github.com/rustzx/rustzx) <img src="https://img.shields.io/github/stars/rustzx/rustzx?style=social" alt="Stars" width="80"> — [![RustZX CI](https://github.com/rustzx/rustzx/actions/workflows/ci.yml/badge.svg)](https://github.com/rustzx/rustzx/actions/workflows/ci.yml)

### File manager

* [broot](https://github.com/Canop/broot) <img src="https://img.shields.io/github/stars/Canop/broot?style=social" alt="Stars" width="80"> - A new way to see and navigate directory trees (get an overview of a directory, even a big one; find a directory then `cd` to it; never lose track of file hierarchy while you search; manipulate your files, ...), further reading [dystroy.org/broot](https://dystroy.org/broot/) [![Latest Version](https://img.shields.io/crates/v/broot.svg)](https://crates.io/crates/broot)
* [joshuto](https://github.com/kamiyaa/joshuto) <img src="https://img.shields.io/github/stars/kamiyaa/joshuto?style=social" alt="Stars" width="80"> - ranger-like terminal file manager written in Rust
* [xplr](https://github.com/sayanarijit/xplr) <img src="https://img.shields.io/github/stars/sayanarijit/xplr?style=social" alt="Stars" width="80"> - A hackable, minimal, fast TUI file explorer
* [yazi](https://github.com/sxyazi/yazi) <img src="https://img.shields.io/github/stars/sxyazi/yazi?style=social" alt="Stars" width="80"> - Blazing fast terminal file manager written in Rust, based on async I/O.

### Games

See also [Games Made With Piston](https://github.com/PistonDevelopers/piston/wiki/Games-Made-With-Piston).

* [chess-tui](https://github.com/thomas-mauran/chess-tui) —  A Chess TUI implementation in rust ♟️
* [citybound](https://github.com/citybound/citybound) <img src="https://img.shields.io/github/stars/citybound/citybound?style=social" alt="Stars" width="80"> — The city sim you deserve
* [cristicbz/rust-doom](https://github.com/cristicbz/rust-doom) — A renderer for Doom, may progress to being a playable game
* [doukutsu-rs](https://github.com/doukutsu-rs/doukutsu-rs) — A Rust reimplementation of Cave Story engine with some enhancements.
* [garkimasera/rusted-ruins](https://github.com/garkimasera/rusted-ruins) — Extensible open world rogue like game with pixel art
* [gorilla-devs/ferium](https://github.com/gorilla-devs/ferium) — Ferium is a fast and feature rich CLI program for downloading and updating Minecraft mods from Modrinth, CurseForge, and GitHub Releases, and modpacks from Modrinth and CurseForge ![ferium build](https://github.com/gorilla-devs/ferium/actions/workflows/build.yml/badge.svg?branch=main)
* [lifthrasiir/angolmois-rust](https://github.com/lifthrasiir/angolmois-rust) — A minimalistic music video game which supports the BMS format
* [maras-archive/rsnake](https://github.com/maras-archive/rsnake) — Snake written in Rust.
* [mtkennerly/ludusavi](https://github.com/mtkennerly/ludusavi) <img src="https://img.shields.io/github/stars/mtkennerly/ludusavi?style=social" alt="Stars" width="80"> — Backup tool for PC game saves [![build badge](https://img.shields.io/github/actions/workflow/status/mtkennerly/ludusavi/main.yaml?logo=github)](https://github.com/mtkennerly/ludusavi/actions/workflows/main.yaml) [![crate](https://img.shields.io/crates/v/ludusavi?logo=rust)](https://crates.io/crates/ludusavi)
* [ozkriff/zemeroth](https://github.com/ozkriff/zemeroth) <img src="https://img.shields.io/github/stars/ozkriff/zemeroth?style=social" alt="Stars" width="80"> — A small 2D turn-based hexagonal strategy game
* [rhex](https://github.com/dpc/rhex) <img src="https://img.shields.io/github/stars/dpc/rhex?style=social" alt="Stars" width="80"> — hexagonal ascii roguelike
* [rsaarelm/magog](https://github.com/rsaarelm/magog) <img src="https://img.shields.io/github/stars/rsaarelm/magog?style=social" alt="Stars" width="80"> — A roguelike game in Rust
* [SoftbearStudios/mk48](https://github.com/SoftbearStudios/mk48) <img src="https://img.shields.io/github/stars/SoftbearStudios/mk48?style=social" alt="Stars" width="80"> — Mk48.io is an online multiplayer naval combat game
* [swatteau/sokoban-rs](https://github.com/swatteau/sokoban-rs) — A Sokoban implementation
* [thetawavegame/thetawave-legacy](https://github.com/thetawavegame/thetawave-legacy) - A space shooter game that strives to be an entry point for new game developers to make their first contributions. ![build badge](https://github.com/thetawavegame/thetawave-legacy/actions/workflows/ci.yml/badge.svg?branch=master)
* [Thinkofname/rust-quake](https://github.com/Thinkofname/rust-quake) — Quake map renderer in Rust
* [ttyperacer/terminal-typeracer](https://gitlab.com/ttyperacer/terminal-typeracer) - Single player typing test game written for the terminal
* [Veloren](https://gitlab.com/veloren/veloren) — An open world, open source multiplayer voxel RPG game currently in alpha development [![build badge](https://gitlab.com/veloren/veloren/badges/master/pipeline.svg)](https://gitlab.com/veloren/veloren/-/pipelines)
* [Zone of Control](https://github.com/ozkriff/zoc) — A turn-based hexagonal strategy game

### Graphics

* [dps/rust-raytracer](https://github.com/dps/rust-raytracer) - An implementation of a very simple raytracer based on Ray Tracing in One Weekend by Peter Shirley in Rust.
* [flxzt/rnote](https://github.com/flxzt/rnote) <img src="https://img.shields.io/github/stars/flxzt/rnote?style=social" alt="Stars" width="80"> - Sketch and take handwritten notes.
* [ivanceras/svgbob](https://github.com/ivanceras/svgbob) <img src="https://img.shields.io/github/stars/ivanceras/svgbob?style=social" alt="Stars" width="80"> — converts ASCII diagrams into SVG graphics
* [KaminariOS/rustracer](https://github.com/KaminariOS/rustracer) <img src="https://img.shields.io/github/stars/KaminariOS/rustracer?style=social" alt="Stars" width="80"> — A PBR glTF 2.0 renderer based on Vulkan ray-tracing, written in Rust.
* [Limeth/euclider](https://github.com/Limeth/euclider) <img src="https://img.shields.io/github/stars/Limeth/euclider?style=social" alt="Stars" width="80"> — A real-time 4D CPU ray tracer
* [RazrFalcon/resvg](https://github.com/RazrFalcon/resvg) <img src="https://img.shields.io/github/stars/RazrFalcon/resvg?style=social" alt="Stars" width="80"> — An SVG rendering library.
* [rodrigorc/papercraft](https://github.com/rodrigorc/papercraft) <img src="https://img.shields.io/github/stars/rodrigorc/papercraft?style=social" alt="Stars" width="80"> - A tool to unwrap 3D models and create them in paper with scissors and glue.
* [rustq/vue-skia](https://github.com/rustq/vue-skia) — Skia based 2d graphics vue rendering library. It is based on Rust to implement software rasterization to perform rendering.
* [turnage/valora](https://crates.io/crates/valora) — A library for generative fine art ![Rust](https://github.com/turnage/valora/workflows/Rust/badge.svg?branch=master)
* [Twinklebear/tray_rust](https://github.com/Twinklebear/tray_rust) <img src="https://img.shields.io/github/stars/Twinklebear/tray_rust?style=social" alt="Stars" width="80"> — A ray tracer
* [wahn/rs_pbrt](https://github.com/wahn/rs_pbrt) <img src="https://img.shields.io/github/stars/wahn/rs_pbrt?style=social" alt="Stars" width="80"> — Rust crate to implement a counterpart to the PBRT book's (3rd edition) C++ code.

### Image processing

* [Imager](https://github.com/imager-io/imager) <img src="https://img.shields.io/github/stars/imager-io/imager?style=social" alt="Stars" width="80"> — Automated image optimization.
* [shssoichiro/oxipng](https://github.com/shssoichiro/oxipng) <img src="https://img.shields.io/github/stars/shssoichiro/oxipng?style=social" alt="Stars" width="80"> [[oxipng](https://crates.io/crates/oxipng)] — Multithreaded PNG optimizer written in Rust. [![Build Status](https://github.com/shssoichiro/oxipng/workflows/oxipng/badge.svg)](https://github.com/shssoichiro/oxipng/actions?query=branch%3Amaster) [![Version](https://img.shields.io/crates/v/oxipng.svg)](https://crates.io/crates/oxipng)

### Industrial automation

* [locka99/opcua](https://github.com/locka99/opcua) <img src="https://img.shields.io/github/stars/locka99/opcua?style=social" alt="Stars" width="80"> — A pure rust [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/) library.
* [slowtec/tokio-modbus](https://github.com/slowtec/tokio-modbus) — A [tokio](https://tokio.rs)-based [modbus](https://modbus.org) library.

### Observability

* [avito-tech/bioyino](https://github.com/avito-tech/bioyino) — A high-performance scalable StatsD compatible server.
* [openobserve](https://github.com/openobserve/openobserve) <img src="https://img.shields.io/github/stars/openobserve/openobserve?style=social" alt="Stars" width="80"> - 10x easier, 140x lower storage cost, high performance, petabyte scale - Elasticsearch/Splunk/Datadog alternative.
* [OpenTelemetry](https://crates.io/crates/opentelemetry) — OpenTelemetry provides a single set of APIs, libraries, agents, and collector services to capture distributed traces and metrics from your application. You can analyze them using Prometheus, Jaeger, and other observability tools. [![GitHub Actions CI](https://github.com/open-telemetry/opentelemetry-rust/workflows/CI/badge.svg?branch=master)](https://github.com/open-telemetry/opentelemetry-rust/actions?query=workflow%3ACI+branch%3Amaster)
* [Quickwit-oss/quickwit](https://github.com/quickwit-oss/quickwit) - Cloud-native and highly cost-efficient search engine for log management. [![CI](https://github.com/quickwit-oss/quickwit/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/quickwit-oss/quickwit/actions?query=workflow%3ACI)
* [Scaphandre](https://github.com/hubblo-org/scaphandre) <img src="https://img.shields.io/github/stars/hubblo-org/scaphandre?style=social" alt="Stars" width="80"> - A power consumption monitoring agent, to track host and each service power consumption and enable designing systems and applications for more sustainability. Designed to fit any monitoring toolchain (already supports prometheus, warp10, riemann...).
* [vectordotdev/vector](https://github.com/vectordotdev/vector) <img src="https://img.shields.io/github/stars/vectordotdev/vector?style=social" alt="Stars" width="80"> — A High-Performance, Logs, Metrics, & Events Router.

### Operating systems

See also [A comparison of operating systems written in Rust](https://github.com/flosse/rust-os-comparison).
* [0x59616e/SteinsOS](https://github.com/0x59616e/SteinsOS) <img src="https://img.shields.io/github/stars/0x59616e/SteinsOS?style=social" alt="Stars" width="80">  — An OS for armv8-a architecture.
* [Andy-Python-Programmer/aero](https://github.com/Andy-Python-Programmer/aero) — A modern, unix-like operating system following the monolithic kernel design.
* [DragonOS-Community/DragonOS](https://github.com/DragonOS-Community/DragonOS) — An operating system with a self-developed kernel using Rust from scratch and Linux compatibility.
* [redox-os/redox](https://gitlab.redox-os.org/redox-os/redox) —
* [thepowersgang/rust_os](https://github.com/thepowersgang/rust_os) <img src="https://img.shields.io/github/stars/thepowersgang/rust_os?style=social" alt="Stars" width="80"> —
* [theseus-os/Theseus](https://github.com/theseus-os/Theseus) — A safe-language, single address space and single privilege level OS written from scratch in pure Rust - [![build badge](https://img.shields.io/github/workflow/status/theseus-os/Theseus/Documentation?label=docs%20build)](https://www.theseus-os.com/Theseus/book/index.html)
* [tock/tock](https://github.com/tock/tock) <img src="https://img.shields.io/github/stars/tock/tock?style=social" alt="Stars" width="80"> — A secure embedded operating system for Cortex-M based microcontrollers

### Package Managers

* [helsing-ai/buffrs](https://github.com/helsing-ai/buffrs) [[buffrs](https://crates.io/crates/buffrs)] — A modern package manager for protocol buffers and gRPC architectures.

### Payments

* [hyperswitch](https://github.com/juspay/hyperswitch) <img src="https://img.shields.io/github/stars/juspay/hyperswitch?style=social" alt="Stars" width="80"> — An open source payments orchestrator that lets you connect with multiple payment processors and route payment traffic effortlessly, all with a single API integration ![GitHub last commit](https://img.shields.io/github/last-commit/juspay/hyperswitch?style=flat-square)

### Productivity

* [ast-grep](https://github.com/ast-grep/ast-grep) - A CLI tool for code structural search, lint and rewriting. Written in Rust.
* [Bartib](https://github.com/nikolassv/bartib) <img src="https://img.shields.io/github/stars/nikolassv/bartib?style=social" alt="Stars" width="80"> [[Bartib](https://crates.io/crates/bartib)] - A simple timetracker for the command line [![Tests](https://github.com/nikolassv/bartib/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/nikolassv/bartib/actions/workflows/test.yml)
* [espanso](https://github.com/espanso/espanso) <img src="https://img.shields.io/github/stars/espanso/espanso?style=social" alt="Stars" width="80"> — A cross-platform Text Expander written in Rust[![CI](https://github.com/espanso/espanso/actions/workflows/ci.yml/badge.svg?branch=dev&event=push)](https://github.com/espanso/espanso/actions/workflows/ci.yml)
* [eureka](https://crates.io/crates/eureka) — A CLI tool to input and store your ideas without leaving the terminal
* [Furtherance](https://github.com/lakoliu/Furtherance) <img src="https://img.shields.io/github/stars/lakoliu/Furtherance?style=social" alt="Stars" width="80"> - Time tracking app built with Rust and GTK4
* [illacloud/illa](https://github.com/illacloud/illa) <img src="https://img.shields.io/github/stars/illacloud/illa?style=social" alt="Stars" width="80"> [[ILLA Cloud](https://www.illacloud.com/)] - Low-code internal tool builder written with Rust.
* [LLDAP](https://github.com/lldap/lldap) <img src="https://img.shields.io/github/stars/lldap/lldap?style=social" alt="Stars" width="80"> - Simplified LDAP interface for authentication.
* [pier-cli/pier](https://github.com/pier-cli/pier) — A central repository to manage (add, search metadata, etc.) all your one-liners, scripts, tools, and CLIs

### Routing protocols

* [Holo](https://github.com/holo-routing/holo) <img src="https://img.shields.io/github/stars/holo-routing/holo?style=social" alt="Stars" width="80"> - Holo is a suite of routing protocols designed to support high-scale and automation-driven networks
* [RustyBGP](https://github.com/osrg/rustybgp) <img src="https://img.shields.io/github/stars/osrg/rustybgp?style=social" alt="Stars" width="80"> - BGP implemented in the Rust Programming Language

### Security tools

* [AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) <img src="https://img.shields.io/github/stars/AFLplusplus/LibAFL?style=social" alt="Stars" width="80"> - Advanced Fuzzing Library - Slot your Fuzzer together in Rust! Scales across cores and machines. For Windows, Android, MacOS, Linux, no_std, etc. [![build and test](https://github.com/AFLplusplus/LibAFL/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/AFLplusplus/LibAFL/actions/workflows/build_and_test.yml)
* [arp-scan-rs](https://github.com/kongbytes/arp-scan-rs) - A minimalistic ARP scan tool for fast local network scans
* [cargo-audit](https://crates.io/crates/cargo-audit) - Audit Cargo.lock for crates with security vulnerabilities
* [cargo-auditable](https://crates.io/crates/cargo-auditable) - Make production Rust binaries auditable
* [cargo-crev](https://crates.io/crates/cargo-crev) - A cryptographically verifiable code review system for the cargo (Rust) package manager.
* [cargo-deny](https://crates.io/crates/cargo-deny) - Cargo plugin to help you manage large dependency graphs
* [Cherrybomb](https://github.com/blst-security/cherrybomb) <img src="https://img.shields.io/github/stars/blst-security/cherrybomb?style=social" alt="Stars" width="80"> - Stop half-done API specifications with a CLI tool that helps you avoid undefined user behaviour by validating your API specifications.
* [cotp](https://github.com/replydev/cotp) <img src="https://img.shields.io/github/stars/replydev/cotp?style=social" alt="Stars" width="80"> - Trustworthy, encrypted, command-line TOTP/HOTP authenticator app with import functionality.
* [entropic-security/xgadget](https://github.com/entropic-security/xgadget) [[xgadget](https://crates.io/crates/xgadget)] — Fast, parallel, cross-variant ROP/JOP gadget search [![GitHub Actions](https://github.com/entropic-security/xgadget/workflows/test/badge.svg)](https://github.com/entropic-security/xgadget/actions)
* [epi052/feroxbuster](https://github.com/epi052/feroxbuster) <img src="https://img.shields.io/github/stars/epi052/feroxbuster?style=social" alt="Stars" width="80"> - A simple, fast, recursive content discovery tool written in Rust (
* [Inspektor](https://github.com/inspektor-dev/inspektor) <img src="https://img.shields.io/github/stars/inspektor-dev/inspektor?style=social" alt="Stars" width="80"> - A database protocol-aware proxy that is used to enforce access policies 👮
* [kpcyrd/authoscope](https://github.com/kpcyrd/authoscope) <img src="https://img.shields.io/github/stars/kpcyrd/authoscope?style=social" alt="Stars" width="80"> — A scriptable network authentication cracker
* [kpcyrd/rshijack](https://github.com/kpcyrd/rshijack) <img src="https://img.shields.io/github/stars/kpcyrd/rshijack?style=social" alt="Stars" width="80"> — A TCP connection hijacker, rust rewrite of shijack
* [kpcyrd/sn0int](https://github.com/kpcyrd/sn0int) <img src="https://img.shields.io/github/stars/kpcyrd/sn0int?style=social" alt="Stars" width="80"> — A semi-automatic OSINT framework and package manager
* [kpcyrd/sniffglue](https://github.com/kpcyrd/sniffglue) <img src="https://img.shields.io/github/stars/kpcyrd/sniffglue?style=social" alt="Stars" width="80"> — A secure multithreaded packet sniffer
* [ObserverWard](https://github.com/0x727/ObserverWard) <img src="https://img.shields.io/github/stars/0x727/ObserverWard?style=social" alt="Stars" width="80"> — Community based web technologies analysis tool.
* [ripasso](https://github.com/cortex/ripasso/) <img src="https://img.shields.io/github/stars/cortex/ripasso?style=social" alt="Stars" width="80"> — A password manager, filesystem compatible with pass
* [rustscan/rustscan](https://github.com/RustScan/RustScan) <img src="https://img.shields.io/github/stars/RustScan/RustScan?style=social" alt="Stars" width="80"> — Make Nmap faster with this port scanning tool [![build badge](https://github.com/RustScan/RustScan/workflows/Continuous%20integration/badge.svg?branch=master)](https://github.com/RustScan/RustScan/actions?query=workflow%3A%22Continuous+integration%22)

### Social networks

* Mastodon
  * [Rustodon](https://github.com/rustodon/rustodon) <img src="https://img.shields.io/github/stars/rustodon/rustodon?style=social" alt="Stars" width="80"> - A Mastodon-compatible, ActivityPub-speaking server in Rust

### System tools

* [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide/) <img src="https://img.shields.io/github/stars/ajeetdsouza/zoxide?style=social" alt="Stars" width="80"> — A fast alternative to `cd` that learns your habits [![release](https://github.com/ajeetdsouza/zoxide/workflows/.github/workflows/release.yml/badge.svg)](https://github.com/ajeetdsouza/zoxide/actions)
* [Alonely0/Voila](https://github.com/Alonely0/Voila) <img src="https://img.shields.io/github/stars/Alonely0/Voila?style=social" alt="Stars" width="80"> — Voila is a domain-specific language launched through CLI tool for operating with files and directories in massive amounts in a fast & reliable way. [![Linux build](https://github.com/Alonely0/Voila/actions/workflows/linux-ci.yml/badge.svg)](https://github.com/Alonely0/Voila/actions/workflows/linux-ci.yml) [![macOS build](https://github.com/Alonely0/Voila/actions/workflows/mac-ci.yml/badge.svg)](https://github.com/Alonely0/Voila/actions/workflows/mac-ci.yml) [![Windows build](https://github.com/Alonely0/Voila/actions/workflows/windows-ci.yml/badge.svg)](https://github.com/Alonely0/Voila/actions/workflows/windows-ci.yml)
* [atuin](https://github.com/atuinsh/atuin) <img src="https://img.shields.io/github/stars/atuinsh/atuin?style=social" alt="Stars" width="80"> [[atuin](https://crates.io/crates/atuin)] — Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.
* [bandwhich](https://github.com/imsnif/bandwhich) <img src="https://img.shields.io/github/stars/imsnif/bandwhich?style=social" alt="Stars" width="80"> — Terminal bandwidth utilization tool
* [bottom](https://github.com/ClementTsang/bottom) <img src="https://img.shields.io/github/stars/ClementTsang/bottom?style=social" alt="Stars" width="80"> - Yet another cross-platform graphical process/system monitor. [![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/ClementTsang/bottom/ci/master)](https://github.com/ClementTsang/bottom/actions?query=branch%3Amaster)
* [brocode/fblog](https://github.com/brocode/fblog) <img src="https://img.shields.io/github/stars/brocode/fblog?style=social" alt="Stars" width="80"> — Small command-line JSON Log viewer
* [bustd](https://github.com/vrmiguel/bustd) <img src="https://img.shields.io/github/stars/vrmiguel/bustd?style=social" alt="Stars" width="80"> - Lightweight process killer daemon to handle out-of-memory scenarios on Linux. [![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/vrmiguel/bustd/build-and-test)](https://github.com/vrmiguel/bustd/actions?query=branch%3Amaster)
* [buster/rrun](https://github.com/buster/rrun) <img src="https://img.shields.io/github/stars/buster/rrun?style=social" alt="Stars" width="80"> — A command launcher for Linux, similar to gmrun
* [cantino/mcfly](https://github.com/cantino/mcfly) <img src="https://img.shields.io/github/stars/cantino/mcfly?style=social" alt="Stars" width="80"> - Fly through your shell history. Great Scott!
* [crabz](https://github.com/sstadick/crabz) <img src="https://img.shields.io/github/stars/sstadick/crabz?style=social" alt="Stars" width="80"> - Multi-threaded compression and decompression CLI tool [![Build Status](https://github.com/sstadick/crabz/workflows/Check/badge.svg)](https://github.com/sstadick/crabz/actions?query=workflow%3ACheck)
* [cristianoliveira/funzzy](https://github.com/cristianoliveira/funzzy) <img src="https://img.shields.io/github/stars/cristianoliveira/funzzy?style=social" alt="Stars" width="80"> — A configurable filesystem watcher inspired by [entr](http://eradman.com/entrproject/)
* [dalance/procs](https://github.com/dalance/procs) <img src="https://img.shields.io/github/stars/dalance/procs?style=social" alt="Stars" width="80"> — A modern replacement for 'ps' written by Rust [![Regression](https://github.com/dalance/procs/actions/workflows/regression.yml/badge.svg)](https://github.com/dalance/procs/actions/workflows/regression.yml)
* [ddh](https://github.com/darakian/ddh) <img src="https://img.shields.io/github/stars/darakian/ddh?style=social" alt="Stars" width="80"> — Fast duplicate file finder
* [diskonaut](https://github.com/imsnif/diskonaut) <img src="https://img.shields.io/github/stars/imsnif/diskonaut?style=social" alt="Stars" width="80"> — Terminal visual disk space navigator
* [dust](https://github.com/bootandy/dust) <img src="https://img.shields.io/github/stars/bootandy/dust?style=social" alt="Stars" width="80"> — A more intuitive version of du
* [eza-community/eza](https://github.com/eza-community/eza) — A replacement for 'ls'
* [fselect](https://crates.io/crates/fselect) — Find files with SQL-like queries
* [gitui](https://github.com/extrawurst/gitui) <img src="https://img.shields.io/github/stars/extrawurst/gitui?style=social" alt="Stars" width="80"> - Blazing fast terminal client for git written in Rust. [![build](https://github.com/extrawurst/gitui/workflows/CI/badge.svg?branch=master)](https://github.com/extrawurst/gitui/actions)
* [GQL](https://github.com/amrdeveloper/gql) <img src="https://img.shields.io/github/stars/amrdeveloper/gql?style=social" alt="Stars" width="80"> — A SQL like query language to run on .git files.
* [httm](https://github.com/kimono-koans/httm) <img src="https://img.shields.io/github/stars/kimono-koans/httm?style=social" alt="Stars" width="80"> - Interactive, file-level Time Machine-like tool for ZFS/btrfs/nilfs2 (and even actual Time Machine backups!)
* [j0ru/kickoff](https://github.com/j0ru/kickoff) <img src="https://img.shields.io/github/stars/j0ru/kickoff?style=social" alt="Stars" width="80"> - Fast and snappy wayland program launcher [![build](https://github.com/j0ru/kickoff/actions/workflows/ci.yml/badge.svg)](https://github.com/j0ru/kickoff/actions)
* [Kondo](https://github.com/tbillington/kondo) <img src="https://img.shields.io/github/stars/tbillington/kondo?style=social" alt="Stars" width="80"> - CLI & GUI tool for deleting software project artifacts and reclaiming disk space
* [LACT](https://github.com/ilya-zlobintsev/LACT) <img src="https://img.shields.io/github/stars/ilya-zlobintsev/LACT?style=social" alt="Stars" width="80"> - Linux AMDGPU Controller
* [lodosgroup/lpm](https://github.com/lodosgroup/lpm) <img src="https://img.shields.io/github/stars/lodosgroup/lpm?style=social" alt="Stars" width="80"> — An experimental system package manager
* [lotabout/rargs](https://github.com/lotabout/rargs) <img src="https://img.shields.io/github/stars/lotabout/rargs?style=social" alt="Stars" width="80"> [[rargs](https://crates.io/crates/rargs)] — xargs + awk with pattern matching support
* [lotabout/skim](https://github.com/lotabout/skim) <img src="https://img.shields.io/github/stars/lotabout/skim?style=social" alt="Stars" width="80"> — A fuzzy finder in pure rust
* [lsd](https://github.com/lsd-rs/lsd) <img src="https://img.shields.io/github/stars/lsd-rs/lsd?style=social" alt="Stars" width="80"> — An ls with a lot of pretty colors and awesome icons [![build](https://github.com/lsd-rs/lsd/workflows/CICD/badge.svg?branch=master)](https://github.com/lsd-rs/lsd/actions)
* [Luminarys/synapse](https://github.com/Luminarys/synapse) <img src="https://img.shields.io/github/stars/Luminarys/synapse?style=social" alt="Stars" width="80"> — Flexible and fast BitTorrent daemon.
* [m4b/bingrep](https://github.com/m4b/bingrep) <img src="https://img.shields.io/github/stars/m4b/bingrep?style=social" alt="Stars" width="80"> — Greps through binaries from various OSs and architectures, and colors them.
* [mdgaziur/findex](https://github.com/mdgaziur/findex) <img src="https://img.shields.io/github/stars/mdgaziur/findex?style=social" alt="Stars" width="80"> - Findex is a highly customizable application finder written in Rust and uses GTK3
* [mitnk/cicada](https://github.com/mitnk/cicada) <img src="https://img.shields.io/github/stars/mitnk/cicada?style=social" alt="Stars" width="80"> — A bash-like Unix shell
* [mmstick/concurr](https://github.com/mmstick/concurr) <img src="https://img.shields.io/github/stars/mmstick/concurr?style=social" alt="Stars" width="80"> — Alternative to GNU Parallel w/ a client-server architecture
* [mmstick/fontfinder](https://github.com/mmstick/fontfinder) <img src="https://img.shields.io/github/stars/mmstick/fontfinder?style=social" alt="Stars" width="80"> — GTK3 application for previewing and installing Google's fonts
* [mmstick/tv-renamer](https://github.com/mmstick/tv-renamer) — A tv series renaming application with an optional GTK3 frontend.
* [mxseev/logram](https://github.com/mxseev/logram) <img src="https://img.shields.io/github/stars/mxseev/logram?style=social" alt="Stars" width="80"> — Push log files' updates to Telegram
* [nickgerace/gfold](https://github.com/nickgerace/gfold) <img src="https://img.shields.io/github/stars/nickgerace/gfold?style=social" alt="Stars" width="80"> [[gfold](https://crates.io/crates/gfold)] - CLI tool to help keep track of multiple Git repositories [![build](https://img.shields.io/github/workflow/status/nickgerace/gfold/merge/main)](https://github.com/nickgerace/gfold/actions?query=workflow%3Amerge+branch%3Amain)
* [nivekuil/rip](https://github.com/nivekuil/rip) <img src="https://img.shields.io/github/stars/nivekuil/rip?style=social" alt="Stars" width="80"> - A safe and ergonomic alternative to `rm`
* [nushell/nushell](https://github.com/nushell/nushell) <img src="https://img.shields.io/github/stars/nushell/nushell?style=social" alt="Stars" width="80"> - A new type of shell
* [orhun/kmon](https://github.com/orhun/kmon) <img src="https://img.shields.io/github/stars/orhun/kmon?style=social" alt="Stars" width="80"> — Linux Kernel Manager and Activity Monitor ![https://github.com/orhun/kmon/actions](https://img.shields.io/github/actions/workflow/status/orhun/kmon/ci.yml?branch=master&label=build)
* [orhun/systeroid](https://github.com/orhun/systeroid) <img src="https://img.shields.io/github/stars/orhun/systeroid?style=social" alt="Stars" width="80"> — A more powerful alternative to sysctl(8) with a terminal user interface ![https://github.com/orhun/systeroid/actions](https://img.shields.io/github/actions/workflow/status/orhun/systeroid/ci.yml?branch=main&label=build)
* [ouch](https://github.com/ouch-org/ouch) <img src="https://img.shields.io/github/stars/ouch-org/ouch?style=social" alt="Stars" width="80"> - Painless compression and decompression on the command-line [![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/ouch-org/ouch/build-and-test)](https://github.com/ouch-org/ouch/actions?query=branch%3Amaster)
* [pkolaczk/fclones](https://github.com/pkolaczk/fclones) <img src="https://img.shields.io/github/stars/pkolaczk/fclones?style=social" alt="Stars" width="80"> — Efficient duplicate file finder and remover
* [pop-os/popsicle](https://github.com/pop-os/popsicle) — GTK3 & CLI utility for flashing multiple USB devices in parallel
* [pop-os/system76-power](https://github.com/pop-os/system76-power/) — Linux power management daemon (DBus-interface) with CLI tool.
* [pueue](https://github.com/nukesor/pueue) <img src="https://img.shields.io/github/stars/nukesor/pueue?style=social" alt="Stars" width="80"> — Manage your long running shell commands. [![GitHub Actions Workflow](https://github.com/nukesor/pueue/workflows/Test%20build/badge.svg?branch=master)](https://github.com/nukesor/pueue/actions)
* [qarmin/cakawka](https://github.com/qarmin/czkawka) <img src="https://img.shields.io/github/stars/qarmin/czkawka?style=social" alt="Stars" width="80"> - Multi-functional app to find duplicates, empty folders, similar images, etc. [![GitHub Actions Workflow](https://github.com/qarmin/czkawka/actions/workflows/pages/pages-build-deployment/badge.svg?branch=master)](https://github.com/qarmin/czkawka/actions)
* [redox-os/ion](https://github.com/redox-os/ion) — Next-generation system shell
* [sharkdp/bat](https://github.com/sharkdp/bat) <img src="https://img.shields.io/github/stars/sharkdp/bat?style=social" alt="Stars" width="80"> — A cat(1) clone with wings. [![CICD](https://github.com/sharkdp/bat/actions/workflows/CICD.yml/badge.svg?branch=master)](https://github.com/sharkdp/bat/actions/workflows/CICD.yml)
* [sharkdp/fd](https://github.com/sharkdp/fd) <img src="https://img.shields.io/github/stars/sharkdp/fd?style=social" alt="Stars" width="80"> — A simple, fast and user-friendly alternative to find. [![CICD](https://github.com/sharkdp/fd/actions/workflows/CICD.yml/badge.svg)](https://github.com/sharkdp/fd/actions/workflows/CICD.yml)
* [sitkevij/hex](https://github.com/sitkevij/hex) <img src="https://img.shields.io/github/stars/sitkevij/hex?style=social" alt="Stars" width="80"> — A colorized hexdump terminal utility.
* [supercilex/fuc](https://github.com/supercilex/fuc) <img src="https://img.shields.io/github/stars/supercilex/fuc?style=social" alt="Stars" width="80"> - Fast `cp` and `rm` commands
* [trippy](https://github.com/fujiapple852/trippy) <img src="https://img.shields.io/github/stars/fujiapple852/trippy?style=social" alt="Stars" width="80"> - A network diagnostic tool [![build badge](https://github.com/fujiapple852/trippy/workflows/CI/badge.svg)](https://github.com/fujiapple852/trippy/actions/workflows/ci.yml)
* [uutils/coreutils](https://github.com/uutils/coreutils) <img src="https://img.shields.io/github/stars/uutils/coreutils?style=social" alt="Stars" width="80"> — A cross-platform Rust rewrite of the GNU coreutils [[![CICD](https://github.com/uutils/coreutils/actions/workflows/CICD.yml/badge.svg)](https://github.com/uutils/coreutils/actions/workflows/CICD.yml)
* [watchexec](https://github.com/watchexec/watchexec) <img src="https://img.shields.io/github/stars/watchexec/watchexec?style=social" alt="Stars" width="80"> — Executes commands in response to file modifications
* [XAMPPRocky/tokei](https://github.com/XAMPPRocky/tokei) <img src="https://img.shields.io/github/stars/XAMPPRocky/tokei?style=social" alt="Stars" width="80"> — counts the lines of code

### Task scheduling

* [delicate](https://github.com/BinChengZhao/delicate) <img src="https://img.shields.io/github/stars/BinChengZhao/delicate?style=social" alt="Stars" width="80"> — A lightweight and distributed task scheduling platform written in rust. [![Build Status](https://github.com/BinChengZhao/delicate/workflows/CI/badge.svg)](https://github.com/BinChengZhao/delicate/actions)

### Text editors

* [amp](https://amp.rs) — Inspired by Vi/Vim.
* [emacs-ng](https://github.com/emacs-ng/emacs-ng) — Complementing the C codebase with rust code to introduce new features.
* [gchp/iota](https://github.com/gchp/iota) <img src="https://img.shields.io/github/stars/gchp/iota?style=social" alt="Stars" width="80"> — A simple text editor
* [helix](https://github.com/helix-editor/helix) <img src="https://img.shields.io/github/stars/helix-editor/helix?style=social" alt="Stars" width="80"> — A post-modern modal text editor inspired by Neovim/Kakoune. [![build badge](https://github.com/helix-editor/helix/actions/workflows/build.yml/badge.svg)](https://github.com/helix-editor/helix/actions)
* [ilai-deutel/kibi](https://github.com/ilai-deutel/kibi) — A tiny (≤1024 LOC) text editor with syntax highlighting, incremental search and more. [![build badge](https://github.com/ilai-deutel/kibi/workflows/CI/badge.svg?branch=master)](https://github.com/ilai-deutel/kibi/actions?query=branch%3Amaster)
* [Lapce](https://github.com/lapce/lapce) <img src="https://img.shields.io/github/stars/lapce/lapce?style=social" alt="Stars" width="80"> — A modern editor with a backend written in Rust. Taking inspiration from the discontinued [xi-editor](https://github.com/xi-editor/xi-editor).
* [mathall/rim](https://github.com/mathall/rim) <img src="https://img.shields.io/github/stars/mathall/rim?style=social" alt="Stars" width="80"> — Vim-like text editor written in Rust
* [ox](https://github.com/curlpipe/ox) <img src="https://img.shields.io/github/stars/curlpipe/ox?style=social" alt="Stars" width="80"> — An independent Rust text editor that runs in your terminal!
* [vamolessa/pepper](https://github.com/vamolessa/pepper) <img src="https://img.shields.io/github/stars/vamolessa/pepper?style=social" alt="Stars" width="80"> [[pepper](https://crates.io/crates/pepper)] — An opinionated modal editor to simplify code editing from the terminal [![build badge](https://github.com/vamolessa/pepper/workflows/rust/badge.svg?branch=master)](https://github.com/vamolessa/pepper)
* [zed](https://github.com/zed-industries/zed) <img src="https://img.shields.io/github/stars/zed-industries/zed?style=social" alt="Stars" width="80"> — A high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

### Text processing

* [dominikwilkowski/cfonts](https://github.com/dominikwilkowski/cfonts) <img src="https://img.shields.io/github/stars/dominikwilkowski/cfonts?style=social" alt="Stars" width="80"> [[cfonts](https://crates.io/crates/cfonts)] — Sexy ANSI fonts for the console ![build badge](https://github.com/dominikwilkowski/cfonts/actions/workflows/testing.yml/badge.svg)
* [grex](https://github.com/pemistahl/grex) <img src="https://img.shields.io/github/stars/pemistahl/grex?style=social" alt="Stars" width="80"> — A command-line tool and library for generating regular expressions from user-provided test cases
* [jqnatividad/qsv](https://github.com/jqnatividad/qsv) <img src="https://img.shields.io/github/stars/jqnatividad/qsv?style=social" alt="Stars" width="80"> [[qsv](https://crates.io/crates/qsv)] — A high performance CSV data-wrangling toolkit. Forked from xsv, with 34+ additional commands & more. [![Linux build status](https://github.com/jqnatividad/qsv/actions/workflows/rust.yml/badge.svg)](https://github.com/jqnatividad/qsv/actions/workflows/rust.yml) [![Windows build status](https://github.com/jqnatividad/qsv/actions/workflows/rust-windows.yml/badge.svg)](https://github.com/jqnatividad/qsv/actions/workflows/rust-windows.yml) [![macOS build status](https://github.com/jqnatividad/qsv/actions/workflows/rust-macos.yml/badge.svg)](https://github.com/jqnatividad/qsv/actions/workflows/rust-macos.yml)
* [Lisprez/so_stupid_search](https://github.com/Lisprez/so_stupid_search) <img src="https://img.shields.io/github/stars/Lisprez/so_stupid_search?style=social" alt="Stars" width="80"> — A simple and fast string search tool for human beings
* [Melody](https://github.com/yoav-lavi/melody) <img src="https://img.shields.io/github/stars/yoav-lavi/melody?style=social" alt="Stars" width="80"> - A language that compiles to regular expressions and aims to be more easily readable and maintainable [![build badge](https://github.com/yoav-lavi/melody/actions/workflows/rust.yml/badge.svg)](https://github.com/yoav-lavi/melody/actions/workflows/rust.yml) [![crates.io](https://img.shields.io/crates/v/melody_compiler?label=compiler)](https://crates.io/crates/melody_compiler)
* [phiresky/ripgrep-all](https://github.com/phiresky/ripgrep-all) — ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc.
* [replicadse/complate](https://github.com/replicadse/complate) <img src="https://img.shields.io/github/stars/replicadse/complate?style=social" alt="Stars" width="80"> — An in-terminal text templating tool designed for standardizing messages (like for GIT commits). [![crates.io](https://img.shields.io/crates/v/complate.svg)](https://crates.io/crates/complate) [![crates.io](https://img.shields.io/crates/d/complate?label=crates.io%20downloads)](https://crates.io/crates/complate) [![build badge](https://github.com/replicadse/complate/workflows/pipeline/badge.svg?branch=master)](https://github.com/replicadse/complate/actions)
* [ripgrep](https://crates.io/crates/ripgrep) — combines the usability of The Silver Searcher with the raw speed of grep
* [ruplacer](https://github.com/your-tools/ruplacer) <img src="https://img.shields.io/github/stars/your-tools/ruplacer?style=social" alt="Stars" width="80"> — Find and replace text in source files [![Run tests](https://github.com/your-tools/ruplacer/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/your-tools/ruplacer/actions/workflows/test.yml)
* [sd](https://crates.io/crates/sd) — Intuitive find & replace CLI
* [sstadick/hck](https://github.com/sstadick/hck) <img src="https://img.shields.io/github/stars/sstadick/hck?style=social" alt="Stars" width="80"> - A faster and more featureful drop in replacement for `cut` [![build badge](https://github.com/sstadick/hck/workflows/Check/badge.svg?branch=master)](https://github.com/sstadick/hck)
* [vishaltelangre/ff](https://github.com/vishaltelangre/ff) <img src="https://img.shields.io/github/stars/vishaltelangre/ff?style=social" alt="Stars" width="80"> — Find files (ff) by name!
* [whitfin/bytelines](https://github.com/whitfin/bytelines) <img src="https://img.shields.io/github/stars/whitfin/bytelines?style=social" alt="Stars" width="80"> [[bytelines](https://crates.io/crates/bytelines)] — Read input lines as byte slices for high efficiency.
* [whitfin/runiq](https://github.com/whitfin/runiq) <img src="https://img.shields.io/github/stars/whitfin/runiq?style=social" alt="Stars" width="80"> — an efficient way to filter duplicate lines from unsorted input.
* [xsv](https://crates.io/crates/xsv) — A fast CSV command line tool (slicing, indexing, selecting, searching, sampling, etc.)

### Utilities

* [1History](https://github.com/1History/1History) <img src="https://img.shields.io/github/stars/1History/1History?style=social" alt="Stars" width="80"> — Command line interface to backup Firefox/Chrome/Safari history to one SQLite file [![Build Status](https://github.com/1History/1History/actions/workflows/CI.yml/badge.svg)](https://github.com/1History/1History/actions/workflows/CI.yml)
* [brycx/checkpwn](https://github.com/brycx/checkpwn) <img src="https://img.shields.io/github/stars/brycx/checkpwn?style=social" alt="Stars" width="80"> — A Have I Been Pwned (HIBP) command-line utility tool that lets you easily check for compromised accounts and passwords.
* [Epic Asset Manager](https://github.com/AchetaGames/Epic-Asset-Manager) — An unofficial client to install Unreal Engine, download and manage purchased assets, projects, plugins and games from the Epic Games Store.
* [evansmurithi/cloak](https://github.com/evansmurithi/cloak) <img src="https://img.shields.io/github/stars/evansmurithi/cloak?style=social" alt="Stars" width="80"> — A Command Line OTP (One Time Password) Authenticator application.
![CI](https://github.com/evansmurithi/cloak/workflows/CI/badge.svg) [![build badge](https://ci.appveyor.com/api/projects/status/9mlfpfru3ng4c689/branch/master?svg=true)](https://ci.appveyor.com/project/evansmurithi/cloak)
* [fcsonline/tmux-thumbs](https://github.com/fcsonline/tmux-thumbs) — A lightning fast version of tmux-fingers written in Rust, copy/pasting tmux like vimium/vimperator.
* [guoxbin/dtool](https://github.com/guoxbin/dtool) <img src="https://img.shields.io/github/stars/guoxbin/dtool?style=social" alt="Stars" width="80"> — A useful command-line tool collection to assist development including conversion, codec, hashing, encryption, etc.
* [mprocs](https://github.com/pvolok/mprocs) <img src="https://img.shields.io/github/stars/pvolok/mprocs?style=social" alt="Stars" width="80"> — TUI for running multiple processes
* [mrjackwills/oxker](https://github.com/mrjackwills/oxker) <img src="https://img.shields.io/github/stars/mrjackwills/oxker?style=social" alt="Stars" width="80"> [[oxker](https://crates.io/crates/oxker)] - A simple tui to view & control docker containers.
* [nix-community/nix-init](https://github.com/nix-community/nix-init) — Generate Nix packages from URLs with hash prefetching, dependency inference, license detection, and more [![build-badge](https://github.com/nix-community/nix-init/actions/workflows/ci.yml/badge.svg)](https://github.com/nix-community/nix-init/actions/workflows/ci.yml)
* [nix-community/nix-melt](https://github.com/nix-community/nix-melt) — A ranger-like flake.lock viewer [![build-badge](https://github.com/nix-community/nix-melt/actions/workflows/ci.yml/badge.svg)](https://github.com/nix-community/nix-melt/actions/workflows/ci.yml)
* [nix-community/nurl](https://github.com/nix-community/nurl) [[nurl](https://crates.io/crates/nurl)] — Generate Nix fetcher calls from repository URLs [![build-badge](https://github.com/nix-community/nurl/actions/workflows/ci.yml/badge.svg)](https://github.com/nix-community/nurl/actions/workflows/ci.yml)
* [nomino](https://github.com/yaa110/nomino) <img src="https://img.shields.io/github/stars/yaa110/nomino?style=social" alt="Stars" width="80"> — Batch rename utility for developers
* [raftario/licensor](https://github.com/raftario/licensor) <img src="https://img.shields.io/github/stars/raftario/licensor?style=social" alt="Stars" width="80"> — write licenses to stdout [![GitHub Actions](https://github.com/raftario/licensor/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/raftario/licensor/actions/workflows/build.yml)
* [rust-parallel](https://github.com/aaronriekenberg/rust-parallel) - Fast command line app using Tokio to execute commands in parallel.  Similar interface to GNU Parallel or xargs. [![Crate](https://img.shields.io/crates/v/rust-parallel.svg?logo=rust)](https://crates.io/crates/rust-parallel) [![Build Status](https://github.com/aaronriekenberg/rust-parallel/actions/workflows/CI.yml/badge.svg)](https://github.com/aaronriekenberg/rust-parallel/actions/workflows/CI.yml)
* [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) <img src="https://img.shields.io/github/stars/rustdesk/rustdesk?style=social" alt="Stars" width="80"> — A remote desktop software, great alternative to TeamViewer and AnyDesk.
* [rustic-rs/rustic](https://github.com/rustic-rs/rustic) [[rustic-rs](https://crates.io/crates/rustic-rs)] — Fast, encrypted, deduplicated backups powered by Rust. [![Version](https://img.shields.io/crates/v/rustic-rs.svg)](https://crates.io/crates/rustic-rs)
* [suckit](https://github.com/Skallwar/suckit) <img src="https://img.shields.io/github/stars/Skallwar/suckit?style=social" alt="Stars" width="80"> - Recursively visit and download a website's content to your disk. [![Crate](https://img.shields.io/crates/v/suckit.svg?logo=rust)](https://crates.io/crates/suckit) [![Build Status](https://github.com/Skallwar/suckit/workflows/Build%20and%20test/badge.svg)](https://github.com/Skallwar/suckit/blob/master/.github/workflows/build_and_test.yml)
* [tversteeg/emplace](https://github.com/tversteeg/emplace) <img src="https://img.shields.io/github/stars/tversteeg/emplace?style=social" alt="Stars" width="80"> — Synchronize installed packages on multiple machines
* [vamolessa/verco](https://github.com/vamolessa/verco) <img src="https://img.shields.io/github/stars/vamolessa/verco?style=social" alt="Stars" width="80"> [[verco](https://crates.io/crates/verco)] — A simple Git/Hg tui client focused on keyboard shortcuts
* [vaultwarden](https://github.com/dani-garcia/vaultwarden#readme) [![Build](https://github.com/dani-garcia/vaultwarden/actions/workflows/build.yml/badge.svg)](https://github.com/dani-garcia/vaultwarden/actions/workflows/build.yml) — Alternative implementation of the Bitwarden server API written in Rust
* [warpdotdev/Warp](https://github.com/warpdotdev/Warp) <img src="https://img.shields.io/github/stars/warpdotdev/Warp?style=social" alt="Stars" width="80"> :heavy_dollar_sign: — Warp is a blazingly-fast modern Rust based GPU-accelerated terminal built to make you and your team more productive.
* [wrestic](https://github.com/alvaro17f/wrestic) <img src="https://img.shields.io/github/stars/alvaro17f/wrestic?style=social" alt="Stars" width="80"> —  👽 A wrapper around restic built in rust
* [yaa110/cb](https://github.com/yaa110/cb) <img src="https://img.shields.io/github/stars/yaa110/cb?style=social" alt="Stars" width="80"> — Command line interface to manage clipboard

### Video

* [dertuxmalwieder/yaydl](https://github.com/dertuxmalwieder/yaydl) <img src="https://img.shields.io/github/stars/dertuxmalwieder/yaydl?style=social" alt="Stars" width="80"> [[yaydl](https://crates.io/crates/yaydl)] - A simple video downloader
* [gyroflow/gyroflow](https://github.com/gyroflow/gyroflow) <img src="https://img.shields.io/github/stars/gyroflow/gyroflow?style=social" alt="Stars" width="80"> - Video stabilization application using gyroscope data
* [harlanc/xiu](https://github.com/harlanc/xiu) <img src="https://img.shields.io/github/stars/harlanc/xiu?style=social" alt="Stars" width="80"> — A powerful and secure live server by pure rust (rtmp/httpflv/hls/relay). [![crates.io](https://img.shields.io/crates/v/xiu.svg)](https://crates.io/crates/xiu)
* [vidmerger](https://github.com/TGotwig/vidmerger) <img src="https://img.shields.io/github/stars/TGotwig/vidmerger?style=social" alt="Stars" width="80"> — 📼 Merge video & audio files via CLI
* [xiph/rav1e](https://github.com/xiph/rav1e) <img src="https://img.shields.io/github/stars/xiph/rav1e?style=social" alt="Stars" width="80"> — The fastest and safest AV1 encoder.

### Virtualization

* [containers/youki](https://github.com/containers/youki) <img src="https://img.shields.io/github/stars/containers/youki?style=social" alt="Stars" width="80"> — A container runtime in Rust [![build badge](https://github.com/containers/youki/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/containers/youki/actions)
* [firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker) — A lightweight virtual machine for container workload [Firecracker Microvm](https://firecracker-microvm.github.io/)
* [kata-containers/kata-containers](https://github.com/kata-containers/kata-containers) - A implementation of lightweight Virtual Machines (VMs) that feel and perform like containers, but provide the workload isolation and security advantages of VMs.
* [tailhook/vagga](https://github.com/tailhook/vagga) <img src="https://img.shields.io/github/stars/tailhook/vagga?style=social" alt="Stars" width="80"> — A containerization tool without daemons

### Web

* [cfal/tobaru](https://github.com/cfal/tobaru) <img src="https://img.shields.io/github/stars/cfal/tobaru?style=social" alt="Stars" width="80"> - Port forwarder with allowlists, IP and TLS SNI/ALPN rule-based routing, iptables support, round-robin forwarding (load balancing), and hot reloading.
* [LemmyNet/lemmy](https://github.com/LemmyNet/lemmy) <img src="https://img.shields.io/github/stars/LemmyNet/lemmy?style=social" alt="Stars" width="80"> — A link aggregator / reddit clone for the fediverse [![Build Status](https://cloud.drone.io/api/badges/LemmyNet/lemmy/status.svg)](https://cloud.drone.io/LemmyNet/lemmy)
* [libreddit](https://github.com/libreddit/libreddit) <img src="https://img.shields.io/github/stars/libreddit/libreddit?style=social" alt="Stars" width="80"> - An alternative private front-end to Reddit
* [MASQ-Project/Node](https://github.com/MASQ-Project/Node) — MASQ Node software provides a decentralized mesh-network of nodes for global users to access normal internet content - next evolution of tech beyond Tor & VPN [![build badge](https://github.com/MASQ-Project/Node/actions/workflows/ci-matrix.yml/badge.svg)](https://github.com/MASQ-Project/Node/actions)
* [Plume-org/Plume](https://github.com/Plume-org/Plume) — ActivityPub federating blogging application
* [Revolt/backend](https://github.com/revoltchat/backend) <img src="https://img.shields.io/github/stars/revoltchat/backend?style=social" alt="Stars" width="80"> - User-first chat platform built with modern web technologies.

### Web Servers

* [emanuele-em/proxelar](https://github.com/emanuele-em/proxelar) — A MITM Proxy 🦀! Toolkit for HTTP/1, HTTP/2, and WebSockets with SSL/TLS Capabilities [![Rust](https://github.com/emanuele-em/proxelar/actions/workflows/rust.yml/badge.svg)](https://github.com/emanuele-em/proxelar/actions/workflows/rust.yml)
* [mu-arch/skyfolder](https://github.com/mu-arch/skyfolder) - 🪂 Beautiful HTTP/Bittorrent server without the hassle. Secure - GUI - Pretty - Fast
* [mufeedvh/binserve](https://github.com/mufeedvh/binserve) <img src="https://img.shields.io/github/stars/mufeedvh/binserve?style=social" alt="Stars" width="80"> — A blazingly fast static web server with routing, templating, and security in a single binary you can set up with zero code [![build badge](https://github.com/mufeedvh/binserve/workflows/CICD/badge.svg?branch=master)](https://github.com/mufeedvh/binserve/actions)
* [orhun/rustypaste](https://github.com/orhun/rustypaste) <img src="https://img.shields.io/github/stars/orhun/rustypaste?style=social" alt="Stars" width="80"> — A minimal file upload/pastebin service ![https://github.com/orhun/rustypaste/actions](https://img.shields.io/github/actions/workflow/status/orhun/rustypaste/ci.yml?branch=master&label=build)
* [ronanyeah/rust-hasura](https://github.com/ronanyeah/rust-hasura) — A demonstration of how a Rust GraphQL server can be used as a remote schema with [Hasura](https://hasura.io/) ![Rust](https://github.com/ronanyeah/rust-hasura/workflows/Rust/badge.svg?branch=master)
* [static-web-server](https://github.com/static-web-server/static-web-server) — A blazing fast and asynchronous web server for static files-serving. ⚡ [![CI](https://github.com/static-web-server/static-web-server/actions/workflows/devel.yml/badge.svg)](https://github.com/static-web-server/static-web-server/actions/workflows/devel.yml?query=branch%3Amaster)
* [svenstaro/miniserve](https://github.com/svenstaro/miniserve) <img src="https://img.shields.io/github/stars/svenstaro/miniserve?style=social" alt="Stars" width="80"> — A small, self-contained cross-platform CLI tool that allows you to just grab the binary and serve some file(s) via HTTP [![build badge](https://github.com/svenstaro/miniserve/workflows/CI/badge.svg?branch=master)](https://github.com/svenstaro/miniserve/actions)
* [thecoshman/http](https://github.com/thecoshman/http) <img src="https://img.shields.io/github/stars/thecoshman/http?style=social" alt="Stars" width="80"> — Host These Things Please — A basic http server for hosting a folder fast and simply
* [TheWaWaR/simple-http-server](https://github.com/TheWaWaR/simple-http-server) — simple static http server
* [wyhaya/see](https://github.com/wyhaya/see) <img src="https://img.shields.io/github/stars/wyhaya/see?style=social" alt="Stars" width="80"> — Static HTTP file server

## Development tools

* [bacon](https://github.com/Canop/bacon) <img src="https://img.shields.io/github/stars/Canop/bacon?style=social" alt="Stars" width="80"> — background rust code checker, similar to cargo-watch
* [clippy](https://crates.io/crates/clippy) — Rust lints
* [clog-tool/clog-cli](https://github.com/clog-tool/clog-cli) — generates a changelog from git metadata ([conventional changelog](https://blog.thoughtram.io/announcements/tools/2014/09/18/announcing-clog-a-conventional-changelog-generator-for-the-rest-of-us.html))
* [comtrya](https://github.com/comtrya/comtrya) <img src="https://img.shields.io/github/stars/comtrya/comtrya?style=social" alt="Stars" width="80"> — A configuration management tool for localhost / dotfiles [![build badge](https://github.com/comtrya/comtrya/actions/workflows/main.yaml/badge.svg)](https://github.com/comtrya/comtrya/actions)
* [create-rust-app](https://github.com/Wulf/create-rust-app) — Set up a modern rust+react web app by running one command. [![crate](https://img.shields.io/crates/v/create-rust-app.svg)](https://crates.io/crates/create-rust-app)
* [dan-t/rusty-tags](https://github.com/dan-t/rusty-tags) — create ctags/etags for a cargo project and all of its dependencies
* [datanymizer/datanymizer](https://github.com/datanymizer/datanymizer) <img src="https://img.shields.io/github/stars/datanymizer/datanymizer?style=social" alt="Stars" width="80"> - Powerful database anonymizer with flexible rules [![build badge](https://github.com/datanymizer/datanymizer/workflows/CI/badge.svg?branch=main)](https://github.com/datanymizer/datanymizer/actions?query=workflow%3ACI+branch%3Amain)
* [delta](https://crates.io/crates/git-delta) — A syntax-highlighter for git and diff output[![build badge](https://github.com/dandavison/delta/workflows/Continuous%20Integration/badge.svg)](https://github.com/dandavison/delta//actions)
* [dotenv-linter](https://github.com/dotenv-linter/dotenv-linter) — Linter for `.env` files [![build badge](https://github.com/dotenv-linter/dotenv-linter/workflows/CI/badge.svg?branch=master)](https://github.com/dotenv-linter/dotenv-linter/actions?query=workflow%3ACI+branch%3Amaster)
* [frolic](https://github.com/FrolicOrg/Frolic) <img src="https://img.shields.io/github/stars/FrolicOrg/Frolic?style=social" alt="Stars" width="80">  — An API layer to build customer facing dashboards 10x faster
* [fw](https://github.com/brocode/fw) <img src="https://img.shields.io/github/stars/brocode/fw?style=social" alt="Stars" width="80"> — workspace productivity booster [![Rust](https://github.com/brocode/fw/actions/workflows/rust.yml/badge.svg)](https://github.com/brocode/fw/actions/workflows/rust.yml)
* [geiger](https://github.com/geiger-rs/cargo-geiger) <img src="https://img.shields.io/github/stars/geiger-rs/cargo-geiger?style=social" alt="Stars" width="80"> — A program that list statistics related to usage of unsafe Rust code in a Rust crate and all its dependencies [![Build Status](https://dev.azure.com/cargo-geiger/cargo-geiger/_apis/build/status/geiger-rs.cargo-geiger?branchName=master)](https://dev.azure.com/cargo-geiger/cargo-geiger/_build/latest?definitionId=1&branchName=master)
* [git-cliff](https://github.com/orhun/git-cliff) — A highly customizable Changelog Generator that follows Conventional Commit specifications ![https://github.com/orhun/git-cliff/actions](https://img.shields.io/github/actions/workflow/status/orhun/git-cliff/ci.yml?branch=main&label=build)
* [git-journal](https://github.com/saschagrunert/git-journal/) — The Git Commit Message and Changelog Generation Framework
* [hot-lib-reloader](https://github.com/rksm/hot-lib-reloader-rs) — Hot reload Rust code [![build badge](https://github.com/rksm/hot-lib-reloader-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/rksm/hot-lib-reloader-rs/actions/workflows/ci.yml)
* [intelli-shell](https://github.com/lasantosr/intelli-shell) - Bookmark commands with placeholders and search or autocomplete at any time [![crate](https://img.shields.io/crates/v/intelli-shell.svg)](https://crates.io/crates/intelli-shell) [![build badge](https://github.com/lasantosr/intelli-shell/actions/workflows/release.yml/badge.svg)](https://github.com/lasantosr/intelli-shell/actions/workflows/release.yml)
* [just](https://github.com/casey/just) <img src="https://img.shields.io/github/stars/casey/just?style=social" alt="Stars" width="80"> — A handy command runner for project-specific tasks
* [mask](https://github.com/jacobdeichert/mask) <img src="https://img.shields.io/github/stars/jacobdeichert/mask?style=social" alt="Stars" width="80"> — A CLI task runner defined by a simple markdown file [![build badge](https://github.com/jacobdeichert/mask/workflows/CI/badge.svg?branch=master)](https://github.com/jacobdeichert/mask/actions?query=workflow%3ACI)
* [Module Linker](https://github.com/fiatjaf/module-linker) — Extension that adds `<a>` links to references in `mod`, `use` and `extern crate` statements at GitHub.
* [ptags](https://github.com/dalance/ptags) <img src="https://img.shields.io/github/stars/dalance/ptags?style=social" alt="Stars" width="80"> — A parallel universal-ctags wrapper for git repository
* [Racer](https://github.com/racer-rust/racer) <img src="https://img.shields.io/github/stars/racer-rust/racer?style=social" alt="Stars" width="80"> — code completion for Rust
* [Rust Search Extension](https://github.com/huhu/rust-search-extension) — A handy browser extension to search crates and docs in address bar (omnibox). [![Build Status](https://github.com/huhu/rust-search-extension/workflows/build/badge.svg?branch=master)](https://github.com/huhu/rust-search-extension/actions)
* [Rustup](https://github.com/rust-lang/rustup) <img src="https://img.shields.io/github/stars/rust-lang/rustup?style=social" alt="Stars" width="80"> — the Rust toolchain installer [![build badge](https://github.com/rust-lang/rustup/workflows/Linux%20(master)/badge.svg?branch=master)](https://github.com/rust-lang/rustup/actions)
* [scriptisto](https://github.com/igor-petruk/scriptisto) <img src="https://img.shields.io/github/stars/igor-petruk/scriptisto?style=social" alt="Stars" width="80"> A language-agnostic "shebang interpreter" that enables you to write one file scripts in compiled languages. [![Build Status](https://cloud.drone.io/api/badges/igor-petruk/scriptisto/status.svg)](https://cloud.drone.io/igor-petruk/scriptisto)

### Build system

* [Cargo](https://crates.io/) — the Rust package manager
  * [cargo-all-features](https://github.com/frewsxcv/cargo-all-features) - A configurable subcommand to simplify testing, building and much more for all combinations of features [![CI](https://github.com/frewsxcv/cargo-all-features/actions/workflows/ci.yml/badge.svg)](https://github.com/frewsxcv/cargo-all-features/actions/workflows/ci.yml)
  * [cargo-benchcmp](https://crates.io/crates/cargo-benchcmp) — A utility to compare Rust micro-benchmarks
  * [cargo-bitbake](https://crates.io/crates/cargo-bitbake) — A cargo extension that can generate BitBake recipes utilizing the classes from meta-rust
  * [cargo-cache](https://crates.io/crates/cargo-cache) — inspect/manage/clean your cargo cache (`~/.cargo/`/`${CARGO_HOME}`), print sizes etc [![Build Status](https://github.com/matthiaskrgr/cargo-cache/workflows/ci/badge.svg?branch=master)](https://github.com/matthiaskrgr/cargo-cache/actions)
  * [cargo-check](https://crates.io/crates/cargo-check) — A wrapper around `cargo rustc -- -Zno-trans` which can be helpful for running a faster compile if you only need correctness checks
  * [cargo-commander](https://crates.io/crates/cargo-commander) — A subcommand for `cargo` to run CLI commands similar to how the scripts section in `package.json` works [![Build and test](https://github.com/simonhyll/cargo-commander/actions/workflows/build.yml/badge.svg)](https://github.com/simonhyll/cargo-commander/actions/workflows/build.yml)
  * [cargo-count](https://crates.io/crates/cargo-count) — lists source code counts and details about cargo projects, including unsafe statistics
  * [cargo-deb](https://crates.io/crates/cargo-deb) — Generates binary Debian packages
  * [cargo-deps](https://crates.io/crates/cargo-deps) — build dependency graphs of Rust projects
  * [cargo-do](https://crates.io/crates/cargo-do) — run multiple cargo commands in a row
  * [cargo-ebuild](https://crates.io/crates/cargo-ebuild) — cargo extension that can generate ebuilds using the in-tree eclasses
  * [cargo-edit](https://crates.io/crates/cargo-edit) — allows you to add and list dependencies by reading/writing to your Cargo.toml file from the command line
  * [cargo-generate](https://github.com/cargo-generate/cargo-generate) A generator of a rust project by leveraging a pre-existing git repository as a template.
  * [cargo-graph](https://crates.io/crates/cargo-graph) — updated fork of `cargo-dot` with additional features. Unmaintained, see `cargo-deps`
  * [cargo-info](https://crates.io/crates/cargo-info) — queries crates.io for crates details from command line
  * [cargo-license](https://crates.io/crates/cargo-license) — A cargo subcommand to quickly view the licenses of all dependencies.
  * [cargo-limit](https://crates.io/crates/cargo-limit) — Cargo with less noise: warnings are skipped until errors are fixed, Neovim integration, etc. [![build badge](https://github.com/alopatindev/cargo-limit/actions/workflows/rust.yml/badge.svg)](https://github.com/alopatindev/cargo-limit/actions)
  * [cargo-make](https://crates.io/crates/cargo-make) — Rust task runner and build tool. [![build badge](https://github.com/sagiegurari/cargo-make/workflows/CI/badge.svg?branch=master)](https://github.com/sagiegurari/cargo-make/actions)
  * [cargo-modules](https://crates.io/crates/cargo-modules) — A cargo plugin for showing a tree-like overview of a crate's modules.
  * [cargo-multi](https://crates.io/crates/cargo-multi) — runs specified cargo command on multiple crates
  * [cargo-outdated](https://crates.io/crates/cargo-outdated) — displays when newer versions of Rust dependencies are available, or out of date
  * [cargo-rdme](https://github.com/orium/cargo-rdme) [[cargo-rdme](https://crates.io/crates/cargo-rdme)] — Cargo subcommand to create your README from your crate’s documentation. [![build badge](https://github.com/orium/cargo-rdme/workflows/CI/badge.svg)](https://github.com/orium/cargo-rdme/actions?query=workflow%3ACI)
  * [cargo-release](https://crates.io/crates/cargo-release) — tool for releasing git-managed cargo project, build, tag, publish, doc and push [![Rust](https://github.com/crate-ci/cargo-release/actions/workflows/ci.yml/badge.svg)](https://github.com/crate-ci/cargo-release/actions/workflows/rust.yml)
  * [cargo-script](https://crates.io/crates/cargo-script) — lets people quickly and easily run Rust "scripts" which can make use of Cargo's package ecosystem
  * [cargo-udeps](https://github.com/est31/cargo-udeps) [[cargo-udeps](https://crates.io/crates/cargo-udeps)] — find unused dependencies
  * [cargo-update](https://crates.io/crates/cargo-update) — cargo subcommand for checking and applying updates to installed executables
  * [cargo-watch](https://crates.io/crates/cargo-watch) — utility for cargo to compile projects when sources change
  * [dtolnay/cargo-expand](https://github.com/dtolnay/cargo-expand) — Expand macros in your source code
* CMake
  * [Devolutions/CMakeRust](https://github.com/Devolutions/CMakeRust) <img src="https://img.shields.io/github/stars/Devolutions/CMakeRust?style=social" alt="Stars" width="80"> — useful for integrating a Rust library into a CMake project
  * [SiegeLord/RustCMake](https://github.com/SiegeLord/RustCMake) <img src="https://img.shields.io/github/stars/SiegeLord/RustCMake?style=social" alt="Stars" width="80"> — an example project showing usage of CMake with Rust
* [Fleet](https://github.com/dimensionhq/fleet) <img src="https://img.shields.io/github/stars/dimensionhq/fleet?style=social" alt="Stars" width="80"> [[fleet-rs](https://crates.io/crates/fleet-rs)] - The blazing fast build tool for Rust.
* Github actions
  * [icepuma/rust-action](https://github.com/icepuma/rust-action) — rust github action
  * [peaceiris/actions-mdbook](https://github.com/peaceiris/actions-mdbook) — GitHub Actions for mdBook
* [Nix](https://nixos.org/)
  * [nix-community/fenix](https://github.com/nix-community/fenix) — Rust toolchains and rust analyzer nightly for nix [![build-badge](https://github.com/nix-community/fenix/actions/workflows/ci.yml/badge.svg)](https://github.com/nix-community/fenix/actions/workflows/ci.yml)

### Debugging

* GDB
  * [gdbgui](https://github.com/cs01/gdbgui) <img src="https://img.shields.io/github/stars/cs01/gdbgui?style=social" alt="Stars" width="80"> — Browser based frontend for gdb to debug C, C++, Rust, and go.
* LLDB
  * [CodeLLDB](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb) — A LLDB extension for [Visual Studio Code](https://code.visualstudio.com/).

### Deployment

* Docker
  * [emk/rust-musl-builder](https://github.com/emk/rust-musl-builder) — Docker images for compiling static Rust binaries using musl-libc and musl-gcc, with static versions of useful C libraries
  * [kpcyrd/mini-docker-rust](https://github.com/kpcyrd/mini-docker-rust) — An example project for very small rust docker images
  * [liuchong/docker-rustup](https://github.com/liuchong/docker-rustup) — A multiple version (with musl tools) Rust Docker image
  * [LukeMathWalker/cargo-chef](https://github.com/LukeMathWalker/cargo-chef) - A tool and pre-built images for caching compiling remote dependencies between Docker builds.
  * [rust-cross/rust-musl-cross](https://github.com/rust-cross/rust-musl-cross) — Docker images for compiling static Rust binaries using musl-cross [![Build](https://github.com/rust-cross/rust-musl-cross/workflows/Build/badge.svg)](https://github.com/rust-cross/rust-musl-cross/actions?query=workflow%3ABuild)
  * [rust-lang-nursery/docker-rust](https://github.com/rust-lang/docker-rust) — the official Rust Docker image
* Heroku
  * [emk/heroku-buildpack-rust](https://github.com/emk/heroku-buildpack-rust) — A buildpack for Rust applications on Heroku
* [MarcoIeni/release-plz](https://github.com/MarcoIeni/release-plz) [[release-plz](https://crates.io/crates/release-plz)] — Release Rust crates from CI, with changelog generation and semver check. [![build badge](https://github.com/MarcoIeni/release-plz/workflows/CI/badge.svg)](https://github.com/MarcoIeni/release-plz/actions)

### Embedded

[Rust Embedded](https://rust-embedded.org/) focuses on improving the end-to-end experience of using Rust in resource-constrained environments and non-traditional platforms. See [awesome-embedded-rust](https://github.com/rust-embedded/awesome-embedded-rust) for a curated, and more extended list of embedded Rust resources.

* Arduino
  * [avr-rust/ruduino](https://github.com/avr-rust/ruduino) Reusable components for the Arduino Uno.
* Cross compiling
  * [japaric/rust-cross](https://github.com/japaric/rust-cross) — everything you need to know about cross compiling Rust programs
  * [japaric/xargo](https://github.com/japaric/xargo) <img src="https://img.shields.io/github/stars/japaric/xargo?style=social" alt="Stars" width="80"> — effortless cross compilation of Rust programs to custom bare-metal targets like ARM Cortex-M
* Espressif
  * [esp-rs](https://github.com/esp-rs) home to a number of community projects enabling the use of the Rust programming language on various SoCs and modules produced by Espressif Systems.
* Firmware
  * [oreboot/oreboot](https://github.com/oreboot/oreboot) <img src="https://img.shields.io/github/stars/oreboot/oreboot?style=social" alt="Stars" width="80"> — oreboot is a fork of coreboot, with C removed, written in Rust
* nRF
  * [nrf-rs/nrf-hal](https://github.com/nrf-rs/nrf-hal) — A Rust HAL for the nRF family of devices

### FFI

See also [Foreign Function Interface](https://doc.rust-lang.org/book/first-edition/ffi.html), [The Rust FFI Omnibus](http://jakegoulding.com/rust-ffi-omnibus/) (a collection of examples of using code written in Rust from other languages) and [FFI examples written in Rust](https://github.com/alexcrichton/rust-ffi-examples).

* C
  * [mozilla/cbindgen](https://github.com/mozilla/cbindgen) <img src="https://img.shields.io/github/stars/mozilla/cbindgen?style=social" alt="Stars" width="80"> — generates C header files from Rust source files. Used in Gecko for WebRender
  * [Sean1708/rusty-cheddar](https://github.com/Sean1708/rusty-cheddar) — generates C header files from Rust source files
* C#
  * [csbindgen](https://github.com/Cysharp/csbindgen) <img src="https://img.shields.io/github/stars/Cysharp/csbindgen?style=social" alt="Stars" width="80"> - generates C# bindings for Rust source files
* C++
  * [dtolnay/cxx](https://github.com/dtolnay/cxx) <img src="https://img.shields.io/github/stars/dtolnay/cxx?style=social" alt="Stars" width="80"> — Safe interop between Rust and C++ [![build badge](https://img.shields.io/badge/github-dtolnay/cxx-8da0cb?style=for-the-badge&labelColor=555555&logo=github)](https://github.com/dtolnay/cxx)
  * [rust-cpp](https://crates.io/crates/cpp) - Embed C++ code directly in Rust. [![Build status](https://ci.appveyor.com/api/projects/status/uu76vmcrwnjqra0u/branch/master?svg=true)](https://ci.appveyor.com/project/mystor/rust-cpp/branch/master)
  * [rust-lang/rust-bindgen](https://github.com/rust-lang/rust-bindgen) — A Rust bindings generator
* Erlang
  * [rusterlium/rustler](https://github.com/rusterlium/rustler) <img src="https://img.shields.io/github/stars/rusterlium/rustler?style=social" alt="Stars" width="80"> — safe Rust bridge for creating Erlang NIF functions
* Java
  * [bennettanderson/rjni](https://github.com/benanders/rjni) <img src="https://img.shields.io/github/stars/benanders/rjni?style=social" alt="Stars" width="80"> — use Java from Rust
  * [drrb/java-rust-example](https://github.com/drrb/java-rust-example) — use Rust from Java
  * [j4rs](https://crates.io/crates/j4rs) — use Java from Rust
  * [jni](https://crates.io/crates/jni) — use Rust from Java
  * [jni-sys](https://crates.io/crates/jni-sys) — Rust definitions corresponding to jni.h
  * [rucaja](https://crates.io/crates/rucaja) — use Java from Rust
* Lua
  * [jcmoyer/rust-lua53](https://github.com/jcmoyer/rust-lua53) — Lua 5.3 bindings for Rust
  * [lilyball/rust-lua](https://github.com/lilyball/rust-lua) — Safe Rust bindings to Lua 5.1
  * [mlua-rs/mlua](https://github.com/mlua-rs/mlua) — High level Lua 5.4/5.3/5.2/5.1 (including LuaJIT) and Roblox Luau bindings to Rust with async/await support [![build badge](https://github.com/mlua-rs/mlua/workflows/CI/badge.svg)](https://github.com/mlua-rs/mlua/actions)
  * [tickbh/td_rlua](https://github.com/tickbh/td_rlua) <img src="https://img.shields.io/github/stars/tickbh/td_rlua?style=social" alt="Stars" width="80"> [[td_rlua](https://crates.io/crates/td_rlua)] — Zero-cost high-level lua 5.3 wrapper for Rust
  * [tomaka/hlua](https://github.com/tomaka/hlua) <img src="https://img.shields.io/github/stars/tomaka/hlua?style=social" alt="Stars" width="80"> — Rust library to interface with Lua
* mruby
  * [anima-engine/mrusty](https://github.com/anima-engine/mrusty) — mruby safe bindings for Rust
* Node.js
  * [infinyon/node-bindgen](https://github.com/infinyon/node-bindgen) - Easy way to generate nodejs module using Rust
  * [neon-bindings/neon](https://github.com/neon-bindings/neon) — Rust bindings for writing safe and fast native Node.js modules
  * [zhangyuang/node-ffi-rs](https://github.com/zhangyuang/node-ffi-rs) — A module written in Rust and N-API provides interface (FFI) features for Node.js
* Objective-C
  * [SSheldon/rust-objc](https://github.com/SSheldon/rust-objc) — Objective-C Runtime bindings and wrapper for Rust
* PHP
  * [phper-framework/phper](https://github.com/phper-framework/phper) — The framework that allows us to write PHP extensions using pure and safe Rust whenever possible
* Prolog
  * [mthom/scryer-prolog](https://github.com/mthom/scryer-prolog/) — Scryer Prolog is a free software ISO Prolog system written in Rust
* Python
  * [dgrunwald/rust-cpython](https://github.com/dgrunwald/rust-cpython) — Python bindings
  * [getsentry/milksnake](https://github.com/getsentry/milksnake) <img src="https://img.shields.io/github/stars/getsentry/milksnake?style=social" alt="Stars" width="80"> — extension for python setuptools that allows you to distribute dynamic linked libraries in Python wheels in the most portable way imaginable.
  * [PyO3/PyO3](https://github.com/PyO3/PyO3) <img src="https://img.shields.io/github/stars/PyO3/PyO3?style=social" alt="Stars" width="80"> — Rust bindings for the Python interpreter
  * [RustPython](https://github.com/RustPython/RustPython) <img src="https://img.shields.io/github/stars/RustPython/RustPython?style=social" alt="Stars" width="80"> — A Python Interpreter written in Rust [![Build Status](https://github.com/RustPython/RustPython/workflows/CI/badge.svg)](https://github.com/RustPython/RustPython/actions?query=workflow%3ACI)
* Ruby
  * [d-unsed/ruru](https://github.com/d-unsed/ruru) — native Ruby extensions written in Rust
  * [danielpclark/rutie](https://github.com/danielpclark/rutie) <img src="https://img.shields.io/github/stars/danielpclark/rutie?style=social" alt="Stars" width="80"> — native Ruby extensions written in Rust and vice versa
* Web Assembly
  * [rhysd/wain](https://github.com/rhysd/wain) <img src="https://img.shields.io/github/stars/rhysd/wain?style=social" alt="Stars" width="80"> - wain: WebAssembly INterpreter from scratch in Safe Rust with zero dependency [![build badge](https://github.com/rhysd/wain/workflows/CI/badge.svg?branch=master&event=push)](https://github.com/rhysd/wain/actions?query=workflow%3ACI+branch%3Amaster+event%3Apush)
  * [rustwasm/wasm-bindgen](https://github.com/rustwasm/wasm-bindgen) — A project for facilitating high-level interactions between wasm modules and JS.
  * [rustwasm/wasm-pack](https://github.com/rustwasm/wasm-pack) — :package: :sparkles: pack up the wasm and publish it to npm!

### Formatters

* [dprint](https://github.com/dprint/dprint) <img src="https://img.shields.io/github/stars/dprint/dprint?style=social" alt="Stars" width="80"> — A pluggable and configurable code formatting platform [![build badge](https://github.com/dprint/dprint/workflows/CI/badge.svg)](https://github.com/dprint/dprint/actions?query=workflow%3ACI)
* [Prettier Rust](https://github.com/jinxdash/prettier-plugin-rust) — An opinionated Rust code formatter that autofixes bad syntax ([Prettier](https://prettier.io/) community plugin)
* [rustfmt](https://github.com/rust-lang/rustfmt) <img src="https://img.shields.io/github/stars/rust-lang/rustfmt?style=social" alt="Stars" width="80"> — Rust code formatter maintained by the Rust team and included in cargo

### IDEs

See also [Are we (I)DE yet?](https://areweideyet.com/) and [Rust Tools](https://www.rust-lang.org/tools).

  * [Atom](https://github.blog/2022-06-08-sunsetting-atom/)
    * [rust-lang/atom-ide-rust](https://github.com/rust-lang/atom-ide-rust) — Rust IDE support for Atom, powered by the Rust Language Server (RLS)
  * [Eclipse](https://www.eclipse.org/)
    * [Eclipse Corrosion](https://github.com/eclipse-corrosion/corrosion)
  * [Emacs](https://www.gnu.org/software/emacs/)
    * [emacs-racer](https://github.com/racer-rust/emacs-racer) — Autocompletion (see also [company](https://company-mode.github.io) and [auto-complete](https://github.com/auto-complete/auto-complete))
    * [flycheck-rust](https://github.com/flycheck/flycheck-rust) — Rust support for [Flycheck](https://github.com/flycheck/flycheck) <img src="https://img.shields.io/github/stars/flycheck/flycheck?style=social" alt="Stars" width="80">
    * [rust-mode](https://github.com/rust-lang/rust-mode) — Rust Major Mode
    * [rustic](https://github.com/brotzeit/rustic) <img src="https://img.shields.io/github/stars/brotzeit/rustic?style=social" alt="Stars" width="80"> - Rust development environment for Emacs [![build badge](https://github.com/brotzeit/rustic/workflows/CI/badge.svg)](https://github.com/brotzeit/rustic/actions?query=workflow%3ACI)
  * [gitpod.io](https://gitpod.io) — Online IDE with full Rust support based on Rust Language Server
  * [gnome-builder](https://wiki.gnome.org/Apps/Builder) native support for rust and cargo since Version 3.22.2
  * [IntelliJ](https://www.jetbrains.com/idea/)
    * [intellij-rust/intellij-rust](https://github.com/intellij-rust/intellij-rust) —
  * [Kakoune](http://kakoune.org/)
    * [kak-lsp/kak-lsp](https://github.com/kak-lsp/kak-lsp/) — [LSP](https://microsoft.github.io/language-server-protocol/) client. Implemented in Rust and supports rls out of the box.
  * [lapce](https://github.com/lapce/lapce) <img src="https://img.shields.io/github/stars/lapce/lapce?style=social" alt="Stars" width="80"> — Lightning-fast and Powerful Code Editor written in Rust. [![build badge](https://github.com/lapce/lapce/actions/workflows/release.yml/badge.svg)](https://github.com/lapce/lapce/actions/workflows/release.yml)
  * [Ride](https://github.com/madeso/ride) <img src="https://img.shields.io/github/stars/madeso/ride?style=social" alt="Stars" width="80"> —
  * [Sublime Text](https://www.sublimetext.com/)
    * [rust-lang/rust-enhanced](https://github.com/rust-lang/rust-enhanced) — official Rust package
  * [Vim](https://vim.sourceforge.io/) — the ubiquitous text editor
    * [autozimu/LanguageClient-neovim](https://github.com/autozimu/LanguageClient-neovim) — [LSP](https://microsoft.github.io/language-server-protocol/) client. Implemented in Rust and supports rls out of the box.
    * [crates.nvim](https://github.com/Saecki/crates.nvim) - plugin that helps to managing crates.io dependencies.
    * [rust-tools.nvim](https://github.com/simrat39/rust-tools.nvim) - Tools for better development in rust using neovim's builtin lsp
    * [rust.vim](https://github.com/rust-lang/rust.vim) — provides file detection, syntax highlighting, formatting, Syntastic integration, and more.
    * [vim-racer](https://github.com/racer-rust/vim-racer) — allows vim to use [Racer](https://github.com/racer-rust/racer) <img src="https://img.shields.io/github/stars/racer-rust/racer?style=social" alt="Stars" width="80"> for Rust code completion and navigation.
  * Visual Studio
    * [dgriffen/rls-vs2017](https://github.com/ZoeyR/rls-vs2017) — Rust support for Visual Studio 2017 Preview [![build badge](https://ci.appveyor.com/api/projects/status/d2lxlincwninhsng?svg=true)](https://ci.appveyor.com/project/dgriffen/rls-vs2017)
    * [PistonDevelopers/VisualRust](https://github.com/PistonDevelopers/VisualRust) <img src="https://img.shields.io/github/stars/PistonDevelopers/VisualRust?style=social" alt="Stars" width="80"> — A Visual Studio extension for Rust [![Build status](https://ci.appveyor.com/api/projects/status/5nw5no10jj0y4p3f?svg=true)](https://ci.appveyor.com/project/vosen/visualrust)
  * [Visual Studio Code](https://code.visualstudio.com/)
    * [Better TOML](https://marketplace.visualstudio.com/items?itemName=bungcip.better-toml) - TOML support in vscode
    * [CodeLLDB](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb) — A LLDB extension
    * [crates](https://github.com/serayuzgur/crates) <img src="https://img.shields.io/github/stars/serayuzgur/crates?style=social" alt="Stars" width="80"> — crates is an extension for crates.io dependencies. [![build badge](https://img.shields.io/vscode-marketplace/v/serayuzgur.crates.svg)](https://github.com/serayuzgur/crates)
    * [Prettier - Code formatter (Rust)](https://marketplace.visualstudio.com/items?itemName=jinxdash.prettier-rust) — Opinionated Rust code formatter that autofixes bad syntax ([Prettier](https://prettier.io/) community plugin)
    * [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) — An alternative rust language server to the RLS
    * [rust-lang/rls-vscode](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust) — Rust support for Visual Studio Code (supports both RLS and rust-analyzer)

### Profiling

* [Bencher](https://github.com/bencherdev/bencher) <img src="https://img.shields.io/github/stars/bencherdev/bencher?style=social" alt="Stars" width="80"> - A suite of continuous benchmarking tools designed to catch performance regressions in CI
* [bheisler/criterion.rs](https://github.com/bheisler/criterion.rs) — Statistics-driven benchmarking library for Rust
* [Bytehound](https://github.com/koute/bytehound) <img src="https://img.shields.io/github/stars/koute/bytehound?style=social" alt="Stars" width="80"> — A memory profiler for Linux
* [Divan](https://github.com/nvzqz/divan) <img src="https://img.shields.io/github/stars/nvzqz/divan?style=social" alt="Stars" width="80"> — Simple yet powerful benchmarking library with allocation profiling
* [ellisonch/rust-stopwatch](https://github.com/ellisonch/rust-stopwatch) — A stopwatch library
* FlameGraphs
  * [llogiq/flame](https://github.com/llogiq/flame) <img src="https://img.shields.io/github/stars/llogiq/flame?style=social" alt="Stars" width="80"> —
  * [mrhooray/torch](https://github.com/mrhooray/torch) <img src="https://img.shields.io/github/stars/mrhooray/torch?style=social" alt="Stars" width="80"> — generates FlameGraphs based on DWARF Debug Info
* [sharkdp/hyperfine](https://github.com/sharkdp/hyperfine) <img src="https://img.shields.io/github/stars/sharkdp/hyperfine?style=social" alt="Stars" width="80"> — A command-line benchmarking tool

### Services

* [deps.rs](https://github.com/deps-rs/deps.rs) — Detect outdated or insecure dependencies
* [docs.rs](https://docs.rs) — Automatic documentation generation of crates

### Static analysis

[[assert](https://crates.io/keywords/assert), [static](https://crates.io/keywords/static)]

* [facebookexperimental/MIRAI](https://github.com/facebookexperimental/mirai) <img src="https://img.shields.io/github/stars/facebookexperimental/mirai?style=social" alt="Stars" width="80"> — an abstract interpreter operating on Rust's mid-level intermediate representation (MIR) [![Continuous Integration](https://github.com/facebookexperimental/mirai/actions/workflows/rust.yml/badge.svg)](https://github.com/facebookexperimental/mirai/actions/workflows/rust.yml)
* [static_assertions](https://crates.io/crates/static_assertions) — Compile-time assertions to ensure that invariants are met

### Testing

[[test](https://crates.io/keywords/test), [testing](https://crates.io/keywords/testing)]

* Code Coverage
  * [tarpaulin](https://crates.io/crates/cargo-tarpaulin) — A code coverage tool designed for Rust
* Continuous Integration
  * [trust](https://github.com/japaric/trust) <img src="https://img.shields.io/github/stars/japaric/trust?style=social" alt="Stars" width="80"> — A Travis CI and AppVeyor template to test your Rust crate on 5 architectures and publish binary releases of it for Linux, macOS and Windows
* Frameworks and Runners
  * [AlKass/polish](https://github.com/AlKass/polish) <img src="https://img.shields.io/github/stars/AlKass/polish?style=social" alt="Stars" width="80"> — Mini Testing/Test-Driven Framework [![Crates Package Status](https://img.shields.io/crates/v/polish.svg)](https://crates.io/crates/polish)
  * [cargo-dinghy](https://crates.io/crates/cargo-dinghy/) - A cargo extension to simplify running library tests and benches on smartphones and other small processor devices.
  * [cucumber](https://crates.io/crates/cucumber) [![Latest Version](https://img.shields.io/crates/v/cucumber.svg)](https://crates.io/crates/cucumber) — An implementation of the Cucumber testing framework for Rust. Fully native, no external test runners or dependencies. [![Build Status](https://github.com/cucumber-rs/cucumber/workflows/CI/badge.svg?branch=master)](https://github.com/cucumber-rs/cucumber)
  * [d-e-s-o/test-log](https://github.com/d-e-s-o/test-log) [[test-log](https://crates.io/crates/test-log)] — A replacement of the `#[test]` attribute that initializes logging and/or tracing infrastructure before running tests. [![GitHub Workflow Status](https://github.com/d-e-s-o/test-log/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/d-e-s-o/test-log/actions/workflows/test.yml)
  * [demonstrate](https://crates.io/crates/demonstrate) — Declarative Testing Framework [![Build Status](https://github.com/aubaugh/demonstrate/workflows/Continuous%20Integration/badge.svg?branch=master)](https://github.com/aubaugh/demonstrate)
  * [GoogleTest Rust](https://crates.io/crates/googletest) — Powerful test assertion framework based on the C++ test library GoogleTest [![Build Status](https://github.com/google/googletest-rust/workflows/CI/badge.svg)](https://github.com/google/googletest-rust/actions?query=workflow%3ACI+branch%3Amain)
  * [rstest](https://crates.io/crates/rstest) — Fixture-based test framework for Rust [![Build Status](https://github.com/la10736/rstest/workflows/Test/badge.svg?branch=master)](https://github.com/la10736/rstest/actions)
  * [speculate](https://crates.io/crates/speculate) — An RSpec inspired minimal testing framework for Rust
* Mocking and Test Data
  * [asomers/mockall](https://github.com/asomers/mockall) <img src="https://img.shields.io/github/stars/asomers/mockall?style=social" alt="Stars" width="80"> [[mockall](https://crates.io/crates/mockall)] — A powerful mock object library for Rust. [![Cirrus Build Status](https://api.cirrus-ci.com/github/asomers/mockall.svg)](https://cirrus-ci.com/github/asomers/mockall)
  * [fake-rs](https://github.com/cksac/fake-rs) —  A library for generating fake data
  * [goldenfile](https://github.com/calder/rust-goldenfile) <img src="https://img.shields.io/github/stars/calder/rust-goldenfile?style=social" alt="Stars" width="80"> [[goldenfile](https://crates.io/crates/goldenfile)] - A library providing a simple API for goldenfile testing.
  * [httpmock](https://github.com/alexliesenfeld/httpmock) <img src="https://img.shields.io/github/stars/alexliesenfeld/httpmock?style=social" alt="Stars" width="80"> — HTTP mocking [![build badge](https://dev.azure.com/alexliesenfeld/httpmock/_apis/build/status/alexliesenfeld.httpmock?branchName=master)](https://dev.azure.com/alexliesenfeld/httpmock/_build/latest?definitionId=2&branchName=master)
  * [mockiato](https://crates.io/crates/mockiato) — A strict, yet friendly mocking library for Rust 2018
  * [mockito](https://crates.io/crates/mockito) — HTTP mocking
  * [nrxus/faux](https://github.com/nrxus/faux/) <img src="https://img.shields.io/github/stars/nrxus/faux?style=social" alt="Stars" width="80"> [![Latest Version](https://img.shields.io/crates/v/faux.svg)](https://crates.io/crates/faux) — A library to create mocks out of structs. ![build](https://github.com/nrxus/faux/workflows/test/badge.svg?branch=master)
  * [synth](https://github.com/shuttle-hq/synth/) <img src="https://img.shields.io/github/stars/shuttle-hq/synth?style=social" alt="Stars" width="80"> — Generate database data declaratively. [![build](https://github.com/shuttle-hq/synth/actions/workflows/synth-test.yml/badge.svg)](https://github.com/shuttle-hq/synth)
* Mutation Testing
  * [cargo-mutants](https://github.com/sourcefrog/cargo-mutants) [[cargo-mutants](https://crates.io/crates/cargo-mutants)] - Finds inadequately tested code by injecting mutations, no source changes required. [![build badge](https://github.com/sourcefrog/cargo-mutants/actions/workflows/tests.yml/badge.svg?branch=main&event=push)](https://github.com/sourcefrog/cargo-mutants/actions/workflows/tests.yml?query=branch%3Amain)
  * [mutagen](https://github.com/llogiq/mutagen) <img src="https://img.shields.io/github/stars/llogiq/mutagen?style=social" alt="Stars" width="80"> [[mutagen](https://crates.io/crates/mutagen)] — A source-level mutation testing framework (nightly only)
* Property Testing and Fuzzing
  * [proptest](https://crates.io/crates/proptest) — property testing framework inspired by the [Hypothesis](https://hypothesis.works/) framework for Python
  * [quickcheck](https://crates.io/crates/quickcheck) — A Rust implementation of [QuickCheck](https://wiki.haskell.org/Introduction_to_QuickCheck1)
  * [rust-fuzz/afl.rs](https://github.com/rust-fuzz/afl.rs) — A Rust fuzzer, using [AFL](https://lcamtuf.coredump.cx/afl/)

### Transpiling

* [BayesWitnesses/m2cgen](https://github.com/BayesWitnesses/m2cgen) <img src="https://img.shields.io/github/stars/BayesWitnesses/m2cgen?style=social" alt="Stars" width="80"> — A CLI tool to transpile trained classic machine learning models into a native Rust code with zero dependencies. [![GitHub Actions Status](https://github.com/BayesWitnesses/m2cgen/workflows/GitHub%20Actions/badge.svg?branch=master)](https://github.com/BayesWitnesses/m2cgen/actions)
* [immunant/c2rust](https://github.com/immunant/c2rust) <img src="https://img.shields.io/github/stars/immunant/c2rust?style=social" alt="Stars" width="80"> — C to Rust translator and cross checker built atop Clang/LLVM.
* [jameysharp/corrode](https://github.com/jameysharp/corrode) <img src="https://img.shields.io/github/stars/jameysharp/corrode?style=social" alt="Stars" width="80"> — A C to Rust translator written in Haskell.

## Libraries

* [perf-monitor-rs](https://github.com/larksuite/perf-monitor-rs) — A toolkit designed to be a foundation for applications to monitor their performance. [![crates.io](https://img.shields.io/crates/v/perf_monitor.svg)](https://crates.io/crates/perf_monitor)

### Artificial Intelligence

#### Genetic algorithms

* [innoave/genevo](https://github.com/innoave/genevo) <img src="https://img.shields.io/github/stars/innoave/genevo?style=social" alt="Stars" width="80"> — Execute genetic algorithm (GA) simulations in a customizable and extensible way.
* [m-decoster/RsGenetic](https://github.com/m-decoster/RsGenetic) — Genetic Algorithm library in Rust. In maintenance mode.
* [Martin1887/oxigen](https://github.com/Martin1887/oxigen) <img src="https://img.shields.io/github/stars/Martin1887/oxigen?style=social" alt="Stars" width="80"> — Fast, parallel, extensible and adaptable genetic algorithm library. A example using this library solves the N Queens problem for N = 255 in only few seconds and using less than 1 MB of RAM.
* [pkalivas/radiate](https://github.com/pkalivas/radiate) <img src="https://img.shields.io/github/stars/pkalivas/radiate?style=social" alt="Stars" width="80"> — A customizable parallel genetic programming engine capable of evolving solutions for supervised, unsupervised, and reinforcement learning problems. Comes with complete and customizable implementation of NEAT and Evtree.![Crates.io](https://img.shields.io/crates/v/radiate)
* [willi-kappler/darwin-rs](https://github.com/willi-kappler/darwin-rs) — Evolutionary algorithms with Rust

#### Machine learning

See [[Machine learning](https://crates.io/keywords/machine-learning)]

See also [About Rust’s Machine Learning Community](https://medium.com/@autumn_eng/about-rust-s-machine-learning-community-4cda5ec8a790#.hvkp56j3f) and [Are we learning yet?](https://www.arewelearningyet.com).

* [autumnai/leaf](https://github.com/autumnai/leaf) <img src="https://img.shields.io/github/stars/autumnai/leaf?style=social" alt="Stars" width="80"> — Open Machine Intelligence framework.. Abandoned project. The most updated fork is [spearow/juice]( https://github.com/spearow/juice).
* [burn](https://github.com/tracel-ai/burn) <img src="https://img.shields.io/github/stars/tracel-ai/burn?style=social" alt="Stars" width="80"> - A Flexible and Comprehensive Deep Learning Framework in Rust.
* [coreylowman/dfdx](https://github.com/coreylowman/dfdx) <img src="https://img.shields.io/github/stars/coreylowman/dfdx?style=social" alt="Stars" width="80"> — CUDA accelearted machine learning framework that leverages many of Rust's unique features. ![Crates.io](https://img.shields.io/crates/v/dfdx)
* [huggingface/candle](https://github.com/huggingface/candle) <img src="https://img.shields.io/github/stars/huggingface/candle?style=social" alt="Stars" width="80"> [[candle-core](https://crates.io/crates/candle-core)]- a minimalist ML framework with a focus on easiness of use and on performance (including GPU support)
* [huggingface/tokenizers](https://github.com/huggingface/tokenizers) <img src="https://img.shields.io/github/stars/huggingface/tokenizers?style=social" alt="Stars" width="80"> - Hugging Face's tokenizers for modern NLP pipelines written in Rust (original implementation) with bindings for Python. [![Build Status](https://github.com/huggingface/tokenizers/workflows/Rust/badge.svg?branch=master)](https://github.com/huggingface/tokenizers/actions)
* [LaurentMazare/tch-rs](https://github.com/LaurentMazare/tch-rs) — Rust language bindings for PyTorch.
* [maciejkula/rustlearn](https://github.com/maciejkula/rustlearn) <img src="https://img.shields.io/github/stars/maciejkula/rustlearn?style=social" alt="Stars" width="80"> — Machine learning crate for Rust. [![Circle CI](https://circleci.com/gh/maciejkula/rustlearn.svg?style=svg)](https://app.circleci.com/pipelines/github/maciejkula/rustlearn)
* [rust-ml/linfa](https://github.com/rust-ml/linfa) — Machine learning framework.
* [smartcorelib/smartcore](https://github.com/smartcorelib/smartcore) <img src="https://img.shields.io/github/stars/smartcorelib/smartcore?style=social" alt="Stars" width="80"> — Machine Learning Library In Rust [![Build Status](https://img.shields.io/circleci/build/github/smartcorelib/smartcore)](https://smartcorelib.org/)
* [tensorflow/rust](https://github.com/tensorflow/rust) <img src="https://img.shields.io/github/stars/tensorflow/rust?style=social" alt="Stars" width="80"> — Rust language bindings for TensorFlow.

#### OpenAI

* [64bit/async-openai](https://github.com/64bit/async-openai) [[async-openai](https://crates.io/crates/async-openai)] — Ergonomic Rust bindings for OpenAI API based on OpenAPI spec.
* [zurawiki/tiktoken-rs](https://github.com/zurawiki/tiktoken-rs) [[tiktoken-rs](https://crates.io/crates/tiktoken-rs)] — Rust library for tokenizing text with OpenAI models using tiktoken. [![CI](https://github.com/zurawiki/tiktoken-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/zurawiki/tiktoken-rs/actions/workflows/ci.yml)

### Astronomy

[[astronomy](https://crates.io/keywords/astronomy)]

* [cds-astro/aladin-lite](https://github.com/cds-astro/aladin-lite) - Web application for visualizing spatial and planetary image surveys in different projections
* [fitsio](https://crates.io/crates/fitsio) — fits interface library wrapping cfitsio
* [flosse/rust-sun](https://github.com/flosse/rust-sun) [[sun](https://crates.io/crates/sun)] — A rust port of the JS library suncalc
* [saurvs/astro-rust](https://github.com/saurvs/astro-rust) — astronomy for Rust

### Asynchronous

* [async-std](https://async.rs/) [[async-std](https://crates.io/crates/async-std)] - Async version of the Rust standard library [![CI](https://github.com/async-rs/async-std/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/async-rs/async-std/actions/workflows/ci.yml)
* [dpc/mioco](https://github.com/dpc/mioco) <img src="https://img.shields.io/github/stars/dpc/mioco?style=social" alt="Stars" width="80"> — Scalable, coroutine-based, asynchronous IO handling library
* [mio](https://github.com/tokio-rs/mio) <img src="https://img.shields.io/github/stars/tokio-rs/mio?style=social" alt="Stars" width="80"> — MIO is a lightweight IO library for Rust with a focus on adding as little overhead as possible over the OS abstractions
* [rust-lang/futures-rs](https://github.com/rust-lang/futures-rs) — Zero-cost futures in Rust
* [TeaEntityLab/fpRust](https://github.com/TeaEntityLab/fpRust) <img src="https://img.shields.io/github/stars/TeaEntityLab/fpRust?style=social" alt="Stars" width="80"> — Monad/MonadIO, Handler, Coroutine/doNotation, Functional Programming features for Rust
* [Xudong-Huang/may](https://github.com/Xudong-Huang/may) — rust stackful coroutine library
* [zonyitoo/coio-rs](https://github.com/zonyitoo/coio-rs) — A coroutine I/O library with a working-stealing scheduler

### Audio and Music

[[audio](https://crates.io/keywords/audio)]

* [hound](https://crates.io/crates/hound) — A WAV encoding and decoding library
* [insomnimus/nodi](https://github.com/insomnimus/nodi) <img src="https://img.shields.io/github/stars/insomnimus/nodi?style=social" alt="Stars" width="80"> [[nodi](https://crates.io/crates/nodi)] — A library for playback and abstraction of MIDI files. [![build badge](https://github.com/insomnimus/nodi/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/insomnimus/nodi/actions)
* [jhasse/ears](https://github.com/jhasse/ears) <img src="https://img.shields.io/github/stars/jhasse/ears?style=social" alt="Stars" width="80"> — A simple library to play Sounds and Musics, on top of OpenAL and libsndfile
* [musitdev/portmidi-rs](https://github.com/musitdev/portmidi-rs) — [PortMidi](https://portmedia.sourceforge.net/portmidi/) bindings
* [ozankasikci/rust-music-theory](https://github.com/ozankasikci/rust-music-theory) — A Rust music theory library
* [pdeljanov/Symphonia](https://github.com/pdeljanov/Symphonia) <img src="https://img.shields.io/github/stars/pdeljanov/Symphonia?style=social" alt="Stars" width="80"> — A pure Rust audio decoding and media demuxing library supporting AAC, FLAC, MP3, MP4, OGG, Vorbis, and WAV.
* [RustAudio](https://github.com/RustAudio)
  * [RustAudio/cpal](https://github.com/RustAudio/cpal) <img src="https://img.shields.io/github/stars/RustAudio/cpal?style=social" alt="Stars" width="80"> - Low-level cross-platform audio I/O library in pure Rust. [![Actions Status](https://github.com/RustAudio/cpal/workflows/cpal/badge.svg?branch=master)](https://github.com/RustAudio/cpal/actions)
  * [RustAudio/rodio](https://github.com/RustAudio/rodio) <img src="https://img.shields.io/github/stars/RustAudio/rodio?style=social" alt="Stars" width="80"> — A Rust audio playback library
  * [RustAudio/rust-portaudio](https://github.com/RustAudio/rust-portaudio) — PortAudio bindings
* [Serial-ATA/lofty-rs](https://github.com/Serial-ATA/lofty-rs) [[lofty](https://crates.io/crates/lofty)] — A library for reading and editing the metadata of various audio formats [![build badge](https://github.com/Serial-ATA/lofty-rs/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Serial-ATA/lofty-rs/actions)

### Authentication

* [constantoine/totp-rs](https://github.com/constantoine/totp-rs) [[totp-rs](https://crates.io/crates/totp-rs)] — 2fa library to generate and verify TOTP-based tokens ![Build Status](https://github.com/constantoine/totp-rs/workflows/Rust/badge.svg)
* [Keats/jsonwebtoken](https://github.com/Keats/jsonwebtoken) <img src="https://img.shields.io/github/stars/Keats/jsonwebtoken?style=social" alt="Stars" width="80"> — [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token) lib in rust
* [oauth2](https://github.com/ramosbugs/oauth2-rs) <img src="https://img.shields.io/github/stars/ramosbugs/oauth2-rs?style=social" alt="Stars" width="80"> — Extensible, strongly-typed Rust OAuth2 client library
* [oxide-auth](https://github.com/HeroicKatora/oxide-auth) — A OAuth2 server library, for use in combination with actix or other frontends, featuring a set of configurable and pluggable backends [![Build Status](https://api.cirrus-ci.com/github/HeroicKatora/oxide-auth.svg?branch=master)](https://cirrus-ci.com/github/HeroicKatora/oxide-auth)
* [sgrust01/jwtvault](https://github.com/sgrust01/jwtvault) <img src="https://img.shields.io/github/stars/sgrust01/jwtvault?style=social" alt="Stars" width="80"> — Async library to manage and orchestrate JWT workflow
* [yup-oauth2](https://github.com/dermesser/yup-oauth2) — An oauth2 client implementation providing the Device, Installed and Service Account flows

### Automotive

* [idletea/tokio-socketcan](https://github.com/idletea/tokio-socketcan) [[tokio-socketcan](https://crates.io/crates/tokio-socketcan)] — Linux SocketCAN support for tokio based on the socketcan crate
* [marcelbuesing/can-dbc](https://github.com/marcelbuesing/can-dbc) [[can-dbc](https://crates.io/crates/can-dbc)] — A parser for the DBC format
* [marcelbuesing/tokio-socketcan-bcm](https://github.com/marcelbuesing/tokio-socketcan-bcm) [[tokio-socketcan-bcm](https://crates.io/crates/tokio-socketcan-bcm)] — Linux SocketCAN BCM support for tokio
* [mbr/socketcan](https://github.com/socketcan-rs/socketcan-rs) <img src="https://img.shields.io/github/stars/socketcan-rs/socketcan-rs?style=social" alt="Stars" width="80"> [[socketcan](https://crates.io/crates/socketcan)] — Linux SocketCAN library
* [Sensirion/lin-bus](https://github.com/Sensirion/lin-bus-rs) [[lin-bus](https://crates.io/crates/lin-bus)] — LIN bus driver traits and protocol implementation [![build badge](https://circleci.com/gh/Sensirion/lin-bus-rs.svg?style=svg)](https://app.circleci.com/pipelines/github/Sensirion/lin-bus-rs)

### Bioinformatics

* [Rust-Bio](https://github.com/rust-bio) — bioinformatics libraries in Rust.

### Caching

* [06chaynes/http-cache](https://github.com/06chaynes/http-cache) [[http-cache](https://crates.io/crates/http-cache)] - A caching middleware that follows HTTP caching rules [![build badge](https://github.com/06chaynes/http-cache/workflows/http-cache/badge.svg)](https://github.com/06chaynes/http-cache/actions/workflows/http-cache.yml)
* [aisk/rust-memcache](https://github.com/aisk/rust-memcache) — Memcached client library
* [al8n/stretto](https://github.com/al8n/stretto) <img src="https://img.shields.io/github/stars/al8n/stretto?style=social" alt="Stars" width="80"> - A high performance thread-safe memory-bound Rust cache [![build badge](https://github.com/al8n/stretto/actions/workflows/ci.yml/badge.svg)](https://github.com/al8n/stretto/actions/workflows/ci.yml)
* [jaemk/cached](https://github.com/jaemk/cached) <img src="https://img.shields.io/github/stars/jaemk/cached?style=social" alt="Stars" width="80"> — Simple function caching/memoization
* [moka-rs/moka](https://github.com/moka-rs/moka) - A high performance concurrent caching library for Rust inspired by the Caffeine library for Java [![build badge](https://github.com/moka-rs/moka/workflows/CI/badge.svg)](https://github.com/moka-rs/moka/actions/workflows/CI.yml)
* [mozilla/sccache](https://github.com/mozilla/sccache/) <img src="https://img.shields.io/github/stars/mozilla/sccache?style=social" alt="Stars" width="80"> - Shared Compilation Cache, great for Rust compilation
* [zkat/cacache-rs](https://github.com/zkat/cacache-rs) - A high-performance, concurrent, content-addressable disk cache, optimized for async APIs [![build badge](https://github.com/zkat/cacache-rs/workflows/CI/badge.svg)](https://github.com/zkat/cacache-rs/actions/workflows/ci.yml)

### Cloud

* AWS [[aws](https://crates.io/keywords/aws)]
  * [awslabs/aws-lambda-rust-runtime](https://github.com/awslabs/aws-lambda-rust-runtime) [[lambda_runtime](https://crates.io/crates/lambda_runtime)] — A Rust runtime for AWS Lambda [![build badge](https://github.com/awslabs/aws-lambda-rust-runtime/workflows/Rust/badge.svg)](https://github.com/awslabs/aws-lambda-rust-runtime/actions)
  * [awslabs/aws-sdk-rust](https://github.com/awslabs/aws-sdk-rust) - The new AWS SDK for Rust
  * [rusoto/rusoto](https://github.com/rusoto/rusoto) <img src="https://img.shields.io/github/stars/rusoto/rusoto?style=social" alt="Stars" width="80"> —
* Load Balancer
  * [Convey](https://github.com/bparli/convey) <img src="https://img.shields.io/github/stars/bparli/convey?style=social" alt="Stars" width="80"> - Layer 4 Load Balancer with dynamic configuration loading.
* Multi Cloud
  * [Qovery/engine](https://github.com/Qovery/engine) <img src="https://img.shields.io/github/stars/Qovery/engine?style=social" alt="Stars" width="80"> - Abstraction layer library that turns easy application deployment on Cloud providers in just a few minutes

### Command-line

* Argument parsing
  * [clap-rs](https://github.com/clap-rs/clap) [[clap](https://crates.io/crates/clap)] — A simple to use, full featured command-line argument parser
  * [cliparser](https://crates.io/crates/cliparser) — Simple command line parser. [![build badge](https://github.com/sagiegurari/cliparser/workflows/CI/badge.svg?branch=master)](https://github.com/sagiegurari/cliparser/actions)
  * [docopt/docopt.rs](https://github.com/docopt/docopt.rs) [[docopt](https://crates.io/crates/docopt)] — A Rust implementation of [DocOpt](http://docopt.org)
  * [google/argh](https://github.com/google/argh) <img src="https://img.shields.io/github/stars/google/argh?style=social" alt="Stars" width="80"> [[argh](https://crates.io/crates/argh)] — An opinionated Derive-based argument parser optimized for code size [![build badge](https://github.com/google/argh/workflows/Argh/badge.svg?branch=master)](https://github.com/google/argh/actions)
  * [killercup/quicli](https://github.com/killercup/quicli) <img src="https://img.shields.io/github/stars/killercup/quicli?style=social" alt="Stars" width="80"> [[quicli](https://crates.io/crates/quicli)] — quickly build cool CLI apps in Rust
  * [ksk001100/seahorse](https://github.com/ksk001100/seahorse) <img src="https://img.shields.io/github/stars/ksk001100/seahorse?style=social" alt="Stars" width="80"> [[seahorse](https://crates.io/crates/seahorse)] — A minimal CLI framework written in Rust [![Build status](https://github.com/ksk001100/seahorse/workflows/CI/badge.svg?branch=master)](https://github.com/ksk001100/seahorse/actions)
  * [TeXitoi/structopt](https://github.com/TeXitoi/structopt) <img src="https://img.shields.io/github/stars/TeXitoi/structopt?style=social" alt="Stars" width="80"> [[structopt](https://crates.io/crates/structopt)] — parse command line argument by defining a struct
* Data visualization
  * [nukesor/comfy-table](https://github.com/nukesor/comfy-table) [[comfy-table](https://crates.io/crates/comfy-table)] — Beautiful dynamic tables for your cli tools. [![Build status](https://github.com/Nukesor/comfy-table/workflows/Tests/badge.svg?branch=master)](https://github.com/nukesor/comfy-table/actions)
  * [zhiburt/tabled](https://github.com/zhiburt/tabled) <img src="https://img.shields.io/github/stars/zhiburt/tabled?style=social" alt="Stars" width="80"> [[tabled](https://crates.io/crates/tabled)] — An easy to use library for pretty print tables of Rust structs and enums. [![Build Status](https://github.com/zhiburt/tabled/actions/workflows/ci.yml/badge.svg)](https://github.com/zhiburt/tabled/actions)
* Human-centered design
  * [rust-cli/human-panic](https://github.com/rust-cli/human-panic) [[human-panic](https://crates.io/crates/human-panic)] — panic messages for humans
* Line editor
  * [kkawakam/rustyline](https://github.com/kkawakam/rustyline) <img src="https://img.shields.io/github/stars/kkawakam/rustyline?style=social" alt="Stars" width="80"> [[rustyline](https://crates.io/crates/rustyline)] — readline implementation in Rust
  * [MovingtoMars/liner](https://github.com/MovingtoMars/liner) <img src="https://img.shields.io/github/stars/MovingtoMars/liner?style=social" alt="Stars" width="80"> [[liner](https://crates.io/crates/liner)] — A library offering readline-like functionality
  * [murarth/linefeed](https://github.com/murarth/linefeed) <img src="https://img.shields.io/github/stars/murarth/linefeed?style=social" alt="Stars" width="80"> [[linefeed](https://crates.io/crates/linefeed)] — Configurable, extensible, interactive line reader
  * [srijs/rust-copperline](https://github.com/srijs/rust-copperline) [[copperline](https://crates.io/crates/copperline)] — pure-Rust command line editing library
* Other
  * [mgrachev/update-informer](https://github.com/mgrachev/update-informer) [[update-informer](https://crates.io/crates/update-informer)] — Update informer for CLI applications. It checks for a new version on Crates.io and GitHub [![build badge](https://github.com/mgrachev/update-informer/workflows/CI/badge.svg)](https://github.com/mgrachev/update-informer/actions)
* Pipeline
  * [hniksic/rust-subprocess](https://github.com/hniksic/rust-subprocess) [[subprocess](https://crates.io/crates/subprocess)] — facilities for interaction with external pipelines
  * [imp/pager-rs](https://gitlab.com/imp/pager-rs) [[pager](https://crates.io/crates/pager)] — pipe your output through an external pager
  * [oconnor663/duct.rs](https://github.com/oconnor663/duct.rs) [[duct](https://crates.io/crates/duct)] — A builder for subprocess pipelines and IO redirection
  * [rust-cli/rexpect](https://github.com/rust-cli/rexpect) [[rexpect](https://crates.io/crates/rexpect)] — automate interactive applications such as ssh, ftp, passwd, etc [![CI](https://github.com/rust-cli/rexpect/actions/workflows/ci.yml/badge.svg)](https://github.com/rust-cli/rexpect/actions/workflows/ci.yml)
  * [zhiburt/expectrl](https://github.com/zhiburt/expectrl) <img src="https://img.shields.io/github/stars/zhiburt/expectrl?style=social" alt="Stars" width="80"> [[expectrl](https://crates.io/crates/expectrl)] — A library for controlling interactive programs in a pseudo-terminal [![build badge](https://github.com/zhiburt/expectrl/actions/workflows/ci.yml/badge.svg)](https://github.com/zhiburt/expectrl/actions/workflows/ci.yml)
* Progress
  * [a8m/pb](https://github.com/a8m/pb) <img src="https://img.shields.io/github/stars/a8m/pb?style=social" alt="Stars" width="80"> [[pbr](https://crates.io/crates/pbr)] — console progress bar for Rust
  * [console-rs/indicatif](https://github.com/console-rs/indicatif) [[indicatif](https://crates.io/crates/indicatif)] — indicate progress to users
  * [etienne-napoleone/spinach](https://github.com/etienne-napoleone/spinach) [[spinach](https://crates.io/crates/spinach)] — Practical spinner for Rust. [![CI](https://github.com/etienne-napoleone/spinach/actions/workflows/ci.yml/badge.svg)](https://github.com/etienne-napoleone/spinach/actions/workflows/ci.yml)
  * [FGRibreau/spinners](https://github.com/FGRibreau/spinners) <img src="https://img.shields.io/github/stars/FGRibreau/spinners?style=social" alt="Stars" width="80"> [[spinners](https://crates.io/crates/spinners)] — 60+ elegant terminal spinners
* Prompt
  * [hashmismatch/terminal_cli.rs](https://github.com/hashmismatch/terminal_cli.rs) [[terminal_cli](https://crates.io/crates/terminal_cli)]  — build an interactive command prompt
  * [mikaelmello/inquire](https://github.com/mikaelmello/inquire) <img src="https://img.shields.io/github/stars/mikaelmello/inquire?style=social" alt="Stars" width="80"> [[inquire](https://crates.io/crates/inquire)] — A library for building interactive prompts on terminals. [![Build status](https://github.com/mikaelmello/inquire/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/mikaelmello/inquire/actions)
  * [starship/starship](https://starship.rs/) [[starship](https://crates.io/crates/starship)]  — A minimal, blazing fast, and extremely customizable prompt for any shell [![Build status](https://github.com/starship/starship/workflows/Main%20workflow/badge.svg?branch=master)](https://github.com/starship/starship/actions)
  * [ynqa/promkit](https://github.com/ynqa/promkit) <img src="https://img.shields.io/github/stars/ynqa/promkit?style=social" alt="Stars" width="80"> [[promkit](https://crates.io/crates/promkit)]  — A toolkit for building interactive command-line tools [![Build status](https://github.com/ynqa/promkit/workflows/promkit/badge.svg?branch=master)](https://github.com/ynqa/promkit/actions)
* Style
  * [colored](https://github.com/colored-rs/colored) <img src="https://img.shields.io/github/stars/colored-rs/colored?style=social" alt="Stars" width="80"> [[colored](https://crates.io/crates/colored)] — Coloring terminal so simple, you already know how to do it!
  * [console-rs/dialoguer](https://github.com/console-rs/dialoguer) [[dialoguer](https://crates.io/crates/dialoguer)] — A rust library for command line prompts and similar things.
  * [LukasKalbertodt/bunt](https://github.com/LukasKalbertodt/bunt) <img src="https://img.shields.io/github/stars/LukasKalbertodt/bunt?style=social" alt="Stars" width="80"> [[bunt](https://crates.io/crates/bunt)] — cross-platform terminal colors and styling with macros [![Build status](https://github.com/LukasKalbertodt/bunt/actions/workflows/ci.yml/badge.svg)](https://github.com/LukasKalbertodt/bunt/actions?query=workflow%3ACI+branch%3Amaster)
  * [LukasKalbertodt/term-painter](https://github.com/LukasKalbertodt/term-painter) [[term-painter](https://crates.io/crates/term-painter)] — cross-platform styled terminal output
  * [ogham/rust-ansi-term](https://github.com/ogham/rust-ansi-term) [[ansi_term](https://crates.io/crates/ansi_term)] — control colours and formatting on ANSI terminals
  * [SergioBenitez/yansi](https://github.com/SergioBenitez/yansi) <img src="https://img.shields.io/github/stars/SergioBenitez/yansi?style=social" alt="Stars" width="80"> [[yansi](https://crates.io/crates/yansi)] — A dead simple ANSI terminal color painting library
* TUI
  * BearLibTerminal
    * [cfyzium/bearlibterminal](https://github.com/nabijaczleweli/BearLibTerminal.rs) [[bear-lib-terminal](https://crates.io/crates/bear-lib-terminal)] — [BearLibTerminal](https://github.com/tommyettinger/BearLibTerminal) <img src="https://img.shields.io/github/stars/tommyettinger/BearLibTerminal?style=social" alt="Stars" width="80"> bindings
  * [gyscos/Cursive](https://github.com/gyscos/Cursive) <img src="https://img.shields.io/github/stars/gyscos/Cursive?style=social" alt="Stars" width="80"> [[cursive](https://crates.io/crates/cursive)] — build rich TUI applications
  * [ivanceras/titik](https://github.com/ivanceras/titik) <img src="https://img.shields.io/github/stars/ivanceras/titik?style=social" alt="Stars" width="80"> - a crossplatform TUI widget library with the goal of providing interactive widgets
  * ncurses
    * [ihalila/pancurses](https://github.com/ihalila/pancurses) <img src="https://img.shields.io/github/stars/ihalila/pancurses?style=social" alt="Stars" width="80"> [[pancurses](https://crates.io/crates/pancurses)] — curses library, supports linux and windows
    * [jeaye/ncurses-rs](https://github.com/jeaye/ncurses-rs) [[ncurses](https://crates.io/crates/ncurses)] — [ncurses](https://www.gnu.org/software/ncurses/) bindings
  * [ogham/rust-term-grid](https://github.com/ogham/rust-term-grid) [[term_grid](https://crates.io/crates/term_grid)] — Rust library for putting things in a grid
  * [ratatui-org/ratatui](https://github.com/ratatui-org/ratatui) [[ratatui](https://crates.io/crates/ratatui)] — A Rust library that's all about cooking up terminal user interfaces (TUIs)
  * [redox-os/termion](https://github.com/redox-os/termion) [[termion](https://crates.io/crates/termion)] — bindless library for controlling terminals/TTY
  * Termbox
    * [gchp/rustbox](https://github.com/gchp/rustbox) <img src="https://img.shields.io/github/stars/gchp/rustbox?style=social" alt="Stars" width="80"> [[rustbox](https://crates.io/crates/rustbox)] — bindings to [Termbox](https://github.com/nsf/termbox) <img src="https://img.shields.io/github/stars/nsf/termbox?style=social" alt="Stars" width="80">
  * [TimonPost/crossterm](https://github.com/crossterm-rs/crossterm) <img src="https://img.shields.io/github/stars/crossterm-rs/crossterm?style=social" alt="Stars" width="80"> [[crossterm](https://crates.io/crates/crossterm)] — crossplatform terminal library

### Compression

* [7z](https://7-zip.org/7z.html)
  * [dyz1990/sevenz-rust](https://github.com/dyz1990/sevenz-rust) [[sevenz-rust](https://crates.io/crates/sevenz-rust)] — A 7z decompressor/compressor written in pure rust. [![Rust](https://github.com/dyz1990/sevenz-rust/workflows/Rust/badge.svg?branch=main)](https://github.com/dyz1990/sevenz-rust/actions)
* [Brotli](https://opensource.googleblog.com/2015/09/introducing-brotli-new-compression.html)
  * [dropbox/rust-brotli](https://github.com/dropbox/rust-brotli) — Brotli decompressor in Rust that optionally avoids the stdlib
  * [ende76/brotli-rs](https://github.com/ende76/brotli-rs) — implementation of Brotli compression
* bzip2
  * [alexcrichton/bzip2-rs](https://github.com/alexcrichton/bzip2-rs) — [libbz2](https://www.sourceware.org/bzip2/) bindings
* gzip
  * [zopfli](https://github.com/zopfli-rs/zopfli) <img src="https://img.shields.io/github/stars/zopfli-rs/zopfli?style=social" alt="Stars" width="80"> [[zopfli](https://crates.io/crates/zopfli)] — implementation of the Zopfli compression algorithm for higher quality deflate or zlib compression
* gzp
  * [sstadick/gzp](https://github.com/sstadick/gzp/) <img src="https://img.shields.io/github/stars/sstadick/gzp?style=social" alt="Stars" width="80"> - multi-threaded encoding and decoding of deflate formats and snappy
* miniz
  * [rust-lang/flate2-rs](https://github.com/rust-lang/flate2-rs) — [miniz](https://code.google.com/archive/p/miniz) bindings [![build badge](https://github.com/rust-lang/flate2-rs/workflows/CI/badge.svg?branch=master)](https://github.com/rust-lang/flate2-rs/actions)
* snappy
  * [JeffBelgum/rust-snappy](https://github.com/JeffBelgum/rust-snappy) — [snappy](https://github.com/google/snappy) <img src="https://img.shields.io/github/stars/google/snappy?style=social" alt="Stars" width="80"> bindings
* tar
  * [alexcrichton/tar-rs](https://github.com/alexcrichton/tar-rs) — tar archive reading/writing in Rust
* zip
  * [zip-rs/zip](https://github.com/zip-rs/zip) — read and write ZIP archives

### Computation

* [argmin-rs/argmin](https://github.com/argmin-rs/argmin) [[argmin](https://crates.io/crates/argmin)] — A pure Rust optimization library
* [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) [[blas](https://crates.io/keywords/blas)]
  * [mikkyang/rust-blas](https://github.com/mikkyang/rust-blas) — BLAS bindings
* [calebwin/emu](https://github.com/calebwin/emu) <img src="https://img.shields.io/github/stars/calebwin/emu?style=social" alt="Stars" width="80"> — A language for GPGPU numerical computing from a Rust macro
* [dimforge/nalgebra](https://github.com/dimforge/nalgebra) <img src="https://img.shields.io/github/stars/dimforge/nalgebra?style=social" alt="Stars" width="80"> — low-dimensional linear algebra library
* [GSL](http://www.gnu.org/software/gsl/)
  * [GuillaumeGomez/rust-GSL](https://github.com/GuillaumeGomez/rust-GSL) — GSL bindings
* [LAPACK](https://en.wikipedia.org/wiki/LAPACK)
  * [stainless-steel/lapack](https://github.com/blas-lapack-rs/lapack) — LAPACK bindings
* Parallel
  * [arrayfire/arrayfire-rust](https://github.com/arrayfire/arrayfire-rust) — [Arrayfire](https://github.com/arrayfire) bindings
  * [autumnai/collenchyma](https://github.com/autumnai/collenchyma) <img src="https://img.shields.io/github/stars/autumnai/collenchyma?style=social" alt="Stars" width="80"> — An extensible, pluggable, backend-agnostic framework for parallel, high-performance computations on CUDA, OpenCL and common host CPU.
  * [luqmana/rust-opencl](https://github.com/luqmana/rust-opencl) — [OpenCL](https://www.khronos.org/opencl/) bindings
* Scirust
  * [indigits/scirust](https://github.com/indigits/scirust) <img src="https://img.shields.io/github/stars/indigits/scirust?style=social" alt="Stars" width="80"> — scientific computing library in Rust
* Statrs
  * [statrs-dev/statrs](https://github.com/statrs-dev/statrs) — Robust statistical computation library in Rust

### Concurrency

* [crossbeam-rs/crossbeam](https://github.com/crossbeam-rs/crossbeam) – Support for parallelism and low-level concurrency in Rust
* [orium/archery](https://github.com/orium/archery) <img src="https://img.shields.io/github/stars/orium/archery?style=social" alt="Stars" width="80"> [[archery](https://crates.io/crates/archery)] — Library to abstract from `Rc`/`Arc` pointer types. [![build badge](https://github.com/orium/archery/workflows/CI/badge.svg)](https://github.com/orium/archery/actions?query=workflow%3ACI)
* [Rayon](https://github.com/rayon-rs/rayon) <img src="https://img.shields.io/github/stars/rayon-rs/rayon?style=social" alt="Stars" width="80"> – A data parallelism library for Rust
* [rustcc/coroutine-rs](https://github.com/rustcc/coroutine-rs) – Coroutine Library in Rust
* [zonyitoo/coio-rs](https://github.com/zonyitoo/coio-rs) – Coroutine I/O for Rust

### Configuration

* [andoriyu/uclicious](https://github.com/andoriyu/uclicious) <img src="https://img.shields.io/github/stars/andoriyu/uclicious?style=social" alt="Stars" width="80"> [[uclicious](https://crates.io/crates/uclicious)] — [libUCL](https://github.com/vstakhov/libucl) <img src="https://img.shields.io/github/stars/vstakhov/libucl?style=social" alt="Stars" width="80"> based feature-rich configuration library. [![CircleCI](https://circleci.com/gh/vstakhov/libucl.svg?style=svg)](https://app.circleci.com/pipelines/github/vstakhov/libucl)
* [Kixunil/configure_me](https://github.com/Kixunil/configure_me) <img src="https://img.shields.io/github/stars/Kixunil/configure_me?style=social" alt="Stars" width="80"> [[configure_me](https://crates.io/crates/configure_me)] — library for processing application configuration easily
* [mehcode/config-rs](https://github.com/mehcode/config-rs) [[config](https://crates.io/crates/config)] — Layered configuration system for Rust applications (with strong support for 12-factor applications).
* [SergioBenitez/Figment](https://github.com/SergioBenitez/Figment) <img src="https://img.shields.io/github/stars/SergioBenitez/Figment?style=social" alt="Stars" width="80"> [[figment](https://crates.io/crates/figment)] — A configuration library so con-free, it's unreal.
* [softprops/envy](https://github.com/softprops/envy) <img src="https://img.shields.io/github/stars/softprops/envy?style=social" alt="Stars" width="80"> - deserialize env vars into typesafe structs [![Main](https://github.com/softprops/envy/actions/workflows/main.yml/badge.svg)](https://github.com/softprops/envy/actions/workflows/main.yml)

### Cryptography

[[crypto](https://crates.io/keywords/crypto), [cryptography](https://crates.io/keywords/cryptography)]

* [arkworks-rs/circom-compat](https://github.com/arkworks-rs/circom-compat) - Arkworks bindings to Circom's R1CS, for Groth16 Proof and Witness generation in Rust.
* [briansmith/ring](https://github.com/briansmith/ring) <img src="https://img.shields.io/github/stars/briansmith/ring?style=social" alt="Stars" width="80"> — Safe, fast, small crypto using Rust and BoringSSL's cryptography primitives.
* [briansmith/webpki](https://github.com/briansmith/webpki) <img src="https://img.shields.io/github/stars/briansmith/webpki?style=social" alt="Stars" width="80"> — Web PKI TLS X.509 certificate validation in Rust.
* [conradkleinespel/rooster](https://github.com/conradkleinespel/rooster) <img src="https://img.shields.io/github/stars/conradkleinespel/rooster?style=social" alt="Stars" width="80"> [[rooster](https://crates.io/crates/rooster)] — Simple password manager to use in your terminal
* [cossacklabs/themis](https://github.com/cossacklabs/themis) <img src="https://img.shields.io/github/stars/cossacklabs/themis?style=social" alt="Stars" width="80"> [[themis](https://crates.io/crates/themis)] — a high-level cryptographic library for solving typical data security tasks, best fit for multi-platform apps. [![build badge](https://circleci.com/gh/cossacklabs/themis/tree/master.svg?style=shield)](https://app.circleci.com/pipelines/github/cossacklabs/themis)
* [DaGenix/rust-crypto](https://github.com/DaGenix/rust-crypto) — cryptographic algorithms in Rust
* [dalek-cryptography/curve25519-dalek](https://github.com/dalek-cryptography/curve25519-dalek) — Pure Rust implementation of Curve25519 operations
* [dalek-cryptography/ed25519-dalek](https://github.com/dalek-cryptography/ed25519-dalek) — Pure Rust implementation of Ed25519 digital signatures
* [dalek-cryptography/x25519-dalek](https://github.com/dalek-cryptography/x25519-dalek) — Pure Rust implementation of X25519 key exchange
* [debris/tiny-keccak](https://github.com/debris/tiny-keccak) — Pure Rust implementation of the Keccak family (SHA3)
* [exonum/exonum](https://github.com/exonum/exonum) <img src="https://img.shields.io/github/stars/exonum/exonum?style=social" alt="Stars" width="80"> [[exonum](https://crates.io/crates/exonum)] — extensible framework for blockchain projects
* [facebook/opaque-ke](https://github.com/facebook/opaque-ke) — Pure Rust implementation of the recent [OPAQUE](https://datatracker.ietf.org/doc/draft-krawczyk-cfrg-opaque/) password-authenticated key exchange. [![build badge](https://github.com/facebook/opaque-ke/workflows/Rust%20CI/badge.svg?branch=master)](https://github.com/facebook/opaque-ke)
* [iddm/randomorg](https://github.com/iddm/randomorg) <img src="https://img.shields.io/github/stars/iddm/randomorg?style=social" alt="Stars" width="80"> - A random.org client library. [![Crates badge](https://img.shields.io/crates/v/randomorg.svg)](https://crates.io/crates/randomorg)
* [klutzy/suruga](https://github.com/klutzy/suruga) <img src="https://img.shields.io/github/stars/klutzy/suruga?style=social" alt="Stars" width="80"> — A Rust implementation of [TLS 1.2](https://datatracker.ietf.org/doc/html/rfc5246)
* [kornelski/rust-security-framework](https://github.com/kornelski/rust-security-framework) — Bindings for Security Framework (OSX native)
* [libOctavo/octavo](https://github.com/libOctavo/octavo) <img src="https://img.shields.io/github/stars/libOctavo/octavo?style=social" alt="Stars" width="80"> — Modular hash and crypto library in Rust
* [orion-rs/orion](https://github.com/orion-rs/orion) — This library aims to provide easy and usable crypto. 'Usable' meaning exposing high-level API's that are easy to use and hard to misuse. [![Tests](https://github.com/orion-rs/orion/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/orion-rs/orion/actions/workflows/test.yml)
* [racum/rust-djangohashers](https://github.com/racum/rust-djangohashers) [[djangohashers](https://crates.io/crates/djangohashers)] — A Rust port of the password primitives used in the Django Project. It doesn't require Django, only hashes and validates passwords according to its style.
* [RustCrypto/hashes](https://github.com/RustCrypto/hashes) <img src="https://img.shields.io/github/stars/RustCrypto/hashes?style=social" alt="Stars" width="80"> — Collection of cryptographic hash functions written in pure Rust
* [rustls/rustls](https://github.com/rustls/rustls) <img src="https://img.shields.io/github/stars/rustls/rustls?style=social" alt="Stars" width="80"> — A Rust implementation of TLS
* [sfackler/rust-native-tls](https://github.com/sfackler/rust-native-tls) — Bindings for native TLS libraries
* [sfackler/rust-openssl](https://github.com/sfackler/rust-openssl) — [OpenSSL](https://www.openssl.org/) bindings
* [sorairolake/scryptenc-rs](https://github.com/sorairolake/scryptenc-rs) [[scryptenc](https://crates.io/crates/scryptenc)] — An implementation of the scrypt encrypted data format. [![CI](https://github.com/sorairolake/scryptenc-rs/workflows/CI/badge.svg?branch=develop)](https://github.com/sorairolake/scryptenc-rs/actions?query=workflow%3ACI)
* [w3f/schnorrkel](https://github.com/w3f/schnorrkel) <img src="https://img.shields.io/github/stars/w3f/schnorrkel?style=social" alt="Stars" width="80"> - Schnorr VRFs and signatures on the Ristretto group

### Data processing

* [amv-dev/yata](https://github.com/amv-dev/yata) — high perfomance technical analysis library [![Build Status](https://img.shields.io/github/workflow/status/amv-dev/yata/Rust?branch=master)](https://github.com/amv-dev/yata/actions?query=workflow%3ARust)
* [bluss/ndarray](https://github.com/rust-ndarray/ndarray) <img src="https://img.shields.io/github/stars/rust-ndarray/ndarray?style=social" alt="Stars" width="80"> — N-dimensional array with array views, multidimensional slicing, and efficient operations
* [kernelmachine/utah](https://github.com/kernelmachine/utah) <img src="https://img.shields.io/github/stars/kernelmachine/utah?style=social" alt="Stars" width="80"> — Dataframe structure and operations in Rust
* [pola-rs/polars](https://github.com/pola-rs/polars) - Fast feature complete DataFrame library ![Build and test](https://github.com/pola-rs/polars/workflows/Build%20and%20test/badge.svg?branch=master)
* [weld-project/weld](https://github.com/weld-project/weld) — High-performance runtime for data analytics applications

### Data streaming

* [ArroyoSystems/arroyo](https://github.com/ArroyoSystems/arroyo) <img src="https://img.shields.io/github/stars/ArroyoSystems/arroyo?style=social" alt="Stars" width="80"> - High-performance real-time analytics in Rust and SQL [![CI](https://github.com/ArroyoSystems/arroyo/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/ArroyoSystems/arroyo/actions)
* [iggy-rs/iggy](https://github.com/iggy-rs/iggy) [[iggy](https://crates.io/crates/iggy)] — Persistent message streaming platform, supporting QUIC, TCP and HTTP transport protocols [![CI](https://github.com/iggy-rs/iggy/actions/workflows/test.yml/badge.svg)](https://github.com/iggy-rs/iggy/actions/workflows/test.yml)
* [infinyon/fluvio](https://github.com/infinyon/fluvio) <img src="https://img.shields.io/github/stars/infinyon/fluvio?style=social" alt="Stars" width="80"> - Programmable data streaming platform [![CI](https://github.com/infinyon/fluvio/workflows/CI/badge.svg?branch=stable)](https://github.com/infinyon/fluvio/actions)

### Data structures

* [becheran/grid](https://github.com/becheran/grid) <img src="https://img.shields.io/github/stars/becheran/grid?style=social" alt="Stars" width="80"> [[grid](https://crates.io/crates/grid)] —  Provide a two dimensional data structure for rust that is easy to use and fast. [![build status](https://github.com/becheran/grid/actions/workflows/rust.yml/badge.svg)](https://github.com/becheran/grid/actions)
* [billyevans/tst](https://github.com/billyevans/tst) <img src="https://img.shields.io/github/stars/billyevans/tst?style=social" alt="Stars" width="80"> [[tst](https://crates.io/crates/tst)] — Ternary search tree collection
* [contain-rs](https://github.com/contain-rs) — Extension of Rust's std::collections
* [danielpclark/array_tool](https://github.com/danielpclark/array_tool) <img src="https://img.shields.io/github/stars/danielpclark/array_tool?style=social" alt="Stars" width="80"> — Array helpers for Rust. Some of the most common methods you would use on Arrays made available on Vectors. Polymorphic implementations for handling most of your use cases.
* [fizyk20/generic-array](https://github.com/fizyk20/generic-array) – a hack to allow for arrays sized by typenums
* [garro95/priority-queue](https://github.com/garro95/priority-queue)[[priority-queue](https://crates.io/crates/priority-queue)] — A priority queue that implements priority changes.
* [greyblake/nutype](https://github.com/greyblake/nutype) <img src="https://img.shields.io/github/stars/greyblake/nutype?style=social" alt="Stars" width="80"> [[nutype](https://crates.io/crates/nutype)] — define newtype structures with validation constraints. [![build status](https://github.com/greyblake/nutype/actions/workflows/ci.yml/badge.svg)](https://github.com/greyblake/nutype/actions)
* [mrhooray/kdtree-rs](https://github.com/mrhooray/kdtree-rs) — K-dimensional tree in Rust for fast geospatial indexing and nearest neighbors lookup
* [orium/rpds](https://github.com/orium/rpds) <img src="https://img.shields.io/github/stars/orium/rpds?style=social" alt="Stars" width="80"> [[rpds](https://crates.io/crates/rpds)] — Persistent data structures in Rust. [![build badge](https://github.com/orium/rpds/workflows/CI/badge.svg)](https://github.com/orium/rpds/actions?query=workflow%3ACI)
* [RoaringBitmap/roaring-rs](https://github.com/RoaringBitmap/roaring-rs) – Roaring Bitmaps in Rust
* [rust-itertools/itertools](https://github.com/rust-itertools/itertools) —
* [tnballo/scapegoat](https://github.com/tnballo/scapegoat) <img src="https://img.shields.io/github/stars/tnballo/scapegoat?style=social" alt="Stars" width="80"> [[scapegoat](https://crates.io/crates/scapegoat)] — Safe, fallible, stack-only alternative to `BTreeSet` and `BTreeMap`. [![GitHub Actions](https://github.com/tnballo/scapegoat/workflows/test/badge.svg?branch=master)](https://github.com/tnballo/scapegoat/actions)
* [xfix/enum-map](https://codeberg.org/xfix/enum-map) [[enum-map](https://crates.io/crates/enum-map)] — An optimized map implementation for enums using an array to store values.
* [yamafaktory/hypergraph](https://github.com/yamafaktory/hypergraph) <img src="https://img.shields.io/github/stars/yamafaktory/hypergraph?style=social" alt="Stars" width="80"> [[hypergraph](https://crates.io/crates/hypergraph)] — Hypergraph is a data structure library to generate directed hypergraphs. [![ci](https://github.com/yamafaktory/hypergraph/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/yamafaktory/hypergraph/actions/workflows/ci.yml)

### Data visualization

* [blitzarx1/egui_graphs](https://github.com/blitzarx1/egui_graphs) <img src="https://img.shields.io/github/stars/blitzarx1/egui_graphs?style=social" alt="Stars" width="80"> - [[egui_graphs](https://crates.io/crates/egui_graphs)] - Interactive graph visualization widget for rust powered by egui and petgraph. [![Crates.io](https://img.shields.io/crates/v/egui_graphs)](https://crates.io/crates/egui_graphs) [![docs.rs](https://img.shields.io/docsrs/egui_graphs)](https://docs.rs/egui_graphs)
* [djduque/pgfplots](https://github.com/djduque/pgfplots) <img src="https://img.shields.io/github/stars/djduque/pgfplots?style=social" alt="Stars" width="80"> [[pgfplots](https://crates.io/crates/pgfplots)] — A Rust library to generate publication-quality figures. [![build](https://github.com/DJDuque/pgfplots/actions/workflows/rust.yml/badge.svg)](https://github.com/DJDuque/pgfplots/actions/workflows/rust.yml)
* [igiagkiozis/plotly](https://github.com/igiagkiozis/plotly) <img src="https://img.shields.io/github/stars/igiagkiozis/plotly?style=social" alt="Stars" width="80"> — Plotly for Rust.
* [mazznoer/colorgrad-rs](https://github.com/mazznoer/colorgrad-rs) [[colorgrad](https://crates.io/crates/colorgrad)] — Rust color scales library for data visualization, charts, games, maps, generative art and others.
* [milliams/plotlib](https://github.com/milliams/plotlib) <img src="https://img.shields.io/github/stars/milliams/plotlib?style=social" alt="Stars" width="80"> —
* [plotters](https://github.com/plotters-rs/plotters) <img src="https://img.shields.io/github/stars/plotters-rs/plotters?style=social" alt="Stars" width="80"> — [![build badge](https://github.com/plotters-rs/plotters/workflows/CI/badge.svg)](https://github.com/plotters-rs/plotters/actions)
* [rerun](https://github.com/rerun-io/rerun) <img src="https://img.shields.io/github/stars/rerun-io/rerun?style=social" alt="Stars" width="80"> — [[rerun](https://crates.io/crates/rerun)] — An SDK for logging computer vision and robotics data (tensors, point clouds, etc) paired with a visualizer for exploring that data over time.
* [saresend/gust](https://github.com/saresend/Gust) <img src="https://img.shields.io/github/stars/saresend/Gust?style=social" alt="Stars" width="80"> —

### Database

[[database](https://crates.io/keywords/database)]

* NoSQL [[nosql](https://crates.io/keywords/nosql)]

  * [ArangoDB](https://arangodb.com)
    * [Aragog](https://gitlab.com/qonfucius/aragog) [[aragog](https://crates.io/crates/aragog)] - A Lightweight ArangoDB Object document, relational and graph mapper [![pipeline status](https://gitlab.com/qonfucius/aragog/badges/master/pipeline.svg)](https://gitlab.com/qonfucius/aragog/-/commits/master)
    * [Arangors](https://github.com/fMeow/arangors) <img src="https://img.shields.io/github/stars/fMeow/arangors?style=social" alt="Stars" width="80"> [[arangors](https://crates.io/crates/arangors)] - An ArangoDB driver for Rust
  * [Cassandra](https://cassandra.apache.org/_/index.html) [[cassandra](https://crates.io/keywords/cassandra), [cql](https://crates.io/keywords/cql)]
    * [AlexPikalov/cdrs](https://github.com/AlexPikalov/cdrs) <img src="https://img.shields.io/github/stars/AlexPikalov/cdrs?style=social" alt="Stars" width="80"> [[cdrs](https://crates.io/crates/cdrs)] — native client written in Rust
    * [krojew/cdrs-tokio](https://github.com/krojew/cdrs-tokio) [![build badge](https://github.com/krojew/cdrs-tokio/actions/workflows/rust.yml/badge.svg)](https://github.com/krojew/cdrs-tokio/actions)
      * [[cassandra-protocol](https://crates.io/crates/cassandra-protocol)] - Cassandra protocol implementation in Rust
      * [[cdrs-tokio](https://crates.io/crates/cdrs-tokio)] - production-ready async Apache Cassandra driver written in pure Rust
    * [Metaswitch/cassandra-rs](https://github.com/Metaswitch/cassandra-rs) —  bindings to the DataStax C/C++ client
  * CouchDB [[couchdb](https://crates.io/keywords/couchdb)]
    * [chill-rs/chill](https://github.com/chill-rs/chill) [[couchdb](https://crates.io/crates/chill)] — A Rust client for the CouchDB REST API
  * [DynamoDB](https://aws.amazon.com/dynamodb/) [[dynamodb](https://crates.io/keywords/dynamodb)]
    * [softprops/dynomite](https://github.com/softprops/dynomite) <img src="https://img.shields.io/github/stars/softprops/dynomite?style=social" alt="Stars" width="80"> - A library for strongly-typed and convenient interaction with `rusoto_dynamodb` [![build badge](https://github.com/softprops/dynomite/workflows/Main/badge.svg?branch=master)](https://github.com/softprops/dynomite/actions)
  * Elasticsearch [[elasticsearch](https://crates.io/keywords/elasticsearch)]
    * [benashford/rs-es](https://github.com/benashford/rs-es) [[rs-es](https://crates.io/crates/rs-es)] — A Rust client for the [Elastic](https://www.elastic.co/) REST API
    * [elastic-rs/elastic](https://github.com/elastic-rs/elastic) [[elastic](https://crates.io/crates/elastic)] — elastic is an efficient, modular API client for Elasticsearch written in Rust [![build badge](https://ci.appveyor.com/api/projects/status/csa78tcumdpnbur2?svg=true)](https://ci.appveyor.com/project/KodrAus/elastic)
  * etcd
    * [jimmycuadra/rust-etcd](https://github.com/jimmycuadra/rust-etcd) [[etcd](https://crates.io/crates/etcd)] — A client library for CoreOS's etcd.
    * [lodrem/etcd-rs](https://github.com/lodrem/etcd-rs) — An asynchronous etcd client for rust [![CI](https://github.com/lodrem/etcd-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/lodrem/etcd-rs/actions/workflows/ci.yml)
  * ForestDB
    * [vhbit/sherwood](https://github.com/vhbit/sherwood) <img src="https://img.shields.io/github/stars/vhbit/sherwood?style=social" alt="Stars" width="80"> — [ForestDB](https://github.com/couchbase/forestdb) <img src="https://img.shields.io/github/stars/couchbase/forestdb?style=social" alt="Stars" width="80"> bindings
  * [InfluxDB](https://www.influxdata.com/)
    * [driftluo/InfluxDBClient-rs](https://github.com/driftluo/InfluxDBClient-rs) — Synchronization interface
  * LevelDB
    * [skade/leveldb](https://github.com/skade/leveldb) <img src="https://img.shields.io/github/stars/skade/leveldb?style=social" alt="Stars" width="80"> — [LevelDB](https://github.com/google/leveldb) <img src="https://img.shields.io/github/stars/google/leveldb?style=social" alt="Stars" width="80"> bindings
  * LMDB [[lmdb](https://crates.io/keywords/lmdb)]
    * [vhbit/lmdb-rs](https://github.com/vhbit/lmdb-rs) [[lmdb-rs](https://crates.io/crates/lmdb-rs)] — [LMDB](https://www.symas.com/symas-embedded-database-lmdb) bindings
  * MongoDB [[mongodb](https://crates.io/keywords/mongodb)]
    * [mongodb/mongo-rust-driver](https://github.com/mongodb/mongo-rust-driver) [[mongodb](https://crates.io/crates/mongodb)] — [MongoDB](https://www.mongodb.com/) bindings
  * [PickleDB](https://pythonhosted.org/pickleDB/)
    * [seladb/pickledb-rs](https://github.com/seladb/pickledb-rs) — a lightweight and simple key-value store, heavily inspired by Python's PickleDB.
  * [PoloDB](https://www.polodb.org/)
    * [PoloDB](https://github.com/PoloDB/PoloDB) <img src="https://img.shields.io/github/stars/PoloDB/PoloDB?style=social" alt="Stars" width="80"> - An embedded JSON-based database has API similar to MongoDB. ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PoloDB/PoloDB/rust.yml)
  * [Redb](https://www.redb.org/)
    * [Redb](https://github.com/cberner/redb) <img src="https://img.shields.io/github/stars/cberner/redb?style=social" alt="Stars" width="80"> - An embedded key-value database written in pure Rust. It provides a similar interface to other embedded key-value stores such as rocksdb and lmdb. ![GitHub Workflow Status](https://github.com/cberner/redb/actions/workflows/ci.yml/badge.svg)
  * Redis [[redis](https://crates.io/keywords/redis)]
    * [aembke/fred](https://github.com/aembke/fred.rs) [[fred](https://crates.io/crates/fred)] - A high level async [Redis](https://redis.io/) client for Rust with Tokio. [![CircleCI](https://circleci.com/gh/aembke/fred.rs/tree/main.svg?style=svg)]([https://circleci.com/gh/aembke/fred.rs/tree/main](https://app.circleci.com/pipelines/github/aembke/fred.rs?branch=main))
    * [redis-rs](https://github.com/redis-rs/redis-rs) — [Redis](https://redis.io/) library in Rust [![Rust](https://github.com/redis-rs/redis-rs/actions/workflows/rust.yml/badge.svg)](https://github.com/redis-rs/redis-rs/actions/workflows/rust.yml)
  * [RocksDB](https://rocksdb.org/)
    * [rust-rocksdb/rust-rocksdb](https://github.com/rust-rocksdb/rust-rocksdb) — RocksDB bindings [![RocksDB CI](https://github.com/rust-rocksdb/rust-rocksdb/actions/workflows/rust.yml/badge.svg?branch=master)](https://github.com/rust-rocksdb/rust-rocksdb/actions/workflows/rust.yml)
  * [SurrealDB](https://surrealdb.com/)
    * [surrealdb/surrealdb](https://github.com/surrealdb/surrealdb) <img src="https://img.shields.io/github/stars/surrealdb/surrealdb?style=social" alt="Stars" width="80"> — SurrealDB embedded document-graph database
  * [UnQLite](https://unqlite.org/)
    * [zitsen/unqlite.rs](https://github.com/zitsen/unqlite.rs) — UnQLite bindings
  * [ZooKeeper](https://zookeeper.apache.org/)
    * [bonifaido/rust-zookeeper](https://github.com/bonifaido/rust-zookeeper) [[zookeeper](https://crates.io/crates/zookeeper)] — A client library for Apache ZooKeeper.
    * [krojew/rust-zookeeper](https://github.com/krojew/rust-zookeeper) [[zookeeper-async](https://crates.io/crates/zookeeper-async)] - Async Zookeeper client written 100% in Rust, based on tokio.  ![build status](https://github.com/krojew/rust-zookeeper/actions/workflows/rust.yml/badge.svg)
* OGM [[ogm](https://crates.io/keywords/ogm)]
    * [Aragog](https://gitlab.com/qonfucius/aragog) [[aragog](https://crates.io/crates/aragog)] - A Lightweight ArangoDB Object document, relational and graph mapper [![pipeline status](https://gitlab.com/qonfucius/aragog/badges/master/pipeline.svg)](https://gitlab.com/qonfucius/aragog/-/commits/master)
* ORM [[orm](https://crates.io/keywords/orm)]
  * [Brendonovich/prisma-client-rust](https://github.com/Brendonovich/prisma-client-rust) — An autogenerated query builder that provides simple and fully type-safe database access using the Prisma ecosystem. [![Test Status](https://img.shields.io/github/workflow/status/Brendonovich/prisma-client-rust/CI?label=tests&style=flat-square)](https://github.com/Brendonovich/prisma-client-rust/actions)
  * [diesel-rs/diesel](https://github.com/diesel-rs/diesel) — an ORM and Query builder for Rust
  * [ivanceras/rustorm](https://github.com/ivanceras/rustorm) <img src="https://img.shields.io/github/stars/ivanceras/rustorm?style=social" alt="Stars" width="80"> — an ORM for Rust
  * [rbatis/rbatis](https://github.com/rbatis/rbatis) <img src="https://img.shields.io/github/stars/rbatis/rbatis?style=social" alt="Stars" width="80"> — Rust ORM Framework High Performance(JSON based)
  * [SeaQL/sea-orm](https://github.com/SeaQL/sea-orm) — 🐚 An async & dynamic ORM for Rust [![crate](https://img.shields.io/crates/v/sea-orm.svg)](https://crates.io/crates/sea-orm) [![docs](https://img.shields.io/docsrs/sea-orm/latest)](https://docs.rs/sea-orm) [![build status](https://github.com/SeaQL/sea-orm/actions/workflows/rust.yml/badge.svg)](https://github.com/SeaQL/sea-orm/actions/workflows/rust.yml)
  * [SeaQL/seaography](https://github.com/SeaQL/seaography) <img src="https://img.shields.io/github/stars/SeaQL/seaography?style=social" alt="Stars" width="80"> — 🧭 GraphQL framework for SeaORM [![crate](https://img.shields.io/crates/v/seaography.svg)](https://crates.io/crates/seaography) [![docs](https://img.shields.io/docsrs/seaography/latest)](https://docs.rs/seaography) [![build status](https://github.com/SeaQL/seaography/actions/workflows/tests.yaml/badge.svg)](https://github.com/SeaQL/seaography/actions/workflows/tests.yaml)
* [sfackler/r2d2](https://github.com/sfackler/r2d2) <img src="https://img.shields.io/github/stars/sfackler/r2d2?style=social" alt="Stars" width="80"> — generic connection pool
* SQL [[sql](https://crates.io/keywords/sql)]
  * Generic
    * [launchbadge/sqlx](https://github.com/launchbadge/sqlx) <img src="https://img.shields.io/github/stars/launchbadge/sqlx?style=social" alt="Stars" width="80"> - async PostgreSQL/MySQL/SQLite connection pool with strong typing support [![build badge](https://img.shields.io/github/workflow/status/launchbadge/sqlx/Rust/master?style=flat-square)](https://github.com/launchbadge/sqlx)
    * [SeaQL/sea-query](https://github.com/SeaQL/sea-query) - 🔱 A dynamic SQL query builder for MySQL, Postgres and SQLite [![crate](https://img.shields.io/crates/v/sea-query.svg)](https://crates.io/crates/sea-query) [![docs](https://img.shields.io/docsrs/sea-query/latest)](https://docs.rs/sea-query) [![build status](https://github.com/SeaQL/sea-query/actions/workflows/rust.yml/badge.svg)](https://github.com/SeaQL/sea-query/actions/workflows/rust.yml)
    * [SeaQL/sea-schema](https://github.com/SeaQL/sea-schema) - 🌿 SQL schema definition and discovery [![crate](https://img.shields.io/crates/v/sea-schema.svg)](https://crates.io/crates/sea-schema) [![docs](https://img.shields.io/docsrs/sea-schema/latest)](https://docs.rs/sea-schema) [![build status](https://github.com/SeaQL/sea-schema/actions/workflows/rust.yml/badge.svg)](https://github.com/SeaQL/sea-schema/actions/workflows/rust.yml)
  * Microsoft SQL
    * [prisma/tiberius](https://github.com/prisma/tiberius) <img src="https://img.shields.io/github/stars/prisma/tiberius?style=social" alt="Stars" width="80"> — [![Cargo tests](https://github.com/prisma/tiberius/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/prisma/tiberius/actions/workflows/test.yml)
  * MySql [[mysql](https://crates.io/keywords/mysql)]
    * [AgilData/mysql-proxy-rs](https://github.com/AgilData/mysql-proxy-rs) — A MySQL Proxy [![CircleCI](https://circleci.com/gh/AgilData/mysql-proxy-rs/tree/master.svg?style=svg)](https://app.circleci.com/pipelines/github/AgilData/mysql-proxy-rs?branch=master)
    * [blackbeam/mysql_async](https://github.com/blackbeam/mysql_async) <img src="https://img.shields.io/github/stars/blackbeam/mysql_async?style=social" alt="Stars" width="80"> [[mysql_async](https://crates.io/crates/mysql_async)] — asyncronous Rust Mysql driver based on Tokio. [![CircleCI](https://circleci.com/gh/blackbeam/mysql_async/tree/master.svg?style=shield)](https://app.circleci.com/pipelines/github/blackbeam/mysql_async?branch=master)
    * [blackbeam/rust-mysql-simple](https://github.com/blackbeam/rust-mysql-simple) [[mysql](https://crates.io/crates/mysql)] — A native MySql client
  * Oracle
    * [kubo/rust-oracle](https://github.com/kubo/rust-oracle) [[oracle](https://crates.io/crates/oracle)] — Oracle driver for Rust [![build badge](https://github.com/kubo/rust-oracle/actions/workflows/run-tests.yml/badge.svg?branch=master)](https://github.com/kubo/rust-oracle/actions/workflows/run-tests.yml)
  * PostgreSql [[postgres](https://crates.io/keywords/postgres), [postgresql](https://crates.io/keywords/postgresql)]
    * [sfackler/rust-postgres](https://github.com/sfackler/rust-postgres) [[postgres](https://crates.io/crates/postgres)] — A native [PostgreSQL](https://www.postgresql.org/) client
  * Sqlite [[sqlite](https://crates.io/keywords/sqlite)]
    * [rusqlite](https://github.com/rusqlite/rusqlite) <img src="https://img.shields.io/github/stars/rusqlite/rusqlite?style=social" alt="Stars" width="80"> — [Sqlite3](https://www.sqlite.org/index.html) bindings

### Date and time

[[date](https://crates.io/keywords/date), [time](https://crates.io/keywords/time)]

* [chronotope/chrono](https://github.com/chronotope/chrono) <img src="https://img.shields.io/github/stars/chronotope/chrono?style=social" alt="Stars" width="80"> —
* [Mnwa/ms](https://github.com/Mnwa/ms) <img src="https://img.shields.io/github/stars/Mnwa/ms?style=social" alt="Stars" width="80"> [[ms-converter](https://crates.io/crates/ms-converter)] — it's a library for converting human-like times to milliseconds [![build badge](https://github.com/Mnwa/ms/workflows/build/badge.svg?branch=master)](https://github.com/Mnwa/ms/actions?query=workflow%3Abuild)
* [sorairolake/nt-time](https://github.com/sorairolake/nt-time) [[nt-time](https://crates.io/crates/nt-time)] — A Windows file time library. [![CI](https://github.com/sorairolake/nt-time/workflows/CI/badge.svg?branch=develop)](https://github.com/sorairolake/nt-time/actions?query=workflow%3ACI)
* [time-rs/time](https://github.com/time-rs/time) — [![build badge](https://github.com/time-rs/time/workflows/Build/badge.svg)](https://github.com/time-rs/time/actions)

### Distributed systems

* Antimony
  * [antimonyproject/antimony](https://github.com/antimonyproject/antimony) <img src="https://img.shields.io/github/stars/antimonyproject/antimony?style=social" alt="Stars" width="80"> [[antimony](https://crates.io/crates/antimony)] — stream processing / distributed computation platform
* Apache Kafka
  * [fede1024/rust-rdkafka](https://github.com/fede1024/rust-rdkafka) [[rdkafka](https://crates.io/crates/rdkafka)] — [librdkafka](https://github.com/confluentinc/librdkafka) <img src="https://img.shields.io/github/stars/confluentinc/librdkafka?style=social" alt="Stars" width="80"> bindings
  * [gklijs/schema_registry_converter](https://github.com/gklijs/schema_registry_converter) <img src="https://img.shields.io/github/stars/gklijs/schema_registry_converter?style=social" alt="Stars" width="80"> [[schema_registry_converter](https://crates.io/crates/schema_registry_converter)] — to integrate with [confluent schema registry](https://www.confluent.io/product/confluent-platform/data-compatibility/)
  * [kafka-rust/kafka-rust](https://github.com/kafka-rust/kafka-rust) —
* Beanstalkd
  * [schickling/rust-beanstalkd](https://github.com/schickling/rust-beanstalkd) — [Beanstalkd](https://github.com/beanstalkd/beanstalkd) <img src="https://img.shields.io/github/stars/beanstalkd/beanstalkd?style=social" alt="Stars" width="80"> bindings
* HDFS
  * [hyunsik/hdfs-rs](https://github.com/hyunsik/hdfs-rs) [[hdfs](https://crates.io/crates/hdfs)] — libhdfs bindings
* Other
  * [build-trust/ockam](https://github.com/build-trust/ockam) [[ockam](https://crates.io/crates/ockam)] - End-to-End Encryption, Mutual Authentication, and ABAC for distributed applications [![build badge](https://github.com/build-trust/ockam/workflows/Rust/badge.svg)](https://github.com/build-trust/ockam)

### Domain driven design

  * [serverlesstechnology/cqrs](https://github.com/serverlesstechnology/cqrs) <img src="https://img.shields.io/github/stars/serverlesstechnology/cqrs?style=social" alt="Stars" width="80"> [[cqrs-es](https://crates.io/crates/cqrs-es)] — A framework for CQRS and event sourcing with [user guide](https://doc.rust-cqrs.org/)

### eBPF

* [aya/aya-rs](https://github.com/aya-rs/aya) — A Rust library for the Rust programming language, built with a focus on developer experience and operability.
* [libbpf/libbpf-rs](https://github.com/libbpf/libbpf-rs) — A minimal and opinionated eBPF tooling for the Rust ecosystem.

### Email

[[email](https://crates.io/keywords/email), [imap](https://crates.io/keywords/imap), [smtp](https://crates.io/keywords/smtp)]

* [duesee/imap-codec](https://github.com/duesee/imap-codec) [[imap-codec](https://crates.io/crates/imap-codec)] — Rock-solid and complete codec for IMAP [![Build & Test](https://github.com/duesee/imap-codec/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/duesee/imap-codec/actions/workflows/build_and_test.yml)
* [gsquire/sendgrid-rs](https://github.com/gsquire/sendgrid-rs) — unofficial Rust library for SendGrid API
* [jdrouet/catapulte](https://github.com/jdrouet/catapulte) <img src="https://img.shields.io/github/stars/jdrouet/catapulte?style=social" alt="Stars" width="80"> - A microservice to send emails using [MRML](https://github.com/jdrouet/mrml) <img src="https://img.shields.io/github/stars/jdrouet/mrml?style=social" alt="Stars" width="80"> templates.
* [jdrouet/jolimail](https://github.com/jdrouet/jolimail) <img src="https://img.shields.io/github/stars/jdrouet/jolimail?style=social" alt="Stars" width="80"> - A web application to build [MRML](https://github.com/jdrouet/mrml) <img src="https://img.shields.io/github/stars/jdrouet/mrml?style=social" alt="Stars" width="80"> templates.
* [jdrouet/mrml](https://github.com/jdrouet/mrml) <img src="https://img.shields.io/github/stars/jdrouet/mrml?style=social" alt="Stars" width="80"> - A library to generate nice email templates working on any mail client.
* [lettre/lettre](https://github.com/lettre/lettre) <img src="https://img.shields.io/github/stars/lettre/lettre?style=social" alt="Stars" width="80"> — an SMTP-library for Rust [![CI](https://github.com/lettre/lettre/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/
