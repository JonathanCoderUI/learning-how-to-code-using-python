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

        const hasOperator = /[\+\-\*\/]/.test(expression);
        
        if (hasOperator) {
            addHistory(expression, result);
        }

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

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const toggleBtn = document.getElementById('theme-toggle-btn');
    
    if (currentTheme === 'light') {
        document.documentElement.removeAttribute('data-theme');
        toggleBtn.innerHTML = `
            <svg class="theme-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 7c-2.8 0-5 2.2-5 5s2.2 5 5 5 5-2.2 5-5-2.2-5-5-5zm0-5c.6 0 1 .4 1 1v2c0 .6-.4 1-1 1s-1-.4-1-1V3c0-.6.4-1 1-1zm0 14c.6 0 1 .4 1 1v2c0 .6-.4 1-1 1s-1-.4-1-1v-2c0-.6.4-1 1-1zM3.8 4.2c.4-.4 1-.4 1.4 0l1.4 1.4c.4.4.4 1 0 1.4s-1 .4-1.4 0L3.8 5.6c-.4-.4-.4-1 0-1.4zm13.6 13.6c.4-.4 1-.4 1.4 0l1.4 1.4c.4.4.4 1 0 1.4s-1 .4-1.4 0l-1.4-1.4c-.4-.4-.4-1 0-1.4zM2 12c0-.6.4-1 1-1h2c0 .6-.4 1-1 1H3c0-.6-.4-1-1-1zm14 0c0-.6.4-1 1-1h2c0 .6-.4 1-1 1h-2c0-.6-.4-1-1-1zM5.2 17.4c.4-.4 1-.4 1.4 0l1.4 1.4c.4.4.4 1 0 1.4s-1 .4-1.4 0l-1.4-1.4c-.4-.4-.4-1 0-1.4zm13.6-13.6c.4-.4 1-.4 1.4 0l1.4 1.4c.4.4.4 1 0 1.4s-1 .4-1.4 0l-1.4-1.4c-.4-.4-.4-1 0-1.4z"/>
            </svg>
        `;
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        toggleBtn.innerHTML = `
            <svg class="theme-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.3 22c-5.5 0-10-4.5-10-10 0-4.3 2.7-8 6.7-9.4.5-.2 1 .1 1.1.6s-.1 1-.6 1.2c-3.1 1.1-5.2 4-5.2 7.3 0 4.4 3.6 8 8 8 3.3 0 6.2-2.1 7.3-5.2.2-.5.7-.7 1.2-.6.5.2.7.7.6 1.2-.9 4.2-4.6 6.9-9.1 6.9z"/>
            </svg>
        `;
    }
}

function backspace() {
    if (display.value === 'Error') {
        display.value = '';
        display.style.color = '#25d366';
        return;
    }

    display.value = display.value.toString().slice(0, -1);
}