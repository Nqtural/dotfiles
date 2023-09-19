local actions = require("telescope.actions")

require("telescope").setup{
    defaults = {
        path_display = { "smart" },
        preview = false,

        mappings = {
            i = {
                ["<C-n>"] = actions.cycle_history_next,
                ["<C-p>"] = actions.cycle_history_prev,

                ["<C-j>"] = actions.move_selection_next,
                ["<C-k>"] = actions.move_selection_previous,

                ["<C-x>"] = actions.close
            },
            n = {
                ["<C-x>"] = actions.close
            }
        },
        layout_config = {
            bottom_pane = {
                preview_cutoff = false
            }
        }
    },
    pickers = {
        find_files = {
            theme = "dropdown"
        }
    },
    extensions = {
    }
}
