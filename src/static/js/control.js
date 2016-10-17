function autofill(){
    document.getElementById("stories").value="8";
    document.getElementById("dep_of_foun").value="6";
    document.getElementById("plinth_lev").value="4";
    document.getElementById("cclear_height").value="8@10";
    document.getElementById("dep_slab").value="1";
    document.getElementById("rep_span_len").value="6@8";
    document.getElementById("rep_span_wid").value="5@8";
    document.getElementById("col_type").value="0";
    document.getElementById("len_col").value="1";
    document.getElementById("wid_col").value="1";
    document.getElementById("radius_col").value="1";
    document.getElementById("dep_beam").value="1";
    document.getElementById("wid_beam").value="1";
}

$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();
  $("#col_type_0").hide();
  $("#col_type_1").hide();
  $("#col_type_1_2").hide();
});

function showThem(elm){
  if(elm.value == 0){
    document.getElementById("col_type_0").style.display = "block";
    document.getElementById("col_type_1").style.display = "none";
    document.getElementById("col_type_1_2").style.display = "none";
  }
  else if(elm.value == 1){
    document.getElementById("col_type_1").style.display = "block";
    document.getElementById("col_type_1_2").style.display = "block";
    document.getElementById("col_type_0").style.display = "none";
  }
  else{
    //alert("choose!");
  }
}
