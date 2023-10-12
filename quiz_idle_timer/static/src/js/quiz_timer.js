odoo.define('quiz_idle_timer.quiz_timer', function (require) {
    var PublicWidget = require('web.public.widget')
    var count = 0
    var checkInactivity = 0
    var $idleTimerData = this.$(".idle_timer_data")
    var idleTime = $idleTimerData.data('idleTime')
    var turnPageTime = $idleTimerData.data('turnPageTime')
    var quizTimer = PublicWidget.Widget.extend({
        selector: '.o_survey_background',
        start: function () {
            this.inactivityTimeout = null
            $(document).on('mousemove keydown', this.resetInactivityTimer.bind(this))
            this.startInactivityTimer()
            this.startTimer()
        },
        startInactivityTimer: function () {
            // To check if the section is idle from start
            this.inactivityTimeout = setTimeout(() => {
                checkInactivity = 1
            }, (idleTime * 1000))
        },
        resetInactivityTimer: function () {
            // To change the Inactivity value.
            count = 0
            checkInactivity = 0
            clearTimeout(this.inactivityTimeout)
            this.inactivityTimeout = setTimeout(() => {
                checkInactivity = 1
            }, (idleTime * 1000))
        },
        startTimer: function () {
            // To count time.
            var idleTimer = this.$(".idle_timer");

            var timerInterval = setInterval(function () {
                var minutes = Math.floor(count / 60);
                var seconds = count % 60;

                var minutesDisplay = String(minutes).padStart(2, '0');
                var secondsDisplay = String(seconds).padStart(2, '0');
                idleTimer.text(minutesDisplay + ':' + secondsDisplay);

                if (count === turnPageTime) {
                    this.$('.btn-primary').click()
                    count = 0
                    return
                }
                if (checkInactivity === 1) {
                    count++
                } else {
                    count = 0
                }
            }, 1000);
        },
    })
    PublicWidget.registry.quiz_idle_timer = quizTimer
});
