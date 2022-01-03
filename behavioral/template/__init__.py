from behavioral.template.tasks.transfer_money import TransferMoney


class TemplatePattern:
    def __init__(self):
        self.task = TransferMoney()
        self.task.execute()
