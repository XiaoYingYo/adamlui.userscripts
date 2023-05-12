# <picture><source media="(prefers-color-scheme: dark)" srcset="https://i.imgur.com/RduASbD.png"><img width=23 src="https://raw.githubusercontent.com/adamlui/userscripts/master/chatgpt/media/icons/openai-favicon64.png"></picture> ChatGPT Auto Refresh ↻ &nbsp;[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Tired%20of%20constant%20interruptions%20on%20ChatGPT%3F%20Auto-refresh%20your%20sessions%20w%2F%20this%20plug-in%21%20&url=https://github.com/adamlui/userscripts/tree/master/chatgpt/chatgpt-auto-refresh&hashtags=greasemonkey,openai,chatgpt)

![usercount](https://img.shields.io/greasyfork/dt/462422?label=Users&color=)
[![license](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)
[![support](https://img.shields.io/badge/Support-Chrome/Firefox/Edge/Opera/Brave/Vivaldi/Waterfox/LibreWolf/Ghost/QQ-989898.svg)](#compatibility)
[![commits](https://img.shields.io/github/commit-activity/w/adamlui/chatgpt-auto-refresh?label=Commits)](https://github.com/adamlui/chatgpt-auto-refresh/commits/main)
[![code-quality](https://img.shields.io/codefactor/grade/github/adamlui/chatgpt-auto-refresh?label=Code%20Quality)](https://www.codefactor.io/repository/github/adamlui/chatgpt-auto-refresh)
<a alt="chatgpt.js" href="https://chatgpt.js.org"><img height=20 src="https://i.imgur.com/AwQqCmB.png"></a>
[![Mentioned in Awesome Userscripts](https://awesome.re/mentioned-badge.svg)](https://github.com/awesome-scripts/awesome-userscripts#chatgpt)

### Keeps ChatGPT sessions fresh via background requests to eliminate network errors + Cloudflare checks.

###### English | [简体中文](zh-cn#readme)

<a href="https://greasyfork.org/scripts/462422-chatgpt-auto-refresh"><img alt="Install this script" src="https://github.com/adamlui/userscripts/raw/master/media/images/buttons/install-button.svg"></a><a href="#installation"><img alt="How to install" title="How to install" src="https://github.com/adamlui/userscripts/raw/master/media/images/buttons/help-button.svg"></a>
<br>
[Discuss](https://github.com/adamlui/chatgpt-auto-refresh/discussions) /
[Review](https://greasyfork.org/scripts/462422-chatgpt-auto-refresh/feedback#post-discussion) /
[Contact author](https://github.com/adamlui)

#

![image](https://user-images.githubusercontent.com/10906554/234756105-cf367acc-644a-49ee-8586-43c51d43e359.png)
<img alt="↻ Auto-Refresh: ON]" width=355 src="https://raw.githubusercontent.com/adamlui/chatgpt-auto-refresh/main/media/images/screenshots/mode-notification-on.png">

## What it does

- #### Get rid of annoying Cloudflare checks:

<div align="center">
    
![](https://user-images.githubusercontent.com/10906554/229415084-97f55e6d-eb21-4ac0-bc2a-c6174a44cfe1.png)

</div>

- #### Get rid of annoying ChatGPT network errors:

<div align="center">

![](https://user-images.githubusercontent.com/10906554/229413173-7183e459-06ca-4b95-b241-8ca79b18039d.png)
![](https://user-images.githubusercontent.com/10906554/229413421-a6264dc2-a2e3-48a7-ad86-7789dbd7df54.png)
<img width=333 src="https://user-images.githubusercontent.com/10906554/229416105-931e2035-7e30-440a-bdc9-e570daf0d769.png">
    
</div>

## Benefits

&nbsp;&nbsp;&nbsp;🛡️ <strong>Safe</strong> — No unnecessary account-related requests sent

&nbsp;&nbsp;&nbsp;🪶 <strong>Lightweight</strong> — Very little code used, only what's neccessary (keep session alive) saving memory

&nbsp;&nbsp;&nbsp;⌛ <strong>Time-saver</strong> — No more constant copy/paste/refresh just from minutes of inactivity!

&nbsp;&nbsp;&nbsp;🤯 <mark>Works ***even in background tabs!***</mark>

## User feedback

<img width=535 src="https://i.imgur.com/JX3u7Yz.png">

## Installation

1. Install Tampermonkey ([Chrome](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo), [Firefox](https://addons.mozilla.org/firefox/addon/tampermonkey/), [Edge](https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd), [Opera](https://addons.opera.com/extensions/details/tampermonkey-beta/)) or Violentmonkey ([Chrome](https://chrome.google.com/webstore/detail/violent-monkey/jinjaccalgkegednnccohejagnlnfdag), [Firefox](https://addons.mozilla.org/firefox/addon/violentmonkey/), [Edge](https://microsoftedge.microsoft.com/addons/detail/violentmonkey/eeagobfjdenkkddmbclomhiblgggliao))

2. Install [ChatGPT Auto Refresh](https://greasyfork.org/scripts/462422-chatgpt-auto-refresh) (will load in userscript manager installed above)

3. Visit [chat.openai.com](https://chat.openai.com) as normal, and sessions will auto-refresh (in background w/ no penalty to you) at a regular interval!

<div align="center">
    
![Auto-Refresh Enabled](https://raw.githubusercontent.com/adamlui/chatgpt-auto-refresh/main/media/images/screenshots/mode-toggle-on.jpg)

</div>

## Dependencies

<h6>
<div align="center">
<br />

<a href="https://chatgpt.js.org">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/chatgptjs/chatgpt.js/main/media/images/chatgpt.js-logo-dark-mode-5995x619.png">
    <img width=546 alt="chatgpt.js" src="https://raw.githubusercontent.com/chatgptjs/chatgpt.js/main/media/images/chatgpt.js-logo-light-mode-5995x619.png">
</picture></a>
<br /><br />

ChatGPT Auto Refresh relies on code from the powerful [chatgpt.js](https://github.com/chatgptjs/chatgpt.js) library (c) 2023 Adam Lui, chatgpt.js & contributors under the MIT license.

</div>
</h6>

## Compatibility

ChatGPT Auto Refresh is compatible w/ the following browsers using [Tampermonkey](https://www.tampermonkey.net/) or [Violentmonkey](https://violentmonkey.github.io/):

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Opera
- Brave
- Vivaldi
- Waterfox
- LibreWolf
- Ghost
- QQ

If you've tested it to work in a browser not listed, create a [pull request](https://github.com/adamlui/chatgpt-auto-refresh/pulls) to become a contributor!

<a href="https://greasyfork.org/scripts/462422-chatgpt-auto-refresh"><img alt="Install this script" src="https://github.com/adamlui/userscripts/raw/master/media/images/buttons/install-button.svg"></a><a href="#installation"><img alt="How to install" title="How to install" src="https://github.com/adamlui/userscripts/raw/master/media/images/buttons/help-button.svg"></a>
<br>
[Discuss](https://github.com/adamlui/chatgpt-auto-refresh/discussions) / 
[Leave a review](https://greasyfork.org/scripts/462422-chatgpt-auto-refresh/feedback#post-discussion) /
[More ChatGPT userscripts](https://github.com/adamlui/userscripts/tree/master/chatgpt)

## Author links

[![Follow @adamlui on GitHub](https://img.shields.io/github/followers/adamlui?label=Follow%20%40adamlui&style=social "GitHub")](https://github.com/adamlui)
[![Follow @adamluitube on YouTube](https://img.shields.io/youtube/channel/subscribers/UCgBMqK7SRL5R__3qM-YAcSg?label=Follow%20%40adamluitube&style=social)](https://www.youtube.com/AdamLuiTube?sub_confirmation=1)
<a href="https://elonsucks.org/@adam" target="_blank"><img align="bottom" src="https://img.shields.io/mastodon/follow/109387703022229926?domain=https%3A%2F%2Felonsucks.org&style=social" alt="Follow @adam on Mastodon" title="Mastodon"></a>
[![Follow @adamllui on Twitter](https://img.shields.io/twitter/follow/adamllui?style=social)](https://twitter.com/adamllui)

## More ChatGPT apps

For even more epic ChatGPT apps, go here: https://github.com/adamlui/chatgpt-apps
<br><br>

## Related scripts

### <img width=17 style="margin-bottom:-1px" src="https://raw.githubusercontent.com/adamlui/chatgpt-widescreen/main/media/images/icons/widescreen-robot-emoji/icon32.png"> [ChatGPT Widescreen Mode](https://chatgptevo.com/widescreen/github) <img src="https://raw.githubusercontent.com/adamlui/chatgpt-widescreen/main/media/images/badges/product-hunt/product-of-the-week-2-larger-centered-rounded-light.svg" alt="ChatGPT&#0032;Widescreen&#0032;Mode - Add&#0032;widescreen&#0032;&#0043;&#0032;full&#0032;window&#0032;modes&#0032;to&#0032;ChatGPT | Product Hunt" style="width: auto; height: 24px; margin:0 0 -4px 5px;" width="auto" height="24" />

Adds Widescreen + Full-Window modes to ChatGPT for reduced scrolling.
<br>[Install](https://github.com/adamlui/chatgpt-widescreen#installation) / 
[Readme](https://github.com/adamlui/chatgpt-widescreen#readme) / 
[Discuss](https://chatgptevo.com/widescreen/discussions)

### <img style="margin-bottom:-1px" src="https://media.bravegpt.com/images/bravegpt-icon48.png" width=18> [BraveGPT](https://bravegpt.com/greasemonkey) <a href="https://www.producthunt.com/posts/bravegpt?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-bravegpt" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=385630&theme=light" alt="BraveGPT - Bring&#0032;the&#0032;magic&#0032;of&#0032;ChatGPT&#0032;to&#0032;Brave&#0032;Search&#0033; | Product Hunt" style="width: 112px; height: 24px; margin:0 0 -3px 5px;" width="112" height="24" /></a>

Display ChatGPT answers in Brave Search sidebar.
<br>[Install](https://greasyfork.org/scripts/462440-bravegpt) / 
[Readme](https://github.bravegpt.com/#readme) / 
[Discuss](https://github.bravegpt.com/discussions)

### <picture><source media="(prefers-color-scheme: dark)" srcset="https://i.imgur.com/RduASbD.png"><img width=16 src="https://raw.githubusercontent.com/adamlui/chatgpt-userscripts/main/media/icons/openai-favicon64.png"></picture> [ChatGPT Infinity ∞](https://chatgptevo.com/infinity/github) <a href="https://github.com/awesome-scripts/awesome-userscripts#chatgpt"><img src="https://awesome.re/mentioned-badge.svg" alt="Mentioned in Awesome Userscripts" style="margin:0 0 -2px 4px"></a>

Generate endless answers from all-knowing ChatGPT (in any language!)
<br>[Install](https://greasyfork.org/scripts/465051-chatgpt-infinity) / 
[Readme](https://github.com/adamlui/chatgpt-infinity#readme) / 
[Discuss](https://chatgptevo.com/infinity/discussions)

#
  
<a href="https://github.com/adamlui/userscripts">**More userscripts**</a> / 
<a href="#-chatgpt-auto-refresh--">Back to top ↑</a>
