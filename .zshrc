# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

export PATH="/usr/local/sbin:/usr/local/bin:/usr/bin:/home/samarth/.emacs.d/bin"
export PATH="$PATH:/home/samarth/.local/lib/python3.8/site-packages"
export PATH="$PATH:/home/samarth/.local/bin"
export PATH="$PATH:/home/samarth/.vim/bundle/vim-live-latex-preview/bin"

# Path to your oh-my-zsh installation.
export ZSH="/home/samarth/.oh-my-zsh"

export TERM="xterm-256color"

fpath+=$HOME/.zsh/pure

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME=""

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

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
HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git
	zsh-autosuggestions
    zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
export LANG=en_US.UTF-8

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# echo -e $blue"                              __________"
# echo -e $blue"                     ________|          |________"
# echo -e $blue"                    |       /   ||||||   \       |"
# echo -e $blue"                    |     ,'              '.     |"
# echo -e $blue"                    |   ,'                  '.   |"
# echo -e $blue"                    | ,'   ||||||||||||||||   '. |"
# echo -e $blue"                    ,'  /____________________\  '."
# echo -e $blue"                   /______________________________\\"
# echo -e $blue"                  |                                |"
# echo -e $blue"                  |                                |"
# echo -e $blue"                  |                                |"
# echo -e $blue"                  |________________________________|"
# echo -e $blue"                    |____________________________|"
# echo -e $blue"                                                              "
# echo -e $blue"        ,----------------------------------------------------,"
# echo -e $blue"        | [][][][][]  [][][][][]  [][][][]  [][__]  [][][][] |"
# echo -e $blue"        |                                                    |"
# echo -e $blue"        |  [][][][][][][][][][][][][][_]    [][][]  [][][][] |"
# echo -e $blue"        |  [_][][][][][][][][][][][][][ |   [][][]  [][][][] |"
# echo -e $blue"        | [][_][][][][][][][][][][][][]||     []    [][][][] |"
# echo -e $blue"        | [__][][][][][][][][][][][][__]    [][][]  [][][]|| |"
# echo -e $blue"        |   [__][________________][__]              [__][]|| |"
# echo -e $blue"        '----------------------------------------------------'"

# figlet "Welcome, Samarth"
# echo "CHANGE THE WORLD!"

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# # SPACESHIP PROMPT

# eval "$(starship init zsh)"

# PROMPT
autoload -Uz vcs_info
precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )

setopt prompt_subst
zstyle ':vcs_info:*' enable git
zstyle ':vcs_info:*' actionformats \
    '%F{5}(%f%s%F{5})%F{3}-%F{5}[%F{2}%b%F{3}|%F{1}%a%F{5}]%f '
zstyle ':vcs_info:*' formats       \
    '%F{5}(%f%s%F{5})%F{3}-%F{5}[%F{2}%b%F{5}]%f '
zstyle ':vcs_info:(sv[nk]|bzr):*' branchformat '%b%F{1}:%F{3}%r'
precmd () { vcs_info }

PROMPT='%F{cyan}%f %(?.%F{green}%B✔%f%b.%F{red}%B✘ %?)%f%b %U%B%F{blue}%0~%f%b%u ${vcs_info_msg_0_}
%F{cyan}%(!.!⟫.❱)%f '

RPROMPT='%F{yellow}%n@%M%f%E'

source /home/samarth/.config/broot/launcher/bash/br
