const display = document.getElementById('display');
const historyList = document.getElementById('history-list');

function appendValue(value) {
    if (display.value === 'Error') {
        display.value = '';
        display.style.color = '#25d366';
    }
    display.value += value;
}

function clearDisplay() {
    display.value = '';
    display.style.color = '#25d366';
}

function calculate() {
    let expression = display.value;
    
    if (!expression) return;

    try {
        let formattedExpression = expression.replace(/%/g, '/100');
        
        let result = eval(formattedExpression);
        
        if (result % 1 !== 0) {
            result = parseFloat(result.toFixed(4));
        }

        if (result < 0) {
            display.style.color = '#ff3b30';
        } else {
            display.style.color = '#25d366';
        }
        
        display.value = result;

        addHistory(expression, result);

    } catch (error) {
        display.value = 'Error';
        display.style.color = '#ff3b30';

        setTimeout(function() {
            if (display.value === 'Error') {
                display.value = '';
                display.style.color = '#25d366';
            }
        }, 3000);
    }
}

function addHistory(formula, result) {
    const emptyLi = historyList.querySelector('.empty');
    if (emptyLi) emptyLi.remove();

    const li = document.createElement('li');
    li.innerHTML = `${formula} = <strong>${result}</strong>`;
    
    historyList.insertBefore(li, historyList.firstChild);
}

function clearHistory() {
    historyList.innerHTML = '<li class="empty">Belum ada riwayat</li>';
}