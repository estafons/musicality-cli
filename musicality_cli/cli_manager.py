
def _get_scale(scale_str):
    midi_dict = { 'E': 40, 'F': 41, 'F#': 42,\
            'G': 43, 'G#': 44, 'A': 45, 'A#': 46, 'B': 47,\
            'C': 48, 'C#': 49, 'D': 50, 'D#': 51 }
    
    if len(scale_str) == 1:
        return midi_dict[scale_str[0]], "MAJOR_SCALE"
    elif len(scale_str) == 2:
        if scale_str[1] == 'm':
            return midi_dict[scale_str[0]], "MINOR_SCALE"
    raise ValueError("Invalid scale: {}".format(scale_str))

def compose_with_GA(idea, scale, output_filename):
    from musicality.classes.melody import Melody
    from musicality.classes.scale import Scale
    if scale is None:
        raise NotImplementedError("Automatic scale recognition is not yet implemented")
    
    notes_in_idea = [int(note) for note in idea.split()]
    idea = Melody(notes_in_idea)

    scale = Scale(*_get_scale(scale))

    composed = idea.genetize_melody(scale)

    composed.write_melody(output_filename)
