# -*- coding: utf-8 -*-
from dagger.browser_emulator import BrowserEmulator
from dagger.common import GloableSettings as gs
import sys
sys.path.append("..")

from sfa_ent.config import SetupInfo

import time
import os
be = None

def custom_setup():
	global be

	gs.set_chrome_driver_path(SetupInfo.chrome_driver_path)
	gs.set_timeout(SetupInfo.time_out)
	gs.set_step_interval(1)
	timestamp = time.strftime('%Y-%m-%d_%H%M%S',time.localtime(time.time()))
	reportFile = './capture/' + timestamp + '_report/'
	os.makedirs(reportFile)
	gs.set_capture_screenshort_path(reportFile)
	be = BrowserEmulator()
	be.open(SetupInfo.url)