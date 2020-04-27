# -*- coding: utf-8 -*-
from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets

from chaosaws import aws_client
from chaosaws.types import AWSResponse

__all__ = ["disable_distribution"]


def disable_distribution(
    distribution_id: str, configuration: Configuration = None, secrets: Secrets = None,
) -> AWSResponse:
    """
    Disables a cloudfront distribution. 

    Input distribution id. 
    """

    if not distribution_id:
        raise FailedActivity(
            "you must specify the distribution id"
        )

    client = aws_client("cloudfront", configuration, secrets)
    distribution_config = client.get_distribution_config(Id=distribution_id)
    distribution_config["DistributionConfig"].update(Enabled=False)

    result = client.update_distribution(
        DistributionConfig=distribution_config["DistributionConfig"],
        Id=distribution_id,
        IfMatch=distribution_config["ETag"],
    )
