from mpf.core.custom_code import CustomCode

delay = 250 # type: int()

class DropCollector(CustomCode):

    def on_load(self):
        self.info_log("DropCollector custom code started successfully.")
        self.machine.events.add_handler('shot_collect_ab_hit', self._start_collect_ab)
        self.machine.events.add_handler('shot_collect_cd_hit', self._start_collect_cd)

    def _start_collect_ab(self, **kwargs):
        del kwargs
        if self.machine.game.player.group_ab_value == 4:
            self.machine.events.post('target_group_ab_collected_full')
        for i in range(self.machine.game.player.group_ab_value):
            global delay
            self.machine.delay.add(ms=delay*(i+1), callback=self._do_decrement_ab)

    def _start_collect_cd(self, **kwargs):
        del kwargs
        if self.machine.game.player.group_cd_value == 4:
            self.machine.events.post('target_group_cd_collected_full')
        for i in range(self.machine.game.player.group_cd_value):
            global delay
            self.machine.delay.add(ms=delay*(i+1), callback=self._do_decrement_cd)

    def _do_decrement_ab(self, **kwargs):
        del kwargs
        self.machine.game.player.group_ab_value -= 1
        self.machine.events.post('target_group_ab_collect', num_remaining=self.machine.game.player.group_ab_value)

    def _do_decrement_cd(self, **kwargs):
        del kwargs
        self.machine.game.player.group_cd_value -= 1
        self.machine.events.post('target_group_cd_collect', num_remaining=self.machine.game.player.group_cd_value)