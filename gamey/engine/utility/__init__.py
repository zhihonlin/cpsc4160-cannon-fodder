###
### Entities
###
def make_total_counter():
    import gamey.engine.utility.entity.total_counter as tc
    result = tc.Total_Counter()
    return result


def make_success_counter():
    import gamey.engine.utility.entity.success_counter as sc
    result = sc.Success_Counter()
    return result

def make_timer():
    import gamey.engine.utility.entity.timer as tm
    result = tm.Timer()
    return result

###
### Actions
###

def make_start_timer_action():
    import gamey.engine.utility.action.start_timer as st
    return st.StartTimer()

def make_update_timer_action():
    import gamey.engine.utility.action.update_timer as ut
    return ut.UpdateTimer()

def make_alarm_action():
    import gamey.engine.utility.action.alarm as al
    return al.Alarm()

def make_activate_action():
    import gamey.engine.utility.action.activate_entity as ae
    return ae.ActivateEntity()

def make_deactivate_action():
    import gamey.engine.utility.action.deactivate_entity as de
    return de.DeactivateEntity()
