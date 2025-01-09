+++
date = '2025-01-07T13:33:19+08:00'
draft = true
title = 'Ssh_config_best'
toc = true
+++


# zsh 配置

## 安装 oh my zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

配置 `.zshrc`
```bash

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time Oh My Zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# ZSH_THEME="robbyrussell"
ZSH_THEME="amuse"
# theme:
# git: xiong-chiamiov-plus amuse powerlevel10k
# time: crunch

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  extract
  autojump
  zsh-autosuggestions
  zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

export EDITOR='vim'

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='nvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch $(uname -m)"

# Set personal aliases, overriding those provided by Oh My Zsh libs,
# plugins, and themes. Aliases can be placed here, though Oh My Zsh
# users are encouraged to define aliases within a top-level file in
# the $ZSH_CUSTOM folder, with .zsh extension. Examples:
# - $ZSH_CUSTOM/aliases.zsh
# - $ZSH_CUSTOM/macos.zsh
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"


# IDEA path
#

# PATH env
source "$HOME/.cargo/env"
# for autojump https://github.com/wting/autojump
[ -f /opt/homebrew/etc/profile.d/autojump.sh ] && . /opt/homebrew/etc/profile.d/autojump.sh

# fnm
# fnm
FNM_PATH="$HOME/.local/share/fnm"
if [ -d "$FNM_PATH" ]; then
  export PATH="$FNM_PATH:$PATH"
  eval "`fnm env`"
fi

# IDEA path
export PATH="/Applications/IntelliJ IDEA CE.app/Contents/MacOS:$PATH"
export PATH="/opt/homebrew/opt/dotnet@6/bin:$PATH"
export PATH="/home/simons/.local/bin:$PATH"
export PATH="/Users/simons/.yarn/bin:/Users/simons/.config/yarn/global:$PATH"

# pnpm
export PNPM_HOME="/Users/simons/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end
#
#

# poetry
export PATH="$HOME/.local/bin:$PATH"

# go
export PATH="$PATH:$GOPATH/bin"

```

# 配置 Github

## 生成密钥对

```bash
# 生成一对 SSH 密钥
ssh-keygen -t ed25519 -C "your_email@example.com" # 输入邮箱
# 启动 SSH 代理，用于管理 SSH 密钥
eval "$(ssh-agent -s)"
# 将 SSH 私钥添加到 SSH 代理
ssh-add ~/.ssh/id_ed25519
# 显示公钥内容
cat ~/.ssh/id_ed25519.pub
```
##  配置 SSH 密钥：

1. 将公钥内容复制并添加到 GitHub 的 SSH 密钥设置中。

2. 使用 SSH 克隆仓库或推送代码，无需每次都输入密码。

# 远程服务器登录

生成 SSH 密钥。

将公钥内容复制到远程服务器的 ~/.ssh/authorized_keys 文件中。

使用 SSH 私钥登录远程服务器，无需输入密码。



# 设置 Git

1. 重新设置 `https` 为 `ssh`

```bash
git remote -v。# 查看协议

ggit remote set-url origin git@github.com:caoyang2002/web3_obsidian.git。# 设置为 ssh

ssh -T git@github.com. # 测试连接
```




## 配置代理（可选）
```bash
export https_proxy=http://127.0.0.1:7897 http_proxy=http://127.0.0.1:7897 all_proxy=socks5://127.0.0.1:7897

export https_proxy=http://192.168.5.1:7890 http_proxy=http://192.168.5.1:7890 all_proxy=socks5://192.168.5.1:7891
```

安装 ts-node

安装 service

# Mysql

```bash
brew install mysql

brew services start mysql

mysql_secure_installation

mysql -u root -p
# 可以直接登录

# 修改密码
ALTER USER 'root'@'localhost' IDENTIFIED BY '新密码';
# or
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('新密码');

# 刷新
FLUSH PRIVILEGES

# 创建新用户
CREATE USER '新用户名'@'%' IDENTIFIED BY '密码';

# 授予所有权限
GRANT ALL PRIVILEGES ON *.* TO '新用户名'@'localhost';

# 授予特定数据库权限
GRANT ALL PRIVILEGES ON 数据库名.* TO '新用户名'@'localhost';

# 授予特定的操作权限
RANT SELECT, INSERT, UPDATE, DELETE ON 数据库名.* TO '新用户名'@'localhost';

# 刷新
FLUSH PRIVILEGES;

# 删除用户
DROP USER '用户名'@'localhost';
```
