# tudu

`tudu` is a simple command line tool with a tui mode for managing your to-do lists

#### Used libraries:

- `sqlalchemy`  : database
- `curses`      : TUI
- `plyer`       : notifications

The documentation has been generated using `Sphinx`

[link to github](https://github.com/lubczanska/tudu)
## Installation

#### pip

```console
# pip3 install tudu
```
#### use locally

You will need to have `sqlalchemy` and `plyer` packages installed
```
$ git clone https://github.com/lubczanska/tudu
$ cd tudu
$ python3 tudu.py
```  

-----

`dbus-python` is a dependency of `plyer` that doesn't get automatically installed by pip. The app works without it, but will display warnings

## Usage

```console
$ tudu --help

usage: tudu [-h] [--quiet]
               {add,rm,edit,check,uncheck,sticky,ls,show} ...

A simple to-do list app

options:
  -h, --help            show this help message and exit
  --quiet, -q           run tui without triggering notifications

commands:
  {add,rm,edit,check,uncheck,sticky,ls,show}
    add                 add new list or tasks
    rm                  remove list or tasks
    edit                edit list/task details
    check               mark task as completed
    uncheck             mark task as not completed
    sticky              add task to startup list
    ls                  display all tasks in a list in tui mode
    show                display task details

If no command is specified tui mode will be opened. In tui mode
press ':' to enter commands

```
#### EXAMPLES

```console
# Add a weekly reminder to water plants by sunday
$ tudu add "My list" "Water plants" --deadline sunday --priority 1 --repeat 7

# Edit a typo in task name
$ tudu edit "My list" "Task with a tpyo in name" --name "Task with no typo in name"

# Remove "My list"
$ tudu rm "My list"
```
If you want to see tasks or lists without opening the tui mode:
```console
# See all lists in the database
$ tudu ls

# See all tasks on "My list"
$ tudu show "My list"
```
----
### Task mode
```console
$ tudu show [-h] [--center] [--color COLOR] LIST [TASK]
```
Task mode displays a task in a tui mode that allows you to check the task with `Space`, display more information with `i` or delete it with `d`
 
`--center` flag centers the text in the terminal and `--color COLOR` changes task name color to the specified color [0-7]

-----
### TUI mode
```console
# Shows all lists in tui mode
$ tudu

# Shows "My list" in tui mode
$ ls "My list"
```

#### Navigation
Use arrow keys or `h` `j` `k` `l` to navigate, `Enter` or `Space` to check tasks and `q` to quit

Other keybindings:

| `:` | open the command prompt |
|`a`  | Start adding a list or a task to the currently displayed list |
|`d`  | Start deleting selected entry |
|`e`  | Start editing selected entry |
|`i`  | Show more information |

#### Commands in TUI mode

Press `:` to enter command mode normally or `a` `d` or `e` to have it filled with the begging of the corresponding command.

Type `help` `--help` or `-h` for tui-specific help or `<command> help` for help about a specific command.

`ls` and `show` are unavailable in TUI mode

`<command>`  triggers assist mode, where you will be prompted for further arguments. Be sure to escape all spaces or wrap the text in quotes.

When displaying a list you can use `.` to denote it in commands instead of writing the name
_____
##### WARNING
A small or unexpectedly resized terminal window may cause the content to not display as intended. In that situation simply resize the terminal to appropriate dimensions.
