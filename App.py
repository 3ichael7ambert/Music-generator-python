from flask import Flask, render_template, jsonify
from midiutil import MIDIFile
from music_generator import generate_melody  # Replace with your actual music generation function

app = Flask(__name__)

# generation function (replace with your logic)
def generate_melody():
    # music generation logic here

    return [(60, 500, 0.5), (62, 500, 0.5), (64, 500, 0.5)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_music')
def generate_music():
    # Generate melody
    melody_data = generate_melody()

    # Create MIDI file
    midi = MIDIFile(1)
    track = 0
    time = 0

    for note in melody_data:
        pitch, duration, velocity = note
        midi.addNote(track, 0, pitch, time, duration, velocity)

    # Save MIDI file
    midi_filename = 'generated_music.mid'
    with open(midi_filename, 'wb') as midi_file:
        midi.writeFile(midi_file)

    return jsonify({'message': 'Music generated successfully!', 'midi_filename': midi_filename})

if __name__ == '__main__':
    app.run(debug=True)
