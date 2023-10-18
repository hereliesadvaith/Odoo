odoo.define('survey_contact_creation.contact_creation', function (require) {
    var PublicWidget = require('web.public.widget')
    var contactCreation = PublicWidget.Widget.extend({
        selector: '.o_survey_background',
        start: function () {
            console.log("hello")
        },
        events: {
            'click .btn-primary:contains("Submit")': 'createContact',
        },
        createContact: function () {
            console.log(this)
        }
    })
    PublicWidget.registry.survey_contact_creation = contactCreation
});