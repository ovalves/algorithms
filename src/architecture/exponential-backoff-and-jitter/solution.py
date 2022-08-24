from __future__ import annotations
from typing import Union
import random
import time

base = 10
cap = 15

def backoff(attempt):
    return min(cap, base * 2 ** attempt)

def backoff_with_jitter(attempt):
    return random.randrange(0, min(cap, base * 2 ** attempt))

def sample_service(service_name: str = 'A') -> Union[str, bool]:
    if random.choice([True, False]):
        return f"Service {service_name} not available", True

    return f"Service {service_name} called", False

def simulate_service_call(service: callable, name: str = 'A', initial_timeout: int = 0, backoff_alg: callable = backoff_with_jitter) -> Union[str, None]:
    try:
        print(f"Calling Service: {name}")
        print(f"Last waiting: {initial_timeout} seconds")
        msg, err = service()
        if err == True:
            print(f"{msg} -> Retrying...")
            sleep = backoff_alg(initial_timeout)
            time.sleep(sleep)
            return simulate_service_call(service, name, sleep, backoff_alg)

        print(f"Success: {msg}")
    except Exception as e:
        print(f"Error: {str(e)} -> Added Backoff timeout")

simulate_service_call(service=sample_service, name='A', initial_timeout=0, backoff_alg=backoff_with_jitter)
# simulate_service_call(service=sample_service, name='Service B', initial_timeout=0, backoff_alg=backoff)