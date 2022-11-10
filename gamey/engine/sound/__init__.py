###
### Actions
###
def make_emit_sound_action(sound_path):
    import gamey.engine.sound.action.emit_sound as es
    return es.EmitSound(sound_path)