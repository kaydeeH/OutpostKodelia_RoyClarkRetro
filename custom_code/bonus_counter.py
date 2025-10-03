from mpf.core.custom_code import CustomCode

delay = 500 # type: int()
initial_bonus = 0 # type: int()

class BonusCounter(CustomCode):

    def on_load(self):
        self.info_log("BonusCountdown custom code started successfully.")
        #Either collect_seismic or bonus_start can trigger a countdown.
        self.machine.events.add_handler('bonus_start', self._start_bonus_countdown)
        self.machine.events.add_handler('bonus_countdown_decrement', self._decrement_bonus, 1)
        self.machine.events.add_handler('flipper_cancel', self._speed_up_bonus)

    def _start_bonus_countdown(self, **kwargs):
        del kwargs
        global initial_bonus

        if self.machine.game.player.bonus_val > 0:
            initial_bonus = self.machine.game.player.bonus_val
            self.machine.game.player.bonus_val -= 1
            self.machine.events.post('bonus_countdown_decrement')
        else:
            self.machine.events.post('finish_up_bonus')

    def _decrement_bonus(self, **kwargs):
            global delay
            self.machine.delay.add(ms=delay, callback=self._do_decrement)

    @staticmethod
    def _speed_up_bonus(**kwargs):
        global delay
        delay = 150

    def _do_decrement(self):
        if self.machine.game.player.bonus_val > 0:
            self.machine.game.player.bonus_val -= 1
            self.machine.events.post('bonus_countdown_decrement')
        else:
            #Decrement the bonus multiplier by 1 if greater than 1, reset the initial bonus value, keep counting
            global initial_bonus
            if self.machine.game.player.bonus_multiplier > 1:
                self.machine.game.player.bonus_multiplier -= 1
                for i in range(initial_bonus):
                    self.machine.game.player.bonus_val += 1
                self.machine.events.post('bonus_countdown_decrement')
            else:
                self.machine.events.post('finish_up_bonus')