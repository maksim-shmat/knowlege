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
  if g:colors_name != colorScheme  # g:color_name --> j ?
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
  if g:colors_name != g:Favcolorschemes[g:CurrentHour]
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

#5 Autocommands (autocmd)

autocmd [group] event pattern [nested] command

Events(80+):

BufNewFile  # start cmd how start new file
BufReadPre  # start cmd before move new buffer
BufRead, BufReadPost  # after read file
BufWrite, BufWritePre  # before write buffer into file
FileType  # after set option filetype
VimResized  # after resized window
WinEnter, WinLeave  # in/out window
CursorMoved, CursorMovedI  # moved cursor in normal/insert mode

Example: (check file type)

autocmd CursorMovedI * call CheckFileType()

# write a function

function CheckFileType()
if exists("b:countCheck") == 0
  let b:countCheck = 0
endif
let b:countCheck += 1
"Don't start detecting until approx. 20 chars. "
  if &filetype == "" && b:contCheck > 20 && b:countCheck < 200
    filetype detect
  endif
  endfunction

#6 Add autocmd to auto group

augroup newFileDetection
autocmd CursorMovedI * call CheckFileType()
augroup END

#7 Del autocmd

autocmd! newFileDetection

# Final assemble

augroup newFileDetection
autocmd CursorMovedI * call CheckFileType()
augroup END

function CheckFileType()
  if exists("b:countCheck") == 0
    let b:countCheck = 0
  endif

  let b:countCheck += 1

  " Don't start detecting until approx. 20 chars. "
  if &filetype == "" && b:countCheck > 20 && b:countCheck < 200
    filetype detect
  " If we've exceeded the count theshold (200), OR a filetype has been detected "
  "delete the autocmd! "
  elseif b:countCheck >= 200 || &filetype != ""
    autocmd! newFileDetection
  endif
endfunction

#8 Script how show time into .html (but may more formats)

autocmd BufWritePre,FileWritePre * .html mark s|call LastMod()| 's
"'my mark not includ it 
fun LastMod()
  " if therer are more than 20 lines, set our max to 20, oterwise, scan "
  " entire file. "
  if line("$") > 20
    let lastModifiedline = 20
  else
    let lastModifiedline = line("$")
  endif
  exe "1," . lastModifiedline . "g/Last modified: /s/Last modified:
  .*/Last modified: " .
  \ strftime("%Y %b %d")
endfun

#9 simple autocmd

autocmd BufRead,BufNewFile * .html set shiftwidth=2
autocmd BufRead,BufNewFile * .c, *.h set shiftwidth=4

#10
