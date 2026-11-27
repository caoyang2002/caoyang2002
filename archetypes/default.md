+++
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
date = {{ .Date }}
draft = false
author = "{{ .Site.Params.defaults.author | default "simons" }}"

categories = {{ .Site.Params.defaults.categories | default (slice "暂无") | jsonify }}
tags = {{ .Site.Params.defaults.tags | default (slice "暂无") | jsonify }}
series = ""
weight = 0

description = "{{ .Site.Params.defaults.description | default "" }}"
summary = ""
keywords = []
cover = ""
image = ""
images = []

toc = true
comments = true
showShare = true
codeRunners = false

aliases = []

# 可选：有实质更新时再启用
# lastmod = {{ .Date }}
# slug = ""
# password = ""
+++
