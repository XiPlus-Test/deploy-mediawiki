# deploy-mediawiki

## Example workflow
```yaml
name: Deploy to MediaWiki

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - uses: xiplus-mediawiki-programs/deploy-mediawiki/.github/actions/setup@main
        with:
          username: YOUR_USERNAME
          botname: ${{ secrets.BOT_NAME }}
          password: ${{ secrets.BOT_PASS }}
          family: wikipedia
          mylang: zh

      - name: Get short sha
        id: vars
        run: echo "sha_short=$(git rev-parse --short HEAD)" >> $GITHUB_OUTPUT

      - uses: xiplus-mediawiki-programs/deploy-mediawiki/.github/actions/deploy@main
        with:
          src: common.js
          dst: User:YOUR_USERNAME/common.js
          summary: ${{ steps.vars.outputs.sha_short }} ${{ github.event.head_commit.message }}
```

## Deploy to private wiki
```yaml
- uses: xiplus-mediawiki-programs/deploy-mediawiki/.github/actions/setup@main
  with:
    username: YOUR_USERNAME
    botname: ${{ secrets.BOT_NAME }}
    password: ${{ secrets.BOT_PASS }}
    url: https://example.com/testwiki/w/api.php
```
