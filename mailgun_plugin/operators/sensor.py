from airflow.operators.sensors import BaseSensorOperator


class EmailListChangedSensor(BaseSensorOperator):
    """
    Has the email list changed since the last run?
    """

    def poke(self, context):
        # TODO: implement - diff the hash of the previous list vs the new list (could store it in xcoms)
        return True
