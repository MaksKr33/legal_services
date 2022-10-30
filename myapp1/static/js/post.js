
  const filter_fieds = [
    {
      "filter_key": "type_case=",
      "filter_value": "1"
    }];
  //   // {
  //   //   "filter_key": "status_case",
  //   //   "filter_value": status_dropdown.select
  //   // }
  // ];
  

  var request_url = "";
  for (var key  of filter_fieds) {
  //   // do something with 'key' and 'value' {
  //     // if (value === undefined)
      request_url = key + menu[key] ;
      console.log(request_url)}