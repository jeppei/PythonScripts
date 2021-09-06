find = '\\"'
replace = '"'
num_selections = editor.getSelections()
for sel_nbr in range(num_selections):
    start_pos = editor.getSelectionNStart(sel_nbr)
    end_pos = editor.getSelectionNEnd(sel_nbr)
    editor.replace(find, replace, 0, start_pos, end_pos)

#editor.replace('\\"', '"')

