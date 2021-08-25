#include <iostream> 
using namespace std; 
  

int binarySearch(int arr[], int first, int last, int x) 
{ 
    if (last >= first) { 
        int mid = first + (last - first) / 2; 
  
		// Kalau Elemen ditengah sama dengan elemen yang dicari, kembalikan elemen tengah
        if (arr[mid] == x) 
            return mid; 
  
		// kalau elemen yang dicari kurang dari nilai tengah
        if (arr[mid] > x) 
            return binarySearch(arr, first, mid - 1, x); 
  
        // kalau elemen yang dicari lebih dari nilai tengah
        return binarySearch(arr, mid + 1, last, x); 
    } 
  
	// Kalau Elemen tidak ada dalam array kembalikan nilai -999 yang kemungkinan besar tidak akan di pakai oleh user
    return -999; 
} 
  	
int main() 
{ 
	
	int banyakAngka, i, x;
    
	cout<<"Anda ingin memasukkan berapa angka? : ";
    cin>>banyakAngka;
    
    int arr[banyakAngka] = {};
    
    for (int j = 0; j < banyakAngka; j++) {
    	cout<<"Silakan masukkan angka ke-"<< j+1 << " : ";
		cin>>arr[j];
	}
    
	// cetak array
	cout<<"\n\nAngka anda : ";
	cout<<"\n\n[";
    for (i = 0; i <= banyakAngka-1; i++) {
    	if(i <= banyakAngka-1 && i >= 1) {
    		cout<<", ";
		}
    	cout<<arr[i];
	}
	cout<<"]";
	cout<<"\n\n";
	
	//    elemen yang akan dicari
	
	cout<<"Masukkan angka yang ingin anda cari :  ";
	cin >> x; 
	
		
    int result = binarySearch(arr, 0, banyakAngka - 1, x); 
       
    (result == -999) ? cout << "Angka yang anda cari tidak ada di dalam array" : cout << "\nAngka yang anda cari ada di index ke- " << result; 
    
    return 0; 
} 
