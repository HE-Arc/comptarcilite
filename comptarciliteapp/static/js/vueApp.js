const url = "/listAccounts/";

let vue = new Vue({
    delimiters: ['[[', ']]', ],
    el: '#app',
    data: {
        results: [],
        accountId: null,
        transactions: [],
        accountGet: false,
    },
    mounted() {
        axios.get(url).then(response => {
            this.results = response.data;
            console.log(this.results);
        });
    },
    methods: {
        getAccount: function(id) {
            axios.get('/transactions/account/' + id).then(response => {
                this.transactions = response.data;
                this.accountId = id;
                this.accountGet = true;
                console.log(this.transactions);
            });
        }
    },
});