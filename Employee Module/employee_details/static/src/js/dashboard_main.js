odoo.define('employee_details', function (require) {
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');

var Dashboard = Widget.extend({
    template: 'DashboardMain',

    events: {
		'click #plusbutton1': 'increment_counter',
	},

    init: function(parent, data){
        return this._super.apply(this, arguments);
    },

    start: function(){
    },

    increment_counter: function() {
    	new CounterEx().appendTo(this.$('.add_template'));
    },
});


var CounterEx = Widget.extend({
    template: 'Subtemplate',

    events: {
		'click #plusbutton2': 'incrementcounter',
		'click #minusbutton2': 'decrementcounter',
		'click #minusbutton1': 'decrement_counter'
	},

    init: function(parent, data){
    	this._super.apply(this, arguments);
    	console.log('init calle');
    	this.counter = 0;
    },

    start: function(){
        this.$input = this.$('input');
    },

    incrementcounter: function() {
    	this.$input.val(++this.counter);
    },
    
    decrementcounter: function() {
    	this.$input.val(--this.counter);
    },
    decrement_counter: function() {
    	this.destroy()
    },

});

// registry of main Dashboard
core.action_registry.add('employee_details.main', Dashboard);

return Dashboard;
});