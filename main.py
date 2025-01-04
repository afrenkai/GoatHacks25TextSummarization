from summarize import summarizeText

TEXT = '''

Just installed LazyVim and liking it quite a bit, though I don't understand how to switch between open tabs.

It seems like <leader>-<tab>-[ or <leader>-<tab>-] should do it, but after I hit '[' or ']' the popup menu simply goes away instead of actually switching to a different open tab. By contrast, <leader>-<tab>-<tab> will create a new tab, and <leader>-<tab>-d will delete the current tab.

Am I misunderstanding how this feature is supposed to work?

(I searched for this and didn't find anything recent or specific so maybe I'm doing something wrong)

[edit] so, yes, it is a misunderstanding on my part. What appear as "tabs" across the top of the screen are not neovim tabs, but visual representations of open buffers. Which, yes, look visually like "tabs," but they're not actual vim tabs. So the way to move between "tabs" (buffers) in LazyVim using the default keymaps is <S-h> and <S-l>.

*Actual* neovim tabs have some shortcuts via the <leader><tab> sequence. When you create a new tab in lazyvim (<leader><tab><tab>) it and other tabs will appear to the right of the open buffers along the top of the screen as numbered ui-widgets-which-look-like-tabs-but-need-a-different-name-since-its-confusing.

TLDR: <S-h>, <S-l> and what I'm calling tabs are actually buffers

'''

summary = summarizeText(TEXT, numSentencesTarget = 2)
print("Summary", summary)

