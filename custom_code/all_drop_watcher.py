from mpf.core.custom_code import CustomCode

firstHits = [0,0,0,0]
secondHits = [0,0,0,0]
thirdHits = [0,0,0,0]

class AllDropWatcher(CustomCode):

    def on_load(self):
        self.info_log("AllDropWatcher custom code started successfully.")
        self.machine.events.add_handler('shot_drop_a_unhit_hit', self._register_a_once)
        self.machine.events.add_handler('shot_drop_b_unhit_hit', self._register_b_once)
        self.machine.events.add_handler('shot_drop_c_unhit_hit', self._register_c_once)
        self.machine.events.add_handler('shot_drop_d_unhit_hit', self._register_d_once)
        self.machine.events.add_handler('shot_drop_a_hit_once_hit', self._register_a_twice)
        self.machine.events.add_handler('shot_drop_b_hit_once_hit', self._register_b_twice)
        self.machine.events.add_handler('shot_drop_c_hit_once_hit', self._register_c_twice)
        self.machine.events.add_handler('shot_drop_d_hit_once_hit', self._register_d_twice)
        self.machine.events.add_handler('shot_drop_a_hit_twice_hit', self._register_a_thrice)
        self.machine.events.add_handler('shot_drop_b_hit_twice_hit', self._register_b_thrice)
        self.machine.events.add_handler('shot_drop_c_hit_twice_hit', self._register_c_thrice)
        self.machine.events.add_handler('shot_drop_d_hit_twice_hit', self._register_d_thrice)
        self.machine.events.add_handler('finish_up_bonus', self._reset_all)

    def _register_a_once(self, **kwargs):
        del kwargs
        global firstHits
        firstHits[0] = 1
        self._check_first_hits()

    def _register_b_once(self, **kwargs):
        del kwargs
        global firstHits
        firstHits[1] = 1
        self._check_first_hits()

    def _register_c_once(self, **kwargs):
        del kwargs
        global firstHits
        firstHits[2] = 1
        self._check_first_hits()

    def _register_d_once(self, **kwargs):
        del kwargs
        global firstHits
        firstHits[3] = 1
        self._check_first_hits()

    def _register_a_twice(self, **kwargs):
        del kwargs
        global secondHits
        secondHits[0] = 1
        self._check_second_hits()

    def _register_b_twice(self, **kwargs):
        del kwargs
        global secondHits
        secondHits[1] = 1
        self._check_second_hits()

    def _register_c_twice(self, **kwargs):
        del kwargs
        global secondHits
        secondHits[2] = 1
        self._check_second_hits()

    def _register_d_twice(self, **kwargs):
        del kwargs
        global secondHits
        secondHits[3] = 1
        self._check_second_hits()

    def _register_a_thrice(self, **kwargs):
        del kwargs
        global thirdHits
        thirdHits[0] = 1
        self._check_third_hits()

    def _register_b_thrice(self, **kwargs):
        del kwargs
        global thirdHits
        thirdHits[1] = 1
        self._check_third_hits()

    def _register_c_thrice(self, **kwargs):
        del kwargs
        global thirdHits
        thirdHits[2] = 1
        self._check_third_hits()

    def _register_d_thrice(self, **kwargs):
        del kwargs
        global thirdHits
        thirdHits[3] = 1
        self._check_third_hits()

    def _check_first_hits(self, **kwargs):
        del kwargs
        global firstHits
        if firstHits[0] + firstHits[1] + firstHits[2] + firstHits[3] == 4:
            self.machine.events.post('drops_first_hits_complete')

    def _check_second_hits(self, **kwargs):
        del kwargs
        global secondHits
        if secondHits[0] + secondHits[1] + secondHits[2] + secondHits[3] == 4:
            self.machine.events.post('drops_second_hits_complete')

    def _check_third_hits(self, **kwargs):
        del kwargs
        global thirdHits
        if thirdHits[0] + thirdHits[1] + thirdHits[2] + thirdHits[3] == 4:
            self.machine.events.post('drops_third_hits_complete')

    def _reset_all(self, **kwargs):
        del kwargs
        global firstHits
        global secondHits
        global thirdHits
        firstHits = [0,0,0,0]
        secondHits = [0,0,0,0]
        thirdHits = [0,0,0,0]
        self.machine.events.post('drops_reset_complete')