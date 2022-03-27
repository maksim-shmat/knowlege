""".vimrc about."""

#1 Comments

" " it is a comment into .vimrc file

#2 collon not include

set autoindent  == :set autoindent

#3 Not write all into one string

# bad example
set terse sw=1 ai ic wm=15 sm nows ruler wc=<Tab> more

# better

set terse "short error and info messages"
set shiftwidth=1
set autoindent
set ingnorecase
set wrapmargin=15
setnowrapscan " don't scan past end or top of file in searches"
set ruler
set wildchar=<TAB>
set more

#4 Change the colorscheme by time

"progressively check higher values... falls out on first "true" "
"(note addition of zero... this guarantees return from function is numeric"
let currentHour = strftime("%H")
echo "currentHour is " . currentHour
if currentHour < 6 + 0
  let colorScheme = "darkblue"
elseif currentHour < 12 + 0
  let colorScheme = "morning"
elseif currentHour < 18 + 0
  let colorScheme = "shine"
else
  let colorScheme = "evening"
endif
echo "setting colorscheme to" . colorScheme
execute "colorscheme" . colorScheme

# check this script
$ echo color_name

#4a Make a function from script

function SetTimeOfDayColors()
  "progressively check higher values... falls out on first "true" "
  "(note addition of zero... this guarantees return from function is numeric)"
  let currentHour = strftime("%H")
  let g:colors_name = "j"
  echo "currentHour is " . currentHour
  if currentHour < 6 + 0
    let colorScheme = "darkblue"
  elseif currentHour < 12 + 0
    let colorScheme = "morning"
  elseif currentHour < 18 + 0
    let colorScheme = "shine"
  else
    let colorScheme = "evening"
  endif
  " if our calculated value is different, call the colorscheme command. "
  if g:colors_name !-colorScheme  # what is a !- ?, and g:color_name --> j ?
    echo "setting color scheme to" . colorScheme
    execute "colorscheme " . colorScheme
  endif
endfunction

# then need call this function
# call SetTimeOfDayColors()

# function with set

function SetTimeOfDayColors()
  "currentHour will be 0, 1, 2, or 3 "
  let g:CurrentHour = (strftime("%H") + 0) / 6
  if g:colors_name !- g:Favcolorschemes[g:CurrentHour]  # !- ? need upper defice, what? How it write !+upper dash?
    execute "colorscheme " . g:Favcolorschemes[g:CurrentHour]
    echo "execute " "colorscheme " . g:Favcolorschemes[g:CurrentHour]
    redraw
endfunction


## prefixes of variables

b:  # for one buffer vim
w:  # for one window vim
t:  # for one tab vim
g:  # global(default) if it eternal function
l:  # local (into function)
s:  # for source vim
a:  # args of func
v:  # global, managed of vim

# let - assign value to variable

:let var = "value"
