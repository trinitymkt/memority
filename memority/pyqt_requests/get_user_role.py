from PyQt5.QtCore import pyqtSignal

from .base import AbstractGetRequest


class GetUserRoleRequest(AbstractGetRequest):
    finished = pyqtSignal(str)

    def __init__(self):
        super().__init__('/user/role/')

    def process_response_data(self, data: dict):
        if data.get('status') == 'success':
            self.finished.emit(
                data.get('data').get('role') or ''
            )