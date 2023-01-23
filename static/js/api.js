const fromCurrency = document.getElementById('from-currency')
const toCurrency = document.getElementById('to-currency')
const amount = document.getElementById('amount-input')
const convertButton = document.getElementById('convert-button')
const resultBox = document.getElementById('result-box')
const conversionResult = document.getElementById('conversion-result')

document.addEventListener('DOMContentLoaded', () => {
    getCurrencies()
})

convertButton.addEventListener('click', e => {
    e.preventDefault();
    convertCurrency();
})

async function getCurrencies() {
    const URL = '/api/get_currencies/';

    const response = await fetch(URL, {
        headers: {
            'Accept': 'application/json',
        },
    })

    const data = await response.json()

    for (const key in data.symbols) {
        const toCurrencyOptions = document.createElement('option')
        const fromCurrencyOptions = document.createElement('option')

        toCurrencyOptions.value = key
        fromCurrencyOptions.value = key

        toCurrencyOptions.innerText = `${key} - ${data.symbols[key]}`
        fromCurrencyOptions.innerText = `${key} - ${data.symbols[key]}`

        toCurrency.appendChild(toCurrencyOptions)
        fromCurrency.appendChild(fromCurrencyOptions)
    }
}


async function convertCurrency() {

    if (!amount.value || amount.value == 0) {
        displayError('You must enter an amount to convert')
        return
    }

    conversionResult.innerText = ''
    resultBox.classList.add('is-hidden');

    try {
        const URL = '/api/converter/'
        const conversion = {
            'from_query': fromCurrency.value,
            'to_query': toCurrency.value,
            'amount_query': amount.value,
        }

        const response = await fetch(URL, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
            },
            body: JSON.stringify(conversion)
        })

        const data = await response.json()
        resultBox.classList.remove('is-hidden');
        conversionResult.innerText = `${data.result.toFixed(2)} ${data.query.to} with an exchange rate of ${data.info.rate}`
    } catch (err) {
        console.error(err);
    }
}

function displayError(error) {
    resultBox.classList.remove('is-hidden')
    conversionResult.innerText = error
}