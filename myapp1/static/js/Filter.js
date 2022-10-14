new Vue({
    el: '#Filter_new',
    data: {
    FilterClient:[]
    },
    created: function() {
        const vm = this;
        axios.get('Filter')
        .then(function(response){
        vm.FilterClient =response.data
        }) 
    }
}

)