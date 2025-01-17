<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://media.duckduckgpt.com/images/ddgpt-logo-dark-mode-371x65.png">
    <img alt="DuckDuckGPT" src="https://media.duckduckgpt.com/images/ddgpt-logo-light-mode-371x65.png">
  </picture>
<a href="https://www.producthunt.com/posts/duckduckgpt?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-duckduckgpt" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=379261&theme=light" alt="DuckDuckGPT - Bring&#0032;the&#0032;magic&#0032;of&#0032;ChatGPT&#0032;to&#0032;DuckDuckGo | Product Hunt" style="width: 156px; height: 34px; margin:0 0 11px 5px;" width="156" height="34" /></a>
  <a href="https://twitter.com/intent/tweet?text=Want%20%23ChatGPT%20answers%20right%20alongside%20DuckDuckGo%20results%3F%20This%20%23userscript%20does%20just%20that%21&url=https://duckduckgpt.com&hashtags=greasemonkey,javascript,ai"><img alt="Tweet" style="margin:0 0 14px 5px;" src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social"></a>
</h1>

![usercount](https://img.shields.io/greasyfork/dt/459849?label=Users)
[![license](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE.md)
[![support](https://img.shields.io/badge/Support-Chrome/Firefox/Edge/Opera/Brave/Vivaldi/LibreWolf/Ghost/QQ-989898.svg)](#compatibility)
[![commits](https://img.shields.io/github/commit-activity/m/kudoai/duckduckgpt?label=Commits)](https://github.com/kudoai/duckduckgpt/commits/main)
![vulnerabilities](https://img.shields.io/snyk/vulnerabilities/github/kudoai/duckduckgpt?label=Vulnerabilities&labelColor=464646&color=gold)
[![code-quality](https://img.shields.io/codefactor/grade/github/kudoai/duckduckgpt?label=Code%20Quality)](https://www.codefactor.io/repository/github/kudoai/duckduckgpt)
<a alt="chatgpt.js" href="https://chatgpt.js.org"><img height=20 src="https://i.imgur.com/AwQqCmB.png"></a>
[![Mentioned in Awesome Userscripts](https://awesome.re/mentioned-badge.svg)](https://github.com/awesome-scripts/awesome-userscripts#duckduckgo)

<h3><b>DuckDuckGPT</b> brings the magic of ChatGPT to search results.</h3>

<a href="https://greasyfork.org/scripts/459849-duckduckgpt"><img alt="Install this script" src="https://github.com/adamlui/userscripts/raw/master/media/images/buttons/install-button.svg"></a><a href="#installation"><img alt="How to install" title="How to install" src="https://github.com/adamlui/userscripts/raw/master/media/images/buttons/help-button.svg"></a>
<br>
[Discuss](https://github.duckduckgpt.com/discussions) /
[Review](https://duckduckgpt.com/userscript/review) /
[Contact author](https://github.com/adamlui)

#

<img src="https://i.imgur.com/emsmP6p.png">

## Installation

1. Install Tampermonkey ([Chrome](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo), [Firefox](https://addons.mozilla.org/firefox/addon/tampermonkey/), [Edge](https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd), [Opera](https://addons.opera.com/extensions/details/tampermonkey-beta/)) or Violentmonkey ([Chrome](https://chrome.google.com/webstore/detail/violent-monkey/jinjaccalgkegednnccohejagnlnfdag), [Firefox](https://addons.mozilla.org/firefox/addon/violentmonkey/), [Edge](https://microsoftedge.microsoft.com/addons/detail/violentmonkey/eeagobfjdenkkddmbclomhiblgggliao))

2. Install [DuckDuckGPT](https://greasyfork.org/scripts/459849-duckduckgpt) (will load in userscript manager installed above)

3. Visit [duckduckgo.com](https://duckduckgo.com), type your search, engage bot!

<div align="center">

![ddgpt-demo](https://user-images.githubusercontent.com/10906554/220238659-9b59de4f-31d0-468a-a41d-528ac924732f.gif)
  
</div>

## Dependencies

<h6>
<div align="center">
<br />

<a href="https://chatgpt.js.org">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/chatgptjs/chatgpt.js/main/media/images/chatgpt.js-logo-dark-mode-5995x619.png">
    <img width=455 alt="chatgpt.js" style="margin: 0 0 -13px 18px" src="https://raw.githubusercontent.com/chatgptjs/chatgpt.js/main/media/images/chatgpt.js-logo-light-mode-5995x619.png">
</picture></a>
<a href="https://katex.org">
    <img width=175 alt="KaTeX" style="margin: 0 0 -13px 24px" src="https://i.imgur.com/3FBdSCi.png">
</a>
<br /><br />

DuckDuckGPT relies on code from the powerful [chatgpt.js](https://github.com/chatgptjs/chatgpt.js) library (c) 2023 KudoAI & contributors under the MIT license
<br>...and the [KaTeX](https://github.com/KaTeX/KaTeX) library (c) 2013–2020 Khan Academy & contributors under the MIT license.

</div>
</h6>

## Compatibility 

**DuckDuckGPT** is compatible w/ the following browsers using [Tampermonkey](https://www.tampermonkey.net/) or [Violentmonkey](https://violentmonkey.github.io/):

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Opera
- Brave
- Vivaldi
- LibreWolf
- Ghost
- QQ

If you've tested it to work in a browser not listed, simply create a [pull request](https://github.duckduckgpt.com/pulls) to become a contributor!

## Proxy Mode

Proxy API Mode (disabled by default) returns text responses using GPT-4, without the need for a chat.openai.com account.

When disabled, a ChatGPT account is required to fetch responses, but they are faster stream-type ones (like in demo).

If OpenAI API is acting unreliable, enable Proxy Mode like this:

<div align='center'>

![image](https://user-images.githubusercontent.com/10906554/229062641-abff9d17-21cc-49b2-a98e-7793c231c4f2.png)
![image](https://user-images.githubusercontent.com/10906554/229728672-3fec6a2d-c4fe-4738-871d-56c1d97cb2c5.png)

</div>

<br>

<a href="https://greasyfork.org/scripts/459849-duckduckgpt"><img alt="Install this script" src="https://github.com/adamlui/userscripts/raw/master/media/images/buttons/install-button.svg"></a><a href="#installation"><img alt="How to install" title="How to install" src="https://github.com/adamlui/userscripts/raw/master/media/images/buttons/help-button.svg"></a>
<br>
[Discuss](https://github.duckduckgpt.com/discussions) /
[Leave a review](https://duckduckgpt.com/userscript/review) /
[More ChatGPT userscripts](https://github.com/adamlui/userscripts/tree/master/chatgpt)

## Social links

<a href="https://technodon.org/@duckduckgpt" target="_blank"><img align="bottom" src="https://img.shields.io/mastodon/follow/109876284007792895?domain=https%3A%2F%2Ftechnodon.org&style=social" alt="Follow @duckduckgpt on Mastodon" title="Mastodon"></a>
[![Follow @adamlui on GitHub](https://img.shields.io/github/followers/adamlui?label=Follow%20%40adamlui&style=social "GitHub")](https://github.com/adamlui)
[![Follow @adamluitube on YouTube](https://img.shields.io/badge/YouTube-@AdamLuiTube-blue?style=social&logo=youtube&link=https://www.youtube.com/@AdamLuiTube)](https://www.youtube.com/AdamLuiTube?sub_confirmation=1)
<a href="https://elonsucks.org/@adam" target="_blank"><img align="bottom" src="https://img.shields.io/mastodon/follow/109387703022229926?domain=https%3A%2F%2Felonsucks.org&style=social" alt="Follow @adam on Mastodon" title="Mastodon">
[![Follow @adamllui on Twitter](https://img.shields.io/twitter/follow/adamllui?style=social)](https://twitter.com/adamllui)

## Contributors

This app exists thanks to code, translations, issues & ideas from the following contributors:

[![@adamlui](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/10906554?first-contrib=2023.02.11&h=50&w=50&mask=circle&maxage=7d "@adamlui")](https://github.com/adamlui)
[![@Delamcode](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/68170410?first-contrib=2023.02.19-unproxied-buggy-report-lead-to-proxied-mode&h=50&w=50&mask=circle&maxage=7d "@Delamcode")](https://github.com/Delamcode)
[![@Quoid](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/7660254?first-contrib=2023.03.01-stick-w-gm-api-recommendation&h=50&w=50&mask=circle&maxage=7d "@Quoid")](https://github.com/Quoid)
[![@Nord1cWarr1or](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/47604048?first-contrib=2023.04.01-proxy-ip-bug-report&h=50&w=50&mask=circle&maxage=7d "@Nord1cWarr1or")](https://github.com/Nord1cWarr1or)
[![@luetage](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/13988217?first-contrib=2023.04.21-ddg-dark-theme-bug-report&h=50&w=50&mask=circle&maxage=7d "@luetage")](https://github.com/luetage)
[![@afkvido](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/69060894?first-contrib=2023.05.16-katex-idea&h=50&w=50&mask=circle&maxage=7d "@afkvido")](https://github.com/afkvido)
[![@AliAlSarre](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/129722778?first-contrib=2023.05.23-css-readability&h=50&w=50&mask=circle&maxage=7d "@AliAlSarre")](https://github.com/AliAlSarre)
[![@wznmickey](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/44784663?first-contrib=2023.05.26-ddg-centered-mode-bug-report&h=50&w=50&mask=circle&maxage=7d)](https://github.com/wznmickey)
[![ChatGPT](https://images.weserv.nl/?url=https://i.imgur.com/tNyIPmG.jpg?h=50&w=50&mask=circle&maxage=7d "ChatGPT")](https://chat.openai.com)

## More ChatGPT apps

For even more epic ChatGPT apps, go here: https://github.com/adamlui/chatgpt-apps
<br><br>

## Related scripts

### <picture><source media="(prefers-color-scheme: dark)" srcset="https://i.imgur.com/RduASbD.png"><img width=16 src="https://raw.githubusercontent.com/adamlui/chatgpt-userscripts/main/media/icons/openai-favicon64.png"></picture> [ChatGPT Infinity ∞](https://chatgptevo.com/infinity/github) <a href="https://github.com/awesome-scripts/awesome-userscripts#chatgpt"><img src="https://awesome.re/mentioned-badge.svg" alt="Mentioned in Awesome Userscripts" style="margin:0 0 -2px 4px"></a>

Generate endless answers from all-knowing ChatGPT (in any language!)
<br>[Install](https://greasyfork.org/scripts/465051-chatgpt-infinity) / 
[Readme](https://github.com/adamlui/chatgpt-infinity#readme) / 
[Discuss](https://chatgptevo.com/infinity/discussions)

### <img src="https://media.bravegpt.com/images/bravegpt-icon48.png" width=18> [BraveGPT](https://bravegpt.com/greasemonkey) <a href="https://www.producthunt.com/posts/bravegpt?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-bravegpt" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=385630&theme=light" alt="BraveGPT - Bring&#0032;the&#0032;magic&#0032;of&#0032;ChatGPT&#0032;to&#0032;Brave&#0032;Search&#0033; | Product Hunt" style="width: 112px; height: 24px; margin:0 0 -4px 5px;" width="112" height="24" /></a>

Display ChatGPT answers in Brave Search sidebar.
<br>[Install](https://greasyfork.org/scripts/462440-bravegpt) / 
[Readme](https://bravegpt.com/greasemonkey/README.md) / 
[Discuss](https://github.bravegpt.com/discussions)

### <picture><source media="(prefers-color-scheme: dark)" srcset="https://i.imgur.com/RduASbD.png"><img width=16 src="https://raw.githubusercontent.com/adamlui/userscripts/master/chatgpt/media/icons/openai-favicon64.png"></picture> [ChatGPT Widescreen Mode 🖥️](https://github.com/adamlui/chatgpt-widescreen/tree/main/greasemonkey) <img src="https://raw.githubusercontent.com/adamlui/chatgpt-widescreen/main/media/images/badges/product-hunt/product-of-the-week-2-larger-centered-rounded-light.svg" alt="ChatGPT&#0032;Widescreen&#0032;Mode - Add&#0032;widescreen&#0032;&#0043;&#0032;full&#0032;window&#0032;modes&#0032;to&#0032;ChatGPT | Product Hunt" style="width: auto; height: 24px; margin:0 0 -4px 3px;" width="auto" height="24" />

Adds Widescreen + Full-Window modes to ChatGPT for enhanced viewing.
<br>[Install](https://greasyfork.org/scripts/461473-chatgpt-widescreen-mode) / 
[Readme](https://github.com/adamlui/chatgpt-widescreen/blob/main/greasemonkey/README.md) / 
[Discuss](https://github.com/adamlui/chatgpt-widescreen/discussions)

#

<a href="https://github.com/adamlui/userscripts">**More userscripts**</a> / 
<a href="#--------------">Back to top ↑</a>
