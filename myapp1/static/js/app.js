var user_list = new Vue({
    el: '#contact_new',
    data: {
        Client: []
    },
    created: function() {
        const vm = this;
        axios.get('client')
        .then(function(response){
        vm.Client =response.data
        }) 
    }
});

var filter_button = new Vue({
    el: '#filter_button',
    methods: {
      filter: function () {
        const vm = user_list;
        const type_value = type_dropdown;
        axios.get('client/?type_case=' + type_dropdown.selected_value).then( function(response) {
            vm.Client = response.data
        }) 
      }
    }
});

var type_dropdown = new Vue({
    el: "#type_case_select",
    data: {
        selected_value: 1
    },
});