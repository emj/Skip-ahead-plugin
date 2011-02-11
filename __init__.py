# Skips ahead in the currently played song. 
# GPLv3 licensed.
# Author: Mr Copy and Paste
# 
import rb
#import rhythmdb
import gtk

ui_str = """
<ui>
    <popup name="BrowserSourceViewPopup">
      <placeholder name="BrowserSourcePopupPlaylistMorePlaceholder">
        <menuitem name="SkipAheadInSong" action="SkipAhead"/>
      </placeholder>
    </popup>
</ui>
"""

class TimeSkipper(rb.Plugin):
    def __init__(self):
        rb.Plugin.__init__(self)
        print "hello"

    def on_skip(self,*args):
        self.skip_ahead()

    def skip_ahead(self,seconds=20):
        if not self.shell.props.shell_player.get_playing():
            return
        new_pos=self.shell.props.shell_player.get_playing_time()+seconds
        duration=self.shell.props.shell_player.get_playing_song_duration()
        if(new_pos < duration and new_pos > 0):
            self.shell.props.shell_player.set_playing_time(new_pos)

    def activate(self, shell):
        self.shell=shell
        print "helloasdasd2"
        # First lets see if we can add to the context menu
        ui = shell.get_ui_manager()

        # Create Actions for the plugin
        action = gtk.Action ('SkipAheadInSong', _('Skip 20 seconds'),
                             _('Skips 20 seconds into the song'),
                             'lastfm')
        activate_id = action.connect ('activate', self.on_skip, shell)

        # Group and it's actions
        self.action_group = gtk.ActionGroup ('skipLastFmPluginActions')
        self.action_group.add_action_with_accel(action,"<Control>v")
        ui.insert_action_group(self.action_group, -1)

        # Add to the UI
        self.uid = ui.add_ui_from_string(ui_str)
        ui.ensure_update()

    def deactivate(self, shell):
        pass
