+++
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
date = {{ .Date }}
draft = true
author = "{{ .Site.Params.defaults.author }}"
categories = {{ .Site.Params.defaults.categories  | jsonify }}
tags = {{ .Site.Params.defaults.tags  | jsonify }}
description = "{{ .Site.Params.defaults.description }}"
+++
