# Personal Tooling

Small scripts, automations, and customizations I use to make life a little *fun* and easier.

## Contents

```text
personal-tooling/
├── shell/
│   └── terminal_greeting.py
├── scripts/
└── automations/
```

## Terminal Greeting

A small Bash startup script that shows a random `cowsay` animal with a random Dōgen quote.

Requires:

```bash
python3
cowsay
```

Add this to `~/.bashrc` to run it on every new terminal:

```bash
python3 ~/personal-tooling/shell/terminal_greeting.py
```
