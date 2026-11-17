# ABOUTME: Retries flaky calls such as the label printer.
# ABOUTME: Logs each failed attempt for the on-call channel.
import logging
import time

log = logging.getLogger(__name__)


def call_with_retry(fn, attempts=3, delay=0.5):
    for n in range(attempts):
        try:
            return fn()
        except TimeoutError:
            log.warning("attempt %d of %d timed out", n, attempts)
            time.sleep(delay)
    raise TimeoutError(f"gave up after {attempts} attempts")
