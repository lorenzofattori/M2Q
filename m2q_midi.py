#   m2q_midi.py
#   Everything related the MIDI communication of m2q
#

from rtmidi.midiutil import open_midiinput

# Class MidiInputHandler - Revised version of the rtmidi example for non-polling midi handling
class MidiInputHandler(object):
    def __init__(self, port):
        self.port = port
        # self._wallclock = time.time()

    def __call__(self, event, data=None):
        (
            message,
            _,
        ) = event  # second variable is deltatime, no idea what it means and why using it
        # self._wallclock += deltatime

        # message[0] is a combination of type of midi and channel
        # Example: 0x90 = note On - channel 1
        # 0x80 = note off - channel 1
        # 0x91 = note on - channel 2
        # 0xb0 = control change - channel 1
        # 0x9f = note on - channel 16
        # here I split them separately

        # WARNING - channel goes from 0 to 15 not from 1 to 16!
        channel = message[0] & 0x0F
        # this is in decimal, if you want to print 0x80 you need to convert it in hex
        midiType = message[0] & 0xF0
        note = message[1]
        value = message[2]

        print("[%s] %r" % (self.port, message))
        print(
            f"Channel: {channel}, type: {hex(midiType)}, note: {note}, value: {value}"
        )

# Midi setup - from the rtmidi example for non-polling midi handling
def midiSetup():
    # Prompts user for MIDI input port, unless a valid port number or name
    # is given as the first argument on the command line.
    # API backend defaults to ALSA on Linux.
    port = sys.argv[1] if len(sys.argv) > 1 else None

    try:
        midiin, port_name = open_midiinput(port)
    except (EOFError, KeyboardInterrupt):
        sys.exit()

    print("Attaching MIDI input callback handler.")
    midiin.set_callback(MidiInputHandler(port_name))

    return midiin



''' 
Midi Handling Functions
'''
'''
def onNoteOn(channel, note, velocity):
    if


void OnNoteOn(byte channel, byte note, byte velocity)         // Note on usato per il jumb to cue
{
  byte type;
  if(channel == 16)
  {
    type = 2;            // 2 = activate cuestack triggering
    DEBUG_PRINT("Cuestack Trigger ON ");
    DEBUG_PRINT(" channel: "); 
    DEBUG_PRINT(channel);
    DEBUG_PRINT(" Cue: "); 
    DEBUG_PRINTLN(note);
  }

  else
  {
    type = 0;              // 0 = jump to cue
    DEBUG_PRINT("Jump to cue ");
    DEBUG_PRINT(" channel: "); 
    DEBUG_PRINT(channel);
    DEBUG_PRINT(" Cue: "); 
    DEBUG_PRINTLN(note);
  }  
  CreateMessage(type, channel, note);   //crea pacchetto con type 0 (jump) e i valori richiesti e invialo

  '''