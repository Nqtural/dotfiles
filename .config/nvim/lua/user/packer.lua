-- This file can be loaded by calling `lua require("plugins")` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require("packer").startup(function(use)
    -- Packer can manage itself
    use "wbthomason/packer.nvim"
    use {
        "nvim-telescope/telescope.nvim",
        requires = { "nvim-lua/plenary.nvim" }
    }
    use { "catppuccin/nvim", as = "catppuccin" }
    use ("nvim-treesitter/nvim-treesitter", { run = ":TSUpdate" })
    use "nvim-treesitter/playground"
    use "mbbill/undotree"
    use {
        "nvim-tree/nvim-tree.lua",
        requires = { "nvim-tree/nvim-web-devicons" }
    }
    use {
        "goolord/alpha-nvim",
        requires = { "nvim-tree/nvim-web-devicons" },
        config = function ()
            require("alpha").setup(require"alpha.themes.startify".config)
        end
    }
end)
