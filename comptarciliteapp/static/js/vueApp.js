const url = "/listAccounts/";

let vue = new Vue({
    delimiters: ['[[', ']]', ],
    el: '#app',
    data: {
        accounts: [],
        accountId: null,
        transactions: [],
        accountGet: false,
        members: [],
        memberId: null,
        memberName: "",
        membersList: [],
        total: 0,
    },
    mounted() {
        axios.get(url).then(response => {
            this.accounts = response.data;
        });
        this.getMembers();
    },
    methods: {
        getAccount: function(id) {
            axios.get('/transactions/account/' + id).then(response => {
                this.transactions = response.data;
                this.accountId = this.accounts.findIndex(account => account.id === id);
                this.accountGet = true;
                console.log(this.transactions);

                for (let t in this.transactions) {
                    this.total += parseFloat(this.transactions[t].amount);
                }

                console.log(this.total);
            });
        },

        getMember: function(id) {
            axios.get('/members/' + id).then(response => {
                this.members.push(response.data);
                this.memberName = "";
                console.log(this.members);
            });
        },

        getMembers: function() {
            axios.get('/members/').then(response => {
                this.membersList = response.data;
                console.log(this.membersList);
            });
        },
    },
});