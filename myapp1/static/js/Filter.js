new Vue({
    el: '#Search',
    data: {
   SearchClient:[]
    },
    created: function() {
        const vm = this;
        axios.get('Filter')
        .then(function(response){
        vm.SearchClient =response.data
        }) 
    }
}

)