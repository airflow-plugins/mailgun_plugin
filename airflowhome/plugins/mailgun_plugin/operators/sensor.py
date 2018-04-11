from airflow.operators.sensors import BaseSensorOperator


class EmailListChangedSensor(BaseSensorOperator):
    """
    Has the email list changed since the last run?
    """

    def poke(self, context):
        print('* EmailListChangedSensor.poke')
        return True
        # return False
