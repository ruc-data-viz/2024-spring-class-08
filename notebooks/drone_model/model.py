import numpy as np

center = (-75.12601884604852, 39.95066669151871)
radius = 0.001


def fly(time_s: float) -> tuple[float, float]:
    """fly the drone to the designated point in time"""
    return (
        center[0] + radius * np.cos(time_s),
        center[1] + radius * np.sin(time_s),
    )


def model_sensor_noise(
    latitude: float, longitude: float, std_dev: float
) -> tuple[float, float]:
    """Model sensor noise (for visualization demonstration only)"""
    sensor_noise = np.random.normal(loc=0, scale=std_dev, size=latitude.shape)
    latitude_with_noise = latitude + sensor_noise
    longitude_with_noise = longitude + sensor_noise
    return latitude_with_noise, longitude_with_noise
