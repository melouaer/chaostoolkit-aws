# -*- coding: utf-8 -*-
from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets

from chaosaws import aws_client
from chaosaws.types import AWSResponse

__all__ = ["put_parameter"]


def put_parameter(
    parameter: str,
    value: str,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> AWSResponse:
    """
    Puts a parameter in ssm parameter store. 

    Input parameter prefix.
    Input parameter value.
    """

    if not parameter or not value:
        raise FailedActivity("you must specify the parameter and the value")

    client = aws_client("ssm", configuration, secrets)

    result = client.put_parameter(
        Name=parameter,
        Description="parameter injected with chaostoolkit",
        Value=value,
        Type="String",
        Overwrite=True,
    )
