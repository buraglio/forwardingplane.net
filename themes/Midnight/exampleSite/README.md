# Midnight Site Template

This repository serves as a replacement for the `hugo new site` command for
users of [Midnight](https://bluestnight.com/products/midnight).

After cloning the repository, run the following command from inside it to also
download the latest version of Midnight:

```
git clone https://gitlab.com/BluestNight/Midnight.git themes/Midnight
```

The template comes with the usual empty folders created by `hugo new`, as well
as a documented `config.toml` file, and a `netlify.toml` file to make it
easier for people who plan to use [Netlify](https://netlify.com).

Users not planning on publishing to Netlify can safely delete the
`netlify.toml` file.

# Getting Started

To prepare the site for your own use, delete the content under `content/` and
remove or modify the `[params.social] gitlab` and `[menu]` options in
`config.toml`.

# Attributions

This example site uses content and settings necessary to make it display the
[Hugo example site](https://github.com/gohugoio/hugoBasicExample), available
under the [MIT license](https://github.com/gohugoio/hugoBasicExample/blob/master/LICENSE). 

The background image included in this example site is by
[Patrick Carr](https://unsplash.com/photos/pAoo1Rs1Yy8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
on [Unsplash](https://unsplash.com/).
