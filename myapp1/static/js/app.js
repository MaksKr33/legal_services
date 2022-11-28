
var user_list = new Vue({
    el: '#contact_new',
    data: {
        Client: []
    },
    created: function () {
        const vm = this;
        axios.get('client')
        .then( function(response) {
          vm.Client = response.data
        }) 
    },
    methods: {
      delete_user: function(user_name, user_id) {
        if (confirm("Ви хочете видалити клієнта " + user_name )) {
          axios.get('client/' + user_id).then( function(response) {
            location.reload();
          })
        }
      }
    }
});

var search = new Vue({
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
});


const btnSearchEl = document.getElementById('SearchButton')
  document.querySelector('#Search_now').oninput = function(){
  btnSearchEl.click()
  btnSearchEl.addEventListener('click')};


var type_dropdown = new Vue({
    el: "#type_case_select",
    data: {
      case_types: [{"id": 0, "NameTypeCase": "Тип справи"}],
      selected: 0
    },
    created: function() {
        const vm = this;
        axios.get('typecase').then(function(response) {
          vm.case_types.push(...response.data);
      }) 
    }
});


var status_dropdown = new Vue({
  el: "#status_case_select",
  data: {
    case_status: [{"id": 0, "NameStatusCase": "Cтатус справи"}],
    select: 0
  },
  created: function() {
      const vm = this;
      axios.get('statuscase').then(function(response) {
        vm.case_status.push(...response.data);
    }) 
  }
});


var filterbutton = new Vue({
  el: '#filter_button',
  methods: {
    filter: function () {
      const vm = user_list;
      const url_type ='client/?';
      const data_value = document.getElementById("date").value;
      const date_contract_value = document.getElementById("date_contract").value;
      const selected_case = type_dropdown.selected;
      const select_status = status_dropdown.select;
      
     var general_filtering = new Map();
     general_filtering.set("type_case=", selected_case);
     general_filtering.set( "status_case=", select_status );
     general_filtering.set('date=', data_value);
     general_filtering.set('date_contract=', date_contract_value);
         
      var reg = ''
      for (var [key, value] of general_filtering) {
          if (value !=0){
             reg = reg +'&'+ key + value}}
      axios.get(url_type + reg.slice(1))
      .then( function(response) {
      vm.Client = response.data
      }) 
    }
  }
})


const btnFilterDate = document.getElementById('filter_button')
    document.querySelector('#date').oninput = function(){
    btnFilterDate.click()
    btnFilterDate.addEventListener('click')};

  const btnFilterDateContract = document.getElementById('filter_button')
  document.querySelector('#date_contract').oninput = function(){
  btnFilterDateContract.click()
  btnFilterDateContract.addEventListener('click')};
 
  const btnFilterTypeCase = document.getElementById('filter_button')
  function foo(){
    btnFilterTypeCase.click()
    btnFilterTypeCase.addEventListener('click')};
  