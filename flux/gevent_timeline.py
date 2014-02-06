from .timeline import Timeline

class GeventTimeline(Timeline):
    def sleep(self, time):
        super(GeventTimeline, self).sleep(time)
        if self._time_factor == 0:
            self._real_sleep(0.0)
    def _real_sleep(self, seconds):
        try:
            import gevent
            gevent.sleep(seconds)
        except ImportError:
            super(GeventTimeline, self)._real_sleep(seconds)
