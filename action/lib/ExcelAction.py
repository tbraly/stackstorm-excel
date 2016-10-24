"""
Copyright 2016 Brocade Communications Systems, Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from st2actions.runners.pythonrunner import Action


class ExcelAction(Action):
    def __init__(self, config):
        super(ExcelAction, self).__init__(config)
        self._excel_file = self.config['excel_file']
        self._key_column = self.config['key_column']
        self._variable_name_row = self.config['variable_name_row']
        self._lock_retries = self.config['lock_file_retries']
        self._lock_delay = self.config['lock_file_delay']