odoo.define('quiz_idle_timer.quiz_timer', function (require) {
    var PublicWidget = require('web.public.widget')
    var quizTimer = PublicWidget.Widget.extend({
        selector: '.o_survey_wrap',
        events: {
            'click .button_time': 'startTimer',
        },
        start: function () {
            this.inactivityTimeout = null
            $(document).on('mousemove keydown', this.resetInactivityTimer.bind(this))
            this.startInactivityTimer()
        }
        resetInactivityTimer: function () {
            clearTimeout(this.inactivityTimeout)
        }
    })
    PublicWidget.registry.quiz_idle_timer = quizTimer
});