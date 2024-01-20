"""Усталёўванне языкоў."""


set keymap=belarusian-jcuken  # but it is temporary in this session

set keymap=russuan-jcuken  # воткнул только это, смена lang по Ctrl+^

set iminsert=0  # default eng
set imsearch=0  # search eng
cmap <silent> <C-F> <C-^>  # change eng/ru for Ctrl+F
imap <silent> <C-F> <C-^>X<Esc>:call MyKeyMapHighlight()<CR>a<C-H>
nmap <silent> <C-F> a<C-^><Esc>:call MyKeyMapHighlight()<CR>
vmap <silent> <C-F> <Esc>a<C-^><Esc>:call MyKeyMapHighlight()<CR>gv

function MyKeyMapHighlight()
    if &iminsert == 0
        hi StatusLine ctermfg=DarkBlue guifg=DarkBlue
    else
        hi StatusLine ctermfg=DarkRed guifg=DarkRed
    endif
endfunction  # change language and changed statusbar color
call MyKeyMapHighlight()  # call function for start vim
au WinEnter * :cal MyKeyMapHighlight()  # for reload color indication for new window

highlight lCursor guifg=None guibg=Cyan  # change cursor for Cian when russian


:setlocal spell spelllang=ru_yo,en_us  # change Ё , [s ]s - is spellchecking from vocabulary use it for code bitch
but it for russian
or in .vimrc
:set spellang=ru_yo,en_us  # and then in vim :set spell/:set nospell

:set spell - fork for default for eng!
