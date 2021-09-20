const btn = document.querySelector("#button");
btn.addEventListener('click', () => {

  const itemName = document.getElementById("itemName").value;
  const photo = document.getElementById("formFile").value;
  const price = document.getElementById("price").value;
  if (itemName == "" || photo == "" || price == "") {
  Swal.fire({
    title: 'Gagal!',
    text: 'Klik OK untuk melanjutkan',
    icon: 'error',
    confirmButtonText: 'OK'
  })
  } else {
    Swal.fire({
      title: 'Berhasil!',
      text: 'Klik OK untuk melanjutkan',
      icon: 'success',
      confirmButtonText: 'OK'
    }).then(() => { 
      location.reload()
  });
    
  }
})