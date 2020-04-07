const url = "/listAccounts/";

let vue = new Vue({
    delimiters: ['[[', ']]', ],
    el: '#app',
    data: {
        accounts: [],
        accountId: null,
        transactions: [],
        accountGet: false,
        total: 0,
    },
    mounted() {
        axios.get(url).then(response => {
            this.accounts = response.data;
            console.log(this.accounts);
        });
    },
    methods: {
        getAccount: function(id) {
            axios.get('/transactions/account/' + id).then(response => {
                this.transactions = response.data;
                this.accountId = this.accounts.findIndex(account => account.id === id);
                this.accountGet = true;
                console.log(this.transactions);

                for(let t in this.transactions)
                {
                    this.total += parseFloat(this.transactions[t].amount);
                }

                console.log(this.total);
            });
        }
    },
});
