const swiper = new Swiper('.swiper', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
  },
  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
});


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
  // Swal.fire({
  //   title: 'Apa Anda Yakin?',
  //   text: "Jika terdapat kesalahan, anda tetap dapat mengeditnya!",
  //   icon: 'warning',
  //   showCancelButton: true,  
  //   confirmButtonColor: '#3085d6',
  //   cancelButtonColor: '#d33',
  //   confirmButtonText: 'Ya, Posting!'
  // }).then((result) => {
  //   if (result.isConfirmed) {
  //     Swal.fire(
  //       'Berhasil!',
  //       'Barang telah diunggah!.',
  //       'success'
  //     )
  //   }
  // })
