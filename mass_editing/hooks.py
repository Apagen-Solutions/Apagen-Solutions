def uninstall_hook(cr, registry):
    cr.execute("""DELETE FROM ir_act_window WHERE
    res_model = 'mass.editing.wizard'""")
