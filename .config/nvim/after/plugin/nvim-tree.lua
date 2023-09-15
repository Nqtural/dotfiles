local function on_attach_func(bufnr)
    local api = require "nvim-tree.api"

    local function opts(desc)
        return { desc = "nvim-tree: " .. desc, buffer = bufnr, noremap = true, silent = true, nowait = true }
    end

    -- default mappings
    api.config.mappings.default_on_attach(bufnr)

    -- custom mappings
    vim.keymap.set("n", "<leader><CR>", api.tree.change_root_to_node, opts("Down Directory"))
    vim.keymap.set("n", "<leader>.", api.tree.change_root_to_parent, opts("Up Directory"))
end

require("nvim-tree").setup {
    on_attach = on_attach_func,
    view = {
        width = 25,
    }
}
