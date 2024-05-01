class BaseController:
  def update(self, target_lataccel, current_lataccel, state):
    raise NotImplementedError

class OpenController(BaseController):
  def update(self, target_lataccel, current_lataccel, state):
    return target_lataccel

class SimpleController(BaseController):
  def update(self, target_lataccel, current_lataccel, state):
    return (target_lataccel - current_lataccel) * 0.3

class PIDController(BaseController):
  def __init__(self):
    self.kp = 0.5
    self.ki = 0.1
    self.kd = 0.05
    self.integral = 0
    self.previous_error = 0

  def update(self, target_lataccel, current_lataccel, state):
    error = target_lataccel - current_lataccel
    self.integral += error
    derivative = error - self.previous_error
    self.previous_error = error
    return (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

CONTROLLERS = {
  'open': OpenController,
  'simple': SimpleController,
  'pid': PIDController,
}
