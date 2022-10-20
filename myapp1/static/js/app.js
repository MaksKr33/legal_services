
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
});


const txtSearchEl = document.getElementById('Search_now')
const btnSearchEl = document.getElementById('SearchButton')
txtSearchEl.addEventListener('keydown', (event) => {
  if (event.key === "Enter") {
    btnSearchEl.click()
  }
})
btnSearchEl.addEventListener('click', () => {
  console.log('search button clicked')
})


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
})


var filter_button = new Vue({
  el: '#filter_button',
  methods: {
    filter: function () {
      const vm = user_list;
      const url_type ='client/?type_case=';
      // const data_value = document.getElementById("date").value;
      // const date_contract_value = document.getElementById("date_contract").value;
      const selected_case = type_dropdown.selected;
      // const select_status = status_dropdown.select;
      // const filter_fieds = [
      //   {
      //     "filter_key": "type_case=",
      //     "filter_value": "Кримінальна"
      //   },
      //   // {
      //   //   "filter_key": "status_case",
      //   //   "filter_value": status_dropdown.select
      //   // }
      // ];
      

      // var request_url = "";
      // for (var key  of filter_fieds) {
      //   // do something with 'key' and 'value' {
      //     // if (value === undefined)
      //     request_url = key + menu[key] ;}

      //   request_url = "type_case=1&status_case=1"
      axios.get(url_type + selected_case)
      .then( function(response) {
      vm.Client = response.data
      }) 
    }
  }
});




