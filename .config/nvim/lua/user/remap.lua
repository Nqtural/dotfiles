-- Set leader key
vim.g.mapleader = " "

-- Skeletons
vim.keymap.set("n", ",html", ":-1read $HOME/.config/nvim/skeletons/skeleton.html<CR>3jwf>a")
vim.keymap.set("n", ",py", ":-1read $HOME/.config/nvim/skeletons/skeleton.py<CR>jA")

-- NvimTree
vim.keymap.set("n", "<leader>o", vim.cmd.NvimTreeToggle)

-- Undotree
vim.keymap.set("n", "<leader>u", vim.cmd.UndotreeToggle)

-- Telescope
vim.keymap.set("n", "<leader>f", ":Telescope find_files<CR>")
vim.keymap.set("n", "<leader>r", ":Telescope oldfiles<CR>")

-- Commentary
vim.keymap.set("n", "<leader>c", ":Commentary<CR>")
vim.keymap.set("v", "<leader>c", ":'<,'>Commentary<CR>")

-- Get rid of arrow keys
-- Insert
vim.keymap.set("i", "<Up>", "<nop>")
vim.keymap.set("i", "<Right>", "<nop>")
vim.keymap.set("i", "<Down>", "<nop>")
vim.keymap.set("i", "<Left>", "<nop>")
-- Normal
vim.keymap.set("n", "<Up>", "<nop>")
vim.keymap.set("n", "<Right>", "<nop>")
vim.keymap.set("n", "<Down>", "<nop>")
vim.keymap.set("n", "<Left>", "<nop>")
-- Visual
vim.keymap.set("v", "<Up>", "<nop>")
vim.keymap.set("v", "<Right>", "<nop>")
vim.keymap.set("v", "<Down>", "<nop>")
vim.keymap.set("v", "<Left>", "<nop>")

-- Move lines in visual mode with K and J
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")

-- Make cursor stay when replacing newline with space
vim.keymap.set("n", "J", "mzJ`z")

-- Make search terms stay in the middle
vim.keymap.set("n", "n", "nzzzv")

vim.keymap.set("n", "N", "Nzzzv")

-- Yank to system clipboard
vim.keymap.set("n", "<leader>y", "\"+y")
vim.keymap.set("v", "<leader>y", "\"+y")
vim.keymap.set("n", "<leader>Y", "\"+Y")

-- Search and replace current word
vim.keymap.set("n", "<leader>sr", [[:%s/\<<C-r><C-w>\>//gI<Left><Left><Left>]])

-- Make file executable
vim.keymap.set("n", "<leader>x", "<cmd>!chmod +x %<CR>", { silent = true })

-- Better window navigation
vim.keymap.set("n", "<C-h>", "<C-w>h")
vim.keymap.set("n", "<C-j>", "<C-w>j")
vim.keymap.set("n", "<C-k>", "<C-w>k")
vim.keymap.set("n", "<C-l>", "<C-w>l")

-- Stay in indent mode
vim.keymap.set("v", "<", "<gv")
vim.keymap.set("v", ">", ">gv")

-- Don't write to clipboard when pasting over selection
vim.keymap.set("v", "p", "_dP")

-- Deselect in visual modes
vim.keymap.set("v", "<leader>d", "<Esc>V")

-- Toggle line numbers
vim.keymap.set("n", "<leader>n", ":set nu! rnu!<CR>")
vim.keymap.set("n", "<leader>N", ":set nu! nu?<CR>")
vim.keymap.set("n", "<leader>rN", ":set rnu! rnu?CR>")

-- Write and quit
vim.keymap.set("n", "<leader>wq", ":wqa<CR>")

-- Split window
vim.keymap.set("n", "<leader>sh", ":split<CR>")
vim.keymap.set("n", "<leader>sv", ":vsplit<CR>")
vim.keymap.set("n", "<leader>sq", ":only<CR>")
