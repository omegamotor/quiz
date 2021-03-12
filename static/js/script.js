function test(){
    nr=5
    for(i = 1; i<=nr; i++){

        if (i%3 == 1){
            console.log(i+' Otwórz kontener i dodaj element')
         }
         else if (i%3 == 2){
             console.log(i+' dodaj element')
         }
         else if (i%3 == 0){
            console.log(i+' dodaj element i zamknij kontener')
         }
        console.log(i)
    }
    if (nr%3 == 2 || nr%3 == 1){
        console.log('zamknij kontener')
    }

    console.log('sadsadasdasdads')
};


function changeBGColor() {
  var cols = document.getElementsByClassName('hidden');
  for(i = 0; i < cols.length; i++) {
    cols[i].style.display = 'block';
  }
}

