const display = document.getElementById('display');
const historyList = document.getElementById('history-list');

function appendValue(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
    display.style.color = '#25d366'; // Reset warna layar kembali ke hijau saat dihapus
}

// Fungsi Hitung Total + Catat Riwayat + Deteksi Angka Negatif
function calculate() {
    let expression = display.value;
    
    if (!expression) return;

    try {
        // Mengubah lambang % menjadi pembagian 100 agar eval() mengerti
        let formattedExpression = expression.replace(/%/g, '/100');
        
        let result = eval(formattedExpression);
        
        // Memastikan hasil desimal tidak terlalu panjang berantakan
        if (result % 1 !== 0) {
            result = parseFloat(result.toFixed(4));
        }

        // --- FITUR BARU: DETEKSI NEGATIF ---
        if (result < 0) {
            display.style.color = '#ff3b30'; // Ubah warna angka jadi merah neon jika negatif
        } else {
            display.style.color = '#25d366'; // Kembalikan jadi hijau neon jika positif/nol
        }
        // ------------------------------------

        // Tampilkan hasil ke layar
        display.value = result;

        // Tambahkan ke panel riwayat
        addHistory(expression, result);

    } catch (error) {
        display.value = 'Error';
        display.style.color = '#ff3b30'; // Jika error, kasih warna merah juga
    }
}

// Fungsi menambahkan list ke dalam HTML Riwayat
function addHistory(formula, result) {
    // Hapus tulisan "Belum ada riwayat" jika ini data pertama
    const emptyLi = historyList.querySelector('.empty');
    if (emptyLi) emptyLi.remove();

    const li = document.createElement('li');
    li.innerHTML = `${formula} = <strong>${result}</strong>`;
    
    // Taruh riwayat terbaru di paling atas list
    historyList.insertBefore(li, historyList.firstChild);
}

// Fungsi membersihkan papan riwayat
function clearHistory() {
    historyList.innerHTML = '<li class="empty">Belum ada riwayat</li>';
}