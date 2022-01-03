from behavioral.template.audit_trail import AuditTrail


class Task:
    def __init__(self, audit_trail: AuditTrail = AuditTrail()):
        self._audit_trail: AuditTrail = audit_trail

    def execute(self):
        self._audit_trail.record()
        self._execute()

    def _execute(self):
        raise NotImplementedError()
