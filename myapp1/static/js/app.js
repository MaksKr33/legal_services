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


var search_button = new Vue({
  el: '#SearchButton',
  methods: {
    search_button: function () {
      const vm = user_list;
      const search_value = document.getElementById("Search_now").value;
      const api_search = 'client/?search=';
      axios.get(api_search + search_value)
      .then( function(response) {
      vm.Client = response.data
      }) 
    }
  }
});var filter_button = new Vue({
    el: '#filter_button',
    methods: {
      filter: function () {
        const vm = user_list;
        const type_value = type_dropdown;
        axios.get('client/?type_case=2')
        .then( function(response) {
        vm.Client = response.data
        }) 
      }
    }
});



var type_dropdown = new Vue({
    el: "#type_case_select",
    data: {
        selected_value:[]
      },
      created: function() {
          const vm = this;
          axios.get('typecase')
          .then(function(response){
          vm.selected_value =response.data
          }) 
      }
    },
)